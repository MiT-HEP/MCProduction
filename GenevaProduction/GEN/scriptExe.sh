#!/bin/bash

echo "Running job $1" 
echo "I'll not allow twiks of the pset"

cmsRun -j FrameworkJobReport.xml hepmc2gen.py jobNum=$1

echo "Done"
