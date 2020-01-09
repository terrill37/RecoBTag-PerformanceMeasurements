# RecoBTag-PerformanceMeasurements

## Software setup for CMSSW_11_0_0

```
cmsrel CMSSW_11_0_0
cd CMSSW_11_0_0/src
cmsenv

git cms-init

git cms-addpkg RecoBTag
git cms-addpkg PhysicsTools/PatAlgos
git cms-addpkg RecoBTag/TensorFlow
git cms-addpkg RecoBTag/Combined
git clone -b PrunedTraining_NoPuppi https://github.com/emilbols/RecoBTag-Combined RecoBTag/Combined/data
wget https://raw.githubusercontent.com/cms-data/RecoBTag-Combined/master/DeepCSV_PhaseII.json -P RecoBTag/Combined/data/
git clone -b PhaseIIOnline --depth 1 https://github.com/johnalison/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements

git cms-merge-topic missirol:devel_pixvtx_buildfile_1100pre13

scram b -j8

```
