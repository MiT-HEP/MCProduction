from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DY_mumu_13TEV_PDF4LHCNNLO100_Mll_50_150_as118_GEN'
config.General.workArea = 'crab_GEN'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'pset.py'
config.JobType.inputFiles=['hepmc2gen.py']
config.JobType.scriptExe = 'scriptExe.sh'
#config.JobType.outputFiles = ['HepMC_GEN.root']
#config.JobType.maxMemoryMB = 2500

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100000
config.Data.totalUnits = 12000000
#config.Data.totalUnits = 100000
#config.JobType.scriptExe="scriptExe.sh"
config.Data.outLFNDirBase = '/store/group/phys_smp/genevamc/2017_11_15_932/' 
config.Data.publication = True
#config.Data.outputPrimaryDataset = 'DY_mumu_13TEV_PDF4LHCNNLO100_Mll_50_150_as118'
config.Data.outputPrimaryDataset= 'DY_mumu_13TEV_PDF4LHCNNLO100_Mll_50_150_as118_scale_MTll_CUETP8M1'
config.Data.outputDatasetTag ='GEN-923'

config.Site.storageSite = 'T2_CH_CERN'
config.Site.whitelist = ['T2_CH_CERN']
#config.Site.blacklist = ['T2_US_Florida', 'T2_BR_*', 'T2_RU_*']

