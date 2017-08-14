from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'PrivateMCProduction_amarini_August17'
config.General.workArea = 'crab_privateMCProduction'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 2500
config.JobType.psetName = 'MINIAODSIM.py'
#config.JobType.outputFiles = ['step5.root','GenSimAODSim_step1.log', 'GenSimAODSim_step2.log', 'FrameworkJobReport.xml', 'job.log']
config.JobType.inputFiles = ['scriptExe.sh', 'LHE.py', 'GEN.py','MINIAODSIM.py']
config.JobType.scriptExe='scriptExe.sh'
config.JobType.numCores=4

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
config.Data.totalUnits = 200000
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshmm/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputPrimaryDataset = 'GluGluHToMuMu_M125_13TeV_amcatnloFXFX_pythia8'
config.Data.outputDatasetTag ='PUMoriond17-MINIAODSIM'

config.Site.storageSite = 'T2_CH_CERN'

