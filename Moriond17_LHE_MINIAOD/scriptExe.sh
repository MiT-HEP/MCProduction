#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc481
echo "================= CMSRUN setting up CMSSW_7_1_20 ===================="| tee -a job.log
if [ -r CMSSW_7_1_20/src ] ; then 
     echo release CMSSW_7_1_20 already exists
 else
     scram p CMSSW CMSSW_7_1_20
 fi

 BASE=$PWD
 NUM=500

 cd CMSSW_7_1_20/src
 eval `scram runtime -sh`

 mkdir -p Configuration/GenProduction/python
 cp -v $BASE/LHE.py $BASE/GEN.py Configuration/GenProduction/python/

 scram b
 cd ../../

echo "================= CMSRUN starting Step 1 ====================" >> job.log
 cmsDriver.py Configuration/GenProduction/python/LHE.py --fileout file:step1.root --mc --eventcontent LHE --datatier LHE --conditions MCRUN2_71_V1::All --step LHE --python_filename step1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n ${NUM} || exit $? ; 
 cmsRun -j GenSimAODSim_step1.log step1.py 

echo "================= CMSRUN starting Step 2 ====================" >> job.log
 cmsDriver.py Configuration/GenProduction/python/GEN.py --filein file:step1.root --fileout file:step2.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step GEN,SIM --magField 38T_PostLS1 --python_filename step2.py --no_exec -n ${NUM} || exit $? ; 

 cmsRun -j GenSimAODSim_step2.log step2.py
 echo "-> cleaning"
 rm -v step1.root  

cd $BASE
echo "================= CMSRUN setting up CMSSW_8_0_21 ===================="| tee -a job.log
export SCRAM_ARCH=slc6_amd64_gcc530
if [ -r CMSSW_8_0_21/src ] ; then 
     echo release CMSSW_8_0_21 already exists
 else
     scram p CMSSW CMSSW_8_0_21
 fi
 cd CMSSW_8_0_21/src
 eval `scram runtime -sh`


scram b

cd ../../
echo "================= CMSRUN starting Step 3 ===================="| tee -a job.log
cmsDriver.py step3 --filein file:step2.root --fileout file:step3.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISpring15PrePremix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v2-v2/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016 --nThreads 4 --datamix PreMix --era Run2_2016 --python_filename step3.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n ${NUM} || exit $? ; 

 cmsRun -e -j GenSimAODSim_step3.log step3.py
 echo "-> cleaning"
 rm -v step2.root  

echo "================= CMSRUN starting Step 4 ====================" | tee -a job.log
cmsDriver.py step4 --filein file:step3.root --fileout file:step4.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,RECO,EI --nThreads 4 --era Run2_2016 --python_filename step4.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n ${NUM} || exit $? ; 

 cmsRun -e -j GenSimAODSim_step4.log step4.py
 echo "-> cleaning"
 rm -v step3.root  

echo "================= CMSRUN starting Step 5 ====================" | tee -a job.log
cmsDriver.py step5 --fileout file:step5.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step PAT --nThreads 4 --era Run2_2016 --python_filename step5.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n ${NUM} || exit $? ; 

 cmsRun -e -j FrameworkJobReport.xml  step5.py
 echo "-> cleaning"
 rm -v step4.root  
echo "================= CMSRUN finished Step 5 ====================" | tee -a job.log
