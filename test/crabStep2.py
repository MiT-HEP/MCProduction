from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'PYTHIA8_MC_Higgs_generation'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

## JobType
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2.py'

### DATA configuration
config.Data.inputDataset = '/MinBias/soffi-Higgs_scalar_nohdecay_gg_1GeV_13TeV-a3a9f79104271b5b0a2231156aced621/USER'
config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 100
config.Data.totalUnits = -1
config.Data.outLFNDirBase = '/store/user/%s/mc/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.publishDataName ='%s_PrivateMC_HPlusToTauNu_RECO_June2015'% (getUsernameFromSiteDB())

config.Site.storageSite = 'T2_CH_CERN'

