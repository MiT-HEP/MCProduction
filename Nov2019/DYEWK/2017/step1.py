# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/HIG-RunIIFall17wmLHEGS-04504-fragment.py --fileout file:step1.root --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN,SIM --nThreads 2 --geometry DB:Extended --era Run2_2017 --python_filename step1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 500
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')
options.register('jobNum', 0, VarParsing.multiplicity.singleton,VarParsing.varType.int,"jobNum")
options.parseArguments()

process = cms.Process('SIM',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2017Collision_cfi')
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
    annotation = cms.untracked.string('Configuration/GenProduction/python/HIG-RunIIFall17wmLHEGS-04504-fragment.py nevts:500'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:step1.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.LHEoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('LHE'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step1_inLHE.root'),
    outputCommands = process.LHEEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '93X_mc2017_realistic_v3', '')

process.generator = cms.EDFilter("Herwig7GeneratorFilter",
    configFiles = cms.vstring(),
    crossSection = cms.untracked.double(-1),
    dataLocation = cms.string('${HERWIGPATH:-6}'),
    eventHandlers = cms.string('/Herwig/EventHandlers'),
    filterEfficiency = cms.untracked.double(1.0),
    generatorModule = cms.string('/Herwig/Generators/EventGenerator'),
    herwig7CH3AlphaS = cms.vstring('cd /Herwig/Shower', 
        'set AlphaQCD:AlphaMZ 0.118', 
        'cd /'),
    herwig7CH3MPISettings = cms.vstring('read snippets/SoftModel.in', 
        'set /Herwig/Hadronization/ColourReconnector:ReconnectionProbability 0.4712', 
        'set /Herwig/UnderlyingEvent/MPIHandler:pTmin0 3.04', 
        'set /Herwig/UnderlyingEvent/MPIHandler:InvRadius 1.284', 
        'set /Herwig/UnderlyingEvent/MPIHandler:Power 0.1362', 
        'set /Herwig/Partons/RemnantDecayer:ladderPower -0.08', 
        'set /Herwig/Partons/RemnantDecayer:ladderNorm 0.95'),
    herwig7CH3PDF = cms.vstring('cd /Herwig/Partons', 
        'create ThePEG::LHAPDF PDFSet_nnlo ThePEGLHAPDF.so', 
        'set PDFSet_nnlo:PDFName NNPDF31_nnlo_as_0118.LHgrid', 
        'set PDFSet_nnlo:RemnantHandler HadronRemnants', 
        'set /Herwig/Particles/p+:PDF PDFSet_nnlo', 
        'set /Herwig/Particles/pbar-:PDF PDFSet_nnlo', 
        'set /Herwig/Partons/PPExtractor:FirstPDF  PDFSet_nnlo', 
        'set /Herwig/Partons/PPExtractor:SecondPDF PDFSet_nnlo', 
        'set /Herwig/Shower/ShowerHandler:PDFA PDFSet_nnlo', 
        'set /Herwig/Shower/ShowerHandler:PDFB PDFSet_nnlo', 
        'create ThePEG::LHAPDF PDFSet_lo ThePEGLHAPDF.so', 
        'set PDFSet_lo:PDFName NNPDF31_lo_as_0130.LHgrid', 
        'set PDFSet_lo:RemnantHandler HadronRemnants', 
        'set /Herwig/Shower/ShowerHandler:PDFARemnant PDFSet_lo', 
        'set /Herwig/Shower/ShowerHandler:PDFBRemnant PDFSet_lo', 
        'set /Herwig/Partons/MPIExtractor:FirstPDF PDFSet_lo', 
        'set /Herwig/Partons/MPIExtractor:SecondPDF PDFSet_lo', 
        'cd /'),
    herwig7StableParticlesForDetector = cms.vstring('set /Herwig/Decays/DecayHandler:MaxLifeTime 10*mm', 
        'set /Herwig/Decays/DecayHandler:LifeTimeOption Average'),
    hw_PSWeights_settings = cms.vstring('cd /', 
        'cd /Herwig/Shower', 
        'do ShowerHandler:AddVariation RedHighAll 1.141 1.141  All', 
        'do ShowerHandler:AddVariation RedLowAll 0.707 0.707 All', 
        'do ShowerHandler:AddVariation DefHighAll 2 2 All', 
        'do ShowerHandler:AddVariation DefLowAll 0.5 0.5 All', 
        'do ShowerHandler:AddVariation ConHighAll 4 4 All', 
        'do ShowerHandler:AddVariation ConLowAll 0.25 0.25 All', 
        'do ShowerHandler:AddVariation RedHighHard 1.141 1.141  Hard', 
        'do ShowerHandler:AddVariation RedLowHard 0.707 0.707 Hard', 
        'do ShowerHandler:AddVariation DefHighHard 2 2 Hard', 
        'do ShowerHandler:AddVariation DefLowHard 0.5 0.5 Hard', 
        'do ShowerHandler:AddVariation ConHighHard 4 4 Hard', 
        'do ShowerHandler:AddVariation ConLowHard 0.25 0.25 Hard', 
        'do ShowerHandler:AddVariation RedHighSecondary 1.141 1.141  Secondary', 
        'do ShowerHandler:AddVariation RedLowSecondary 0.707 0.707 Secondary', 
        'do ShowerHandler:AddVariation DefHighSecondary 2 2 Secondary', 
        'do ShowerHandler:AddVariation DefLowSecondary 0.5 0.5 Secondary', 
        'do ShowerHandler:AddVariation ConHighSecondary 4 4 Secondary', 
        'do ShowerHandler:AddVariation ConLowSecondary 0.25 0.25 Secondary', 
        'set SplittingGenerator:Detuning 2.0', 
        'cd /'),
    hw_lhe_MG5aMCatNLO_settings = cms.vstring('set /Herwig/Shower/KinematicsReconstructor:InitialInitialBoostOption LongTransBoost', 
        'set /Herwig/Shower/KinematicsReconstructor:ReconstructionOption General', 
        'set /Herwig/Shower/KinematicsReconstructor:FinalStateReconOption Default', 
        'set /Herwig/Shower/KinematicsReconstructor:InitialStateReconOption Rapidity', 
        'set /Herwig/Shower/ShowerHandler:SpinCorrelations Yes', 
        'set /Herwig/Particles/t:NominalMass 172.5'),
    hw_lhe_common_settings = cms.vstring('read snippets/PPCollider.in', 
        'cd /Herwig/Generators', 
        'cd /Herwig/EventHandlers', 
        'library LesHouches.so', 
        'create ThePEG::LesHouchesEventHandler LesHouchesHandler', 
        'set LesHouchesHandler:PartonExtractor /Herwig/Partons/PPExtractor', 
        'set LesHouchesHandler:CascadeHandler /Herwig/Shower/ShowerHandler', 
        'set LesHouchesHandler:DecayHandler /Herwig/Decays/DecayHandler', 
        'set LesHouchesHandler:HadronizationHandler /Herwig/Hadronization/ClusterHadHandler', 
        'set LesHouchesHandler:WeightOption VarNegWeight', 
        'set LesHouchesHandler:Weighted On', 
        'set /Herwig/Generators/EventGenerator:EventHandler /Herwig/EventHandlers/LesHouchesHandler', 
        'create ThePEG::Cuts /Herwig/Cuts/NoCuts', 
        'create ThePEG::LHAPDF /Herwig/Partons/LHAPDF ThePEGLHAPDF.so', 
        'set /Herwig/Partons/LHAPDF:PDFName NNPDF31_nnlo_as_0118', 
        'set /Herwig/Partons/LHAPDF:RemnantHandler /Herwig/Partons/HadronRemnants', 
        'set /Herwig/Particles/p+:PDF /Herwig/Partons/LHAPDF', 
        'set /Herwig/Particles/pbar-:PDF /Herwig/Partons/LHAPDF', 
        'set /Herwig/Partons/PPExtractor:FirstPDF  /Herwig/Partons/LHAPDF', 
        'set /Herwig/Partons/PPExtractor:SecondPDF /Herwig/Partons/LHAPDF', 
        'create ThePEG::LesHouchesFileReader LesHouchesReader', 
        'set LesHouchesReader:FileName cmsgrid_final.lhe', 
        'set LesHouchesReader:AllowedToReOpen No', 
        'set LesHouchesReader:InitPDFs 0', 
        'set LesHouchesReader:Cuts /Herwig/Cuts/NoCuts', 
        'set LesHouchesReader:MomentumTreatment RescaleEnergy', 
        'set LesHouchesReader:PDFA /Herwig/Partons/LHAPDF', 
        'set LesHouchesReader:PDFB /Herwig/Partons/LHAPDF', 
        'insert LesHouchesHandler:LesHouchesReaders 0 LesHouchesReader'),
    hw_user_settings = cms.vstring('cd /Herwig/EventHandlers', 
        'set EventHandler:LuminosityFunction:Energy 13000*GeV', 
        'cd /'),
    parameterSets = cms.vstring('hw_lhe_common_settings', 
        'hw_lhe_MG5aMCatNLO_settings', 
        'herwig7CH3PDF', 
        'herwig7CH3AlphaS', 
        'herwig7CH3MPISettings', 
        'herwig7StableParticlesForDetector', 
        'hw_PSWeights_settings', 
        'hw_user_settings'),
    repository = cms.string('${HERWIGPATH}/HerwigDefaults.rpo'),
    run = cms.string('InterfaceMatchboxTest'),
    runModeList = cms.untracked.string('read,run')
)

import os
print "-> Using gridpack",os.environ['PWD']+'/LLJJ_EWK_pTj0_SM_5f_LO_ptJ0_MLL_105-160_NNPDF31NNLO_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz'

process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring(os.environ['PWD']+'/LLJJ_EWK_pTj0_SM_5f_LO_ptJ0_MLL_105-160_NNPDF31NNLO_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(500),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    #scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
    scriptName = cms.FileInPath('run_generic_tarball.sh')
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.lhe_step = cms.Path(process.externalLHEProducer)
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)
process.LHEoutput_step = cms.EndPath(process.LHEoutput)

# Schedule definition
process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step,process.LHEoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(1)
process.options.numberOfStreams=cms.untracked.uint32(0)
# filter all path with the production filter sequence
for path in process.paths:
	if path in ['lhe_step']: continue
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

# customisation of the process.
import os,random
random.seed = os.urandom(10) #~10^14
process.RandomNumberGeneratorService.externalLHEProducer.initialSeed = random.randint(0,999999)
process.RandomNumberGeneratorService.generator.initialSeed = random.randint(0,999999)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
