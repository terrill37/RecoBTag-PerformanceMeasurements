#!/bin/bash

echo "!!!! WARNING: Submitting for Data!!!!"
###echo "!!!! WARNING: Submitting for MC!!!"
python submit_allHLT.py \
  runHLTBTagAnalyzer_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T3_US_FNALLPC \
  -p groups="HLTEventInfo,HLTJetInfo,HLTTagVar,HLTJetTrack,HLTJetSV,HLTCSVTagVar" runOnData=True \
  -o /store/user/johnda/BTagNTuples/2017RAW/ \
  -l /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt \
  -v crab_projects_v4



  #-l /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt \