#!/bin/bash

#cat 2018/crab.py | grep 'do==' | cut -d '=' -f 3 | cut -d ':' -f 1 | tr -d "'" | grep -v xxx

#LIST="vbs_zjj_zjj_ewk"
LIST="qcd_ht_100_200_bfilter qcd_ht_200_300_bfilter qcd_ht_300_500_bfilter qcd_ht_500_700_bfilter qcd_ht_700_1000_bfilter qcd_ht_1000_1500_bfilter qcd_ht_1500_2000_bfilter qcd_ht_2000_Inf_bfilter"

for year in 2016 2016_HIPM 2017 2018; do
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
