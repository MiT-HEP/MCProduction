#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log
echo " >> Options $2"

chain="$2"

[[ "$2" == "chain=vbs_"* ]] && {
    echo "> VBS Configuration"
    a1=$(echo -n "$2" | cut -d '_' -f 2 )
    a2=$(echo -n "$2" | cut -d '_' -f 3 )
    a3=$(echo -n "$2" | cut -d '_' -f 4,5 )
    
    p1=$( echo $a1 | tr [:lower:] [:upper:] | sed 's:NOB:noB:g' | sed 's:NU:Nu:g' | sed 's:LEP:lep:g' | sed 's:HAD:had:g')
    p2=$( echo $a2 | tr [:lower:] [:upper:] | sed 's:NOB:noB:g' | sed 's:NU:Nu:g' | sed 's:LEP:lep:g' | sed 's:HAD:had:g')
    p3=$( echo $a3 | tr [:lower:] [:upper:] | sed 's:NOB:noB:g' | sed 's:NU:Nu:g' | sed 's:LEP:lep:g' | sed 's:HAD:had:g')

    export GRIDPACK=${p1}${p2}jj_${p3}_LO_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz

    echo $2 | grep -i lep 2>&1 >/dev/null && {
        export GRIDPACK=${p1}${p2}JJ_${p3}_LO_SM_mjj100_pTj10_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz ;
    }

    chain='chain=vbs_all' ## will use the gridpack variable
    echo "> chain is ${chain}"
    echo "> gridpack is ${GRIDPACK}"
    curl --insecure https://amarini.web.cern.ch/amarini/gridpack/$GRIDPACK --retry 2 -o ./$GRIDPACK
    file $GRIDPACK

    file $GRIDPACK | grep 'ASCII' && exit 1

    ls -ltr 
}

[[ "$2" == "chain=aqgc_"* ]] && {

    a1=$(echo -n "$2" | cut -d '_' -f 2 )
    a2=$(echo -n "$2" | cut -d '_' -f 3 )

    p1=$( echo $a1 | tr [:lower:] [:upper:] | sed 's:NOB:noB:g' | sed 's:NU:Nu:g' | sed 's:HAD:had:g' | sed 's:LEP:lep:g' )
    p2=$( echo $a2 | tr [:lower:] [:upper:] | sed 's:NOB:noB:g' | sed 's:NU:Nu:g' | sed 's:HAD:had:g' | sed 's:LEP:lep:g' )
    
    export GRIDPACK=aQGC_${p1}${p2}jj_EWK_LO_NPle1_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz
    echo -n "$2" | grep lep >/dev/null && export GRIDPACK=aQGC_${p1}${p2}JJ_EWK_LO_SM_mjj100_pTj10_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz
    chain='chain=vbs_all' ## will use the gridpack variable
    
    echo "GRIDPACK: $GRIDPACK"
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

[[ "$2" == "chain=mssm_bbahmm"* ]] && {
    chain="chain=mssm_bbahmm"    
    ma=$(echo -n "$2" | cut -d '_' -f 3 | sed 's:ma::g')
    tb=$(echo -n "$2" | cut -d '_' -f 4 | sed 's:tb::g')
    echo "> Configuring chain MA=$ma TB=$tb" 
    sed -i'' "s:^ma=None:ma='$ma':" fragment_mssm_bbahmm.py
    sed -i'' "s:^tb=None:tb='$tb':" fragment_mssm_bbahmm.py
}

[[ "$2" == "chain=mssm_bbhhmm"* ]] && {
    chain="chain=mssm_bbhhmm"    
    ma=$(echo -n "$2" | cut -d '_' -f 3 | sed 's:ma::g')
    tb=$(echo -n "$2" | cut -d '_' -f 4 | sed 's:tb::g')
    echo "> Configuring chain MA=$ma TB=$tb" 
    sed -i'' "s:^ma=None:ma='$ma':" fragment_mssm_bbhhmm.py
    sed -i'' "s:^tb=None:tb='$tb':" fragment_mssm_bbhhmm.py
}


source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700

BASE=$PWD

MYCMSSW=CMSSW_10_6_19
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

MYCMSSW=CMSSW_10_6_20
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

[[ "$2" == "chain=aqgc_"* ]] && {
    ### add aqgc weights to the nano output
    echo "================= Add AQGC branch to nano ====================" | tee -a job.log
# do I need a file: before step6?
    #python addBranch.py  -f 'PARENT' -u step7.root -p step6.root --minME "fs0_m200p00" --maxME "ft9_20p00" 
    python addBranch.py  -f 'PARENT' -u step7.root -p step6.root --minME "fs0_m30p00" --maxME "ft9_20p00" 
    EXIT=$?
    echo " exit status for addBranch is $EXIT"
    [ "$EXIT" != "0" ] && rm FrameworkJobReport.xml
    python <<-EOF || { echo "ERROR. Branch not added Correctly"; rm FrameworkJobReport.xml; } 
import ROOT
import sys
fIn=ROOT.TFile.Open("step7.root")
tIn=fIn.Get("Events")
if tIn.GetLeaf("ft9_20p00"): sys.exit(0)
else: sys.exit(1)
EOF
    
}

echo "================= CMSRUN finished ====================" | tee -a job.log
