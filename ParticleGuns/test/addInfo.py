import FWCore.ParameterSet.Config as cms

process= cms.Process("INFO")

process.load("MCProduction.ParticleGuns.AsciiReaderInfo_cfi")
################### DEFINE MY PROCESS 
### process.InfoProducer = cms.EDProducer("AsciiReaderInfo",
### 		fVerbosity = cms.untracked.int32(1),
### 		fileName = cms.untracked.string("embedding.txt"),
### 		)
### 
### process.infoProducerSequence     = cms.Sequence( InfoProducer )
### 
#################### ACCESSORIES

process.load('FWCore.MessageService.MessageLogger_cfi')

process.source = cms.Source("PoolSource",
		fileNames = cms.untracked.vstring(['file:step3.root'])
		)

process.maxEvents = cms.untracked.PSet(  input= cms.untracked.int32(-1)              )


process.p = cms.Path( process.infoProducerSequence  )

process.output = cms.OutputModule(
		        "PoolOutputModule",
		        SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')),
		        fileName = cms.untracked.string('step4.root'),
										                           )
process.output_step = cms.EndPath(process.output)

