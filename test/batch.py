#!env python

import os, sys
import re
from subprocess import call,check_output

from optparse import OptionParser

from library import *

usage = ''' Examples:
	\t python batch.py -n 100 -q 1nh -f MCProduction/ThirteenTeV/python/HplusToTauNu_M_500_TuneCUETP8M1_tauola_13TeV_pythia8_cfi.py  -d mysub/step1 --put-in /store/user/amarini/mc/batch/HplusToTauNu-M500/RunII/GEN-SIM-RAW -s step1
	\t python batch.py -n 100 -q 1nh  -d mysub/step2  -e /store/user/amarini/mc/HplusToTauNu-M500/ --put-in /store/user/amarini/mc/batch/HplusToTauNu-M500/RunII/AODSIM -s step2
	\t python batch.py -n 100 -q 1nh  -d mysub/step3  -e /store/user/amarini/mc/HplusToTauNu-M500/ --put-in /store/user/amarini/mc/batch/HplusToTauNu-M500/RunII/MINIAODSIM -s step3
	\t python batch.py -n 100 -q 1nh -d mysub/step4 -e /store/user/amarini/mc/HplusToTauNu-M500/ --put-in /store/user/amarini/mc/MINIAODv2 -s step4
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
parser.add_option("" ,"--follow", dest="follow", action="store_true",help= "follow eos directory, and if new files are created look into submission [default=%default]" , default=False)
parser.add_option("" ,"--dryrun", dest="dryrun", action="store_true",help= "do not submit jobs [default=%default]" , default=False)

opts, args = parser.parse_args()

if opts.status:
        PrintSummary(opts.dir)
        exit(0)

PWD=os.getcwd()

## get list of input files

## check if working directory exists
status = CheckDir(opts.dir)

if status == 0 and not opts.follow:
      print "Directory",opts.dir,"is not empty"
      raise Exception('Directory not empty')

## creating a working directory
MkDir(opts.dir)

if opts.eos != "":
	fileList=GetEosFileList(opts.eos)
else:
	fileList = []

if len(fileList) == 0 and opts.eos != "" and not opts.eos.startswith("dbs:"):
        print "ERROR no file is given"
	raise Exception('No file tu run')

if opts.follow:
	## jobN file
	maxn,fileList = ReadFromDatabase(opts.dir + "/database.txt",fileList )

fileChunks = chunksNum(fileList, opts.nJobs)

if opts.eos == "" or opts.eos.startswith("dbs:"): 
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

Step4 = "cmsDriver.py step4 --conditions auto:run2_mc -n -1 --eventcontent MINIAODSIM --filein %%FILEIN%% "
Step4 += " -s EI:MiniAODfromMiniAOD --datatier MINIAODSIM "
Step4 += " --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --mc "
Step4 += " --fileout file:%%OUT%% --processName MINIAODfromMINIAOD "
Step4 += " --python_filename step4.py"
driver['step4']= Step4

StepLHE  = "cmsDriver.py "
StepLHE += "Configuration/GenProduction/python/ThirteenTeV/Hadronizer_MgmMatchTune4C_13TeV_madgraph_pythia8_Tauola_cff.py "
#StepLHE += "--filein dbs:/TTZJets_Tune4C_13TeV-madgraph-tauola/Fall13pLHE-START62_V1-v1/GEN "
StepLHE += "--filein %%FILEIN%% "
StepLHE += "--mc " 
StepLHE += "--eventcontent AODSIM " 
StepLHE += "--datatier AODSIM " 
StepLHE += "--pileup 2015_25ns_Startup_PoissonOOTPU " 
StepLHE += "--pileup_input dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM " 
StepLHE += "--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring  " 
StepLHE += "--conditions MCRUN2_74_V9 " 
StepLHE += "--magField 38T_PostLS1 " 
StepLHE += "--step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:@frozen25ns,RAW2DIGI,L1Reco,RECO " 
StepLHE += "--python_filename stepLHE.py --fileout file:%%OUT%% "
StepLHE += "-n 500 "
driver["stepLHE"]=StepLHE

cmdFile = open(opts.dir+"/cmdFile.sh","a")

for idx,fl in enumerate(fileChunks):
	if opts.follow:
		idx += maxn
		for f in fl:
			WriteIntoDatabase( opts.dir + "/database.txt" ,idx,f)
	## open a script file
	shName,sh = OpenSh(opts.dir,idx)
	BeginJobStatusFiles(sh,opts.dir,idx)
	CdWorkDir(sh)
	
	cmd = driver[opts.step]	
	fileIn = ','.join(fl)
	if fileIn != "" : cmd = re.sub( "%%FILEIN%%",fileIn,cmd)
	elif opts.eos.startswith("dbs:"):cmd = re.sub( "%%FILEIN%%",opts.eos,cmd)
	outName = opts.step + "_" + str(idx) + ".root"
	cmd = re.sub("%%OUT%%",outName,cmd)
	
	sh.write(cmd + "\n")
	
	sh.write("EXIT=$?\n")
	sh.write( "cmsMkdir "+ opts.putin + "\n")
	sh.write( "cmsStage -f " + outName + " " +opts.putin + "/ \n")

	sh.write("STAGE=$?\n")

	EndJobStatusFiles(sh,opts.dir,idx)	

	bsub =BsubCmd(opts.queue,opts.dir,idx)

	print >> cmdFile, bsub

	print bsub
	if not opts.dryrun: 
		call(bsub,shell=True)

