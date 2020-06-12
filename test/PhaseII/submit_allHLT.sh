#!/bin/bash

echo "!!!! WARNING: Submitting for MC!!!"
python submit_allHLT.py \
  runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f CRAB/tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=hltPhase2_TRKv00 \
  -v crab_projects_HLTTDR_TrackingV0_DebugPuppiv3 \
  -t 2750 \
  -m 3500

# python submit_allHLT.py \
#   runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f CRAB/tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=hltPhase2_TRKv02 \
#   -v crab_projects_HLTTDR_TrackingV2_v6 \
#   -t 2750 \
#   -m 3500

# python submit_allHLT.py \
#   runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f CRAB/tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=hltPhase2_TRKv06 \
#   -v crab_projects_HLTTDR_TrackingV6_v6 \
#   -t 2750 \
#   -m 3500

# python submit_allHLT.py \
#   runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f CRAB/tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=hltPhase2_TRKv06_skimmedTracks \
#   -v crab_projects_HLTTDR_TrackingV6_skimmedTracks_v6 \
#   -t 2750 \
#   -m 3500

# python submit_allHLT.py \
#   runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f CRAB/tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=hltPhase2_TRKv00_TICL \
#   -v crab_projects_HLTTDR_TrackingV0TICL_v6 \
#   -t 2750 \
#   -m 4500
#
# python submit_allHLT.py \
#   runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f CRAB/tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=hltPhase2_TRKv02_TICL \
#   -v crab_projects_HLTTDR_TrackingV2TICL_v6 \
#   -t 2750 \
#   -m 4500
#
# python submit_allHLT.py \
#   runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f CRAB/tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=hltPhase2_TRKv06_TICL \
#   -v crab_projects_HLTTDR_TrackingV6TICL_v6 \
#   -t 2750 \
#   -m 4500

# python submit_allHLT.py \
#   runHLTBTagAnalyzer_PhaseII_cfg.py \
#   -f CRAB/tosubmit.txt \
#   -s T2_DE_DESY \
#   -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
#   -p reco=hltPhase2_TRKv06_TICL_skimmedTracks \
#   -v crab_projects_HLTTDR_TrackingV6TICL_skimmedTracks_v6 \
#   -t 2750 \
#   -m 4500
