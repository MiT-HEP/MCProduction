#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530

BASE=$PWD


echo "================= CMSRUN setting up CMSSW_8_0_31 ===================="| tee -a job.log

if [ -r CMSSW_8_0_31/src ] ; then 
    echo release CMSSW_8_0_31 already exists
else
    scram p CMSSW CMSSW_8_0_31
fi
cd CMSSW_8_0_31/src
eval `scram runtime -sh`

cd $BASE
echo "================= CMSRUN starting Step 1 ====================" | tee -a job.log
cmsRun -j GenSimAODSim_step1.log step1.py jobNum=$1


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

echo "================= CMSRUN starting Step 2 ====================" | tee -a job.log
#cmsRun -j MiniAODSim_Step2.log Step2.py 
cmsRun -e -j FrameworkJobReport.xml step2.py 

echo "================= CMSRUN finished ====================" | tee -a job.log
