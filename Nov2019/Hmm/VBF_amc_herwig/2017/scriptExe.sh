#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log

source /cvmfs/cms.cern.ch/cmsset_default.sh

echo "================= CURL GRIDPACK ===================="| tee -a job.log
curl --insecure https://amarini.web.cern.ch/amarini/vbfh_5f_NLO_125_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz --retry 2 -o ./vbfh_5f_NLO_125_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz

BASE=$PWD

echo "================= CMSRUN setting up CMSSW_9_3_13_patch3 ===================="| tee -a job.log
export SCRAM_ARCH=slc6_amd64_gcc630
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_9_3_13_patch3/src ] ; then 
     echo release CMSSW_9_3_13_patch3 already exists
 else
     scram p CMSSW CMSSW_9_3_13_patch3
 fi
 cd CMSSW_9_3_13_patch3/src
 eval `scram runtime -sh`

cd $BASE


echo "================= CMSRUN starting Step 1 ====================" | tee -a job.log
cmsRun -j GenSimAODSim_step1.log step1.py jobNum=$1

echo "================= CMSRUN setting up CMSSW_9_4_7 ===================="| tee -a job.log

if [ -r CMSSW_9_4_7/src ] ; then 
    echo release CMSSW_9_4_7 already exists
else
    scram p CMSSW CMSSW_9_4_7
fi
cd CMSSW_9_4_7/src
eval `scram runtime -sh`

cd $BASE

echo "================= CMSRUN starting Step 2 ====================" | tee -a job.log
cmsRun -j GenSimAODSim_step2.log step2.py 

echo "================= CMSRUN starting Step 3 ====================" | tee -a job.log
cmsRun -j Reco_step3.log step3.py 

echo "================= CMSRUN starting Step 4 ====================" | tee -a job.log
cmsRun -e -j FrameworkJobReport.xml step4.py 

echo "================= CMSRUN finished ====================" | tee -a job.log
