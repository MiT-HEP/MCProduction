from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'amarini_UL2018_GGHMH125_powheg'
config.General.workArea = 'crab_privateMCProduction'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 2500
config.JobType.psetName = 'fake.py' ## fake the last step -> step4 + empty source
from glob import glob
config.JobType.inputFiles = ['scriptExe.sh', 'step1_cfg.py','step2_cfg.py','step3_cfg.py','step4_cfg.py','step5_cfg.py','step6_cfg.py','step7_cfg.py','pu.py'] + glob('fragment*py')
config.JobType.scriptExe='scriptExe.sh'
config.JobType.scriptArgs=['hbbg']
config.JobType.numCores=4

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
config.Data.totalUnits = 500000
#config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshmm/%s/' % (getUsernameFromSiteDB())
config.Data.outLFNDirBase = '/store/user/amarini/'
config.Data.publication = True
config.Data.outputPrimaryDataset = 'GluGlu_HiggsZG_Zbb_M125_13TeV_powheg_pythia8'
config.Data.outputDatasetTag ='UL2018-NANOAODSIMv8'

config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T3_US_MIT'

