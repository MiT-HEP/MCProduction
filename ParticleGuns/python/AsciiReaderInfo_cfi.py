import FWCore.ParameterSet.Config as cms

InfoProducer = cms.EDProducer("AsciiReaderInfo",
	fVerbosity = cms.untracked.int32(1),
	fileName = cms.untracked.string("embedding.txt"),
	)

infoProducerSequence     = cms.Sequence( InfoProducer )
