# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/PYTHIA_ChargedHToTauNu_mH140_13TeV_cff.py --fileout file:step1.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step GEN,SIM --magField 38T_PostLS1 --python_filename step1.py --no_exec -n 500
import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')
options.register('jobNum', 0, VarParsing.multiplicity.singleton,VarParsing.varType.int,"jobNum")
options.parseArguments()

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500)
)

# Input source
firstLumi=10*options.jobNum+1 ## eventsPerJob/eventsPerLumi*jobNum +1
process.source = cms.Source("EmptySource",
		firstLuminosityBlock  = cms.untracked.uint32(firstLumi),
		numberEventsInLuminosityBlock = cms.untracked.uint32(100)
        )

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('Configuration/GenProduction/python/PYTHIA_ChargedHToTauNu_mH140_13TeV_cff.py nevts:500'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:step1.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_71_V1::All', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            UseTauolaPolarization = cms.bool(True),
            InputCards = cms.PSet(
                mdtau = cms.int32(0),
                pjak2 = cms.int32(0),
                pjak1 = cms.int32(0)
            )
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(1),
    PythiaParameters = cms.PSet(
        processParameters = cms.vstring('Higgs:useBSM = on', 
            'HiggsHchg:coup2H1W = 0.0', 
            '25:m0 = 125.', 
            '35:m0 = 140.', 
            '36:m0 = 140.', 
            '37:m0 = 140.', 
            'HiggsHchg:tanBeta = 30', 
            # Top:all   (default = off), includes other channel, this is consistent with runI
            'Top:gg2ttbar    = on',
            'Top:qqbar2ttbar = on',
            '6:m0 = 172.5', # top mass',
            ## disable t decays
            '6:onMode = 0',
            ## enable top -> W
            '6:onPosIfAny = 24',
            ## enable anti-top -> H+
            '6:onNegIfAny = 37',
            ## disable all charged higgs decay
            '37:onMode = 0',
            ## enable H+->tau
            '37:onIfAny = 15',
            'Tune:pp 5', 
            'Tune:ee 3', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tauMax = 10'),
        parameterSets = cms.vstring('processParameters')
    )
)

import os,random
random.seed = os.urandom(10) #~10^14
process.RandomNumberGeneratorService.generator.initialSeed = random.randint(0,999999)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions
