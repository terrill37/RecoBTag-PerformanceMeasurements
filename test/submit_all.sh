#!/bin/bash

### 2018
#echo "!!!! WARNING: Submitting for Data 2018!!!!"
###echo "!!!! WARNING: Submitting for MC!!!"
#python submit_all.py \
#  runBTagAnalyzer_cfg.py \
#  -f CRAB/tosubmitMINIAOD.txt \
#  -s T3_US_FNALLPC \
#  -p miniAOD=True  runOnData=True groups='EventInfo,PV,TagVar,JetInfo,JetSV,JetTrack,CSVTagVar,PFElectron,PFMuon,PatMuon,JetDeepCSV,PatElec' dataGlobalTag='101X_dataRun2_Prompt_v11' JPCalibration='JPcalib_Data102X_2018_v1' usePrivateJEC=True     jecDBFileData='Autumn18_RunABCD_V8_DATA'     eras='Run2_2018' runDeepFlavourTagVariables=False \
#  -o /store/user/johnda/BTagNTuples/2018/ \
#  -l /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt \
#  -v crab_projects_v8

#echo "!!!! WARNING: Submitting for Data 2018!!!!"
###echo "!!!! WARNING: Submitting for MC!!!"
#python submit_all.py \
#  runBTagAnalyzer_cfg.py \
#  -f CRAB/tosubmitMINIAOD.txt \
#  -s T3_US_FNALLPC \
#  -p miniAOD=True  runOnData=True groups='EventInfo,PV,TagVar,JetInfo,JetSV,JetTrack,CSVTagVar,PFElectron,PFMuon,PatMuon,JetDeepCSV,PatElec,JetDeepFlavour' dataGlobalTag='102X_dataRun2_Sep2018Rereco_v1' JPCalibration='JPcalib_Data102X_2018_v1' usePrivateJEC=True     jecDBFileData='Autumn18_RunABCD_V8_DATA'     eras='Run2_2018' runDeepFlavourTagVariables=True \
#  -o /store/user/johnda/BTagNTuples/2018/ \
#  -l /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt \
#  -v crab_projects_v9



# 2017
echo "!!!! WARNING: Submitting for Data 2017!!!!"
##echo "!!!! WARNING: Submitting for MC!!!"
python submit_all.py \
  runBTagAnalyzer_cfg.py \
  -f CRAB/tosubmitMINIAOD.txt \
  -s T3_US_FNALLPC \
  -p miniAOD=True  runOnData=True groups='EventInfo,PV,TagVar,JetInfo,JetSV,JetTrack,CSVTagVar,PFElectron,PFMuon,PatMuon,JetDeepCSV,PatMuon,PatElec,JetDeepFlavour' dataGlobalTag='94X_dataRun2_ReReco_EOY17_v2' JPCalibration='JPcalib_Data94X_2017_v1' usePrivateJEC=True     jecDBFileData='Fall17_17Nov2017_V32_94X_DATA'     eras='Run2_2017' runDeepFlavourTagVariables=True \
  -o /store/user/johnda/BTagNTuples/2017/ \
  -l /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt \
  -v crab_projects_v3

