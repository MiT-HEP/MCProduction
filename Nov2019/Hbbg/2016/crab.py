from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'amarini_FullSim_GGHMH125_powheg'
config.General.workArea = 'crab_privateMCProduction'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 2500
config.JobType.psetName = 'fake.py' ## fake the last step -> step4 + empty source
config.JobType.inputFiles = ['scriptExe.sh', 'step1.py','step2.py','step3.py','step4.py','pu.py']
config.JobType.scriptExe='scriptExe.sh'
config.JobType.numCores=4

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
config.Data.totalUnits = 500000
#config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshmm/amarini/'
config.Data.outLFNDirBase = '/store/user/amarini/' 
config.Data.publication = True
config.Data.outputPrimaryDataset = 'GluGlu_HiggsZG_Zbb_M125_13TeV_powheg_pythia8'
config.Data.outputDatasetTag ='FullSim_94X-MINIAODSIM'

config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T3_US_MIT'

