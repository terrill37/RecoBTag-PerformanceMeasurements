### configuration file to re-run customized HLT Menu on RAW
# from RecoBTag.PerformanceMeasurements.Simone_TrackingV0 import cms, process
# process.load("RecoBTag.PerformanceMeasurements.BTagHLT_stripped_cff")
from RecoBTag.PerformanceMeasurements.Simone_TrackingV2_PF import cms, process
process.load("RecoBTag.PerformanceMeasurements.BTagHLT_stripped_trackV2PF_cff")

process.maxEvents = cms.untracked.PSet(
    # input = cms.untracked.int32(options.maxEvents)
    input = cms.untracked.int32(350)
)


# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    # "root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19MiniAOD/TTbar_14TeV_TuneCP5_Pythia8/MINIAODSIM/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/F0225E24-F876-D448-8318-2D89795D632F.root",
    # "root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/QCD_Pt_50to80_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3-v1/10000/19286DB0-FDED-5A4D-B5F9-4FCDB39A99CE.root",
    #"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/QCD_Pt-15to3000_EMEnriched_TuneCP5_13TeV_pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3-v1/50000/BBB89FE4-5C9D-7842-BDE3-C89FF77630B6.root",
# "file:/eos/cms/store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/A7DE6079-B3AE-4743-A5F3-2050EDEB8383.root"
# "/TTbar_14TeV_TuneCP5_Pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3_ext1-v3/GEN-SIM-DIGI-RAW"
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/EB1607A3-B053-1E42-B9C5-418657AD9E2A.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/B59A04E2-CF58-F346-B0B6-A7454B14C0F3.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/957621E3-08FF-084B-8E89-3D747AB9DC59.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/20061031-92A3-4D47-AF08-4EC299FDC752.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/9D36CE9C-17B4-E145-BA68-77F81AC0ACFD.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/E28C7B13-55CC-0646-BAFD-4F0085B8AC81.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/98E835B6-0AB0-6D40-A949-C448667B8215.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/1C03F9A2-9CB6-7C4C-9560-9F19C89A51A2.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/1A4F16BD-FDB4-A84F-9EB6-19C8A88B81AB.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/42A08D40-F9AC-8C49-90F8-E0B7C9F759E2.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/AE96BA32-D504-464C-8DDA-CB20622335A3.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/36CDD768-084C-454F-8376-3F77C10BB97A.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/3D4C2F0B-3695-1E48-9B41-96969182B6BE.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/ECB818B0-4351-774B-A035-FBDABD1CA90E.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/6C17E344-DF3D-224A-98E9-F79E1B7BA2B5.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/880F8247-B079-F94E-8E6A-32950662D829.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/85BC8B9C-9FAE-E346-9E76-CC5031BFD982.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/3E1FFA6E-B29B-0F43-BDBB-EAA7B7853A51.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/63B2E1B8-B8C9-5146-BFDB-A925C2F4B777.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/29740B47-2365-C34A-9677-EC5D76C73C53.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/B818C522-FDEB-4B41-B829-6CE8DB468280.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/B3310886-C00F-984D-9423-75B9D508543A.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/776AE786-9272-5242-99EA-E92723C41883.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/55BC76FC-8CC9-B44B-B851-BB8AA9920175.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/D1D20C84-37B0-B84F-A7C5-7FEBD3C33D25.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/5349146B-4DB7-2140-A66C-C21D517A252B.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/FAA44C43-4F04-0A42-9555-7D37B2974302.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/02A89E6A-3272-7F46-8FC8-23797F90EB69.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/C9CFC952-60AB-7A4F-A2D1-89BDF2DA99DB.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/FFB5D0CA-208F-6040-A9BF-3F5354D0AA59.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/D7E64507-2006-7C4E-A9D8-97AA44D12419.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/E7B49A7A-079E-8841-A9CA-438B041628F7.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/770E164F-D55E-3143-9F3E-B852C2376DB2.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/090EFD97-8D94-4C4C-9861-375807BBE2A8.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/C4247150-91A1-F046-A5B8-59B07E6CF8B6.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/3518C366-3A54-8742-ADDB-C4B0A4B3F965.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/4809DC89-177E-EE4A-801B-C007977ACC1A.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/23BF8320-DE5D-554E-BDAF-47C0BD9F252B.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/68FD0011-FF20-4F49-970C-7FAB27FF37BC.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/73841836-E91B-9B40-A2EB-970BC6215F80.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/CC9B68BF-A35D-304B-BB3B-4D63567E748F.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/E20E7D32-64C7-F34F-A35F-B6043C5B70CA.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/4C88CF44-5BE1-4442-902C-6BAC1F6A1D2C.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/557F77C0-EDF6-DA42-BCF5-B4398DAA4FE1.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/4DB9081B-5CC7-794B-B297-921AF19D2090.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/EC9BDA84-4F7E-0646-B9EA-5D95EAE21AA4.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/F0EA2FED-7FAB-2741-9862-443DE2B5752B.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/5C3F016E-3339-EE43-A996-C4D40CD77BF5.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/13ED7538-A397-1444-9721-BBE50951AF58.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/464A5A17-5B90-284B-8DE4-AC5B3A7F8701.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/8BB35336-83E6-AF4C-A70F-6CF1D0CA431B.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/9FB41A06-90B4-0B46-BCA5-5DBEA52EEBE6.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/6266D978-3199-8C41-9357-215D40573C46.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/EE49EB78-D071-0643-B158-A776C404E8DF.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/D7BC8491-AB79-8E49-90DC-B7EA2F30E307.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/BFC141F2-5C97-3541-9309-DC7E1C7AA2F9.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/5C715B9B-609E-C748-AD36-D4EFA3865AD8.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/26B0FC53-B098-BA47-97E6-60A8780BC51D.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/34C43DCE-AB2D-744F-BABF-229547AC7DCA.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/8BA2A340-7994-3E4E-98EC-1E955C42DEAB.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/9411003A-FDE6-B442-9D8D-55BDE7CD2D07.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/DED805CC-B940-C849-9922-B316F6ABB754.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/6C579EAD-8401-6848-8B64-95D2EEE9ECAD.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/31510D23-2FA8-E04C-A409-757DF2121A3E.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/3CEDC4EC-04D0-0E46-84C2-C8DF51A3A4E8.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/F693A9AC-6484-5147-99B1-8F281C407BA5.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/06F354F3-2398-D041-A566-9B2930EB8C67.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/FA8F143E-26A5-0D46-BFB5-BF6619A2B779.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/8C9153C2-EF1A-F042-8D53-0B12C50B16BF.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/8D4E3195-3907-AC4C-832D-24EE6307FAD2.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/5E10854A-65BC-3D42-94CF-CD95EE352F57.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/00A52F21-0965-6B45-A642-784D38648683.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/A7DE6079-B3AE-4743-A5F3-2050EDEB8383.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/84253CC9-7E7E-C449-A29D-72A43DD2B781.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/237F12A7-62D3-364A-804F-6448B4DB0FD2.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/34E5241D-86C4-264F-BBDC-032076322A3C.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/E6E9D899-3EDE-FD44-A8DD-0211C5FEAF5F.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/69A9A68B-65ED-314B-B128-DBB93F71A7F3.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/F037A381-8FA4-EC45-9B30-7CDA025AEAE3.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/12295F4B-5623-F94E-B317-19CE0C00AA7E.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/548D3D43-859D-7946-9991-447B104708E5.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/5B0A76CA-2DEA-064F-BFF5-9FF6831386D6.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/CF0F8489-9CBC-3240-8F07-FF24D439BD3A.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/E9F104F6-8E35-C041-A3C4-DE02C9B5EABE.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/C750C1DF-582D-894C-ACEE-4C021759446D.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/D2A456B1-37D2-ED43-AA13-E63E4833C0C0.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/7EE88168-9B7A-AA4E-9C6C-B0A3C4BF4897.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/FAD64ED8-12B6-8944-8A92-DB34B8302AD3.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/A44C4AA0-79C4-D648-9CF1-1673C17B1A2D.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/92DE8C19-3A3A-1848-A7F1-9A077A2FEE51.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/B2E0A432-285C-E34D-BAB4-70F36BDF29F2.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/577B8911-8971-BF48-935E-88E1D7A2FFAC.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/7ABC6C4A-2DB6-0046-BD19-B698E838BB73.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/6F9A2266-C6F2-AC49-B739-879F7DF6F12D.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/116EA228-010D-214E-AA92-2E43F7BBCD2E.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/C60EF8E4-4D9F-C245-9B39-D20868E079DD.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/8F6B0F80-35F1-2240-BC27-F5B9B67461BC.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/278CC614-3BB6-7E47-8A06-D7A4A975D237.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/071EF918-4749-8440-836B-D95D561B2DC4.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/EADD0493-D560-BF4C-8BDE-52D2E29AE588.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/5E8F45C0-190C-2F4C-ABF9-38E44820D598.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/4272D7E2-F8FF-484C-9EA3-41D0B0EBC983.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/9CF634A4-4DA7-C548-83B7-819914139795.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/5F01965B-C017-6448-84CA-0B878DD6A4B5.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/0FEC7389-361E-A448-AB3A-CB1E4E641670.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/6BEC1341-7694-0A43-92C1-5AFF90DB4B4A.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/1345A820-2449-9E43-810A-CC30953865F3.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/73DEB829-CBEF-104E-B042-73882C5255C0.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/6CE50491-57E8-D040-85DD-38BC60D2C78E.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/C00F67EC-6C3D-1340-B17D-EDD384A8B829.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/07DBE6EF-4109-CA4D-855B-3160655A0712.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/D3628B26-FCAC-C741-94FD-5B6764835AEE.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/42F1B648-F3CD-164E-A7EB-29F7D4F34BA7.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/CC74D6D4-8BFE-074E-9008-51AEABE03ED2.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/8B6A225E-812B-4B48-AF84-9A17941D79EC.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/56ED674C-F6BB-184C-BEEA-3AD1B1B5E177.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/3549DF64-8CAF-F346-A626-8612475DBBB9.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/B731670E-2B61-FB4C-85E0-4CB98A680814.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/EC424AE8-76A8-5142-8111-640534C1EF7A.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/F5B6A85F-F39C-1A4A-9313-B0AE5E469F4A.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/C1345D53-79EC-B74D-A725-DC6594186F31.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/599708A5-F52F-3340-BA0C-44B31A5D6E8B.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/852B8056-D213-7944-8075-136990279113.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/18F690FB-6D4B-8A4F-B01D-6243CAF8E9FD.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/5CB15C44-9FB9-3247-9463-F65EE8A690E7.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/B7171723-7DBD-6D45-8CF9-02BCB61F3A86.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/1DE0B9E3-A1C0-C042-A38E-F1FEECB8DF56.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/26044055-8CDA-334A-8840-485D98586DD4.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/E48ABBC9-01D0-6B49-8919-32AADE090354.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/E21BE6B8-F362-B140-A049-56619C42C050.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/A4664AD2-9D37-0B40-A78E-6FFE3D6BA16C.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/0C8795A3-EF1D-D449-981B-994DF71D415F.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/E0AA2631-0C70-2649-B703-6F95E8F1547A.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/B4374A34-478F-274C-B88C-D7C9A9A11D4D.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/9B28B018-5094-4B4E-801B-A79073FD45E7.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/C4CE0C0A-D3F7-9642-9460-6FE89FC0EE3A.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/7395F93A-66F3-AA4D-86C9-A04A8FED69F5.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/2DC88D55-3191-9E42-9AED-AC34867B8A82.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/8062FD05-0BE2-F64D-AF71-EF7FD8E72B3E.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/4E1629C4-74D8-894F-967C-806B8E24562F.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/3AC9C8FB-7464-3C4D-BFD2-7D6FDBC33CC0.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/63D7D147-1CB7-274E-A5FB-D87C2A942004.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/07E225BE-8790-C64B-BB3B-7FBD56C7AC08.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/3CD082D2-9FAB-B047-9A52-7973B1009540.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/29581CC9-9993-5449-AF0E-BFF473BFCCF1.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/0744F53B-F477-6C4A-92E2-796F4CDEECB2.root"
),
#    fileNames = cms.untracked.vstring('file:/eos/cms/store/mc/PhaseIITDRSpring19DR/QCD_Pt-15to3000_TuneCP5_Flat_14TeV-pythia8/GEN-SIM-DIGI-RAW/NoPU_castor_106X_upgrade2023_realistic_v3-v2/270000/07A5023E-D011-E448-87A6-FD9586277D47.root'),
    secondaryFileNames = cms.untracked.vstring()
)
process.options = cms.untracked.PSet(
)


