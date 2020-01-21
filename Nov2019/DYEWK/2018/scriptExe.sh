#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log
echo "job counting $(($1+2000))"

source /cvmfs/cms.cern.ch/cmsset_default.sh

echo "================= CURL GRIDPACK ===================="| tee -a job.log
curl --insecure https://amarini.web.cern.ch/amarini/LLJJ_EWK_pTj0_SM_5f_LO_ptJ0_MLL_105-160_NNPDF31NNLO_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz --retry 2 -o ./LLJJ_EWK_pTj0_SM_5f_LO_ptJ0_MLL_105-160_NNPDF31NNLO_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz

BASE=$PWD

echo "================= CMSRUN setting up CMSSW_10_2_16_patch2 ===================="| tee -a job.log
export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_16_patch2/src ] ; then 
     echo release CMSSW_10_2_16_patch2 already exists
 else
     scram p CMSSW CMSSW_10_2_16_patch2
 fi
 cd CMSSW_10_2_16_patch2/src
 eval `scram runtime -sh`

cd $BASE

# for my run generic tarball
mv -v run_generic_tarball.sh CMSSW_10_2_16_patch2/src/

echo "================= CMSRUN starting Step 1 ====================" | tee -a job.log
cmsRun -j GenSimAODSim_step1.log step1.py jobNum=$(($1+2000))

echo "================= CMSRUN setting up CMSSW_10_2_5 ===================="| tee -a job.log

if [ -r CMSSW_10_2_5/src ] ; then 
    echo release CMSSW_10_2_5 already exists
else
    scram p CMSSW CMSSW_10_2_5
fi
cd CMSSW_10_2_5/src
eval `scram runtime -sh`

cd $BASE

echo "================= CMSRUN starting Step 2 ====================" | tee -a job.log
cmsRun -j GenSimAODSim_step2.log step2.py 

echo "================= CMSRUN starting Step 3 ====================" | tee -a job.log
cmsRun -j Reco_step3.log step3.py 

echo "================= CMSRUN starting Step 4 ====================" | tee -a job.log
cmsRun -e -j FrameworkJobReport.xml step4.py 

echo "================= CMSRUN finished ====================" | tee -a job.log
