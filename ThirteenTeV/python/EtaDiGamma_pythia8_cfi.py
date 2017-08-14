import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    displayPythiaCards = cms.untracked.bool(False),
    filterEfficiency = cms.untracked.double(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),

    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
		processParameters = cms.vstring(
			'SoftQCD:all = on',
			#'HardQCD:all = on',
			#'WeakSingleBoson:ffbar2gmZ = on',
		#	'23:onMode = off',
		#	'23:onIfMatch = 13 -13'
			'221:onMode = off',
			'221:onIfAny = 13 -13 22 13 -13',
			'223:onMode = off',
			'223:onIfAny = 13 -13',
			'333:onMode = off',
			'333:onIfAny = 13 -13',
			#'113:onMode = off',
			#'113:onIfAny = 13 -13'
						
),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'processParameters'
        )
    )
)

#                pythiaEtab = cms.vstring(
#                       'Main:timesAllowErrors = 10000',


#                       'WeakSingleBoson:ffbar2gmZ = on',
#                       'WeakZ0:gmZmode = 2',
#                       '23:addChannel 1 1.00 100 13 -13 443',
##                       '23:addChannel 1 1.00 100 11 -11 443',
#                       '23:onMode = off',
#                       '23:onIfMatch 13 -13 443',
##                       '23:onIfMatch 11 -11 443',
#                       '443:onMode = off',
#                       '443:onIfMatch 13 -13'
##                       '23:m0=11.0',
##                       '23:mWidth =0.00'
#),
