from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'PYTHIA8_MC_Higgs_RECO_M-500'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

## JobType
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2.py'

### DATA configuration
#config.Data.inputDataset = '/HplusToTauNu-M500/amarini-amarini_PrivateMC_HPlusToTauNu_June2015-16aa19d591b8b49c55c4508e7a7c9233/USER'
config.Data.inputDataset = '/SingleTau_FlatPt_pythia8/amarini-SingleTau_FlatPt_pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_GENSIMRAW-5acfbcd257d5e726b08870647d1dc244/USER'
#config.Data.inputDataset = '/HplusToTauNu/amarini-amarini_PrivateMC_HPlusToTauNu_June2015-9e71add12689a20c13001f387193a79f/USER'
config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.outLFNDirBase = '/store/user/%s/mc/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.publishDataName ='%s_PrivateMC_HPlusToTauNu_RECO_June2015'% (getUsernameFromSiteDB())
config.Data.publishDataName ='RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_RECO'

config.Site.storageSite = 'T2_CH_CERN'

