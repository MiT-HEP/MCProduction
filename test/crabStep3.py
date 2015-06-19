from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'PYTHIA8_MC_Higgs_MINIAOD_M-500'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

## JobType
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3.py'

### DATA configuration
config.Data.inputDataset = '/HplusToTauNu-M500/amarini-RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_RECO-ede2f89505a05d00af372143a993465e/USER'
#config.Data.inputDataset = '/HplusToTauNu/amarini-amarini_PrivateMC_HPlusToTauNu_June2015-9e71add12689a20c13001f387193a79f/USER'
config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.outLFNDirBase = '/store/user/%s/mc/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.publishDataName ='RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_MINIAOD'

config.Site.storageSite = 'T2_CH_CERN'

