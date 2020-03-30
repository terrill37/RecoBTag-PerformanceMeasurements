from WMCore.Configuration import Configuration

store_dir = 'BTagServiceWork/PhaseII/Online/CMSSW11_NewGT_TrackingV2_1'
sample_name = 'TT_14TeV_NoPU'

RAW_DSET = '/TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8/Phase2HLTTDRWinter20DIGI-NoPU_110X_mcRun4_realistic_v3-v2/GEN-SIM-DIGI-RAW'

config = Configuration()

config.section_('General')
config.General.requestName = 'bTagHLTAnalyzer_'+sample_name+"_CMSSW11_NewGT_TrackingV2_1"
config.General.transferOutputs = True
config.General.transferLogs = False

config.section_('JobType')
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName = 'runHLTBTagAnalyzer_PhaseII_cfg.py'
config.JobType.inputFiles = []
config.JobType.pyCfgParams = ['doTrackV0=True']
# config.JobType.pyCfgParams = []
config.JobType.maxJobRuntimeMin = 2750
config.JobType.maxMemoryMB = 3500
#config.JobType.numCores = 1

config.section_('Data')
config.Data.publication = False
config.Data.ignoreLocality = True
config.Data.splitting = 'EventAwareLumiBased'
config.Data.inputDataset = RAW_DSET
config.Data.outLFNDirBase = '/store/user/sewuchte/'+store_dir+'/'+sample_name
config.Data.unitsPerJob = 40
config.Data.totalUnits = -1

config.section_('Site')
config.Site.storageSite = 'T2_DE_DESY'
if config.Data.ignoreLocality:
   #~ config.Site.whitelist = ['T2_CH_CERN', 'T2_DE_*']
   config.Site.whitelist = ['T2_DE_*','T1_DE_*']

config.section_('User')
