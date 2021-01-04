from CRABClient.UserUtilities import config
config = config()

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
#config.JobType.numCores=4

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
config.Data.totalUnits = 500000
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshmm/amarini/' # % (getUsernameFromSiteDB())
#config.Data.outLFNDirBase = '/store/user/amarini/'
config.Data.publication = True
config.Data.outputDatasetTag ='UL2018-NANOAODSIMv8'

config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T3_US_MIT'


do='xxx'
if do=='xxx': raise ValueError('Set do')
if do=='hbbg' :
    config.General.requestName = 'amarini-UL2018_GGHMH125_powheg'
    config.Data.outputPrimaryDataset = 'GluGlu_HiggsZG_Zbb_M125_13TeV_powheg_pythia8'
    config.JobType.scriptArgs=['chain=hbbg']
if do=='vbf-hbbg':
    config.General.requestName = 'amarini-UL2018_VBFMH125_powheg'
    config.Data.outputPrimaryDataset = 'VBF_HiggsZG_Zbb_M125_13TeV_powheg_pythia8'
    config.JobType.scriptArgs=['chain=vbf-hbbg']
if do=='hwz1500' :
    config.General.requestName = 'amarini_UL2018_SinglyChargedHiggsGMmodel_HWZ_Znn_M1500_madgraph'
    config.Data.outputPrimaryDataset = 'SinglyChargedHiggsGMmodel_HWZ_Znn_M1500_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplus_hwz_1500']
if do=='hwz1000' :
    config.General.requestName = 'amarini_UL2018_SinglyChargedHiggsGMmodel_HWZ_Znn_M1000_madgraph'
    config.Data.outputPrimaryDataset = 'SinglyChargedHiggsGMmodel_HWZ_Znn_M1000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplus_hwz_1000']
if do=='hwz2000' :
    config.General.requestName = 'amarini_UL2018_SinglyChargedHiggsGMmodel_HWZ_Znn_M2000_madgraph'
    config.Data.outputPrimaryDataset = 'SinglyChargedHiggsGMmodel_HWZ_Znn_M2000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplus_hwz_2000']
if do=='hww1500' :
    config.General.requestName = 'amarini_UL2018_DoublyChargedHiggsGMmodel_HWW_M1500_13TeV-madgraph'
    config.Data.outputPrimaryDataset = 'DoublyChargedHiggsGMmodel_HWW_M1500_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplusplus_hww_1500']
if do=='hww1000' :
    config.General.requestName = 'amarini_UL2018_DoublyChargedHiggsGMmodel_HWW_M1000_13TeV-madgraph'
    config.Data.outputPrimaryDataset = 'DoublyChargedHiggsGMmodel_HWW_M1000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplusplus_hww_1000']
if do=='hww2000' :
    config.General.requestName = 'amarini_UL2018_DoublyChargedHiggsGMmodel_HWW_M2000_13TeV-madgraph'
    config.Data.outputPrimaryDataset = 'DoublyChargedHiggsGMmodel_HWW_M2000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplusplus_hww_2000']
if do=='hwz_zbb_1500' :
    config.General.requestName = 'amarini_UL2018_SinglyChargedHiggsGMmodel_HWZ_Zbb_M1500_madgraph'
    config.Data.outputPrimaryDataset = 'SinglyChargedHiggsGMmodel_HWZ_Zbb_M1500_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplus_hwz_zbb_1500']
if do=='hwz_zbb_1000' :
    config.General.requestName = 'amarini_UL2018_SinglyChargedHiggsGMmodel_HWZ_Zbb_M1000_madgraph'
    config.Data.outputPrimaryDataset = 'SinglyChargedHiggsGMmodel_HWZ_Zbb_M1000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplus_hwz_zbb_1000']
if do=='hwz_zbb_2000' :
    config.General.requestName = 'amarini_UL2018_SinglyChargedHiggsGMmodel_HWZ_Zbb_M2000_madgraph'
    config.Data.outputPrimaryDataset = 'SinglyChargedHiggsGMmodel_HWZ_Zbb_M2000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplus_hwz_zbb_2000']
if do=='WWjj_ss_pol_hadronic_ll' :
    config.General.requestName = 'amarini_UL2018_WWjj_SS_ll_hadronic'
    config.Data.outputPrimaryDataset = 'WWjj_SS_ll_hadronic'
    config.JobType.scriptArgs=['chain=WWjj_ss_pol_hadronic_ll']
if do=='WWjj_ss_pol_hadronic_lt' :
    config.General.requestName = 'amarini_UL2018_WWjj_SS_lt_hadronic'
    config.Data.outputPrimaryDataset = 'WWjj_SS_lt_hadronic'
    config.JobType.scriptArgs=['chain=WWjj_ss_pol_hadronic_lt']
if do=='WWjj_ss_pol_hadronic_tt' :
    config.General.requestName = 'amarini_UL2018_WWjj_SS_tt_hadronic'
    config.Data.outputPrimaryDataset = 'WWjj_SS_tt_hadronic'
    config.JobType.scriptArgs=['chain=WWjj_ss_pol_hadronic_tt']

#SinglyChargedHiggsGMmodel_HWZ_Zbb_M1500_13TeV-madgraph
#
#WWjj_SS_ll_hadronic
#WWjj_SS_lt_hadronic
#WWjj_SS_tt_hadronic
