from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'ttH_HToMuMu_GENSIM'
config.General.workArea = 'GENSIM'

config.General.transferOutputs = True
config.General.transferLogs = False

## JobType
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_gp.py'
config.JobType.inputFiles=['pu.py']
config.JobType.numCores = 4
config.JobType.maxMemoryMB=4000

### DATA configuration
config.Data.inputDataset = '/ttHToGG_M125_13TeV_powheg_pythia8_v2/RunIIWinter15wmLHE-MCRUN2_71_V1-v1/LHE'
#config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
#config.Data.outLFNDirBase = '/store/user/%s/mc/' % (getUsernameFromSiteDB())
#config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshmm/amarini/'
config.Data.outLFNDirBase = '/store/group/phys_smp/genevamc/v03' 
config.Data.publication = True
config.Data.outputDatasetTag ='GEN-SIM'

config.Site.storageSite = 'T2_CH_CERN'

