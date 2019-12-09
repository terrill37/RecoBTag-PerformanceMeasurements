from WMCore.Configuration import Configuration
from multiprocessing import Process

def submit(config):
    print " to do: ",config
    res = crabCommand('submit', config = config)


if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand

    datalist = [
        "/QCD_Pt_80to120_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v1/GEN-SIM-DIGI-RAW",
        "/QCD_Pt_600oInf_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v1/GEN-SIM-DIGI-RAW",
        "/QCD_Pt_50to80_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v1/GEN-SIM-DIGI-RAW",
        "/QCD_Pt_470to600_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v1/GEN-SIM-DIGI-RAW",
        "/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v1/GEN-SIM-DIGI-RAW",
        "/QCD_Pt_300to470_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v1/GEN-SIM-DIGI-RAW",
        "/QCD_Pt_170to300_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v2/GEN-SIM-DIGI-RAW",
        "/QCD_Pt_120to170_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v1/GEN-SIM-DIGI-RAW",
        "/QCD_Pt_0_1000_14TeV_TuneCUETP8M1/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v2/GEN-SIM-DIGI-RAW",

        "/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v1/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-80to120_EMEnriched_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v3/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v2/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-50to80_EMEnriched_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v2/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v1/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-30to50_EMEnriched_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v2/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-300toInf_MuEnrichedPt5_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v1/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-300toInf_EMEnriched_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v3/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v3/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-20to30_EMEnriched_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v2/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v1/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-170to300_EMEnriched_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v1/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-15to3000_MuEnrichedPt5_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v1/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-15to3000_EMEnriched_TuneCP5_13TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v1/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v3/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-15to20_EMEnriched_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v2/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v2/GEN-SIM-DIGI-RAW",
        "/QCD_Pt-120to170_EMEnriched_TuneCP5_14TeV_pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3-v1/GEN-SIM-DIGI-RAW"
 ]

    for dataset in datalist:

        config = Configuration()

        config.section_("General")
        config.General.transferOutputs = True
        config.General.transferLogs = False

        config.section_("JobType")
        config.JobType.pluginName  = 'Analysis'
        config.JobType.psetName = 'runHLTBTagAnalyzer_PhaseII_cfg.py'
        config.JobType.inputFiles = []
        config.JobType.maxJobRuntimeMin = 2750
        config.JobType.maxMemoryMB = 3000

        config.section_("Data")
        config.Data.publication = False
        config.Data.ignoreLocality = True
        config.Data.splitting = 'EventAwareLumiBased'
        config.Data.unitsPerJob = 100
        config.Data.totalUnits = -1


        config.section_("Site")
        config.Site.storageSite = 'T2_DE_DESY'
        if config.Data.ignoreLocality:
           config.Site.whitelist = ['T2_CH_CERN', 'T2_DE_*']


        config.section_("User") # to be adapted according to your network
        # config.User.voGroup = 'dcms' # to be adapted according to your network #Changed to my group. MHH



        sample_name = dataset.split('/')[1]
        store_dir = 'BTagServiceWork/PhaseII/Online/TrackingV2/'
        config.JobType.pyCfgParams = ['output='+sample_name+'.root']
        config.Data.inputDataset = dataset
        config.General.requestName = 'PhaseII_BTV_HLT_nTuple_'+sample_name
        config.Data.outLFNDirBase = '/store/user/sewuchte/'+store_dir+'/'+sample_name
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
