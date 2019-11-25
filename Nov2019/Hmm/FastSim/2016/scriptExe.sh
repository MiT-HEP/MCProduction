#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530

[ -f x509up_u$(id -u) ] && { chmod go-rwx x509up_u$(id -u); cp -v x509up_u$(id -u) /tmp/ ;}

BASE=$PWD

echo "================= CMSRUN setting up CMSSW_7_1_26 ===================="| tee -a job.log
export SCRAM_ARCH=slc6_amd64_gcc481
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_7_1_26/src ] ; then 
     echo release CMSSW_7_1_26 already exists
 else
     scram p CMSSW CMSSW_7_1_26
 fi
 cd CMSSW_7_1_26/src
 eval `scram runtime -sh`

cd $BASE
echo "================= CMSRUN starting Step 1 ====================" | tee -a job.log
cmsRun -j GenSimAODSim_step1.log step1.py jobNum=$1


echo "================= CMSRUN setting up CMSSW_10_2_11_patch1 ===================="| tee -a job.log

if [ -r CMSSW_10_2_11_patch1/src ] ; then 
    echo release CMSSW_10_2_11_patch1 already exists
else
    scram p CMSSW CMSSW_10_2_11_patch1
fi
cd CMSSW_10_2_11_patch1/src
eval `scram runtime -sh`

cd $BASE
echo "================= CMSRUN starting Step 2 ====================" | tee -a job.log
#cmsRun -j GenSimAODSim_step2.log step2.py jobNum=$1
cmsRun -e -j FrameworkJobReport.xml step2.py jobNum=$1


#echo "================= CMSRUN setting up CMSSW_9_4_9 ===================="| tee -a job.log
#export SCRAM_ARCH=slc6_amd64_gcc630
#if [ -r CMSSW_9_4_9/src ] ; then 
#    echo release CMSSW_9_4_9 already exists
#else
#    scram p CMSSW CMSSW_9_4_9
#fi
#cd CMSSW_9_4_9/src
#eval `scram runtime -sh`
#
#
#scram b
#cd ../../
#cd $BASE
#
#echo "================= CMSRUN starting Step 3 ====================" | tee -a job.log
#cmsRun -j MiniAODSim_Step2.log Step2.py 
#cmsRun -e -j FrameworkJobReport.xml step3.py 

echo "================= CMSRUN finished ====================" | tee -a job.log