# process.load("RecoBTag.PerformanceMeasurements.BTagHLT_stripped_cff")


#redefining reconstruction_step
process.reconstruction = cms.Sequence(process.localreco+
    process.globalreco
    +process.particleFlowReco
    +process.ak4PFJets
    +process.fixedGridRhoFastjetAll
    +process.ak4PFL1FastjetCorrector
    +process.ak4PFJetsCorrected
    +process.particleFlowPtrs
    +process.goodOfflinePrimaryVertices
    +process.pfPileUpJME
    +process.pfNoPileUpJME
    +process.ak4PFJetsCHS
    +process.ak4PFCHSL1FastjetCorrector
    +process.ak4PFCHSL2RelativeCorrector
    +process.ak4PFCHSL3AbsoluteCorrector
    +process.ak4PFCHSL1FastL2L3Corrector
    +process.ak4PFJetsCHSCorrected
)


# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
#process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)

process.noFilter_PFDeepCSV = cms.Path(process.HLTBtagDeepCSVSequencePF)


process.hltOutput = cms.OutputModule( "PoolOutputModule",
     fileName = cms.untracked.string( "hltoutput_hlt.root" ),
     fastCloning = cms.untracked.bool( False ),
     outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_particleFlowTmp*_*_*',
         'keep *_ak4PFJets*_*_*',
         'keep *_ak4PFJets*_*_RECO',
         'keep *_ak4GenJets_*_HLT',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsInfos_*_*',
        # # 'keep *_hltDeepCombinedSecondaryVertexBJetTagsInfosCalo_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsPF*_*_*',
         )
     )

