#!/bin/bash

#cat 2018/crab.py | grep 'do==' | cut -d '=' -f 3 | cut -d ':' -f 1 | tr -d "'" | grep -v xxx

LIST="vbs_zjj_zjj_ewk"

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
