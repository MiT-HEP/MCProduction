from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'amarini_FullSim_WPhadWPhadJJ_EWK'
config.General.workArea = 'crab_privateMCProduction'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 2500
config.JobType.psetName = 'fake.py' ## fake the last step -> step4 + empty source
config.JobType.inputFiles = ['scriptExe.sh', 'step1.py','step2.py','step3.py','step4.py','pu.py']
config.JobType.scriptExe='scriptExe.sh'
config.JobType.numCores=2

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
#config.Data.totalUnits = 2000000
config.Data.totalUnits = 2000000
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshmm/amarini/'
config.Data.publication = True
config.Data.outputPrimaryDataset = 'WPhadWPhadJJ_EWK_LO_SM_mjj100_pTj10_13TeV_madgraphMLM_pythia8'
config.Data.outputDatasetTag ='FullSim_94X-MINIAODSIM'

config.Site.storageSite = 'T2_CH_CERN'

