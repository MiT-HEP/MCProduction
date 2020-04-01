#!/bin/bash

LOCAL=$PWD
TMP=`mktemp -d`

cd $TMP
cp -v $LOCAL/*{py,sh} ./

./scriptExe.sh 0

cd $LOCAL
