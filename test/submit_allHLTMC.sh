
#!/bin/bash

#echo "!!!! WARNING: Submitting for Data!!!!"
echo "!!!! WARNING: Submitting for MC!!!"
python submit_allHLT.py \
  runHLTBTagAnalyzer_cfg.py \
  -f CRAB/tosubmit_MC.txt \
  -s T2_DE_DESY \
  -p groups="HLTEventInfo,HLTJetInfo,HLTTagVar,HLTJetTrack,HLTJetSV,HLTCSVTagVar" runOnData=False globalTag="110X_mcRun3_2021_realistic_v6" \
  -o /store/user/lmastrol/Run3/trackPt0p4 \
  -v crab_projects_run3_trackPt0p4
