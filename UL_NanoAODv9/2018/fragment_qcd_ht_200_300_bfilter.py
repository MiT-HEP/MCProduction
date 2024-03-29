import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/madgraph/V5_2.6.5/QCD_bEnriched_HT200to300//v1/QCD_bEnriched_HT200to300_slc7_amd64_gcc700_CMSSW_10_6_8_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(500),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

#Link to datacards:
#https://github.com/cms-sw/genproductions/tree/master/bin/MadGraph5_aMCatNLO/cards/
#production/2017/13TeV/QCD/QCD_bEnriched_HT_LO_MLM/QCD_bEnriched_HT300to500

generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            'JetMatching:setMad = off',
            'JetMatching:scheme = 1',
            'JetMatching:merge = on',
            'JetMatching:jetAlgorithm = 2',
            'JetMatching:etaJetMax = 5.',
            'JetMatching:coneRadius = 1.',
            'JetMatching:slowJetPower = 1',
            'JetMatching:qCut = 14.', #this is the actual merging scale                                                                                         
            'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme                                     
            'JetMatching:nJetMax = 4', #number of partons in born matrix element for highest multiplicity                                                       
            'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching                                                               
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',
                                    'processParameters',
                                    )
    ),
	nAttempts = cms.uint32(22),
    HepMCFilter = cms.PSet(
		filterName = cms.string('PartonShowerBsHepMCFilter'),
        filterParameters = cms.PSet()
	),
)

#LHEfilter = cms.EDFilter("LHEGenericFilter",
#    src = cms.InputTag("externalLHEProducer"),
#    NumRequired = cms.int32(0),
#    ParticleID = cms.vint32(5),
#    AcceptLogic = cms.string("EQ") # LT meaning < NumRequired, GT >, EQ =, NE !=
#)

#ProductionFilterSequence = cms.Sequence(LHEfilter+generator)
