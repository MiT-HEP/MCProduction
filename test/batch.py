#!env python

import os, sys
import re
from subprocess import call,check_output

from optparse import OptionParser

usage = ''' Examples:
	\t python batch.py -n 100 -q 1nh -f MCProduction/ThirteenTeV/python/HplusToTauNu_M_500_TuneCUETP8M1_tauola_13TeV_pythia8_cfi.py  -d mysub/step1 --put-in /store/user/amarini/mc/batch/HplusToTauNu-M500/RunII/GEN-SIM-RAW -s step1
	\t python batch.py -n 100 -q 1nh  -d mysub/step2  -e /store/user/amarini/mc/HplusToTauNu-M500/ --put-in /store/user/amarini/mc/batch/HplusToTauNu-M500/RunII/AODSIM -s step2
	\t python batch.py -n 100 -q 1nh  -d mysub/step3  -e /store/user/amarini/mc/HplusToTauNu-M500/ --put-in /store/user/amarini/mc/batch/HplusToTauNu-M500/RunII/MINIAODSIM -s step3
	'''

parser = OptionParser(usage = usage)
parser.add_option("-n" ,"--nJobs", dest="nJobs", type="int",help = "Number of jobs [default=%default]" , default=10)
parser.add_option("-q" ,"--queue", dest="queue", type="string",help = "batch queue [default=%default]" , default="1nh")
parser.add_option("-f" ,"--file", dest="file", type="string",help = "input file [default=%default]" , default="step1.py")
parser.add_option("-d" ,"--dir", dest="dir", type="string",help = "script dir [default=%default]" , default="mysub")
parser.add_option("-e" ,"--eos", dest="eos", type="string",help = "input root files (dir) [default=%default]" , default="/store/...")
parser.add_option("" ,"--put-in", dest="putin", type="string",help = "outputDir (dir) [default=%default]" , default="/store/...")

parser.add_option("-s" ,"--step", dest="step", type="string",help= "step  [default=%default]" , default="step1")
parser.add_option("" ,"--status", dest="status", action="store_true",help= "show status of dir [default=%default]" , default=False)

opts, args = parser.parse_args()

def PrintSummary(dir, doPrint=True):
        ''' Print summary informations for dir'''
	from glob import glob
        run  = glob(dir + "/*run")
        fail = glob(dir + "/*fail")
        done = glob(dir + "/*done")

        ## bash color string
        red="\033[01;31m"
        green = "\033[01;32m"
        yellow = "\033[01;33m"
        white = "\033[00m"

        run = [ re.sub('\.run','' , re.sub('.*/sub_','', r) ) for r in run ]
        fail = [ re.sub('\.fail','' , re.sub('.*/sub_','', r) ) for r in fail ]
        done = [ re.sub('\.done','' , re.sub('.*/sub_','', r) ) for r in done ]

        tot = len(run) + len(fail) + len(done)

        color = red
        if len(run) > len(fail) and len(run) > len(done) : color= yellow
        if len(done) == tot and tot >0 : color = green

        if doPrint:
                print " ----  Directory "+ color+opts.dir+white+" --------"
                print " Run : " + yellow + "%3d"%len(run) + " / "  + str(tot) + white + " : " + PrintLine(run)  ### + ",".join(run)  + "|" 
                print " Fail: " + red    + "%3d"%len(fail) + " / " + str(tot) + white + " : " + PrintLine(fail) ### + ",".join(fail) + "|" 
                print " Done: " + green  + "%3d"%len(done) + " / " + str(tot) + white + " : " + PrintLine(done) ### + ",".join(done) + "|" 
                print " -------------------------------------"

        return ( done, run, fail)

if opts.status:
        PrintSummary(opts.dir)
        exit(0)

PWD=os.getcwd()

## get list of input files
EOS = "/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select"

## check if working directory exists
cmd = "[ -d "+ opts.dir+" ]"
status = call( cmd , shell=True)

if status == 0:
        print "Directory",opts.dir,"already exists"
        cmd =  "rmdir " + opts.dir
        status = call(cmd, shell = True)
        if status !=0:
                print "Directory",opts.dir,"is not empty"
                raise Exception('Directory not empty')

## creating a working directory
cmd = ["mkdir","-p", opts.dir]
call(cmd)

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def chunksNum( l, tot):
    """ Yield successive n-sized chunks form l, in total number tot"""
    if len(l) % tot == 0:
        ChunkSize = len(l) / tot
    else:
        ChunkSize = (len(l) / tot) + 1
    return chunks(l,ChunkSize)


cmd = EOS+ " find -f " + opts.eos
print "Going to call cmd:",cmd
outputList = check_output(cmd,shell=True)
fileList0 = outputList.split() ## change lines into list
fileList = [ '"' + re.sub("/eos/cms","",f) +'"' for f in fileList0 ]


