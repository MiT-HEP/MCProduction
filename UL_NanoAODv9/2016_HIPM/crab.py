from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'amarini_UL2016_HIPM_GGHMH125_powheg'
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
#config.JobType.numCores=4

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
config.Data.totalUnits = 1000000
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshmm/amarini/'
#config.Data.outLFNDirBase = '/store/user/amarini/'
config.Data.publication = True
config.Data.outputPrimaryDataset = 'GluGlu_HiggsZG_Zbb_M125_13TeV_powheg_pythia8'
config.Data.outputDatasetTag ='UL2016_HIPM-NANOAODSIMv9'

config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T3_US_MIT'

do='xxx'
if do=='xxx': raise ValueError('Set do')
if do=='hbbg' :
    config.General.requestName = 'amarini-UL2016_HIPM_GGHMH125_powheg'
    config.Data.outputPrimaryDataset = 'GluGlu_HiggsZG_Zbb_M125_13TeV_powheg_pythia8'
    config.JobType.scriptArgs=['chain=hbbg']
if do=='vbf-hbbg':
    config.General.requestName = 'amarini-UL2016_HIPM_VBFMH125_powheg'
    config.Data.outputPrimaryDataset = 'VBF_HiggsZG_Zbb_M125_13TeV_powheg_pythia8'
    config.JobType.scriptArgs=['chain=vbf-hbbg']
if do=='hwz1500' :
    config.General.requestName = 'amarini_UL2016_HIPM_SinglyChargedHiggsGMmodel_HWZ_Znn_M1500_madgraph'
    config.Data.outputPrimaryDataset = 'SinglyChargedHiggsGMmodel_HWZ_Znn_M1500_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplus_hwz_1500']
if do=='hwz1000' :
    config.General.requestName = 'amarini_UL2016_HIPM_SinglyChargedHiggsGMmodel_HWZ_Znn_M1000_madgraph'
    config.Data.outputPrimaryDataset = 'SinglyChargedHiggsGMmodel_HWZ_Znn_M1000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplus_hwz_1000']
if do=='hwz2000' :
    config.General.requestName = 'amarini_UL2016_HIPM_SinglyChargedHiggsGMmodel_HWZ_Znn_M2000_madgraph'
    config.Data.outputPrimaryDataset = 'SinglyChargedHiggsGMmodel_HWZ_Znn_M2000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplus_hwz_2000']
if do=='hwz3000' :
    config.General.requestName = 'amarini_UL2016_HIPM_SinglyChargedHiggsGMmodel_HWZ_Znn_M3000_madgraph'
    config.Data.outputPrimaryDataset = 'SinglyChargedHiggsGMmodel_HWZ_Znn_M3000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplus_hwz_3000']
if do=='hww1500' :
    config.General.requestName = 'amarini_UL2016_HIPM_DoublyChargedHiggsGMmodel_HWW_M1500_13TeV-madgraph'
    config.Data.outputPrimaryDataset = 'DoublyChargedHiggsGMmodel_HWW_M1500_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplusplus_hww_1500']
if do=='hww1000' :
    config.General.requestName = 'amarini_UL2016_HIPM_DoublyChargedHiggsGMmodel_HWW_M1000_13TeV-madgraph'
    config.Data.outputPrimaryDataset = 'DoublyChargedHiggsGMmodel_HWW_M1000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplusplus_hww_1000']
if do=='hww2000' :
    config.General.requestName = 'amarini_UL2016_HIPM_DoublyChargedHiggsGMmodel_HWW_M2000_13TeV-madgraph'
    config.Data.outputPrimaryDataset = 'DoublyChargedHiggsGMmodel_HWW_M2000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplusplus_hww_2000']
if do=='hww3000' :
    config.General.requestName = 'amarini_UL2016_HIPM_DoublyChargedHiggsGMmodel_HWW_M3000_13TeV-madgraph'
    config.Data.outputPrimaryDataset = 'DoublyChargedHiggsGMmodel_HWW_M3000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplusplus_hww_3000']
if do=='hwz_zbb_1500' :
    config.General.requestName = 'amarini_UL2016_HIPM_SinglyChargedHiggsGMmodel_HWZ_Zbb_M1500_madgraph'
    config.Data.outputPrimaryDataset = 'SinglyChargedHiggsGMmodel_HWZ_Zbb_M1500_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplus_hwz_zbb_1500']
