# cmsDriver: python generation
These steps will produce the step.py files used by the generation process
## Create Symlinks
```
cmsrel CMSSW_7_4_5
cd !$
cmsenv
cd MCProduction/ThirteenTeV
scram b -j 16
```

##STEP 1
Step 1 produces the GEN-SIM-RAW datatier. It is heavy production and therefore factorized.

```
cmsDriver.py \
MCProduction/ThirteenTeV/python/HplusToTauNu_M_200_TuneCUETP8M1_tauola_13TeV_pythia8_cfi.py \
--mc \
--eventcontent RAWSIM \
--datatier GEN-SIM-RAW \
--pileup 2015_25ns_Startup_PoissonOOTPU \
--pileup_input dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM \
--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
--conditions MCRUN2_74_V9 \
--magField 38T_PostLS1 \
--step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:@frozen25ns \
--python_filename step1.py  \
--no_exec \
--fileout file:step1.root \
-n 100
```

## STEP 2 
Step 2 runs the Reconstruction algorithm and produces the AOD file content.
```
cmsDriver.py step2 --filein file:step1.root --fileout file:step2.root  \
--mc --eventcontent AODSIM  \
--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
--datatier AODSIM --step RAW2DIGI,L1Reco,RECO \
--conditions MCRUN2_74_V9 \
--magField 38T_PostLS1  \
--python_filename step2.py  \
-n 10  \
--no_exec 
```

## STEP 3 
Step 3 produces MINIAOD (GT MCRUN2_74_V9) out of them (CMSSW_7_4_5), for miniAODv2 change GT (7_4_12)
```
cmsDriver.py step3 --filein file:step2.root  \
--fileout file:step3.root --mc \
--eventcontent MINIAODSIM  \
--runUnscheduled --datatier MINIAODSIM  \
--conditions 74X_mcRun2_asymptotic_v2  \
--step PAT \
--python_filename step3.py  \
--customise Configuration/DataProcessing/Utils.addMonitoring \
-n 10 
```

## STEP1+2
Produce directly AOD w/o storing the GEN-RAW-SIM
```
cmsDriver.py \
MCProduction/ThirteenTeV/python/HplusToTauNu_M_900_TuneCUETP8M1_tauola_13TeV_pythia8_cfi.py \
--mc \
--eventcontent AODSIM \
--datatier AODSIM \
--pileup 2015_25ns_Startup_PoissonOOTPU \
--pileup_input dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM \
--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
--conditions MCRUN2_74_V9 \
--magField 38T_PostLS1 \
--step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:@frozen25ns,RAW2DIGI,L1Reco,RECO \
--python_filename step12.py  \
--no_exec \
--fileout file:step2.root \
-n 100
```

## STEP1+2 from LHE
```
cmsDriver.py \
Configuration/GenProduction/python/ThirteenTeV/Hadronizer_MgmMatchTune4C_13TeV_madgraph_pythia8_Tauola_cff.py \
--filein dbs:/TTZJets_Tune4C_13TeV-madgraph-tauola/Fall13pLHE-START62_V1-v1/GEN \
--mc \
--eventcontent AODSIM \
--datatier AODSIM \
--pileup 2015_25ns_Startup_PoissonOOTPU \
--pileup_input dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM \
--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring  \
--conditions MCRUN2_74_V9 \
--magField 38T_PostLS1 \
--step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:@frozen25ns,RAW2DIGI,L1Reco,RECO \
--python_filename step12_bis.py  \
--no_exec \
--fileout file:step2.root \
-n 100
```

## ReMiniAOD -- STEP4

This step may perform some operation like adding the EGamma variables, but will **not** convert from MINIAODv1 to MINIAODv2

* For data:
```
cmsDriver.py step4 --conditions auto:run2_data -n 100 --eventcontent
MINIAOD --filein file:step3.root -s EI:MiniAODfromMiniAOD --datatier
MINIAOD --customise
SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1
--data --no_exec --fileout file:step4.root --processName MINIAODfromMINIAOD
```

* For MC:
```
cmsDriver.py step4 --conditions auto:run2_mc -n 100 --eventcontent
MINIAODSIM --filein file:step3.root -s EI:MiniAODfromMiniAOD --datatier
MINIAODSIM --customise
SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1
--mc --no_exec --fileout file:step4.root --processName MINIAODfromMINIAOD
```

## Step 12 for 76X
```
cmsDriver.py ABC --mc --eventcontent AODSIM --datatier AODSIM  --pileup 2015_25ns_Startup_PoissonOOTPU --pileup_input dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM --era Run2_25ns --conditions auto:run2_mc --magField 38T_PostLS1 --step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:@frozen25ns,RAW2DIGI,L1Reco,RECO --python_filename step12.py --no_exec  --fileout step12.root -n -1
```

## Step 12 for 76X --- MINBIAS
```
cmsDriver.py MCProduction/ThirteenTeV/python/MinBias_13TeV_pythia8_cfi.py --mc --eventcontent AODSIM --datatier AODSIM  --pileup NoPileUp  --era Run2_25ns --conditions auto:run2_mc --magField 38T_PostLS1 --step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:@frozen25ns,RAW2DIGI,L1Reco,RECO --python_filename step12.py --no_exec  --fileout step12.root -n 100
```

## STEP 3  for 76X
Step 3 produces MINIAOD 
```
cmsDriver.py step3 --filein file:step2.root  \
--fileout file:step3.root --mc \
--eventcontent MINIAODSIM  \
--runUnscheduled --datatier MINIAODSIM  \
--conditions auto:run2_mc  \
--step PAT \
--python_filename step3.py  \
--era Run2_25ns \
--no_exec \
-n -1
```

#Grid Submission
## STEP 1
* Go in test, edit crabStep1.py
```
crab submit crabStep1.py
```
