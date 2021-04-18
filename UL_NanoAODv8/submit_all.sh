#!/bin/bash

#cat 2018/crab.py | grep 'do==' | cut -d '=' -f 3 | cut -d ':' -f 1 | tr -d "'" | grep -v xxx

#LIST="hbbg vbf-hbbg hwz1500 hwz1000 hwz2000 hww1500 hww1000 hww2000 hwz_zbb_1500 hwz_zbb_1000 hwz_zbb_2000 WWjj_ss_pol_hadronic_ll WWjj_ss_pol_hadronic_lt WWjj_ss_pol_hadronic_tt hwz3000 hww3000 hwz_zbb_3000 hww1000_semilep hww2000_semilep"
LIST="vbs_wpjj_wmjj_ewk vbs_wpmjj_wpmjj_ewk vbs_zbb_wpmjj_ewk vbs_zjj_zjj_ewk vbs_znn_wpmjj_ewk"
LIST+=" vbs_wpjj_wmjj_qcd vbs_wpmjj_wpmjj_qcd vbs_zbb_wpmjj_qcd vbs_zjj_zjj_qcd vbs_znn_wpmjj_qcd"
LIST+=" vbs_wpjj_wmjj_ewk_qcd vbs_wpmjj_wpmjj_ewk_qcd vbs_zbb_wpmjj_ewk_qcd vbs_zjj_zjj_ewk_qcd vbs_znn_wpmjj_ewk_qcd"
LIST+=" vbs_hbb_wpmjj_ewk vbs_hbb_wpmjj_qcd"

for year in 2016 2017 2018; do
    echo "->Doing year $year"
    pushd $year
    
    for what in $LIST; do
        echo "Doing $what"
        cp -v crab.py crab_tmp.py
        sed -i'' "s/do='xxx'/do='$what'/g" crab_tmp.py
        crab submit crab_tmp.py
        rm crab_tmp.py
    done
    popd
done
