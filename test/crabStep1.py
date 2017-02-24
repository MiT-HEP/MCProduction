from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'ttH_Hmumu_LHE'
config.General.workArea = 'crab_Step1'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'HIG-RunIIWinter15wmLHE-01149_1_cfg.py'
#config.JobType.maxMemoryMB = 2500

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
config.Data.totalUnits = 500000
config.JobType.scriptExe="scriptExe.sh"
config.Data.outLFNDirBase = '/store/user/%s/mc/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputPrimaryDataset = 'ttHToMuMu_M125_13TeV_powheg_pythia8_v2'
config.Data.outputDatasetTag ='GEN-SIM-71'

config.Site.storageSite = 'T2_CH_CERN'
#config.Site.blacklist = ['T2_US_Florida', 'T2_BR_*', 'T2_RU_*']

