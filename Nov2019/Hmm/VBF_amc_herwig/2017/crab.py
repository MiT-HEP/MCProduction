from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'amarini_FullSim_Hmm_2017'
config.General.workArea = 'crab_privateMCProduction'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 4900
config.JobType.psetName = 'fake.py' ## fake the last step -> step4 + empty source
config.JobType.inputFiles = ['scriptExe.sh', 'step1.py','step2.py','step3.py','step4.py','pu.py']
config.JobType.scriptExe='scriptExe.sh'
config.JobType.numCores=2

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
config.Data.totalUnits = 1000000
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshmm/amarini/'
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputPrimaryDataset = 'VBFHToMuMu_M-125_TuneEEC5_13TeV-amcatnlo-herwigpp'
config.Data.outputDatasetTag ='RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-MINIAODSIM'

config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T3_US_MIT'

