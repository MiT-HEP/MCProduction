import FWCore.ParameterSet.Config as cms

# link to cards:
# https://github.com/cms-sw/genproductions/tree/7282e21844f34c9ce1c242356bd78443593d80a6/bin/MadGraph5_aMCatNLO/cards/production/13TeV/higgs/ggh012j_5f_NLO_FXFX_125

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.2.2/ggh012j_5f_NLO_FXFX_125/v1/ggh012j_5f_NLO_FXFX_125_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(500),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)
