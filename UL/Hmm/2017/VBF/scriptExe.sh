#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700

BASE=$PWD

function setup
{
    echo "================= CMSRUN setting up $1 ===================="| tee -a job.log
    if [ -r $1/src ] ; then 
     echo release $1 already exists
    else
     scram p CMSSW $1
    fi
    cd $1/src
    eval `scram runtime -sh`
    scram b 
    cd $BASE
}

function clean
{
    echo "--> cleaning up $1"
    rm -v $1
}

setup CMSSW_10_6_4

echo "================= CMSRUN starting Step 1 ====================" | tee -a job.log
cmsRun -j step1.log step1_cfg.py jobNum=$1

setup CMSSW_10_6_2

echo "================= CMSRUN starting Step 2 ====================" | tee -a job.log
cmsRun -j step2.log step2_cfg.py

clean step1.root 

echo "================= CMSRUN starting Step 3 ====================" | tee -a job.log
cmsRun -j step3.log step3_cfg.py

clean step2.root 

setup CMSSW_9_4_14_UL_patch1

echo "================= CMSRUN starting Step 4 ====================" | tee -a job.log
cmsRun -j step4.log step4_cfg.py

clean step3.root 

setup CMSSW_10_6_2

echo "================= CMSRUN starting Step 5 ====================" | tee -a job.log
cmsRun -j step5.log step5_cfg.py

clean step4.root 

echo "================= CMSRUN starting Step 6 ====================" | tee -a job.log
cmsRun -e -j FrameworkJobReport.xml step6_cfg.py


echo "================= CMSRUN finished ====================" | tee -a job.log
