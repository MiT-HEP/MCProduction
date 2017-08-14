from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DY_Geneva2_DIGIRAW_4MB'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

## JobType
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_gp.py'
config.JobType.inputFiles=['pu.py']
config.JobType.numCores = 4
config.JobType.maxMemoryMB=4000

### DATA configuration
#config.Data.inputDataset = '/HplusToTauNu_M_200_TuneCUETP8M1_tauola_13TeV_pythia8/amarini-GEN-SIM-71-6edf4b210aa48b81088c0de44a7af6f5/USER'
#config.Data.inputDataset = '/DYJetsToMuMu_mll105To160_madgraph_MLM_pythia8/amarini-GEN-SIM-be5fa469151fc874ffd8c8a54cc6c28b/USER'
config.Data.inputDataset = '/DY_mumu_13TEV_PDF4LHCNNLO100_Mll_50_150_as118/amarini-GEN-SIM-9b8153a64748fc8b50e404570305ee0f/USER'
config.Data.inputDBS = 'phys03'
#config.Data.ignoreLocality = True
config.Data.ignoreLocality = False

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
#config.Data.outLFNDirBase = '/store/user/%s/mc/' % (getUsernameFromSiteDB())
#config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshmm/amarini/'
config.Data.outLFNDirBase = '/store/group/phys_smp/genevamc/v03' 
config.Data.publication = True
config.Data.outputDatasetTag ='DIGI-SIM'

config.Site.storageSite = 'T2_CH_CERN'