if do=='hwz_zbb_1000' :
    config.General.requestName = 'amarini_UL2016_HIPM_SinglyChargedHiggsGMmodel_HWZ_Zbb_M1000_madgraph'
    config.Data.outputPrimaryDataset = 'SinglyChargedHiggsGMmodel_HWZ_Zbb_M1000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplus_hwz_zbb_1000']
if do=='hwz_zbb_2000' :
    config.General.requestName = 'amarini_UL2016_HIPM_SinglyChargedHiggsGMmodel_HWZ_Zbb_M2000_madgraph'
    config.Data.outputPrimaryDataset = 'SinglyChargedHiggsGMmodel_HWZ_Zbb_M2000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplus_hwz_zbb_2000']
if do=='hwz_zbb_3000' :
    config.General.requestName = 'amarini_UL2016_HIPM_SinglyChargedHiggsGMmodel_HWZ_Zbb_M3000_madgraph'
    config.Data.outputPrimaryDataset = 'SinglyChargedHiggsGMmodel_HWZ_Zbb_M3000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplus_hwz_zbb_3000']
if do=='WWjj_ss_pol_hadronic_ll' :
    config.General.requestName = 'amarini_UL2016_HIPM_WWjj_SS_ll_hadronic'
    config.Data.outputPrimaryDataset = 'WWjj_SS_ll_hadronic'
    config.JobType.scriptArgs=['chain=WWjj_ss_pol_hadronic_ll']
if do=='WWjj_ss_pol_hadronic_lt' :
    config.General.requestName = 'amarini_UL2016_HIPM_WWjj_SS_lt_hadronic'
    config.Data.outputPrimaryDataset = 'WWjj_SS_lt_hadronic'
    config.JobType.scriptArgs=['chain=WWjj_ss_pol_hadronic_lt']
if do=='WWjj_ss_pol_hadronic_tt' :
    config.General.requestName = 'amarini_UL2016_HIPM_WWjj_SS_tt_hadronic'
    config.Data.outputPrimaryDataset = 'WWjj_SS_tt_hadronic'
    config.JobType.scriptArgs=['chain=WWjj_ss_pol_hadronic_tt']
if do=='hww1000_semilep' :
    config.General.requestName = 'amarini_UL2016_HIPM_DoublyChargedHiggsGMmodel_HWW_semilep_M1000_13TeV-madgraph'
    config.Data.outputPrimaryDataset = 'DoublyChargedHiggsGMmodel_HWW_semilep_M1000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplusplus_hww_semilep_1000']
if do=='hww2000_semilep' :
    config.General.requestName = 'amarini_UL2016_HIPM_DoublyChargedHiggsGMmodel_HWW_semilep_M2000_13TeV-madgraph'
    config.Data.outputPrimaryDataset = 'DoublyChargedHiggsGMmodel_HWW_semilep_M2000_13TeV-madgraph'
    config.JobType.scriptArgs=['chain=hplusplus_hww_semilep_2000']

if do=='vbs_hbb_wpmjj_ewk':
    config.General.requestName = 'amarini_UL2016_HIPM_HBBWPMJJjj_EWK_LO_TuneCP5_13TeV-madgraph-pythia8'
    config.Data.outputPrimaryDataset = 'HBBWPMJJjj_EWK_LO_TuneCP5_13TeV-madgraph-pythia8'
    config.JobType.scriptArgs=['chain='+do]
if do=='vbs_hbb_wpmjj_qcd':
    config.General.requestName = 'amarini_UL2016_HIPM_HBBWPMJJjj_QCD_LO_TuneCP5_13TeV-madgraph-pythia8'
    config.Data.outputPrimaryDataset = 'HBBWPMJJjj_QCD_LO_TuneCP5_13TeV-madgraph-pythia8'
    config.JobType.scriptArgs=['chain='+do]

htarray=[ "100","200","300","500","700","1000","1500","2000","Inf"]
for iht in xrange(0,len(htarray)-1):
    ht=htarray[iht]
    htn=htarray[iht+1]
    if do=='qcd_ht_'+ht+'_'+htn+'_bfilter':
        config.General.requestName = 'amarini_UL2016_HIPM_QCD_HT'+ht+'to'+htn+'_BGenFilter_TuneCP5_13TeV-madgraph-pythia8'
        config.Data.outputPrimaryDataset = 'QCD_HT'+ht+'to'+htn+'_BGenFilter_TuneCP5_13TeV-madgraph-pythia8'
        config.JobType.scriptArgs=['chain='+do]

