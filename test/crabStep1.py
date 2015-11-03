from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'PYTHIA8_MC_SingleTau_GENSIMRAW'
config.General.workArea = 'crab_Step1'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'step1.py'
#config.JobType.maxMemoryMB = 2500

#/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM
#config.Data.inputDataset = '/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM'
config.Data.primaryDataset = 'SingleTau_FlatPt_pythia8'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
#NJOBS = 20  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = 130000
config.Data.outLFNDirBase = '/store/user/%s/mc/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.publishDataName ='SingleTau_FlatPt_pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_GENSIMRAW'

config.Site.storageSite = 'T2_CH_CERN'
#config.Site.blacklist = ['T2_US_Florida', 'T2_BR_*', 'T2_RU_*']

