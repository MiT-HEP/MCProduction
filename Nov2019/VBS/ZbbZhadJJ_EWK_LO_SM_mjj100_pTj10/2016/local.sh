#!/bin/bash

DIR=$(mktemp -d)
BASE="/afs/cern.ch/user/a/amarini/work/GenProduction/Fall2017/MCProduction/Nov2019/VBS/ZbbZhadJJ_EWK_LO_SM_mjj100_pTj10/2016"
OUT=$BASE/out
LOG=$BASE/log

cd $DIR
cp -v $BASE/*{sh,py} ./
NUM=1002
while [ -f $BASE/log/log.$NUM.txt ] ; do NUM=$((NUM+1)) ; done

echo "(local.sh) using NUM=$NUM"
./scriptExeGenOnly.sh $NUM 2>&1 | tee $LOG/log.${NUM}.txt
mv -v step1.root $OUT/step1_${NUM}.root
