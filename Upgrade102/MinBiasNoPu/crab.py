from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'amarini_MinBias_102'
config.General.workArea = 'crab_privateMCProduction'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 2500
config.JobType.psetName = 'fake.py' ## fake the last step -> step4 + empty source
config.JobType.inputFiles = ['scriptExe.sh', 'MinBias_14TeV_pythia8_TuneCUETP8M1_cfi_GEN_SIM.py', 'step2_DIGI_L1_L1TrackTrigger_DIGI2RAW_HLT.py']
config.JobType.scriptExe='scriptExe.sh'
config.JobType.numCores=1

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
config.Data.totalUnits = 200000
#config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshmm/%s/' % (getUsernameFromSiteDB())
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputPrimaryDataset = 'MinBias_14TeV'
config.Data.outputDatasetTag ='upgrade2023_2023D17_NoPu_GENSIMDIGIRAW'

#config.Site.storageSite = 'T2_CH_CERN'
config.Site.storageSite = 'T3_US_MIT'

