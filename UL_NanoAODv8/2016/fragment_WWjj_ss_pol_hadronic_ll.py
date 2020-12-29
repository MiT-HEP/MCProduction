import os
import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("Pythia8HadronizerFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(1),
    PythiaParameters = cms.PSet(
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings')
    )
)

#print "-> Using gridpack",os.environ['PWD']+"/"+options.gridpack
#if not os.path.isfile(os.environ['PWD']+"/"+options.gridpack): print "ERROR: Unable to find gridpack"
#GRIDPACK=WWjj_ll_hadronic_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz
#GRIDPACK=WWjj_lt_hadronic_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz
#GRIDPACK=WWjj_tt_hadronic_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz
externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    nEvents = cms.untracked.uint32(500),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    numberOfParameters = cms.uint32(1),
    args = cms.vstring(os.environ['PWD']+'/'+"WWjj_ll_hadronic_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz")
)


