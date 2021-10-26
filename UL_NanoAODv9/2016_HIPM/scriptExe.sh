#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log

chain="$2"
#[[ "$2" == "chain=WWjj_ss_pol_hadronic"* ]] && 
[[ "$2" == "chain=vbs_zjj_zjj_ewk"* ]] && {
    echo "================= CURL GRIDPACK ===================="| tee -a job.log
    
    #[ "$2" == "chain=WWjj_ss_pol_hadronic_ll" ] && export GRIDPACK=WWjj_ll_hadronic_slc7_amd64_gcc820_CMSSW_9_3_16_tarball.tgz
    #[ "$2" == "chain=WWjj_ss_pol_hadronic_lt" ] && export GRIDPACK=WWjj_lt_hadronic_slc7_amd64_gcc820_CMSSW_9_3_16_tarball.tgz
    #[ "$2" == "chain=WWjj_ss_pol_hadronic_tt" ] && export GRIDPACK=WWjj_tt_hadronic_slc7_amd64_gcc820_CMSSW_9_3_16_tarball.tgz

    [ "$2" == "chain=vbs_zjj_zjj_ewk" ] && export GRIDPACK=ZJJZJJjj_EWK_LO_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz
    
    curl --insecure https://amarini.web.cern.ch/amarini/gridpack/$GRIDPACK --retry 2 -o ./$GRIDPACK

    file $GRIDPACK

    file $GRIDPACK | grep 'ASCII' && exit 1

    ls -ltr 
}

[[ "$2" == "chain=mssm_gghhmm"* ]] && {
    chain="chain=mssm_gghhmm"    
    ma=$(echo -n "$2" | cut -d '_' -f 3 | sed 's:ma::g')
    tb=$(echo -n "$2" | cut -d '_' -f 4 | sed 's:tb::g')
    echo "> Configuring chain MA=$ma TB=$tb" 
    sed -i'' "s:^ma=None:ma='$ma':" fragment_mssm_gghhmm.py
    sed -i'' "s:^tb=None:tb='$tb':" fragment_mssm_gghhmm.py
}

[[ "$2" == "chain=mssm_ggahmm"* ]] && {
    chain="chain=mssm_ggahmm"    
    ma=$(echo -n "$2" | cut -d '_' -f 3 | sed 's:ma::g')
    tb=$(echo -n "$2" | cut -d '_' -f 4 | sed 's:tb::g')
    echo "> Configuring chain MA=$ma TB=$tb" 
    sed -i'' "s:^ma=None:ma='$ma':" fragment_mssm_ggahmm.py
    sed -i'' "s:^tb=None:tb='$tb':" fragment_mssm_ggahmm.py
}


source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700

BASE=$PWD

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


echo "================= CMSRUN starting Step 1 ====================" | tee -a job.log
cmsRun -j step1.log step1_cfg.py jobNum=$1 $chain

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

MYCMSSW=CMSSW_8_0_33_UL
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

MYCMSSW=CMSSW_10_6_25
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

echo "================= CMSRUN starting Step 6 ====================" | tee -a job.log
#cmsRun -e -j FrameworkJobReport.xml step6_cfg.py
cmsRun -j step6.log step6_cfg.py

MYCMSSW=CMSSW_10_6_26 
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
