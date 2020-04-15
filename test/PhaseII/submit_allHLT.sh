#!/bin/bash

echo "!!!! WARNING: Submitting for MC!!!"
python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p htrk=True reco=hltPhase2_TRKv06 \
  -v crab_projects_HLTTDR_TrackingV6_v1 \
  -t 2750 \
  -m 3500
