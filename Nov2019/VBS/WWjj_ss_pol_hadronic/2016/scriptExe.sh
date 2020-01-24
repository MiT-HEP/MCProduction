#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log

lsb_release -a 

echo "================= CURL GRIDPACK ===================="| tee -a job.log

#GRIDPACK=WWjj_ll_hadronic_slc7_amd64_gcc820_CMSSW_9_3_16_tarball.tar.xz
#GRIDPACK=WWjj_lt_hadronic_slc7_amd64_gcc820_CMSSW_9_3_16_tarball.tar.xz
GRIDPACK=WWjj_tt_hadronic_slc7_amd64_gcc820_CMSSW_9_3_16_tarball.tar.xz

curl --insecure https://amarini.web.cern.ch/amarini/$GRIDPACK --retry 2 -o ./$GRIDPACK

ls -ltr 

source /cvmfs/cms.cern.ch/cmsset_default.sh

BASE=$PWD

echo "================= CMSRUN setting up CMSSW_7_1_45 ===================="| tee -a job.log
export SCRAM_ARCH=slc6_amd64_gcc481
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_7_1_45/src ] ; then 
     echo release CMSSW_7_1_45 already exists
 else
     scram p CMSSW CMSSW_7_1_45
 fi
 cd CMSSW_7_1_45/src
 eval `scram runtime -sh`

cd $BASE
echo "================= CMSRUN starting Step 1 ====================" | tee -a job.log
cmsRun -j GenSimAODSim_step1.log step1.py jobNum=$1 gridpack=$GRIDPACK

echo "================= CMSRUN setting up CMSSW_8_0_31 ===================="| tee -a job.log

if [ -r CMSSW_8_0_31/src ] ; then 
    echo release CMSSW_8_0_31 already exists
else
    scram p CMSSW CMSSW_8_0_31
fi
cd CMSSW_8_0_31/src
eval `scram runtime -sh`

cd $BASE

echo "================= CMSRUN starting Step 2 ====================" | tee -a job.log
cmsRun -j GenSimAODSim_step2.log step2.py 

echo "================= CMSRUN starting Step 3 ====================" | tee -a job.log
cmsRun -j Reco_step3.log step3.py 


echo "================= CMSRUN setting up CMSSW_9_4_9 ===================="| tee -a job.log
export SCRAM_ARCH=slc6_amd64_gcc630
if [ -r CMSSW_9_4_9/src ] ; then 
    echo release CMSSW_9_4_9 already exists
else
    scram p CMSSW CMSSW_9_4_9
fi
cd CMSSW_9_4_9/src
eval `scram runtime -sh`


scram b
cd ../../
cd $BASE

echo "================= CMSRUN starting Step 4 ====================" | tee -a job.log
#cmsRun -j MiniAODSim_Step2.log Step2.py 
cmsRun -e -j FrameworkJobReport.xml step4.py 

echo "================= CMSRUN finished ====================" | tee -a job.log

ls -ltr | tee -a job.log
