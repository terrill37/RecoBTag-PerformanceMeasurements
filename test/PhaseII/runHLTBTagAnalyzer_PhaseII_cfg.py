### configuration file to re-run customized HLT Menu on RAW
# from RecoBTag.PerformanceMeasurements.Simone_TrackingV0 import cms, process
# process.load("RecoBTag.PerformanceMeasurements.BTagHLT_stripped_cff")
from RecoBTag.PerformanceMeasurements.Simone_TrackingV2_PF import cms, process
process.load("RecoBTag.PerformanceMeasurements.BTagHLT_stripped_trackV2PF_cff")

process.maxEvents = cms.untracked.PSet(
    # input = cms.untracked.int32(options.maxEvents)
    input = cms.untracked.int32(250)
)


# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    # "root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19MiniAOD/TTbar_14TeV_TuneCP5_Pythia8/MINIAODSIM/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/F0225E24-F876-D448-8318-2D89795D632F.root",
    # "root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/QCD_Pt_50to80_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3-v1/10000/19286DB0-FDED-5A4D-B5F9-4FCDB39A99CE.root",
    #"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/QCD_Pt-15to3000_EMEnriched_TuneCP5_13TeV_pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3-v1/50000/BBB89FE4-5C9D-7842-BDE3-C89FF77630B6.root",
# "file:/eos/cms/store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/A7DE6079-B3AE-4743-A5F3-2050EDEB8383.root"
# "/TTbar_14TeV_TuneCP5_Pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3_ext1-v3/GEN-SIM-DIGI-RAW"
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
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/0744F53B-F477-6C4A-92E2-796F4CDEECB2.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/29581CC9-9993-5449-AF0E-BFF473BFCCF1.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/3CD082D2-9FAB-B047-9A52-7973B1009540.root"
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
