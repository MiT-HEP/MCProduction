#!/bin/bash

#cat 2018/crab.py | grep 'do==' | cut -d '=' -f 3 | cut -d ':' -f 1 | tr -d "'" | grep -v xxx

#LIST="mssm_gghhmm_ma1000_tb10"
#LIST="mssm_ggahmm_ma1000_tb10"

PROCESSES="ggh gga"
TB="2 5 10 15 20 25 30 35 40 50 60"
MA="130 150 170 200 250 300 350 400 500 600 700 800 1000 1200 1500"

# make list
LIST=""
for proc in $PROCESSES; do
for ma in $MA; do
    for tb in $TB; do
        LIST+=" mssm_${proc}hmm_ma${ma}_tb${tb}"
done
done
done

echo Submitting $LIST for all production years
#exit 0
NOBJS="parallel --semaphore --semaphorename crsub -j 15 "

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
