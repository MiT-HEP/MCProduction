from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#config.General.requestName = 'PYTHIA8_MC_Higgs_MINIAOD_M-900'
config.General.requestName = 'amcAtNLO_MINIAODv2_M200'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

## JobType
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3.py'

### DATA configuration
#config.Data.inputDataset = '/HplusToTauNu-M500/amarini-RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_RECO-ede2f89505a05d00af372143a993465e/USER'
#config.Data.inputDataset = '/HplusToTauNu/amarini-amarini_PrivateMC_HPlusToTauNu_June2015-9e71add12689a20c13001f387193a79f/USER'
#config.Data.inputDataset = '/HplusToTauNu-M900/amarini-RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_AODSIM-99de33e1c31a55fb5b45c03bcfa6de96/USER'
#config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/ChargedHiggs_HplusTB_HplusToTauNu_M-200_13TeV_amcatnlo_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.ignoreLocality = True

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
config.Data.totalUnits = -1
config.Data.outLFNDirBase = '/store/user/%s/mc/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.publishDataName ='RunIISpring15DR74-74X_mcRun2_asymptotic_v2_MINIAODv2'

config.Site.storageSite = 'T2_CH_CERN'

