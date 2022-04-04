#!/bin/bash


#PT="ewk qcd ewk_qcd"
#PROCESSES="wpjj_wmjj wpmjj_wpmjj zbb_wpmjj zjjnob_wpmjj zjj_zjj znunu_wpmjj znunu_zjj"

#PT="4fqcd"
## 4f QCD

#PT="ewk qcd"
#PROCESSES="wmhad_zlep wmlep_wmhad wmlep_zhad wphad_wmlep wphad_zlep wplep_wmhad wplep_wphad wplep_zhad zlep_zhad"

#PT="4fewk"
#PROCESSES="wpjj_wmjj zbb_wpmjj zjj_wpmjj znunu_wpmjj"

PT="4fewk 4fqcd"
#PROCESSES="wplep_wmhad wphad_wmlep"
PROCESSES="wphad_wmlep"

# make list
LIST=""
for proc in $PROCESSES; do
for pt in $PT; do
        LIST+=" vbs_${proc}_${pt}"
done
done

##################
### AQGC BLOCK ###
##################

#LIST=""
#PROCESSES="wmjj_wmjj wmjj_zjj wpjj_wmjj wpjj_wpjj wpjj_zjj zbb_zjjnob zjj_zjj znunu_zjjnob wmlep_wmhad wmlep_zhad wphad_wmlep wplep_wmhad wplep_wphad wplep_zhad"
#PROCESSES="zbb_zjjnob zjj_zjj znunu_zjjnob"
#for proc in $PROCESSES; do
#        LIST+=" aqgc_${proc}"
#done
##################

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
