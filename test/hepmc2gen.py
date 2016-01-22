#!/usr/bin/env cmsRun
import FWCore.ParameterSet.Config as cms

process = cms.Process("GEN")

process.source = cms.Source("MCFileSource",
		        fileNames = cms.untracked.vstring('file:hepmc100.dat'),
			)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))


process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'

process.GEN = cms.OutputModule("PoolOutputModule",
		        fileName = cms.untracked.string('HepMC_GEN.root')
			)


process.outpath = cms.EndPath(process.GEN)

### TO DO: add the following
#* merge the following branch (turn off the MT in g4, mv the stuff below from string to input tag)
# amarini/cmssw topic_genevamc 
# add the following line after the sim and digi loading
#process.g4SimHits.HepMCProductLabel = cms.InputTag("source","","GEN")
#process.g4SimHits.Generator.HepMCProductLabel = cms.InputTag("source","","GEN")
#process.genParticles.src=  cms.InputTag("source","","GEN")


### ADD in the different step the following
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
#process.nero.generator = cms.InputTag("source","generator")
#process.InfoProducer.generator = cms.InputTag("source","generator")
