#!/bin/bash

echo "!!!! WARNING: Submitting for Data!!!!"
##echo "!!!! WARNING: Submitting for MC!!!"
python submit_all.py \
  runBTagAnalyzer_cfg.py \
  -f CRAB/tosubmitMINIAOD.txt \
  -s T3_US_FNALLPC \
  -p miniAOD=True  runOnData=True groups='EventInfo,PV,TagVar,JetInfo,JetSV,JetTrack,CSVTagVar,PFElectron,PFMuon,PatMuon,JetDeepCSV' dataGlobalTag='101X_dataRun2_Prompt_v11' JPCalibration='JPcalib_Data102X_2018_v1' usePrivateJEC=True     jecDBFileData='Autumn18_RunABCD_V8_DATA'     eras='Run2_2018' runDeepFlavourTagVariables=False \
  -o /store/user/johnda/BTagNTuples/2018/ \
  -l /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt \
  -v crab_projects_v5

