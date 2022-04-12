import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/madgraph/V5_2.6.5/ggh012j_5f_NLO/ggh012j_5f_NLO_FXFX_125_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(500),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.Pythia8aMCatNLOSettings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *


generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8aMCatNLOSettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            'JetMatching:setMad = off',
            'JetMatching:scheme = 1',
            'JetMatching:merge = on',
            'JetMatching:jetAlgorithm = 2',
            'JetMatching:etaJetMax = 999.',
            'JetMatching:coneRadius = 1.',
            'JetMatching:slowJetPower = 1',
            'JetMatching:qCut = 30.', #this is the actual merging scale
            'JetMatching:doFxFx = on',
            'JetMatching:qCutME = 10.',#this must match the ptj cut in the lhe generation step
            'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
            'JetMatching:nJetMax = 2', #number of partons in born matrix element for highest multiplicity
            'SLHA:useDecayTable = off',
            '25:m0 = 125.0',
            '25:onMode = off', 
            #'25:onIfAny = 5 -5',        
            '25:onIfMatch = 23 22', ## Z gamma
            '23:mMin = 50.0',
            '23:onMode = off',
            '23:onIfMatch = 5 -5',
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
            'pythia8CP5Settings',
            'pythia8aMCatNLOSettings',
            'pythia8PSweightsSettings',
            'processParameters',
        )
    )
)

ProductionFilterSequence = cms.Sequence(generator)
