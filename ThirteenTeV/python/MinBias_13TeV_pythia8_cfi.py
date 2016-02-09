# Pythia8 fragment for minbias with tune A2MB-MSTW2008LO

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from MCProduction.ThirteenTeV.Pythia8CUETP8M2Settings_MBR_cfi import *

source = cms.Source("EmptySource")

generator = cms.EDFilter("Pythia8GeneratorFilter",
   crossSection = cms.untracked.double(78400000000),
   maxEventsToPrint = cms.untracked.int32(0),
   pythiaPylistVerbosity = cms.untracked.int32(1),
   filterEfficiency = cms.untracked.double(1.0),
   pythiaHepMCVerbosity = cms.untracked.bool(False),
   comEnergy = cms.double(13000.0),
   PythiaParameters = cms.PSet(
       pythia8CommonSettingsBlock,
       pythia8CUETP8M2MBRSettingsBlock,
       processParameters = cms.vstring(
           'Main:timesAllowErrors    = 10000',
           'ParticleDecays:limitTau0 = on',
           'ParticleDecays:tauMax = 10',
           'SoftQCD:nonDiffractive = on',
           'SoftQCD:singleDiffractive = on',
	   'SoftQCD:doubleDiffractive = on',
           ),
       parameterSets = cms.vstring(
	       'pythia8CommonSettings',
	       'pythia8CUETP8M2MBRSettings',
	       'processParameters'
	       )
   )
)

ProductionFilterSequence = cms.Sequence(generator)
