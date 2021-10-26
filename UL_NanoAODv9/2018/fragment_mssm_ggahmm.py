
import FWCore.ParameterSet.Config as cms

# link to cards:
# https://github.com/cms-sw/genproductions/tree/master/bin/Powheg/production/2017/13TeV/Higgs/MSSM/ggA_MuMu_NNPDF31_13TeV

ma=None
tb=None
print "> Loading Configuration for MA",ma,"TB",tb

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/powheg/V2/slc7_amd64_gcc700_CMSSW_10_6_19_MSSMGluGluToAToMuMu_ma130_tb40/v1/slc7_amd64_gcc700_CMSSW_10_6_19_MSSMGluGluToAToMuMu_ma'+ma+'_tb'+tb+'.tgz'),
    nEvents = cms.untracked.uint32(500),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)


from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *
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
        pythia8PowhegEmissionVetoSettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
                                                                                                                                                                                                       
    'Higgs:useBSM = on',
    'POWHEG:nFinal = 1',
    '35:onMode = off', # turn OFF all H decays
    '35:onIfMatch = 13 -13', # turn ON H->tautau

            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PowhegEmissionVetoSettings',
                                    'pythia8PSweightsSettings',
                                    'processParameters'
                                    )
        )
                         )
                         
ProductionFilterSequence = cms.Sequence(generator)
