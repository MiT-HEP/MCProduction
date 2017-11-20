import FWCore.ParameterSet.Config as cms

#process = cms.Process('HLT')
process = cms.Process('FAKE')

process.load("FWCore.MessageService.MessageLogger_cfi")
# If you run over many samples and you save the log, remember to reduce
# the size of the output by prescaling the report of the event number
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

fileList = []


#process.source = cms.Source("PoolSource",
#    	fileNames = cms.untracked.vstring(fileList)
#    )
process.source = cms.Source("EmptySource"
    )

# ---- define the output file -------------------------------------------
#------------------------------------------------------
process.GEN = cms.OutputModule("PoolOutputModule",
		        fileName = cms.untracked.string('HepMC_GEN.root')
			)

process.p = cms.Path()
process.outpath = cms.EndPath(process.GEN)