#~ process.DQMStore.enableMultiThread = True
process.DQMStore.enableMultiThread = False

#~ process.options.numberOfStreams = cms.untracked.uint32(4)
#~ process.options.numberOfThreads = cms.untracked.uint32(4)
process.options.numberOfStreams = cms.untracked.uint32(1)
process.options.numberOfThreads = cms.untracked.uint32(1)



#===========
# Begin BTagAna

###############################
####### Parameters ############
###############################

groups = ["HLTEventInfo","HLTJetInfo","HLTTagVar","HLTJetTrack","HLTJetSV","HLTCSVTagVar"]



from RecoBTag.PerformanceMeasurements.BTagAnalyzer_cff import *
btagana_tmp = bTagAnalyzer.clone()
print('Storing the variables from the following groups:')
options_to_change = set() #store which swtiches we need on
# for requiredGroup in options.groups:
for requiredGroup in groups:
  print(requiredGroup)
  found=False
  for existingGroup in btagana_tmp.groups:
    if(requiredGroup==existingGroup.group):
      existingGroup.store=True
      for var in existingGroup.variables:
        if "CaloJet." in var:
          var = var.split(".")[1]
        if "PFJet." in var:
          var = var.split(".")[1]
        options_to_change.update([i for i in variableDict[var].runOptions])
      found=True
      break
  if(not found):
    print('WARNING: The group ' + requiredGroup + ' was not found')




