
#!/bin/bash

#echo "!!!! WARNING: Submitting for Data!!!!"
echo "!!!! WARNING: Submitting for MC!!!"
python submit_allHLT.py \
  runHLTBTagAnalyzer_cfg.py \
  -f CRAB/tosubmit_MC.txt \
  -s T3_US_FNALLPC \
  -p groups="HLTEventInfo,HLTJetInfo,HLTTagVar,HLTJetTrack,HLTJetSV,HLTCSVTagVar" runOnData=False globalTag="102X_upgrade2018_realistic_v15" \
  -o /store/user/johnda/BTagNTuples/2018/ \
  -v crab_projects_v2

