from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'PYTHIA8_MC_SingleTau_GENSIMRECO'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'step12.py'
#config.JobType.maxMemoryMB = 2500

config.Data.primaryDataset = 'SingleTau_FlatPt_pythia8'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
config.Data.totalUnits = 130000
config.Data.outLFNDirBase = '/store/user/%s/mc/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.publishDataName ='SingleTau_FlatPt_pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_AODSIM'

config.Site.storageSite = 'T2_CH_CERN'
#config.Site.blacklist = ['T2_US_Florida', 'T2_BR_*', 'T2_RU_*']

