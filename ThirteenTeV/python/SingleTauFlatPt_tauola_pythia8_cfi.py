import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8PtGun",
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
	#
	#

        PGunParameters = cms.PSet(
            ParticleID = cms.vint32([15,-15]),
	    AddAntiParticle = cms.bool(True),
            MinPhi = cms.double(-3.14159265359),
            MaxPhi = cms.double(3.14159265359), ## in radians
            MinEta = cms.double(-2.1),
            MaxEta = cms.double(2.1),
            MinPt = cms.double(50.), # in GeV
            MaxPt = cms.double(2000.) # 2 TeV
        ),

        Verbosity = cms.untracked.int32(0), ## set to 1 (or greater)  for printouts

        pythiaTauJets = cms.vstring(
                        'ParticleDecays:sophisticatedTau = 2',
                        'ParticleDecays:tauPolarization = 0',
                        "15:onMode = off",
                        "15:onIfAny = 211 -211 321 -321" # turn on if there is a charged k or pi in the decay products 
                        ),
        #
        parameterSets = cms.vstring(
                        'pythia8CommonSettings',
                        #'pythia8CUEP8M1Settings', # not applicable for taus
                        'pythiaTauJets'
                        ),
        #
        PythiaParameters = cms.PSet(parameterSets = cms.vstring())
)

