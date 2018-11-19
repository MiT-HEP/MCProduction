#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630

BASE=$PWD


echo "================= CMSRUN setting up CMSSW_10_2_6 ===================="| tee -a job.log
if [ -r CMSSW_10_2_6/src ] ; then 
     echo release CMSSW_10_2_6 already exists
 else
     scram p CMSSW CMSSW_10_2_6
 fi
 cd CMSSW_10_2_6/src



 eval `scram runtime -sh`

 scram b

cd $BASE

echo "================= CMSRUN starting Step 1 ====================" | tee -a job.log
cmsRun -j GenSimAODSim_step1.log MinBias_14TeV_pythia8_TuneCUETP8M1_cfi_GEN_SIM.py jobNum=$1


echo "================= CMSRUN starting Step 2 ====================" | tee -a job.log

 cmsRun -e -j FrameworkJobReport.xml step2_DIGI_L1_L1TrackTrigger_DIGI2RAW_HLT.py
 echo "-> cleaning"
 rm -v step1.root  

echo "================= CMSRUN finished ====================" | tee -a job.log