# print "Running on data: %s"%('True' if options.runOnData else 'False')
# print "Running with globalTag: %s"%(options.globalTag)
print "Running with globalTag: %s"%("auto:phase2_realistic")

# trigresults='TriggerResults::HLT'
# trigresults='TriggerResults'

# if options.inputFiles:
#     process.source.fileNames = options.inputFiles



## Define the output file name
# if options.runOnData :
#     options.outFilename += '_data'
# else :
#     options.outFilename += '_mc'
#
# options.outFilename += '.root'
outFilename = 'JetTree_mc.root'

## Output file
process.TFileService = cms.Service("TFileService",
   # fileName = cms.string(options.outFilename)
   fileName = cms.string(outFilename)
)


## Options and Output Report
process.options   = cms.untracked.PSet(
    # wantSummary = cms.untracked.bool(options.wantSummary),
    wantSummary = cms.untracked.bool(False),
    allowUnscheduled = cms.untracked.bool(True)
)


#-------------------------------------
## Output Module Configuration (expects a path 'p')
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent
process.out = cms.OutputModule("PoolOutputModule",
                               # fileName = cms.untracked.string(options.outFilename),
                               fileName = cms.untracked.string(outFilename),
                               # save only events passing the full path
                               SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               # save PAT Layer 1 output; you need a '*' to
                               # unpack the list of commands 'patEventContent'
                               outputCommands = cms.untracked.vstring('drop *', *patEventContent)
                               #outputCommands = cms.untracked.vstring('keep *')
)


