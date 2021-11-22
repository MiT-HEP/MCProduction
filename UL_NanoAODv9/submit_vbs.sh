#!/bin/bash


PT="ewk qcd ewk_qcd"
#PROCESSES="wpjj_wmjj wpmjj_wpmjj zbb_wpmjj zjjnob_wpmjj zjj_zjj znunu_wpmjj znunu_zjj"
PROCESSES="zjj_zjj"

# make list
LIST=""
for proc in $PROCESSES; do
for pt in $PT; do
        LIST+=" vbs_${proc}_${pt}"
done
done

echo Submitting $LIST for all production years
#exit 0
PARALLEL="parallel --semaphore --semaphorename crsub -j 5 "

for year in 2016 2016_HIPM 2017 2018; do
    echo "->Doing year $year"
    pushd $year
    
    for what in $LIST; do
        echo "Doing $what"
        MYNUM=$RANDOM
        [ -f crab_tmp_${MYNUM}.py ] && MYNUM=$RANDOM ## some protection against collisions
        [ -f crab_tmp_${MYNUM}.py ] && MYNUM=$RANDOM
        [ -f crab_tmp_${MYNUM}.py ] && MYNUM=$RANDOM
        MYFILE=crab_tmp_${MYNUM}.py
        cp -v crab.py $MYFILE
        sed -i'' "s/do='xxx'/do='$what'/g" $MYFILE
        $PARALLEL "(crab submit $MYFILE ; rm $MYFILE ; rm ${MYFILE}c )"
    done
    popd
done
