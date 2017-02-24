#!/bin/bash
echo "Running JOB=$1"
cmsRun -j FrameworkJobReport.xml PSet.py jobNum=$1

