from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'amarini_FullSim_DYEWK_2018'
config.General.workArea = 'crab_privateMCProduction'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 4900
config.JobType.psetName = 'fake.py' ## fake the last step -> step4 + empty source
config.JobType.inputFiles = ['scriptExe.sh', 'step1.py','step2.py','step3.py','step4.py','pu.py','run_generic_tarball.sh']
config.JobType.scriptExe='scriptExe.sh'
config.JobType.numCores=4

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
config.Data.totalUnits = 1000000
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshmm/%s/' % (getUsernameFromSiteDB())
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputPrimaryDataset = 'EWK_LLJJ_MLL_105-160_ptJ-0_SM_5f_LO_TuneEEC5_13TeV-madgraph-herwigpp'
config.Data.outputDatasetTag ='RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-MINIAODSIM'

config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T3_US_MIT'

