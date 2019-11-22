CONFIG="runBTagAnalyzer_PhaseII_cfg.py"
DIR1="Phase2_output"
WORKDIR="/afs/cern.ch/work/s/sewuchte/private/BTag_Upgrade/new/CMSSW_11_0_0_pre7/src/RecoBTag/PerformanceMeasurements/test/PhaseII/"
OUTDIR="/eos/home-s/sewuchte/BTV/PhaseII/Offline/"
PROXYPATH="/afs/cern.ch/user/s/sewuchte/.vomsproxy/x509"

./cmsCondor.py $CONFIG -n 1 -d $DIR1 $WORKDIR $OUTDIR -p $PROXYPATH



# 1. -n 1 indicate you want one file per job
#
# 2. The directory Phase2_output is the where the Jobs are created
#
# 3. /afs/cern.ch/user/g/gennai/Phase2/CMSSW_11_0_0_pre7/src/RatesProd/
# Is the working dir from where you create and submit the jobs
#
# 4. /afs/cern.ch/user/g/gennai/Phase2/CMSSW_11_0_0_pre7/src/RatesProd/Phase2_output
# Is she directory where you want the output root files to be stored (you can use your /eos area if you wish)
#
# 5. -p  /afs/cern.ch/user/g/gennai/x509up_u28895 is the directory where you copy your proxy (it is needed if you try to access data through xrootd protocol).
#
# To submit the jobs you have to use the command:
# ./sub_total.jobb
# (The file will be produced by the script)
