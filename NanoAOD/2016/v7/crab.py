from CRABClient.UserUtilities import config
config = config()

#config.General.requestName = 'amarini_NanoAOD_GluGlu_HiggsZG'
config.General.requestName = 'amarini_NanoAOD_VBF_HiggsZG'
config.General.workArea = 'crab_privateNanoAOD'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 2500
config.JobType.psetName = 'nano.py' ## 
config.JobType.numCores=2

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.outLFNDirBase = '/store/user/amarini/'
config.Data.publication = True
config.Data.outputDatasetTag ='NANOAODSIMv7_2016'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDBS = 'phys03'
#config.Data.inputDBS = 'global'
#config.Data.inputDataset = '/GluGlu_HiggsZG_Zbb_M125_13TeV_powheg_pythia8/amarini-FullSim_94X-MINIAODSIM-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
config.Data.inputDataset='/VBF_HiggsZG_Zbb_M125_13TeV_powheg_pythia8/amarini-FullSim_94X-MINIAODSIM-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'


config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T3_US_MIT'

