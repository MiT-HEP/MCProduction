#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630

BASE=$PWD


echo "================= CMSRUN setting up CMSSW_9_3_6 ===================="| tee -a job.log
if [ -r CMSSW_9_3_6/src ] ; then 
     echo release CMSSW_9_3_6 already exists
 else
     scram p CMSSW CMSSW_9_3_6
 fi
 cd CMSSW_9_3_6/src


 NUM=500

 cd CMSSW_9_3_6/src
 eval `scram runtime -sh`

 mkdir -p Configuration/GenProduction/python
 cp -v $BASE/LHE.py $BASE/GEN.py Configuration/GenProduction/python/

 scram b
cd $BASE

echo "================= CMSRUN starting Step 1 ====================" | tee -a job.log
cmsRun -j GenSimAODSim_step1.log step1.py jobNum=$1

echo "================= CMSRUN setting up CMSSW_9_3_6 ===================="| tee -a job.log
if [ -r CMSSW_9_4_0_patch1/src ] ; then 
     echo release CMSSW_9_3_6 already exists
 else
     scram p CMSSW CMSSW_9_4_0_patch1
 fi
 cd CMSSW_9_4_0_patch1/src
 eval `scram runtime -sh`
 scram b

cd $BASE
echo "================= CMSRUN starting Step 2 ====================" | tee -a job.log

 cmsRun -j GenSimAODSim_step2.log step2.py
 echo "-> cleaning"
 rm -v step1.root  

echo "================= CMSRUN starting Step 3 ====================" | tee -a job.log

 cmsRun -j GenSimAODSim_step3.log step3.py
 echo "-> cleaning"
 rm -v step2.root  

echo "================= CMSRUN starting Step 4 ====================" | tee -a job.log

 cmsRun -e -j FrameworkJobReport.xml step4.py
 echo "-> cleaning"
 rm -v step3.root  

echo "================= CMSRUN finished ====================" | tee -a job.log