#-------------------------------------
from RecoBTag.PerformanceMeasurements.BTagHLTAnalyzer_cff import *
process.btagana = bTagHLTAnalyzer.clone()

#------------------
#Handle groups
for requiredGroup in process.btagana.groups:
   for storedGroup in btagana_tmp.groups:
     if (requiredGroup.group == storedGroup.group):
       requiredGroup.store = storedGroup.store

process.btagana.MaxEta                = 2.4
process.btagana.MinPt                 = 30
# process.btagana.triggerTable          = cms.InputTag('TriggerResults::HLT') # Data and MC
process.btagana.triggerTable          = cms.InputTag('TriggerResults::RECO2') # Data and MC
process.btagana.primaryVertexColl     = cms.InputTag('hltVerticesPF')
# process.btagana.primaryVertexColl     = cms.InputTag('firstStepPrimaryVertices')

process.btagana.runHLTJetVariables     = cms.bool(True)
# process.btagana.runOnData = options.runOnData
process.btagana.runOnData = False

process.btagana.PFJets               = cms.InputTag('ak4PFJetsCHSCorrected')
process.btagana.PFJetTags            = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsInfos')
process.btagana.PFSVs                = cms.InputTag('hltDeepSecondaryVertexTagInfosPF')
# process.btagana.PFJetCSVTags         = cms.InputTag('hltCombinedSecondaryVertexBJetTagsPF')
process.btagana.PFJetDeepCSVTags     = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPF:probb')



#---------------------------------------
## Event counter
from RecoBTag.PerformanceMeasurements.eventcounter_cfi import eventCounter
process.allEvents = eventCounter.clone()
process.selectedEvents = eventCounter.clone()
#---------------------------------------




## Define analyzer sequence
process.analyzerSeq = cms.Sequence(process.btagana)



process.p = cms.Path(
    process.allEvents
    #* process.filtSeq
    * process.selectedEvents
    # * process.analyzerSeq
)


process.analysisNTupleEndPath = cms.EndPath(process.analyzerSeq)


del process.out

# open('pydump.py','w').write(process.dumpPython())
