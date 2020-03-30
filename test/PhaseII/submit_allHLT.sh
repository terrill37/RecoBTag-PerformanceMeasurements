#!/bin/bash

echo "!!!! WARNING: Submitting for MC!!!"
python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p htrk=True doTrackV0=True \
  -v crab_projects_HLTTDR_TrackingV0_v2 \
  -t 2750 \
  -m 3500

python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p htrk=True doTrackV0=False \
  -v crab_projects_HLTTDR_TrackingV2_v2 \
  -t 2750 \
  -m 3500
