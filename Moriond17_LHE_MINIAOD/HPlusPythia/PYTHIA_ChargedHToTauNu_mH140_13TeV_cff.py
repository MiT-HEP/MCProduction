import FWCore.ParameterSet.Config as cms

# Import settings for modules
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            TauolaPolar,
            TauolaDefaultInputCards
            ),
        parameterSets = cms.vstring('Tauola'),
            ),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(processParameters=cms.vstring('Higgs:useBSM = on',
                                'HiggsHchg:coup2H1W = 0.0',
                                '25:m0 = 125.',
                                '35:m0 = 140.',
                                '36:m0 = 140.',
                                '37:m0 = 140.',
                                'HiggsHchg:tanBeta = 30',
                                #'HiggsBSM:allH+- = on',
                                'HiggsBSM:bg2H+-t  = on',
                                '37:onMode = 0',
                                '37:onIfAny = 15',
                                'Tune:pp 5',
                                'Tune:ee 3',
                                'ParticleDecays:limitTau0 = on',
                                'ParticleDecays:tauMax = 10',
                                ),
                                parameterSets = cms.vstring('processParameters'),
                                )
)
