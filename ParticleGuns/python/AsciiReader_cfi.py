import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("AsciiReaderGun",
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
	#
	#
        PGunParameters = cms.PSet(
			fileName = cms.string("embedding.txt"),
			ParticleID = cms.vint32(15),  ### who use it -- Py8GunBase. NOT USED
			MinPhi     = cms.double(-3.14159265358979323846), ## NOT USED
	   		MaxPhi     = cms.double( 3.14159265358979323846), ## NOT USED
        		),
	#
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
	#
        )