if do.startswith("mssm_gghhmm"):
    import re
    #"mssm_hmm_ma1000_tb10"
    ma=re.sub('ma','',do.split("_")[2])
    tb=re.sub('tb','',do.split("_")[3])
    config.Data.totalUnits = 10000
    config.General.requestName = 'amarini_UL2016_HIPM_'+ 'MSSMGluGluToHToMuMu_MA-'+ma+'_Tanb-'+tb+'_TuneCP5_13TeV-powheg-pythia8'
    config.Data.outputPrimaryDataset = 'MSSMGluGluToHToMuMu_MA-'+ma+'_Tanb-'+tb+'_TuneCP5_13TeV-powheg-pythia8'
    config.JobType.scriptArgs=['chain='+do]

if do.startswith("mssm_ggahmm"):
    import re
    ma=re.sub('ma','',do.split("_")[2])
    tb=re.sub('tb','',do.split("_")[3])
    config.Data.totalUnits = 10000
    config.General.requestName = 'amarini_UL2016_HIPM_'+ 'MSSMGluGluToAToMuMu_MA-'+ma+'_Tanb-'+tb+'_TuneCP5_13TeV-powheg-pythia8'
    config.Data.outputPrimaryDataset = 'MSSMGluGluToAToMuMu_MA-'+ma+'_Tanb-'+tb+'_TuneCP5_13TeV-powheg-pythia8'
    config.JobType.scriptArgs=['chain='+do]

if do.startswith("mssm_bbhhmm"):
    import re
    ma=re.sub('ma','',do.split("_")[2])
    tb=re.sub('tb','',do.split("_")[3])
    config.Data.totalUnits = 10000
    config.General.requestName = 'amarini_UL2016_HIPM_'+ 'MSSMBBToHToMuMu_MA-'+ma+'_Tanb-'+tb+'_TuneCP5_13TeV-powheg-pythia8'
    config.Data.outputPrimaryDataset = 'MSSMBBToHToMuMu_MA-'+ma+'_Tanb-'+tb+'_TuneCP5_13TeV-powheg-pythia8'
    config.JobType.scriptArgs=['chain='+do]

if do.startswith("mssm_bbahmm"):
    import re
    ma=re.sub('ma','',do.split("_")[2])
    tb=re.sub('tb','',do.split("_")[3])
    config.Data.totalUnits = 10000
    config.General.requestName = 'amarini_UL2016_HIPM_'+ 'MSSMBBToAToMuMu_MA-'+ma+'_Tanb-'+tb+'_TuneCP5_13TeV-powheg-pythia8'
    config.Data.outputPrimaryDataset = 'MSSMBBToAToMuMu_MA-'+ma+'_Tanb-'+tb+'_TuneCP5_13TeV-powheg-pythia8'
    config.JobType.scriptArgs=['chain='+do]

if do.startswith('vbs_'):
    import re
    p1=do.split('_')[1]
    p2=do.split('_')[2]
    ewk='_'.join(do.split('_')[3:])
    madspin=''
    if p1+"_"+p2 == 'wpjj_wmjj':    madspin='-madspin'
    if p1+"_"+p2 == 'wpmjj_wpmjj':  madspin='-madspin'
    if p1+"_"+p2 == 'zjjnob_wpmjj': madspin='-madspin'

    four=""
    if ewk == '4fqcd': 
        ewk='qcd'
        four="_4f"
    if ewk == '4fewk': 
        ewk='ewk'
        four="_4f"

    config.Data.outputPrimaryDataset = p1.upper()+p2.upper()+'jj_'+ewk.upper()+'_LO'+four+'_TuneCP5_13TeV-madgraph'+madspin+'-pythia8'
    config.General.requestName = 'amarini_UL2016_HIPM_'+ config.Data.outputPrimaryDataset
    config.JobType.scriptArgs=['chain='+do]

if do.startswith('aqgc_'):
    import re
    config.JobType.inputFiles.extend( ['addBranch.py'] )
    p1=do.split('_')[1]
    p2=do.split('_')[2]
    #aQGC_WMJJZJJjj_EWK_LO_NPle1_
    config.Data.outputPrimaryDataset = 'aQGC_' + p1.upper()+p2.upper()+'jj_'+'EWK_LO_NPle1_TuneCP5_13TeV-madgraph-pythia8'
    config.General.requestName = 'amarini_UL2016_HIPM_'+ config.Data.outputPrimaryDataset
    config.JobType.scriptArgs=['chain='+do]
#SinglyChargedHiggsGMmodel_HWZ_Zbb_M1500_13TeV-madgraph
#
#WWjj_SS_ll_hadronic
#WWjj_SS_lt_hadronic
#WWjj_SS_tt_hadronic
