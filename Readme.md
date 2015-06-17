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
Step 3 produces MINIAOD out of them (CMSSW_7_4_5)
```
cmsDriver.py step3 --filein file:step2.root  \
--fileout file:step3.root --mc \
--eventcontent MINIAODSIM  \
--runUnscheduled --datatier MINIAODSIM  \
--conditions MCRUN2_74_V9  \
--step PAT \
--python_filename step3.py  \
--customise Configuration/DataProcessing/Utils.addMonitoring \
-n 10 
```

#Grid Submission
## STEP 1
* Go in test, edit crabStep1.py
```
crab submit crabStep1.py
```
