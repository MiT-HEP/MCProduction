#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log

[[ "$2" == "chain=WWjj_ss_pol_hadronic"* ]] && {
    echo "================= CURL GRIDPACK ===================="| tee -a job.log
    
    [ "$2" == "chain=WWjj_ss_pol_hadronic_ll" ] && export GRIDPACK=WWjj_ll_hadronic_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tgz
    [ "$2" == "chain=WWjj_ss_pol_hadronic_lt" ] && export GRIDPACK=WWjj_lt_hadronic_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tgz
    [ "$2" == "chain=WWjj_ss_pol_hadronic_tt" ] && export GRIDPACK=WWjj_tt_hadronic_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tgz
    
    curl --insecure https://amarini.web.cern.ch/amarini/$GRIDPACK --retry 2 -o ./$GRIDPACK

    ls -ltr 
}

[[ "$2" == "chain=hplusplus"* ]] && {
    ## copy GRIDPACKS locally and rename them in tgz
    cp -v /cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/DoublyChargedHiggsGMmodel_HWW_M1000/v1/DoublyChargedHiggsGMmodel_HWW_M1000_tarball.tar.xz ./DoublyChargedHiggsGMmodel_HWW_M1000_tarball.tgz
    cp -v /cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/DoublyChargedHiggsGMmodel_HWW_M2000/v1/DoublyChargedHiggsGMmodel_HWW_M2000_tarball.tar.xz ./DoublyChargedHiggsGMmodel_HWW_M2000_tarball.tgz
    cp -v /cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/DoublyChargedHiggsGMmodel_HWW_M1500/v1/DoublyChargedHiggsGMmodel_HWW_M1500_tarball.tar.xz ./DoublyChargedHiggsGMmodel_HWW_M1500_tarball.tgz
}

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700

BASE=$PWD

MYCMSSW=CMSSW_10_6_18
STEP1=step1_cfg.py
[[ "$2" == "chain=hplusplus"* ]] && { 
    export SCRAM_ARCH=slc6_amd64_gcc481 
    MYCMSSW=CMSSW_7_1_26
    STEP1=step1_71_cfg.py
}
[[ "$2" == "chain=hbbg" ]] && export SCRAM_ARCH=slc6_amd64_gcc630

    echo "================= CMSRUN setting up $MYCMSSW ===================="| tee -a job.log
    if [ -r $MYCMSSW/src ] ; then 
     echo release $MYCMSSW already exists
    else
     scram p CMSSW $MYCMSSW
    fi
    cd $MYCMSSW/src
    eval `scram runtime -sh`
    scram b 
    cd $BASE


echo "================= CMSRUN starting Step 1 ====================" | tee -a job.log
cmsRun -j step1.log $STEP1 jobNum=$1 $2

export SCRAM_ARCH=slc7_amd64_gcc700
MYCMSSW=CMSSW_10_6_17_patch1
    echo "================= CMSRUN setting up $MYCMSSW ===================="| tee -a job.log
    if [ -r $MYCMSSW/src ] ; then 
     echo release $MYCMSSW already exists
    else
     scram p CMSSW $MYCMSSW
    fi
    cd $MYCMSSW/src
    eval `scram runtime -sh`
    scram b 
    cd $BASE

echo "================= CMSRUN starting Step 2 ====================" | tee -a job.log
cmsRun -j step2.log step2_cfg.py

CLEAN=step1.root
    echo "--> cleaning up $CLEAN"
    rm -v $CLEAN

MYCMSSW=CMSSW_10_6_17_patch1
    echo "================= CMSRUN setting up $MYCMSSW ===================="| tee -a job.log
    if [ -r $MYCMSSW/src ] ; then 
     echo release $MYCMSSW already exists
    else
     scram p CMSSW $MYCMSSW
    fi
    cd $MYCMSSW/src
    eval `scram runtime -sh`
    scram b 
    cd $BASE

echo "================= CMSRUN starting Step 3 ====================" | tee -a job.log
cmsRun -j step3.log step3_cfg.py

CLEAN=step2.root
    echo "--> cleaning up $CLEAN"
    rm -v $CLEAN

MYCMSSW=CMSSW_10_2_16_UL
    echo "================= CMSRUN setting up $MYCMSSW ===================="| tee -a job.log
    if [ -r $MYCMSSW/src ] ; then 
     echo release $MYCMSSW already exists
    else
     scram p CMSSW $MYCMSSW
    fi
    cd $MYCMSSW/src
    eval `scram runtime -sh`
    scram b 
    cd $BASE

echo "================= CMSRUN starting Step 4 ====================" | tee -a job.log
cmsRun -j step4.log step4_cfg.py

CLEAN=step3.root
    echo "--> cleaning up $CLEAN"
    rm -v $CLEAN

MYCMSSW=CMSSW_10_6_17_patch1
    echo "================= CMSRUN setting up $MYCMSSW ===================="| tee -a job.log
    if [ -r $MYCMSSW/src ] ; then 
     echo release $MYCMSSW already exists
    else
     scram p CMSSW $MYCMSSW
    fi
    cd $MYCMSSW/src
    eval `scram runtime -sh`
    scram b 
    cd $BASE

echo "================= CMSRUN starting Step 5 ====================" | tee -a job.log
cmsRun -j step5.log step5_cfg.py

CLEAN=step4.root
    echo "--> cleaning up $CLEAN"
    rm -v $CLEAN

echo "================= CMSRUN starting Step 6 ====================" | tee -a job.log
#cmsRun -e -j FrameworkJobReport.xml step6_cfg.py
cmsRun -j step6.log step6_cfg.py

MYCMSSW=CMSSW_10_6_19_patch2
    echo "================= CMSRUN setting up $MYCMSSW ===================="| tee -a job.log
    if [ -r $MYCMSSW/src ] ; then 
     echo release $MYCMSSW already exists
    else
     scram p CMSSW $MYCMSSW
    fi
    cd $MYCMSSW/src
    eval `scram runtime -sh`
    scram b 
    cd $BASE

echo "================= CMSRUN starting Step 7 ====================" | tee -a job.log
cmsRun -e -j FrameworkJobReport.xml step7_cfg.py

echo "================= CMSRUN finished ====================" | tee -a job.log