if len(fileList) == 0:
        print "ERROR no file is given"
        if opts.eos != "":
                print "eos cmd was:",cmd

fileChunks = chunksNum(fileList, opts.nJobs)

if opts.eos == "" : 
	fileChunks = [];
	for i in range(0,opts.nJobs):
		fileChunks.append( [] ) 

####### CONFIGURE DRIVER #####
driver = {}

Step1  = "cmsDriver.py "
Step1 += opts.file + " "
#Step1 += "MCProduction/ThirteenTeV/python/HplusToTauNu_M_200_TuneCUETP8M1_tauola_13TeV_pythia8_cfi.py "
Step1 += "--mc "
Step1 += "--eventcontent RAWSIM "
Step1 += "--datatier GEN-SIM-RAW "
Step1 += "--pileup 2015_25ns_Startup_PoissonOOTPU "
Step1 += "--pileup_input dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM "
Step1 += "--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring "
Step1 += "--conditions MCRUN2_74_V9 "
Step1 += "--magField 38T_PostLS1 "
Step1 += "--step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:@frozen25ns "
Step1 += "--python_filename step1.py  "
Step1 += "--fileout file:%%OUT%% "
Step1 += "-n 100 "
driver["step1"]=Step1

Step2= "cmsDriver.py step2 --filein %%FILEIN%% --fileout file:%%OUT%%  "
Step2 += "--mc --eventcontent AODSIM  "
Step2 += "--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring "
Step2 += "--datatier AODSIM --step RAW2DIGI,L1Reco,RECO "
Step2 += "--conditions MCRUN2_74_V9 "
Step2 += "--magField 38T_PostLS1  "
Step2 += "--python_filename step2.py  "
Step2 += "-n -1 "
driver['step2'] = Step2

Step3  = "cmsDriver.py step3 --filein %%FILEIN%%  "
Step3 += "--fileout file:%%OUT%% --mc "
Step3 += "--eventcontent MINIAODSIM  "
Step3 += "--runUnscheduled --datatier MINIAODSIM  "
Step3 += "--conditions MCRUN2_74_V9  "
Step3 += "--step PAT "
Step3 += "--python_filename step3.py  "
Step3 += "--customise Configuration/DataProcessing/Utils.addMonitoring "
Step3 += "-n -1 "
driver['step3'] = Step3

cmdFile = open(opts.dir+"/cmdFile.sh","w")

for idx,fl in enumerate(fileChunks):
	## open a script file
	shName = opts.dir + "/sub_%d.sh"%idx
	sh = open( shName,"w") 
	sh.write("#!/bin/bash\n")
	call("chmod u+x "+ shName , shell=True)
	sh.write("cd %s\n"%PWD)
	sh.write("eval `scramv1 runtime -sh`\n") #cmsenv
	sh.write("touch "+PWD+"/"+opts.dir+"/sub_"+str(idx) + ".run\n")
	sh.write("rm "+PWD+"/"+opts.dir+"/sub_"+str(idx) + ".done\n")
	sh.write("rm "+PWD+"/"+opts.dir+"/sub_"+str(idx) + ".fail\n")
	sh.write('[ "${WORKDIR}" == "" ] && export WORKDIR=/tmp/$USER/ \n') ## make the script work on interactive lxplus
	sh.write('cd $WORKDIR \n' )
	
	cmd = driver[opts.step]	
	fileIn = ','.join(fl)
	cmd = re.sub( "%%FILEIN%%",fileIn,cmd)
	outName = opts.step + "_" + str(idx) + ".root"
	cmd = re.sub("%%OUT%%",outName,cmd)
	
	sh.write(cmd + "\n")
	
	sh.write("EXIT=$?\n")
	sh.write( "cmsMkdir "+ opts.putin + "\n")
	sh.write( "cmsStage -f " + outName + " " +opts.putin + "/ \n")

	sh.write("STAGE=$?\n")

	sh.write("rm "+PWD+"/"+opts.dir+"/sub_"+str(idx) + ".run\n")
	sh.write("[ \"${EXIT}\" == \"0\" ] && [ \"${STAGE}\" == \"0\" ] && touch "+PWD+"/"+opts.dir+"/sub_"+str(idx) + ".done\n")
	sh.write("[ \"${EXIT}\" == \"0\" ] || echo \"exit code : ${EXIT}\"> "+PWD+"/"+opts.dir+"/sub_"+str(idx) + ".fail\n")
	sh.write("[ \"${STAGE}\" == \"0\" ] || echo \"stage code : ${STAGE}\">> "+PWD+"/"+opts.dir+"/sub_"+str(idx) + ".fail\n")


	bsub = "bsub -q " + opts.queue + " -J " + opts.dir + "_"+str(idx) + " "
	bsub += PWD + "/" + shName

	print >> cmdFile, bsub
	print bsub

