from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DY_LO_MLM_AODSIM'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

## JobType
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3.py'
config.JobType.numCores = 4

### DATA configuration
#config.Data.inputDataset = '/DYJetsToMuMu_mll105To160_madgraph_MLM_pythia8/amarini-DIGI-SIM-16ca0fac1b892ff3c3d45d801745cbbf/USER'
config.Data.inputDataset = '/DY_mumu_13TEV_PDF4LHCNNLO100_Mll_50_150_as118/amarini-DIGI-SIM-d6bae82ab2e5563af1a5cace28bcd443/USER'
config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
#config.Data.outLFNDirBase = '/store/user/%s/mc/' % (getUsernameFromSiteDB())
#config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshmm/amarini/'
config.Data.outLFNDirBase = '/store/group/phys_smp/genevamc/v03' 
config.Data.publication = True
config.Data.outputDatasetTag ='AODSIM'

config.Site.storageSite = 'T2_CH_CERN'

