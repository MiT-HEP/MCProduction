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
        processParameters = cms.vstring(
                                        '24:onMode = off', 
                                        '24:onIfAny = 1 2 3 4 5 11 13 15',
                                        'ResonanceDecayFilter:filter = on',
 						                'ResonanceDecayFilter:exclusive = off', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
    									'ResonanceDecayFilter:eMuTauAsEquivalent = on',  #on: treat electrons, muons , and taus as equivalent
										'ResonanceDecayFilter:allNuAsEquivalent  = on',  #on: treat all three neutrino flavours as equivalent
                    					'ResonanceDecayFilter:udscbAsEquivalent  = on', #on: treat u,d,s,c,b quarks as equivalent
										'ResonanceDecayFilter:mothers = 24',
                                        'ResonanceDecayFilter:daughters = 11,1', #Require one quark decay and one leptonic decay
                                        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters'
                                    )
    )
)

import os
externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    nEvents = cms.untracked.uint32(500),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    numberOfParameters = cms.uint32(1),
    #args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/DoublyChargedHiggsGMmodel_HWW_M1000/v1/DoublyChargedHiggsGMmodel_HWW_M1000_tarball.tar.xz'),
    args = cms.vstring(os.environ['PWD']+'/DoublyChargedHiggsGMmodel_HWW_M2000_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz'),
)
