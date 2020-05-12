# RecoBTag-PerformanceMeasurements

## Software setup

```
cmsrel CMSSW_11_1_0_pre5
cd CMSSW_11_1_0_pre5/src
cmsenv

export CMSSW_GIT_REFERENCE=/cvmfs/cms.cern.ch/cmssw.git.daily
git cms-init

git cms-addpkg RecoBTag
git cms-addpkg RecoBTag/TensorFlow
git cms-addpkg RecoBTag/Combined

git clone -b PrunedTraining_NoPuppi https://github.com/emilbols/RecoBTag-Combined RecoBTag/Combined/data
wget https://raw.githubusercontent.com/cms-data/RecoBTag-Combined/master/DeepCSV_PhaseII.json -P RecoBTag/Combined/data/

git clone -b PhaseIIOffline --depth 1 https://github.com/johnalison/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements


```

For running on the HLT one needs to use RAW and there are very few options availbe here is the command I have working:

