#!/usr/bin/env cmsRun

## Original Author: Andrea Carlo Marini
## Porting to 92X HepMC 2 Gen 
## Date of porting: Mon Jul  3 11:52:22 CEST 2017
## Example of hepmc -> gen file

import os,sys, random
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')
options.register('jobNum', 0, VarParsing.multiplicity.singleton,VarParsing.varType.int,"jobNum")
options.parseArguments()

if True:
    ## collect informations
    from subprocess import call, check_output
    import threading
    import time
    def call_exe(cmd):
        print "-> Executing cmd: '"+cmd+"'"
        st=call(cmd,shell=True)
        print "-> End cmd: status=",st
        return
    print '-> You are using a 2 process file to unzip/untar events on the fly'

    ## define stuff
    filename="/tmp/"+os.environ['USER']+"/hepmc_%d.dat"%options.jobNum
    #input_filename0="/eos/theory/user/a/alioli/geneva/CMS/DY_mumu_13TEV_PDF4LHCNNLO100_Mll_50_150_as118/hepmcDY_mumu_13TEV_PDF4LHCNNLO100_Mll_50_150_as118_scale_MTll_run%d.dat.gz"%(options.jobNum +1)
    #input_filename0="/eos/theory/user/a/alioli/geneva/CMS/DY_mumu_13TEV_PDF4LHCNNLO100_Mll_50_150_as118/hepmcDY_mumu_13TEV_PDF4LHCNNLO100_Mll_50_150_as118_scale_MTll_CUETP8M1_run%d.dat.gz"%(options.jobNum+1)
    #input_filename0="/store/group/phys_smp/genevamc/v03/DY_mumu_13TEV_PDF4LHCNNLO100_Mll_50_150_as118/HepMC/hepmcDY_mumu_13TEV_PDF4LHCNNLO100_Mll_50_150_as118_scale_MTll_run%d.dat.gz"%(options.jobNum +1)

    #input_filename="hepmcDY_mumu_13TEV_PDF4LHCNNLO100_Mll_50_150_as118_scale_MTll_run%d.dat.gz"%(options.jobNum +1)

    ## try to eos cp
    #cmd="gfal-copy -p -v  gsiftp://eoscmsftp.cern.ch//eos/cms"+input_filename0 + " file://" +os.environ["PWD"]+ "/"+input_filename
    #cmd="eos root://eospublic cp "+input_filename0 +" ./"
    #print "-> Executing cmd '"+cmd+"'"
    #st=call(cmd,shell=True)
    #print "   * Copy Status = ",st

    ## not copy use eos, whitelist CERN
    input_filename="/eos/theory/user/a/alioli/geneva/CMS/DY_mumu_13TEV_PDF4LHCNNLO100_Mll_50_150_as118/hepmcDY_mumu_13TEV_PDF4LHCNNLO100_Mll_50_150_as118_scale_MTll_CUETP8M1_run%d.dat.gz"%(options.jobNum+1)
\
    ## rm fifo
    cmd="rm " + filename
    print "-> Executing cmd '"+cmd+"'"
    call(cmd,shell=True)

    ## mkdir 
    cmd="mkdir -p /tmp/"+os.environ['USER'] 
    print "-> Executing cmd '"+cmd+"'"
    call(cmd,shell=True)

    ## mkfifo
    cmd="mkfifo " + filename
    print "-> Executing cmd '"+cmd+"'"
    call(cmd,shell=True)

    #prepare cmd to unzip on the fly
    exe="cat "+input_filename+" | gunzip -c > "+filename+" &"
    t = threading.Thread(target=call_exe, args= ( [exe] )  )
    t.start()
    print "(sleep 1s to allow start of pipes)"
    time.sleep(1)


import FWCore.ParameterSet.Config as cms

process = cms.Process("GEN")

## 100k evnts per file ?
firstLumi=1000*options.jobNum+1 

process.source = cms.Source("MCFileSource",
		    #fileNames = cms.untracked.vstring('file:hepmc100.dat'),
			fileNames = cms.untracked.vstring('file:' + filename),
            firstLuminosityBlock  = cms.untracked.uint32(firstLumi),
            numberEventsInLuminosityBlock = cms.untracked.uint32(100)
			)

maxEvents=options.maxEvents
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(maxEvents))


process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'

if False:
    import FWCore.PythonUtilities.LumiList as LumiList
    print "-> UPDATE THE LUMI LIST"
    process.source.lumisToProcess = LumiList.LumiList(filename='lumi_test.json').getVLuminosityBlockRange()

process.GEN = cms.OutputModule("PoolOutputModule",
		        #fileName = cms.untracked.string('HepMC_GEN_%d.root'%options.jobNum)
		        fileName = cms.untracked.string('HepMC_GEN.root')
			)


process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.genParticles.src= cms.InputTag("source","generator")


######### Smearing Vertex example

#from IOMC.EventVertexGenerators.VtxSmearedParameters_cfi import GaussVtxSmearingParameters,VtxSmearedCommon
from IOMC.EventVertexGenerators.VtxSmearedParameters_cfi import *
VtxSmearedCommon.src=cms.InputTag("source","generator")
#process.generatorSmeared = cms.EDProducer("GaussEvtVtxGenerator",
#    GaussVtxSmearingParameters,
#    VtxSmearedCommon
#    )
process.generatorSmeared  = cms.EDProducer("BetafuncEvtVtxGenerator",
            Realistic50ns13TeVCollisionVtxSmearingParameters,
            VtxSmearedCommon
            )

process.load('Configuration.StandardSequences.Services_cff')
process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
            generatorSmeared  = cms.PSet( initialSeed = cms.untracked.uint32(1243987),
            engineName = cms.untracked.string('TRandom3'),
            ),
        )


###################
process.p = cms.Path(process.genParticles * process.generatorSmeared)
process.outpath = cms.EndPath(process.GEN)

### TO DO: add the following
# (amarini/hepmc_portTo9X)
# add the following line after the sim and digi loading
# generator needs to be smeared if you want vertex smearing, you'll have:
#       Type                                  Module               Label         Process   
#       -----------------------------------------------------------------------------------
#       GenEventInfoProduct                   "source"             "generator"   "GEN"     
#       edm::HepMCProduct                     "generatorSmeared"   ""            "GEN"     
#       edm::HepMCProduct                     "source"             "generator"   "GEN"   
# NOT needed to be changed if you smear the generator
#process.g4SimHits.HepMCProductLabel = cms.InputTag("source","generator","GEN")
#process.g4SimHits.Generator.HepMCProductLabel = cms.InputTag("source","generator","GEN")
#process.genParticles.src=  cms.InputTag("source","generator","GEN")


### ADD in the different step the following  (always!)
#
#process.AODSIMoutput.outputCommands.extend([
#		'keep GenRunInfoProduct_*_*_*',
#        	'keep GenLumiInfoProduct_*_*_*',
#		'keep GenEventInfoProduct_*_*_*',
#		])
#
#process.MINIAODSIMoutput.outputcommands.extend([
#       'keep GenRunInfoProduct_*_*_*',
#       'keep GenLumiInfoProduct_*_*_*',
#       'keep GenEventInfoProduct_*_*_*',
#	])
#
# and finally in the ntuples
#process.myanalyzer.generator = cms.InputTag("source","generator")
