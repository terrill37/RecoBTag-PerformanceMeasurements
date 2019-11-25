# import FWCore.ParameterSet.Config as cms

from RecoBTag.PerformanceMeasurements.Simone_TrackingV2_PF import cms, process
# process.load("RecoBTag.PerformanceMeasurements.BTagHLT_stripped_trackV2PF_cff")

# process.maxEvents = cms.untracked.PSet(
#     # input = cms.untracked.int32(options.maxEvents)
#     input = cms.untracked.int32(10)
# )

# from FWCore.ParameterSet.VarParsing import VarParsing
import copy
from pdb import set_trace

###############################
####### Parameters ############
###############################

miniAod=True
groups = ["EventInfo","PV,TagVar","JetInfo","JetSV","JetTrack","CSVTagVar","PFElectron","PFMuon","JetDeepCSV","PatMuon,PatElec","JetDeepFlavour"]
# groups = ["EventInfo"]
runOnData=False

outFilename="JetTree_mc.root"

usePFchs = True
usePuppi = False
usePuppiForFatJets=True
usePuppiForBTagging=False

mcGlobalTag='auto:phase2_realistic'

runJetClustering=False
runFatJetClustering=False
runFatJets=False
runSubJets=False
runEventInfo=False
processStdAK4Jets=True
producePtRelTemplate=False
fatJetRawPtMin=150.
fatJetPtMin=200.
fatJetAbsEtaMax=2.5

useTTbarFilter=False
remakeAllDiscr=False
remakeDoubleB=False
fastSim=False
useSelectedTracks=True
useExplicitJTA=False
jetAlgo='AntiKt'
fatJetRadius=0.8
useLegacyTaggers=False
useSoftDrop=True
usePruned=False
useTrackHistory=False
produceJetTrackTree=False
produceAllTrackTree=False
useNegativeDeepFlavourTags=False
runIVF=False
doBoostedCommissioning=False
runCTagVariables=False
fillPU=True
changeMinNumberOfHits=False
minNumberOfHits=1
maxJetEta=2.5
minJetPt=20.0
usePrivateJEC=False
jecDBFileMC='FIXME'
JPCalibration='JPcalib_MC94X_2017_v1'
jecDBFileData='FIXME'
isReHLT=False
runJetVariables=True
runTagVariables=True
runQuarkVariables=False
runHadronVariables=False
runGenVariables=False
runCSVTagVariables=False
runCSVTagVariablesSubJets=False
runTagVariablesSubJets=False
runCSVTagTrackVariables=False
runPrunedDeepFlavourTaggers=False
runDeepFlavourTagVariables=False
runDeepDoubleXTagVariables=False
runDeepBoostedJetTagVariables=False
runPFElectronVariables=False
runPFMuonVariables=False
runPatMuons=False
runPatElecs=False
defaults=''
eras=[]
groups=['EventInfo','PV','TagVar','JetInfo','JetSV','JetTrack','CSVTagVar','PFElectron','PFMuon','JetDeepCSV','PatMuon','PatElec']
skipEvents=0



#redefining reconstruction_step
# process.reconstruction = cms.Sequence(process.localreco+
#     process.globalreco
#     +process.particleFlowReco
#     +process.ak4PFJets
#     +process.fixedGridRhoFastjetAll
#     +process.ak4PFL1FastjetCorrector
#     +process.ak4PFJetsCorrected
#     +process.particleFlowPtrs
#     +process.goodOfflinePrimaryVertices
#     +process.pfPileUpJME
#     +process.pfNoPileUpJME
#     +process.ak4PFJetsCHS
#     +process.ak4PFCHSL1FastjetCorrector
#     +process.ak4PFCHSL2RelativeCorrector
#     +process.ak4PFCHSL3AbsoluteCorrector
#     +process.ak4PFCHSL1FastL2L3Corrector
#     +process.ak4PFJetsCHSCorrected
# )


# Path and EndPath definitions
# process.raw2digi_step = cms.Path(process.RawToDigi)
#process.L1Reco_step = cms.Path(process.L1Reco)
# process.reconstruction_step = cms.Path(process.reconstruction)

# process.noFilter_PFDeepCSV = cms.Path(process.HLTBtagDeepCSVSequencePF)


# process.hltOutput = cms.OutputModule( "PoolOutputModule",
#      fileName = cms.untracked.string( "hltoutput_hlt.root" ),
#      fastCloning = cms.untracked.bool( False ),
#      outputCommands = cms.untracked.vstring(
#         'drop *',
#         'keep *_particleFlowTmp*_*_*',
#          'keep *_ak4PFJets*_*_*',
#          'keep *_ak4PFJets*_*_RECO',
#          'keep *_ak4GenJets_*_HLT',
#         'keep *_hltDeepCombinedSecondaryVertexBJetTagsInfos_*_*',
#         # # 'keep *_hltDeepCombinedSecondaryVertexBJetTagsInfosCalo_*_*',
#         'keep *_hltDeepCombinedSecondaryVertexBJetTagsPF*_*_*',
#          )
#      )

#~ process.DQMStore.enableMultiThread = True
# process.DQMStore.enableMultiThread = False
#
# #~ process.options.numberOfStreams = cms.untracked.uint32(4)
# #~ process.options.numberOfThreads = cms.untracked.uint32(4)
# process.options.numberOfStreams = cms.untracked.uint32(1)
# process.options.numberOfThreads = cms.untracked.uint32(1)



#===========
# Begin BTagAna


# options.register('defaults', '',
#     VarParsing.multiplicity.singleton,
#     VarParsing.varType.string,
#     'baseline default settings to be used')
# options.register('eras', [],
#     VarParsing.multiplicity.list,
#     VarParsing.varType.string,
#     'era modifiers to be used to be used')
# options.register('groups', [],
#     VarParsing.multiplicity.list,
#     VarParsing.varType.string,
#     'variable groups to be stored')
# options.register(
#     'skipEvents', 0,
#     VarParsing.multiplicity.singleton,
#     VarParsing.varType.int,
#     "skip N events"
# )

## 'maxEvents' is already registered by the Framework, changing default value
# options.setDefault('maxEvents', -1)

# options.parseArguments()
# if defaults:
# 	from importlib import import_module
# 	try:
# 		defaults = import_module('RecoBTag.PerformanceMeasurements.defaults.%s' % defaults)
# 	except ImportError:
# 		raise ValueError('The default settings named %s.py are not present in PerformanceMeasurements/python/defaults/' % defaults)
# 	if not hasattr(defaults, 'common') or not isinstance(defaults.common, dict):
# 		raise RuntimeError('the default file %s.py does not contain a dictionary named common' % defaults)
# 	items = defaults.common.items()
# 	if hasattr(defaults, 'data') and runOnData:
# 		if not isinstance(defaults.data, dict):
# 			raise RuntimeError('the default file %s.py contains an object called "data" which is not a dictionary' % defaults)
# 		items.extend(defaults.data.items())
# 	if hasattr(defaults, 'mc') and not runOnData:
# 		if not isinstance(defaults.mc, dict):
# 			raise RuntimeError('the default file %s.py contains an object called "mc" which is not a dictionary' % defaults)
# 		items.extend(defaults.mc.items())
# 	for key, value in items:
# 		if key not in options._beenSet:
# 			raise ValueError('The key set by the defaults: %s does not exist among the cfg options!' % key)
# 		elif not options._beenSet[key]:
# 			if key == 'inputFiles' and options.inputFiles: continue #skip input files that for some reason are never considered set
# 			print 'setting default option for', key
# 			setattr(options, key, value)

from RecoBTag.PerformanceMeasurements.BTagAnalyzer_cff import *
btagana_tmp = bTagAnalyzer.clone()
print('Storing the variables from the following groups:')
options_to_change = set() #store which swtiches we need on
for requiredGroup in groups:
  print(requiredGroup)
  found=False
  for existingGroup in btagana_tmp.groups:
    if(requiredGroup==existingGroup.group):
      existingGroup.store=True
      for var in existingGroup.variables:
        if "FatJetInfo." in var:
          options_to_change.update({"runFatJets"})
          var = var.split(".")[1]
        if "SubJetInfo." in var:
          options_to_change.update({"runSubJets"})
          var = var.split(".")[1]
        options_to_change.update([i for i in variableDict[var].runOptions])
      found=True
      break
  if(not found):
    print('WARNING: The group ' + requiredGroup + ' was not found')

#change values accordingly
# for switch in options_to_change:
#   if switch not in options._beenSet:
#     raise ValueError('The option set by the variables: %s does not exist among the cfg options!' % switch)
#   elif not options._beenSet[switch]:
#     print 'Turning on %s, as some stored variables demands it' % switch
#     setattr(options, switch, True)


## Use either PFchs or Puppi
if usePFchs and usePuppi:
    print "WARNING: Both usePFchs and usePuppi set to True. Giving priority to Puppi."
    usePFchs = False

## Resolve potential conflicts in Puppi usage
if usePuppi and not usePuppiForFatJets:
    print "WARNING: usePuppi set to True while usePuppiForFatJets set to False. Puppi will be used for all jet types."
    usePuppiForFatJets = True

print "Running on data: %s"%('True' if runOnData else 'False')
print "Running using FastSim samples: %s"%('True' if fastSim else 'False')
print "Running on MiniAOD: %s"%('True' if miniAod else 'False')
print "Using PFchs: %s"%('True' if usePFchs else 'False')
print "Using Puppi: %s"%('True' if usePuppi else 'False')
print "Using Puppi for fat jets: %s"%('True' if usePuppiForFatJets else 'False')
print "Using Puppi for b tagging: %s"%('True' if (usePuppi and usePuppiForBTagging) else 'False')

## Subjets only stored when also running over fat jets
# if runSubJets and not runFatJets:
#     print "WARNING: You are attempting to store subjet information without running over fat jets. Please enable running over fat jets in order to store the subjet information."
#     runSubJets = False

# if not miniAod and runDeepFlavourTagVariables: #FIXME
#     print "WARNING: switching off DeepFlavour, as it is not supported in AOD"
#     runDeepFlavourTagVariables = False

# if doBoostedCommissioning:
#     print "**********NTuples will be made for boosted b tag commissioning. The following switches will be reset:**********"
#     processStdAK4Jets=False
#     print "Option processStdAK4Jets will be set to '",processStdAK4Jets,"'"
#     runFatJets=True
#     runSubJets = True
#     print "Option runFatJets will be set to '",runFatJets,"'"
#     print "Option runSubJets  will be set to '",runSubJets,"'"
#     print "********************"
# if runCTagVariables:
#     print "**********You are making NTuple for CTag*************"

## Global tag
globalTag = mcGlobalTag
# if runOnData:
#     globalTag = options.dataGlobalTag

## Jet energy corrections
jetCorrectionsAK4 = ('AK4PF', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None')
jetCorrectionsAK8 = ('AK8PF', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None')
if usePFchs:
    jetCorrectionsAK4 = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None')
    jetCorrectionsAK8 = ('AK8PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None')
# if usePuppi:
#     jetCorrectionsAK4 = ('AK4PFPuppi', ['L2Relative', 'L3Absolute'], 'None')
if usePuppiForFatJets:
    jetCorrectionsAK8 = ('AK8PFPuppi', ['L2Relative', 'L3Absolute'], 'None')

# if runOnData:
#     jetCorrectionsAK4[1].append('L2L3Residual')
#     jetCorrectionsAK8[1].append('L2L3Residual')

jetCorrectionsSubJets = copy.deepcopy(jetCorrectionsAK4)
if not usePuppi and usePuppiForFatJets:
    jetCorrectionsSubJets = ('AK4PFPuppi', ['L2Relative', 'L3Absolute'], 'None')

trigresults='TriggerResults::HLT'
# if runOnData: isReHLT=False
if isReHLT: trigresults = trigresults+'2'


## b-tag infos
bTagInfosLegacy = [
    'impactParameterTagInfos'
   ,'secondaryVertexTagInfos'
   ,'inclusiveSecondaryVertexFinderTagInfos'
   ,'secondaryVertexNegativeTagInfos'
   ,'inclusiveSecondaryVertexFinderNegativeTagInfos'
   ,'softPFMuonsTagInfos'
   ,'softPFElectronsTagInfos'
]
bTagInfos = [
    'pfImpactParameterTagInfos'
   ,'pfSecondaryVertexTagInfos'
   ,'pfInclusiveSecondaryVertexFinderTagInfos'
   ,'pfSecondaryVertexNegativeTagInfos'
   ,'pfInclusiveSecondaryVertexFinderNegativeTagInfos'
   ,'softPFMuonsTagInfos'
   ,'softPFElectronsTagInfos'
   ,'pfInclusiveSecondaryVertexFinderCvsLTagInfos'
   ,'pfInclusiveSecondaryVertexFinderNegativeCvsLTagInfos'
   ,'pfDeepFlavourTagInfos'
]
bTagInfos_noDeepFlavour = bTagInfos[:-1]
## b-tag discriminators
bTagDiscriminatorsLegacy = set([
    'jetBProbabilityBJetTags'
   ,'jetProbabilityBJetTags'
   ,'positiveOnlyJetBProbabilityBJetTags'
   ,'positiveOnlyJetProbabilityBJetTags'
   ,'negativeOnlyJetBProbabilityBJetTags'
   ,'negativeOnlyJetProbabilityBJetTags'
   ,'trackCountingHighPurBJetTags'
   ,'trackCountingHighEffBJetTags'
   ,'negativeTrackCountingHighEffBJetTags'
   ,'negativeTrackCountingHighPurBJetTags'
   ,'simpleSecondaryVertexHighEffBJetTags'
   ,'simpleSecondaryVertexHighPurBJetTags'
   ,'negativeSimpleSecondaryVertexHighEffBJetTags'
   ,'negativeSimpleSecondaryVertexHighPurBJetTags'
   ,'combinedSecondaryVertexV2BJetTags'
   ,'positiveCombinedSecondaryVertexV2BJetTags'
   ,'negativeCombinedSecondaryVertexV2BJetTags'
   ,'combinedInclusiveSecondaryVertexV2BJetTags'
   ,'positiveCombinedInclusiveSecondaryVertexV2BJetTags'
   ,'negativeCombinedInclusiveSecondaryVertexV2BJetTags'
   ,'softPFMuonBJetTags'
   ,'positiveSoftPFMuonBJetTags'
   ,'negativeSoftPFMuonBJetTags'
   ,'softPFElectronBJetTags'
   ,'positiveSoftPFElectronBJetTags'
   ,'negativeSoftPFElectronBJetTags'
   ,'combinedMVAv2BJetTags'
   ,'negativeCombinedMVAv2BJetTags'
   ,'positiveCombinedMVAv2BJetTags'
])
bTagDiscriminators = set([
    'pfJetBProbabilityBJetTags'
   ,'pfJetProbabilityBJetTags'
   ,'pfPositiveOnlyJetBProbabilityBJetTags'
   ,'pfPositiveOnlyJetProbabilityBJetTags'
   ,'pfNegativeOnlyJetBProbabilityBJetTags'
   ,'pfNegativeOnlyJetProbabilityBJetTags'
   ,'pfTrackCountingHighPurBJetTags'
   ,'pfTrackCountingHighEffBJetTags'
   ,'pfNegativeTrackCountingHighPurBJetTags'
   ,'pfNegativeTrackCountingHighEffBJetTags'
   ,'pfSimpleSecondaryVertexHighEffBJetTags'
   ,'pfSimpleSecondaryVertexHighPurBJetTags'
   ,'pfNegativeSimpleSecondaryVertexHighEffBJetTags'
   ,'pfNegativeSimpleSecondaryVertexHighPurBJetTags'
   ,'pfCombinedSecondaryVertexV2BJetTags'
   ,'pfPositiveCombinedSecondaryVertexV2BJetTags'
   ,'pfNegativeCombinedSecondaryVertexV2BJetTags'
   ,'pfCombinedInclusiveSecondaryVertexV2BJetTags'
   ,'pfPositiveCombinedInclusiveSecondaryVertexV2BJetTags'
   ,'pfNegativeCombinedInclusiveSecondaryVertexV2BJetTags'
   ,'softPFMuonBJetTags'
   ,'positiveSoftPFMuonBJetTags'
   ,'negativeSoftPFMuonBJetTags'
   ,'softPFElectronBJetTags'
   ,'positiveSoftPFElectronBJetTags'
   ,'negativeSoftPFElectronBJetTags'
   ,'pfCombinedMVAV2BJetTags'
   ,'pfNegativeCombinedMVAV2BJetTags'
   ,'pfPositiveCombinedMVAV2BJetTags'
   ,'pfCombinedCvsBJetTags'
   ,'pfNegativeCombinedCvsBJetTags'
   ,'pfPositiveCombinedCvsBJetTags'
   ,'pfCombinedCvsLJetTags'
   ,'pfNegativeCombinedCvsLJetTags'
   ,'pfPositiveCombinedCvsLJetTags'
    # DeepCSV
  , 'pfDeepCSVJetTags:probudsg'
  , 'pfDeepCSVJetTags:probb'
  , 'pfDeepCSVJetTags:probc'
  , 'pfDeepCSVJetTags:probbb'
  , 'pfNegativeDeepCSVJetTags:probudsg'
  , 'pfNegativeDeepCSVJetTags:probb'
  , 'pfNegativeDeepCSVJetTags:probc'
  , 'pfNegativeDeepCSVJetTags:probbb'
  , 'pfPositiveDeepCSVJetTags:probudsg'
  , 'pfPositiveDeepCSVJetTags:probb'
  , 'pfPositiveDeepCSVJetTags:probc'
  , 'pfPositiveDeepCSVJetTags:probbb'
    # DeepFlavour
  # , 'pfDeepFlavourJetTags:probb'
  # , 'pfDeepFlavourJetTags:probbb'
  # , 'pfDeepFlavourJetTags:problepb'
  # , 'pfDeepFlavourJetTags:probc'
  # , 'pfDeepFlavourJetTags:probuds'
  # , 'pfDeepFlavourJetTags:probg'
  # , 'pfNegativeDeepFlavourJetTags:probb'
  # , 'pfNegativeDeepFlavourJetTags:probbb'
  # , 'pfNegativeDeepFlavourJetTags:problepb'
  # , 'pfNegativeDeepFlavourJetTags:probc'
  # , 'pfNegativeDeepFlavourJetTags:probuds'
  # , 'pfNegativeDeepFlavourJetTags:probg'
    # DeepFlavour with pruned input
  # , 'pfDeepFlavourPrunedJetTags:probb'
  # , 'pfDeepFlavourPrunedJetTags:probbb'
  # , 'pfDeepFlavourPrunedJetTags:problepb'
  # , 'pfDeepFlavourPrunedJetTags:probc'
  # , 'pfDeepFlavourPrunedJetTags:probuds'
  # , 'pfDeepFlavourPrunedJetTags:probg'
  # , 'pfNegativeDeepFlavourPrunedJetTags:probb'
  # , 'pfNegativeDeepFlavourPrunedJetTags:probbb'
  # , 'pfNegativeDeepFlavourPrunedJetTags:problepb'
  # , 'pfNegativeDeepFlavourPrunedJetTags:probc'
  # , 'pfNegativeDeepFlavourPrunedJetTags:probuds'
  # , 'pfNegativeDeepFlavourPrunedJetTags:probg'

])

## Legacy taggers not supported with MiniAOD
# if miniAod and useLegacyTaggers:
#     print "WARNING: Legacy taggers not supported with MiniAOD"
#     useLegacyTaggers = False

## If using legacy taggers
# if useLegacyTaggers:
#     bTagInfos = bTagInfosLegacy
#     bTagDiscriminators = bTagDiscriminatorsLegacy

## If not including negative deep flavour jet taggers
if not useNegativeDeepFlavourTags:
  bTagDiscriminators = {i for i in bTagDiscriminators if 'NegativeDeepFlavour' not in i}

## Clustering algorithm label
algoLabel = 'CA'
if jetAlgo == 'AntiKt':
    algoLabel = 'AK'

## Figure out if jet clustering is needed
if not runFatJetClustering:
    runFatJetClustering = runJetClustering
# if not miniAod and usePuppi and not runJetClustering:
#     print "WARNING: You requested Puppi jets which are not stored in AOD. Enabling jet clustering."
#     runJetClustering = True

if miniAod and not (usePFchs or usePuppi) and not runJetClustering:
    print "WARNING: You requested non-PU-subtracted jets which are not stored in MiniAOD. Enabling jet clustering."
    runJetClustering = True

print "Jet clustering: %s"%('True' if runJetClustering else 'False')

## Figure out if fat jet clustering is needed
# if runFatJets and (jetAlgo != 'AntiKt' or fatJetRadius != 0.8) and not runFatJetClustering:
#     print "WARNING: You requested fat jets with an algorithm or size not stored in any of the data-tiers. Enabling fat jet clustering."
#     runFatJetClustering = True

# if runFatJets and not (usePFchs or usePuppi or usePuppiForFatJets) and not runFatJetClustering:
#     print "WARNING: You requested non-PU-subtracted fat jets which are not stored in any of the data-tiers. Enabling fat jet clustering."
#     runFatJetClustering = True

# if miniAod and runFatJets and usePFchs and not usePuppiForFatJets and not runFatJetClustering:
#     print "WARNING: You requested CHS fat jets which are not stored in MiniAOD. Enabling fat jet clustering."
#     runFatJetClustering = True

# if not miniAod and runFatJets and (usePuppi or usePuppiForFatJets) and not runFatJetClustering:
#     print "WARNING: You requested Puppi fat jets which are not stored in AOD. Enabling fat jet clustering."
#     runFatJetClustering = True

# if miniAod and runSubJets and usePruned and not runFatJetClustering:
#     print "WARNING: You requested pruned subjets which are not stored in MiniAOD. Enabling fat jet clustering."
#     runFatJetClustering = True

# if not miniAod and runSubJets and usePruned and not runFatJetClustering:
#     print "WARNING: You requested pruned subjets which are not stored in AOD. Will run pruned fat jet clustering."

# print "Fat jet clustering: %s"%('True' if runFatJetClustering else 'False')

## For fat jets we want to re-run all taggers in order to use the setup adapted to the larger fat jet cone size
# bTagInfosFat = copy.deepcopy(bTagInfos_noDeepFlavour)
# bTagInfosFat += ([] if useLegacyTaggers else ['pfImpactParameter' + ('CA15' if algoLabel=='CA' else 'AK8') + 'TagInfos'])
# bTagInfosFat += ([] if useLegacyTaggers else ['pfInclusiveSecondaryVertexFinder' + ('CA15' if algoLabel=='CA' else 'AK8') + 'TagInfos'])
# bTagInfosFat += ([] if useLegacyTaggers else ['pfBoostedDoubleSV' + ('CA15' if algoLabel=='CA' else 'AK8') + 'TagInfos'])
# ## Add DeepDoubleX tag infos
# bTagInfosFat += ([] if useLegacyTaggers else ['pfDeepDoubleXTagInfos'])

bTagDiscriminators_no_deepFlavour = {i for i in bTagDiscriminators if 'DeepFlavour' not in i}

# bTagDiscriminatorsFat = copy.deepcopy(bTagDiscriminators_no_deepFlavour)
## Add DeepDoubleX tag infos
# bTagInfosFat += ([] if useLegacyTaggers else ['pfDeepDoubleXTagInfos'])

## Add DeepDoubleX tagger to fat jets
# bTagDiscriminatorsFat.update(set([
#     'pfDeepDoubleBvLJetTags:probQCD',
#     'pfDeepDoubleBvLJetTags:probHbb',
#     'pfDeepDoubleCvLJetTags:probQCD',
#     'pfDeepDoubleCvLJetTags:probHcc',
#     'pfDeepDoubleCvBJetTags:probHbb',
#     'pfDeepDoubleCvBJetTags:probHcc',
#     'pfMassIndependentDeepDoubleBvLJetTags:probQCD',
#     'pfMassIndependentDeepDoubleBvLJetTags:probHbb',
#     'pfMassIndependentDeepDoubleCvLJetTags:probQCD',
#     'pfMassIndependentDeepDoubleCvLJetTags:probHcc',
#     'pfMassIndependentDeepDoubleCvBJetTags:probHbb',
#     'pfMassIndependentDeepDoubleCvBJetTags:probHcc',
# ]))
## Add DeepBoostedJet discriminators
# from RecoBTag.MXNet.pfDeepBoostedJet_cff import _pfMassDecorrelatedDeepBoostedJetTagsProbs, _pfMassDecorrelatedDeepBoostedJetTagsMetaDiscrs
# bTagDiscriminatorsFat.update(set([]) if (useLegacyTaggers or not miniAod) else set([
#     "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:bbvsLight",
#     "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ccvsLight",
#     "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:TvsQCD",
#     "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ZHccvsQCD",
#     "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:WvsQCD",
#     "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ZHbbvsQCD"
# ]))
## Add DeepBoostedJet tag infos
# bTagInfosFat += ([] if (useLegacyTaggers or not miniAod) else ['pfDeepBoostedJetTagInfos'])

# if runJetClustering:
#     remakeAllDiscr = True
# if runFatJetClustering:
#     remakeDoubleB = True
# if remakeDoubleB:
#     bTagDiscriminatorsFat.update(set([]) if useLegacyTaggers else set(['pfBoostedDoubleSecondaryVertex' + ('CA15' if algoLabel=='CA' else 'AK8') + 'BJetTags']))

## Full list of bTagDiscriminators for SoftDrop subjets
bTagDiscriminatorsSubJets  = copy.deepcopy(bTagDiscriminators_no_deepFlavour)
bTagDiscriminatorsSoftDrop = copy.deepcopy(bTagDiscriminators_no_deepFlavour)

## If using MiniAOD and not reclustering jets, only run taggers not already stored (with the exception of JP taggers and DeepCSV)
if miniAod and not runJetClustering and not remakeAllDiscr:
    from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import _patJets as patJetsDefault
    storedDiscriminators = set([x.value() for x in patJetsDefault.discriminatorSources])
    print "INFO: Removing b-tag discriminators already stored in MiniAOD (with the exception of JP taggers)"
    jptaggers = {i for i in bTagDiscriminators if 'ProbabilityBJetTags' in i or i.startswith('pfDeepCSV')}
    bTagDiscriminators = (bTagDiscriminators - storedDiscriminators) | jptaggers
if miniAod and not runFatJetClustering and not remakeAllDiscr:
    ## SoftDrop subjets in MiniAOD have only CSVv2AVR and CSVv2IVF discriminators stored
    bTagDiscriminatorsSoftDrop -= {'pfCombinedSecondaryVertexV2BJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'}

## Postfix
postfix = "PFlow"
## Various collection names
# genParticles = 'genParticles'
# jetSource = 'pfJetsPFBRECO'+postfix
# patJetSource = 'selectedPatJets'+postfix
# genJetCollection = 'ak4GenJetsNoNu'
# pfCandidates = 'particleFlow'
# pvSource = 'offlinePrimaryVertices'
# pvSource = 'offlineSlimmedPrimaryVertices'
# svSource = 'inclusiveCandidateSecondaryVertices'
# muSource = 'muons'
# elSource = 'gedGsfElectrons'
# patMuons = 'selectedPatMuons'
# patElecs = 'selectedPatElectrons'
# trackSource = 'generalTracks'
# fatJetSource = 'fatPFJetsCHS'
fatJetSourceSoftDrop = 'fatPFJetsSoftDrop'
fatJetSourcePruned = 'fatPFJetsPruned'
fatGenJetCollection = 'genFatJetsNoNu'
fatGenJetCollectionSoftDrop = 'genFatJetsNoNuSoftDrop'
fatGenJetCollectionPruned = 'genFatJetsNoNuPruned'
# patFatJetSource = 'packedPatJetsFatPF'
# subJetSourceSoftDrop = 'fatPFJetsSoftDrop:SubJets'
# patSubJetSourceSoftDrop = 'selectedPatJetsSoftDropFatPFPacked:SubJets'
if not runJetClustering:
    jetSource = ('ak4PFJetsCHS' if usePFchs else 'ak4PFJets')
if not runFatJetClustering:
    fatJetSource = 'ak8PFJetsCHS'
    fatJetSourceSoftDrop = 'ak8PFJetsCHSSoftDrop'
    fatGenJetCollection = 'ak8GenJetsNoNu'
## If running on MiniAOD
if miniAod:
    genParticles = 'prunedGenParticles'
    jetSource = 'ak4Jets'
    genJetCollection = 'slimmedGenJets'
    pfCandidates = 'packedPFCandidates'
    pvSource = 'offlineSlimmedPrimaryVertices'
    svSource = 'slimmedSecondaryVertices'
    trackSource = 'unpackedTracksAndVertices'
    # trackSource = 'generalTracks'
    muSource = 'slimmedMuons'
    elSource = 'slimmedElectrons'
    patMuons = 'slimmedMuons'
    patElecs = 'slimmedElectrons'
    if not runJetClustering:
        jetSource = ('slimmedJetsPuppi' if usePuppi else 'slimmedJets')
        # patJetSource = 'selectedUpdatedPatJets'+postfix
        patJetSource = 'slimmedJets'
    if not runFatJetClustering:
        fatJetSource = 'slimmedJetsAK8'
        # patFatJetSource = 'selectedUpdatedPatJetsFatPF'+postfix
        patFatJetSource = 'slimmedJetsAK8'
        # subJetSourceSoftDrop = 'slimmedJetsAK8PFPuppiSoftDropPacked:SubJets'
        # patSubJetSourceSoftDrop = 'selectedUpdatedPatJetsSoftDropSubjetsPF'+postfix
        subJetSourceSoftDrop = 'slimmedJetsAK8PFPuppiSoftDropPacked:SubJets'
        patSubJetSourceSoftDrop = 'slimmedJetsAK8PFPuppiSoftDropPacked:SubJets'



# if not eras:
# process = cms.Process("BTagAna")
# else:
# 	from Configuration.StandardSequences.Eras import eras
# 	eras_to_use = []
# 	for era in eras:
# 		if hasattr(eras, era):
# 			eras_to_use.append(getattr(eras, era))
# 		else:
# 			raise ValueError('The requested era (%s) is not available' % era)
# 	process = cms.Process("BTagAna", *eras_to_use)


## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
# If you run over many samples and you save the log, remember to reduce
# the size of the output by prescaling the report of the event number
# process.MessageLogger.cerr.FwkReport.reportEvery = options.reportEvery
process.MessageLogger.cerr.FwkReport.reportEvery = 10
process.MessageLogger.cerr.default.limit = 10


# from RecoBTag.PerformanceMeasurements.Simone_TrackingV2_PF import cms, process
# process.load("RecoBTag.PerformanceMeasurements.BTagHLT_stripped_trackV2PF_cff")


# from Configuration.Eras.Era_Phase2C8_timing_layer_bar_cff import Phase2C8_timing_layer_bar
# process = cms.Process('RECO2', Phase2C8_timing_layer_bar)

# from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000
# process = customise_aging_1000(process)

# import of standard configurations
# process.load('Configuration.StandardSequences.Services_cff')
# process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
# process.load('FWCore.MessageService.MessageLogger_cfi')
# process.load('Configuration.EventContent.EventContent_cff')
# process.load('SimGeneral.MixingModule.mixNoPU_cfi')
# process.load('Configuration.Geometry.GeometryExtended2026D41Reco_cff')
# process.load('Configuration.StandardSequences.MagneticField_cff')
# process.load('Configuration.StandardSequences.RawToDigi_cff')
# process.load('Configuration.StandardSequences.L1Reco_cff')
# process.load('Configuration.StandardSequences.Reconstruction_cff')
# process.load('Configuration.StandardSequences.RecoSim_cff')
# process.load('Configuration.StandardSequences.EndOfProcess_cff')
# process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
# from Configuration.AlCa.GlobalTag import GlobalTag
# process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

## Input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    # "root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19MiniAOD/TTbar_14TeV_TuneCP5_Pythia8/MINIAODSIM/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/F0225E24-F876-D448-8318-2D89795D632F.root",
    "root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19MiniAOD/TTbar_14TeV_TuneCP5_Pythia8/MINIAODSIM/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/53CA5A7D-9114-2D4C-8E51-C04EE9B68C08.root"
    )
)

# if miniAod:
#     process.source.fileNames = [
#         #/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM
#         '/store/mc/RunIIFall17MiniAOD/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v1/00000/C8E934F8-1C06-E811-888D-0242AC130002.root'
#     ]
#     if runOnData:
#         process.source.fileNames = [
#             #/JetHT/Run2017A-PromptReco-v2/MINIAOD
#             '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/168/00000/3E20EA58-0F4D-E711-851C-02163E0139CE.root',
#         ]
#     if fastSim:
#         process.source.fileNames = [
#             '/store/relval/CMSSW_8_0_0/RelValTTbar_13/MINIAODSIM/PU25ns_80X_mcRun2_asymptotic_v4_FastSim-v2/10000/8E75D08A-3FDE-E511-8374-0CC47A4C8F26.root'
#         ]
# else:
#     process.source.fileNames = [
#         '/store/mc/PhaseIFall16DR/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/AODSIM/PhaseIFall16PUFlat20to50_81X_upgrade2017_realistic_v26-v1/50000/0039E945-35E3-E611-AF8D-001E675A6C2A.root'
#     ]
#     if runOnData:
#         process.source.fileNames = [
#             '/store/data/Run2016B/SingleMuon/AOD/PromptReco-v2/000/275/125/00000/DA2EC189-7E36-E611-8C63-02163E01343B.root'
#         ]
#     if fastSim:
#         process.source.fileNames = [
#             '/store/relval/CMSSW_8_0_0/RelValTTbar_13/GEN-SIM-DIGI-RECO/PU25ns_80X_mcRun2_asymptotic_v4_FastSim-v2/10000/0400D094-63DD-E511-8B51-0CC47A4C8ED8.root'
#         ]
# # if options.inputFiles:
# #     process.source.fileNames = options.inputFiles
#
# process.source.fileNames = cms.untracked.vstring(
#     "root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19MiniAOD/TTbar_14TeV_TuneCP5_Pythia8/MINIAODSIM/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/F0225E24-F876-D448-8318-2D89795D632F.root"
# )

## Define the output file name
# if runOnData :
#     options.outFilename += '_data'
# else :
#     options.outFilename += '_mc'
#
# if runFatJets :
#     options.outFilename += '_FatJets'
#
# if runSubJets :
#     options.outFilename += '_Subjets'
#
# if fastSim :
#     options.outFilename += '_FastSim'
#
# if doBoostedCommissioning:
#   options.outFilename += '_BoostedCommissioning'
#
# options.outFilename += '.root'

## Output file
process.TFileService = cms.Service("TFileService",
   fileName = cms.string(outFilename)
)

## Events to process
process.source.skipEvents = cms.untracked.uint32(skipEvents)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

## Options and Output Report
process.options   = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False),
    allowUnscheduled = cms.untracked.bool(True)
)

#Set GT by hand:
# process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# from Configuration.AlCa.GlobalTag import GlobalTag
# process.GlobalTag.globaltag = globalTag
#Choose automatically:
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_' + ('data' if runOnData else 'mc'))

#Loading calibrations from db file, example of code for any future use
#process.load("CondCore.DBCommon.CondDBSetup_cfi")
#process.BTauMVAJetTagComputerRecord = cms.ESSource("PoolDBESSource",
#    process.CondDBSetup,
#    timetype = cms.string('runnumber'),
#    toGet = cms.VPSet(
#        cms.PSet(
#            record = cms.string('BTauGenericMVAJetTagComputerRcd'),
#            tag = cms.string('MVAJetTags')
#        )
#    ),
#    connect = cms.string('sqlite_fip:RecoBTag/PerformanceMeasurements/data/MVAJetTags.db'),
#    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService')
#)
#process.es_prefer_BTauMVAJetTagComputerRecord = cms.ESPrefer("PoolDBESSource","BTauMVAJetTagComputerRecord")

# if usePrivateJEC:
#
#     from CondCore.DBCommon.CondDBSetup_cfi import *
#     import os
#     dbfile=''
#     if runOnData: dbfile=jecDBFileData
#     else: dbfile=jecDBFileMC
#     print "\nUsing private SQLite file", dbfile, "\n"
#     process.jec = cms.ESSource("PoolDBESSource",CondDBSetup,
# 		    connect = cms.string( "sqlite_fip:RecoBTag/PerformanceMeasurements/data/"+dbfile+'.db'),
# 		    toGet =  cms.VPSet(
# 			    cms.PSet(
# 				    record = cms.string("JetCorrectionsRecord"),
# 				    tag = cms.string("JetCorrectorParametersCollection_"+dbfile+"_AK4PF"),
# 				    label= cms.untracked.string("AK4PF")
# 				    ),
# 			    cms.PSet(
# 				    record = cms.string("JetCorrectionsRecord"),
# 				    tag = cms.string("JetCorrectorParametersCollection_"+dbfile+"_AK4PFchs"),
# 				    label= cms.untracked.string("AK4PFchs")
# 				    ),
# 			    cms.PSet(
# 				    record = cms.string("JetCorrectionsRecord"),
# 				    tag = cms.string("JetCorrectorParametersCollection_"+dbfile+"_AK4PFPuppi"),
# 				    label= cms.untracked.string("AK4PFPuppi")
# 				    ),
# 			    cms.PSet(
# 				    record = cms.string("JetCorrectionsRecord"),
# 				    tag = cms.string("JetCorrectorParametersCollection_"+dbfile+"_AK8PF"),
# 				    label= cms.untracked.string("AK8PF")
# 				    ),
# 			    cms.PSet(
# 				    record = cms.string("JetCorrectionsRecord"),
# 				    tag = cms.string("JetCorrectorParametersCollection_"+dbfile+"_AK8PFchs"),
# 				    label= cms.untracked.string("AK8PFchs")
# 				    ),
# 			    cms.PSet(
# 				    record = cms.string("JetCorrectionsRecord"),
# 				    tag = cms.string("JetCorrectorParametersCollection_"+dbfile+"_AK8PFPuppi"),
# 				    label= cms.untracked.string("AK8PFPuppi")
# 				    ),
# 			    )
# 		    )
#
#     process.es_prefer_jec = cms.ESPrefer("PoolDBESSource",'jec')

### to activate the new JP calibration: using the data base
trkProbaCalibTag = JPCalibration
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string("BTagTrackProbability3DRcd"),
      tag = cms.string(trkProbaCalibTag),
      connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
    )
)

# process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
# process.load("Configuration.Geometry.GeometryRecoDB_cff")
# process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

#-------------------------------------
## Output Module Configuration (expects a path 'p')
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent
process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string(outFilename),
    # save only events passing the full path
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    # save PAT Layer 1 output; you need a '*' to
    # unpack the list of commands 'patEventContent'
    outputCommands = cms.untracked.vstring('drop *', *patEventContent)
)

#-------------------------------------
# if not miniAod:
#     ## PAT Configuration
#     jetAlgo="AK4"
#
#     from PhysicsTools.PatAlgos.tools.pfTools import *
#     usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo, runOnMC=not runOnData, postfix=postfix,
#               jetCorrections=jetCorrectionsAK4, pvCollection=cms.InputTag(pvSource))
#
#     ## Top projections in PF2PAT
#     getattr(process,"pfPileUpJME"+postfix).checkClosestZVertex = False
#     getattr(process,"pfNoPileUpJME"+postfix).enable = usePFchs
#     getattr(process,"pfNoMuonJMEPFBRECO"+postfix).enable = False
#     getattr(process,"pfNoElectronJMEPFBRECO"+postfix).enable = False
#
#     if usePuppi or usePuppiForFatJets:
#         process.load('CommonTools.PileupAlgos.Puppi_cff')
#         if usePuppi:
#             from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
#             _pfJets = ak4PFJets.clone(src = cms.InputTag('puppi'), doAreaFastjet = True, srcPVs = cms.InputTag(pvSource))
#             setattr(process,'pfJetsPFBRECO'+postfix,_pfJets)
#         if usePuppiForBTagging: pfCandidates = 'puppi'
# else:
## GenJetsNoNu selection
process.packedGenParticlesForJetsNoNu = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedGenParticles"), cut = cms.string("abs(pdgId) != 12 && abs(pdgId) != 14 && abs(pdgId) != 16"))

## PFchs selection
process.pfCHS = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedPFCandidates"), cut = cms.string("fromPV"))

## Reco jets
from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
if usePFchs:
    process.ak4Jets = ak4PFJets.clone(src = cms.InputTag('pfCHS'), doAreaFastjet = True, srcPVs = cms.InputTag(pvSource))
elif usePuppi:
    process.ak4Jets = ak4PFJets.clone(src = cms.InputTag('puppi'), doAreaFastjet = True, srcPVs = cms.InputTag(pvSource))
else:
    process.ak4Jets = ak4PFJets.clone(src = cms.InputTag('packedPFCandidates'), doAreaFastjet = True, srcPVs = cms.InputTag(pvSource))

if usePuppi or usePuppiForFatJets:
    process.load('CommonTools.PileupAlgos.Puppi_cff')
    process.puppi.candName           = cms.InputTag(pfCandidates)
    process.puppi.vertexName         = cms.InputTag(pvSource)
    process.puppi.useExistingWeights = cms.bool(True)
    process.puppi.clonePackedCands   = cms.bool(True)
    if usePuppiForBTagging: pfCandidates = 'puppi'

## Load standard PAT objects (here we only need PAT muons but the framework will figure out what it needs to run using the unscheduled mode)
# process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")

from PhysicsTools.PatAlgos.tools.jetTools import *
## Updated the default jet collection
# if miniAod and not runJetClustering:
#     updateJetCollection(
#         process,
#         jetSource = cms.InputTag(jetSource),
#         jetCorrections = jetCorrectionsAK4,
#         pfCandidates = cms.InputTag(pfCandidates),
#         pvSource = cms.InputTag(pvSource),
#         svSource = cms.InputTag(svSource),
#         muSource = cms.InputTag(muSource),
#         elSource = cms.InputTag(elSource),
#         btagInfos = bTagInfos,
#         btagDiscriminators = list(bTagDiscriminators),
#         explicitJTA = useExplicitJTA,
#         postfix = postfix
#     )
## Switch the default jet collection (done in order to use the above-specified b-tag infos and discriminators)
# else:
#     #switch off deep flavour on AOD for the moment
#     switchJetCollection(
#         process,
#         jetSource = cms.InputTag(jetSource),
#         pfCandidates = cms.InputTag(pfCandidates),
#         pvSource = cms.InputTag(pvSource),
#         svSource = cms.InputTag(svSource),
#         muSource = cms.InputTag(muSource),
#         elSource = cms.InputTag(elSource),
#         btagInfos = list(bTagInfos_noDeepFlavour), #list(bTagInfos),
#         btagDiscriminators = list(bTagDiscriminators_no_deepFlavour), #bTagDiscriminators),
#         jetCorrections = jetCorrectionsAK4,
#         genJetCollection = cms.InputTag(genJetCollection),
#         genParticles = cms.InputTag(genParticles),
#         explicitJTA = useExplicitJTA,
#         postfix = postfix
#     )

#-------------------------------------

#-------------------------------------
# if runFatJets:
#     if miniAod and not runFatJetClustering:
#         updateJetCollection(
#             process,
#             labelName='FatPF',
#             jetSource=cms.InputTag(fatJetSource),
#             jetCorrections = jetCorrectionsAK8,
#             pfCandidates = cms.InputTag(pfCandidates),
#             pvSource = cms.InputTag(pvSource),
#             svSource = cms.InputTag(svSource),
#             muSource = cms.InputTag(muSource),
#             elSource = cms.InputTag(elSource),
#             btagInfos = bTagInfosFat,
#             btagDiscriminators = list(bTagDiscriminatorsFat),
#             explicitJTA = useExplicitJTA,
#             runIVF = runIVF,
#             postfix = postfix
#         )
#         getattr(process,'selectedUpdatedPatJetsFatPF'+postfix).cut = cms.string("pt > %f && abs(eta) < %f"%(float(fatJetPtMin), float(fatJetAbsEtaMax)))
#         updateJetCollection(
#             process,
#             labelName='SoftDropSubjetsPF',
#             jetSource=cms.InputTag(subJetSourceSoftDrop),
#             jetCorrections = jetCorrectionsSubJets,
#             pfCandidates = cms.InputTag(pfCandidates),
#             pvSource = cms.InputTag(pvSource),
#             svSource = cms.InputTag(svSource),
#             muSource = cms.InputTag(muSource),
#             elSource = cms.InputTag(elSource),
#             btagInfos = bTagInfos_noDeepFlavour,
#             btagDiscriminators = list(bTagDiscriminatorsSoftDrop),
#             explicitJTA = True,          # needed for subjet b tagging
#             svClustering = False,        # needed for subjet b tagging (IMPORTANT: Needs to be set to False to disable ghost-association which does not work with slimmed jets)
#             fatJets = cms.InputTag(fatJetSource), # needed for subjet b tagging
#             rParam=fatJetRadius, # needed for subjet b tagging
#             algo=algoLabel,              # has to be defined but is not used since svClustering=False
#             runIVF = runIVF,
#             postfix = postfix
#         )
#     else:
#         _src = getattr(process,'ak4Jets').src if miniAod else getattr(process,'pfJetsPFBRECO'+postfix).src
#         if usePuppiForFatJets and not usePuppi:
#             _src = cms.InputTag('puppi')
#         _srcPVs = getattr(process,'ak4Jets').srcPVs if miniAod else getattr(process,'pfJetsPFBRECO'+postfix).srcPVs
#         ## Fat jets (Gen and Reco)
#         from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets
#         process.genFatJetsNoNu = ak4GenJets.clone(
#             jetAlgorithm = cms.string(jetAlgo),
#             rParam = cms.double(fatJetRadius),
#             src = (cms.InputTag("packedGenParticlesForJetsNoNu") if miniAod else cms.InputTag("genParticlesForJetsNoNu"+postfix))
#         )
#         from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
#         process.fatPFJetsCHS = ak4PFJets.clone(
#             jetAlgorithm = cms.string(jetAlgo),
#             rParam = cms.double(fatJetRadius),
#             src = _src,
#             srcPVs = _srcPVs,
#             doAreaFastjet = cms.bool(True),
#             jetPtMin = cms.double(fatJetRawPtMin)
#         )
#         ## Pruned fat jets (Gen and Reco) (each module produces two jet collections, fat jets and subjets)
#         from RecoJets.JetProducers.SubJetParameters_cfi import SubJetParameters
#         process.genFatJetsNoNuPruned = ak4GenJets.clone(
#             SubJetParameters,
#             jetAlgorithm = cms.string(jetAlgo),
#             rParam = cms.double(fatJetRadius),
#             src = (cms.InputTag("packedGenParticlesForJetsNoNu") if miniAod else cms.InputTag("genParticlesForJetsNoNu"+postfix)),
#             usePruning = cms.bool(True),
#             writeCompound = cms.bool(True),
#             jetCollInstanceName=cms.string("SubJets")
#         )
#
#         from RecoJets.JetProducers.ak8PFJets_cfi import ak8PFJetsCHSPruned
#         process.fatPFJetsPruned = ak8PFJetsCHSPruned.clone(
#             jetAlgorithm = cms.string(jetAlgo),
#             rParam = cms.double(fatJetRadius),
#             src = _src,
#             srcPVs = _srcPVs,
#             doAreaFastjet = cms.bool(True),
#             writeCompound = cms.bool(True),
#             jetCollInstanceName=cms.string("SubJets"),
#             jetPtMin = cms.double(fatJetRawPtMin)
#         )
#         ## SoftDrop fat jets (Gen and Reco) (each module produces two jet collections, fat jets and subjets)
#         process.genFatJetsNoNuSoftDrop = ak4GenJets.clone(
#             jetAlgorithm = cms.string(jetAlgo),
#             rParam = cms.double(fatJetRadius),
#             src = (cms.InputTag("packedGenParticlesForJetsNoNu") if miniAod else cms.InputTag("genParticlesForJetsNoNu"+postfix)),
#             useSoftDrop = cms.bool(True),
#             zcut = cms.double(0.1),
#             beta = cms.double(0.0),
#             R0 = cms.double(fatJetRadius),
#             writeCompound = cms.bool(True),
#             jetCollInstanceName=cms.string("SubJets")
#         )
#         from RecoJets.JetProducers.ak8PFJets_cfi import ak8PFJetsCHSSoftDrop
#         process.fatPFJetsSoftDrop = ak8PFJetsCHSSoftDrop.clone(
#             jetAlgorithm = cms.string(jetAlgo),
#             rParam = cms.double(fatJetRadius),
#             R0 = cms.double(fatJetRadius),
#             src = _src,
#             srcPVs = _srcPVs,
#             doAreaFastjet = cms.bool(True),
#             writeCompound = cms.bool(True),
#             jetCollInstanceName=cms.string("SubJets"),
#             jetPtMin = cms.double(fatJetRawPtMin)
#         )
#
#         ## PATify the above jets
#         addJetCollection(
#             process,
#             labelName='FatPF',
#             jetSource=cms.InputTag(fatJetSource),
#             algo=algoLabel,              # needed for jet flavor clustering
#             rParam=fatJetRadius, # needed for jet flavor clustering
#             pfCandidates = cms.InputTag(pfCandidates),
#             pvSource = cms.InputTag(pvSource),
#             svSource = cms.InputTag(svSource),
#             muSource = cms.InputTag(muSource),
#             elSource = cms.InputTag(elSource),
#             btagInfos = bTagInfosFat,
#             btagDiscriminators = list(bTagDiscriminatorsFat),
#             jetCorrections = jetCorrectionsAK8,
#             genJetCollection = cms.InputTag(fatGenJetCollection),
#             genParticles = cms.InputTag(genParticles),
#             explicitJTA = useExplicitJTA,
#             runIVF = runIVF,
#             postfix = postfix
#         )
#         getattr(process,'selectedPatJetsFatPF'+postfix).cut = cms.string("pt > %f && abs(eta) < %f"%(float(fatJetPtMin), float(fatJetAbsEtaMax)))
#         addJetCollection(
#             process,
#             labelName='SoftDropFatPF',
#             jetSource=cms.InputTag(fatJetSourceSoftDrop),
#             algo=algoLabel,
#             pfCandidates = cms.InputTag(pfCandidates),
#             pvSource = cms.InputTag(pvSource),
#             svSource = cms.InputTag(svSource),
#             muSource = cms.InputTag(muSource),
#             elSource = cms.InputTag(elSource),
#             btagInfos=['None'],
#             btagDiscriminators=['None'],
#             jetCorrections=jetCorrectionsAK8,
#             genJetCollection = cms.InputTag(fatGenJetCollection),
#             genParticles = cms.InputTag(genParticles),
#             getJetMCFlavour = False, # jet flavor disabled
#             postfix = postfix
#         )
#         addJetCollection(
#             process,
#             labelName='SoftDropSubjetsPF',
#             jetSource=cms.InputTag(fatJetSourceSoftDrop,'SubJets'),
#             algo=algoLabel,              # needed for subjet flavor clustering
#             rParam=fatJetRadius, # needed for subjet flavor clustering
#             pfCandidates = cms.InputTag(pfCandidates),
#             pvSource = cms.InputTag(pvSource),
#             svSource = cms.InputTag(svSource),
#             muSource = cms.InputTag(muSource),
#             elSource = cms.InputTag(elSource),
#             btagInfos = bTagInfos_noDeepFlavour,
#             btagDiscriminators = list(bTagDiscriminatorsSubJets),
#             jetCorrections = jetCorrectionsSubJets,
#             genJetCollection = cms.InputTag(fatGenJetCollectionSoftDrop,'SubJets'),
#             genParticles = cms.InputTag(genParticles),
#             explicitJTA = True,  # needed for subjet b tagging
#             svClustering = True, # needed for subjet b tagging
#             fatJets = cms.InputTag(fatJetSource),                # needed for subjet flavor clustering
#             groomedFatJets = cms.InputTag(fatJetSourceSoftDrop), # needed for subjet flavor clustering
#             runIVF = runIVF,
#             postfix = postfix
#         )
#
#         ## Establish references between PATified fat jets and subjets using the BoostedJetMerger
#         process.selectedPatJetsSoftDropFatPFPacked = cms.EDProducer("BoostedJetMerger",
#             jetSrc=cms.InputTag("selectedPatJetsSoftDropFatPF"+postfix),
#             subjetSrc=cms.InputTag("selectedPatJetsSoftDropSubjetsPF"+postfix)
#         )
#
#         addJetCollection(
#             process,
#             labelName='PrunedFatPF',
#             jetSource=cms.InputTag(fatJetSourcePruned),
#             algo=algoLabel,
#             pfCandidates = cms.InputTag(pfCandidates),
#             pvSource = cms.InputTag(pvSource),
#             svSource = cms.InputTag(svSource),
#             muSource = cms.InputTag(muSource),
#             elSource = cms.InputTag(elSource),
#             btagInfos=['None'],
#             btagDiscriminators=['None'],
#             jetCorrections=jetCorrectionsAK8,
#             genJetCollection = cms.InputTag(fatGenJetCollection),
#             genParticles = cms.InputTag(genParticles),
#             getJetMCFlavour = False, # jet flavor disabled
#             postfix = postfix
#         )
#         addJetCollection(
#             process,
#             labelName='PrunedSubjetsPF',
#             jetSource=cms.InputTag(fatJetSourcePruned,'SubJets'),
#             algo=algoLabel,              # needed for subjet flavor clustering
#             rParam=fatJetRadius, # needed for subjet flavor clustering
#             pfCandidates = cms.InputTag(pfCandidates),
#             pvSource = cms.InputTag(pvSource),
#             svSource = cms.InputTag(svSource),
#             muSource = cms.InputTag(muSource),
#             elSource = cms.InputTag(elSource),
#             btagInfos = bTagInfos_noDeepFlavour,
#             btagDiscriminators = list(bTagDiscriminatorsSubJets),
#             jetCorrections = jetCorrectionsSubJets,
#             genJetCollection = cms.InputTag(fatGenJetCollectionPruned,'SubJets'),
#             genParticles = cms.InputTag(genParticles),
#             explicitJTA = True,  # needed for subjet b tagging
#             svClustering = True, # needed for subjet b tagging
#             fatJets = cms.InputTag(fatJetSource),              # needed for subjet flavor clustering
#             groomedFatJets = cms.InputTag(fatJetSourcePruned), # needed for subjet flavor clustering
#             runIVF = runIVF,
#             postfix = postfix
#         )
#
#         ## Establish references between PATified fat jets and subjets using the BoostedJetMerger
#         process.selectedPatJetsPrunedFatPFPacked = cms.EDProducer("BoostedJetMerger",
#             jetSrc=cms.InputTag("selectedPatJetsPrunedFatPF"+postfix),
#             subjetSrc=cms.InputTag("selectedPatJetsPrunedSubjetsPF"+postfix)
#         )
#
#         ## Pack fat jets with subjets
#         process.packedPatJetsFatPF = cms.EDProducer("JetSubstructurePacker",
#                 jetSrc = cms.InputTag('selectedPatJetsFatPF'+postfix),
#                 distMax = cms.double(fatJetRadius),
#                 algoTags = cms.VInputTag(),
#                 algoLabels = cms.vstring(),
#                 fixDaughters = cms.bool(False)
#         )
#         if useSoftDrop:
#             process.packedPatJetsFatPF.algoTags.append( cms.InputTag('selectedPatJetsSoftDropFatPFPacked') )
#             process.packedPatJetsFatPF.algoLabels.append( 'SoftDropPuppi' )
#         if usePruned:
#             process.packedPatJetsFatPF.algoTags.append( cms.InputTag('selectedPatJetsPrunedFatPFPacked') )
#             process.packedPatJetsFatPF.algoLabels.append( 'Pruned' )
#
#         #-------------------------------------
#         ## N-subjettiness
#         from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness
#
#         process.Njettiness = Njettiness.clone(
#             src = cms.InputTag(fatJetSource),
#             R0  = cms.double(fatJetRadius)
#         )
#
#         getattr(process,'patJetsFatPF'+postfix).userData.userFloats.src += ['Njettiness:tau1','Njettiness:tau2','Njettiness:tau3']
#
#
#         #-------------------------------------
#         ## Grooming ValueMaps
#         process.SoftDrop = cms.EDProducer("RecoJetDeltaRValueMapProducer",
#             src = cms.InputTag(fatJetSource),
#             matched = cms.InputTag("selectedPatJetsSoftDropFatPFPacked"),
#             distMax = cms.double(fatJetRadius),
#             values = cms.vstring('mass','pt','eta','phi','jecFactor(0)'),
#             valueLabels = cms.vstring('Mass','Pt','Eta','Phi','jecFactor0'),
#             lazyParser = cms.bool(True)
#         )
#         process.Pruned = cms.EDProducer("RecoJetDeltaRValueMapProducer",
#             src = cms.InputTag(fatJetSource),
#             matched = cms.InputTag("selectedPatJetsPrunedFatPFPacked"),
#             distMax = cms.double(fatJetRadius),
#             values = cms.vstring('mass','pt','eta','phi','jecFactor(0)'),
#             valueLabels = cms.vstring('Mass','Pt','Eta','Phi','jecFactor0'),
#             lazyParser = cms.bool(True)
#         )
#
#         getattr(process,'patJetsFatPF'+postfix).userData.userFloats.src += ['SoftDrop:Mass','SoftDrop:Pt','SoftDrop:Eta','SoftDrop:Phi','SoftDrop:jecFactor0',
                                                                               # 'Pruned:Mass'  ,'Pruned:Pt'  ,'Pruned:Eta'  ,'Pruned:Phi'  ,'Pruned:jecFactor0']


#-------------------------------------
# if runOnData:
#     # Remove MC matching when running over data
#     from PhysicsTools.PatAlgos.tools.coreTools import removeMCMatching
#     removeMCMatching( process, ['Photons', 'Electrons','Muons', 'Taus', 'Jets', 'METs', 'PFElectrons','PFMuons', 'PFTaus'] )

#-------------------------------------
## Add GenParticlePruner for boosted b-tagging studies
if not runOnData:
    process.prunedGenParticlesBoost = cms.EDProducer('GenParticlePruner',
        src = cms.InputTag(genParticles),
        select = cms.vstring(
            "drop  *  ", #by default
            "keep ( status = 3 || (status>=21 && status<=29) ) && pt > 0", #keep hard process particles with non-zero pT
            "keep abs(pdgId) = 13 || abs(pdgId) = 15" #keep muons and taus
        )
    )

#-------------------------------------

## Filter for removing scraping events
process.noscraping = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False),
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.25)
)

## Filter for good primary vertex
process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
    vertexCollection = cms.InputTag(pvSource),
    minimumNDOF = cms.uint32(4) ,
    maxAbsZ = cms.double(24),
    maxd0 = cms.double(2)
)
#-------------------------------------

#-------------------------------------
# if useTTbarFilter:
#     process.load("RecoBTag.PerformanceMeasurements.TTbarSelectionFilter_cfi")
#     process.load("RecoBTag.PerformanceMeasurements.TTbarSelectionProducer_cfi")
#
#     if isReHLT and not runOnData:
#         process.ttbarselectionproducer.triggerColl =  cms.InputTag("TriggerResults","","HLT2")
#
#     #electron id
#     from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
#
#     if miniAod:
#         process.ttbarselectionproducer.electronColl = cms.InputTag('slimmedElectrons')
#         process.ttbarselectionproducer.muonColl     = cms.InputTag('slimmedMuons')
#         # process.ttbarselectionproducer.jetColl      = cms.InputTag(patJetSource)
#         process.ttbarselectionproducer.jetColl      = cms.InputTag('slimmedJets')
#         process.ttbarselectionproducer.metColl      = cms.InputTag('slimmedMETs')
#         switchOnVIDElectronIdProducer(process, DataFormat.MiniAOD)
#     else:
#         process.ttbarselectionproducer.electronColl = cms.InputTag('selectedPatElectrons'+postfix)
#         process.ttbarselectionproducer.muonColl     = cms.InputTag('selectedPatMuons'+postfix)
#         # process.ttbarselectionproducer.jetColl      = cms.InputTag(patJetSource)
#         process.ttbarselectionproducer.jetColl      = cms.InputTag('slimmedJets')
#         process.ttbarselectionproducer.metColl      = cms.InputTag('patMETs'+postfix)
#         switchOnVIDElectronIdProducer(process, DataFormat.AOD)

    # Set up electron ID (VID framework)
    # from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
    # switchOnVIDElectronIdProducer(process, dataFormat=DataFormat.MiniAOD)
    # my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Fall17_94X_V1_cff']
    # for idmod in my_id_modules:
    #     setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)



    #process.ttbarselectionproducer.isData       = runOnData
    #process.ttbarselectionproducer.electronColl = cms.InputTag('selectedPatElectrons'+postfix)
    #process.ttbarselectionproducer.muonColl     = cms.InputTag('selectedPatMuons'+postfix)
    #process.ttbarselectionproducer.jetColl      = cms.InputTag(patJetSource)
    #process.ttbarselectionproducer.metColl      = cms.InputTag('patMETs'+postfix)
    #process.ttbarselectionfilter.select_ee   = True
    #process.ttbarselectionfilter.select_mumu = True
    #process.ttbarselectionfilter.select_emu  = True
    #process.ttbarselectionfilter.Keep_all_events  = False

    ## Change the cone size of muon isolation to 0.3
    #getattr(process,"pfIsolatedMuons"+postfix).isolationValueMapsCharged = cms.VInputTag( cms.InputTag( 'muPFIsoValueCharged03'+postfix ) )
    #getattr(process,"pfIsolatedMuons"+postfix).isolationValueMapsNeutral = cms.VInputTag( cms.InputTag( 'muPFIsoValueNeutral03'+postfix ), cms.InputTag( 'muPFIsoValueGamma03'+postfix ) )
    #getattr(process,"pfIsolatedMuons"+postfix).deltaBetaIsolationValueMap = cms.InputTag( 'muPFIsoValuePU03'+postfix )
    #getattr(process,"pfIsolatedMuons"+postfix).combinedIsolationCut = cms.double(9999.)
    #getattr(process,"pfIsolatedMuons"+postfix).isolationCut = cms.double(9999.)

    #getattr(process,"patMuons"+postfix).isolationValues = cms.PSet(
    #    pfNeutralHadrons = cms.InputTag('muPFIsoValueNeutral03'+postfix),
    #    pfPhotons = cms.InputTag('muPFIsoValueGamma03'+postfix),
    #    pfChargedHadrons = cms.InputTag('muPFIsoValueCharged03'+postfix),
    #    pfChargedAll = cms.InputTag('muPFIsoValueChargedAll03'+postfix),
    #    pfPUChargedHadrons = cms.InputTag('muPFIsoValuePU03'+postfix)
    #)

    ## Change the cone size of electron isolation to 0.3
    #getattr(process,'pfElectrons'+postfix).isolationValueMapsCharged  = cms.VInputTag(cms.InputTag('elPFIsoValueCharged03PFId'+postfix))
    #getattr(process,'pfElectrons'+postfix).deltaBetaIsolationValueMap = cms.InputTag('elPFIsoValuePU03PFId'+postfix)
    #getattr(process,'pfElectrons'+postfix).isolationValueMapsNeutral  = cms.VInputTag(cms.InputTag('elPFIsoValueNeutral03PFId'+postfix), cms.InputTag('elPFIsoValueGamma03PFId'+postfix))

    #getattr(process,'pfIsolatedElectrons'+postfix).isolationValueMapsCharged = cms.VInputTag(cms.InputTag('elPFIsoValueCharged03PFId'+postfix))
    #getattr(process,'pfIsolatedElectrons'+postfix).deltaBetaIsolationValueMap = cms.InputTag('elPFIsoValuePU03PFId'+postfix)
    #getattr(process,'pfIsolatedElectrons'+postfix).isolationValueMapsNeutral = cms.VInputTag(cms.InputTag('elPFIsoValueNeutral03PFId'+postfix), cms.InputTag('elPFIsoValueGamma03PFId'+postfix))
    #getattr(process,'pfIsolatedElectrons'+postfix).combinedIsolationCut = cms.double(9999.)
    #getattr(process,'pfIsolatedElectrons'+postfix).isolationCut = cms.double(9999.)

    ## Electron ID
    #process.load("EGamma.EGammaAnalysisTools.electronIdMVAProducer_cfi")
    #process.eidMVASequence = cms.Sequence( process.mvaTrigV0 + process.mvaNonTrigV0 )

    #getattr(process,'patElectrons'+postfix).electronIDSources.mvaTrigV0    = cms.InputTag("mvaTrigV0")
    #getattr(process,'patElectrons'+postfix).electronIDSources.mvaNonTrigV0 = cms.InputTag("mvaNonTrigV0")
    #getattr(process,'patElectrons'+postfix).isolationValues = cms.PSet(
    #    pfChargedHadrons = cms.InputTag('elPFIsoValueCharged03PFId'+postfix),
    #    pfChargedAll = cms.InputTag('elPFIsoValueChargedAll03PFId'+postfix),
    #    pfPUChargedHadrons = cms.InputTag('elPFIsoValuePU03PFId'+postfix),
    #    pfNeutralHadrons = cms.InputTag('elPFIsoValueNeutral03PFId'+postfix),
    #    pfPhotons = cms.InputTag('elPFIsoValueGamma03PFId'+postfix)
    #)

    ## Conversion rejection
    ## This should be your last selected electron collection name since currently index is used to match with electron later. We can fix this using reference pointer.
    #setattr(process,'patConversions'+postfix) = cms.EDProducer("PATConversionProducer",
        #electronSource = cms.InputTag('selectedPatElectrons'+postfix)
    #)
#-------------------------------------
if miniAod:
    process.load('PhysicsTools.PatAlgos.slimming.unpackedTracksAndVertices_cfi')

#-------------------------------------
## Change the minimum number of tracker hits used in the track selection
# if changeMinNumberOfHits:
#     for m in process.producerNames().split(' '):
#         if m.startswith('pfImpactParameterTagInfos'):
#             print "Changing 'minimumNumberOfHits' for " + m + " to " + str(minNumberOfHits)
#             getattr(process, m).minimumNumberOfHits = cms.int32(minNumberOfHits)

from PhysicsTools.PatAlgos.tools.pfTools import *
## Adapt primary vertex collection
adaptPVs(process, pvCollection=cms.InputTag(pvSource))

#-------------------------------------
## Add TagInfos to PAT jets
for i in ['patJets', 'patJetsFatPF', 'patJetsSoftDropSubjetsPF', 'patJetsPrunedSubjetsPF',
          'updatedPatJetsTransientCorrected', 'updatedPatJetsTransientCorrectedFatPF', 'updatedPatJetsTransientCorrectedSoftDropSubjetsPF']:
    m = i + postfix
    if hasattr(process,m) and getattr( getattr(process,m), 'addBTagInfo' ):
        print "Switching 'addTagInfos' for " + m + " to 'True'"
        setattr( getattr(process,m), 'addTagInfos', cms.bool(True) )

#-------------------------------------
## Adapt fat jet b tagging
# if runFatJets:
#     getattr(process,'softPFElectronsTagInfosFatPF'+postfix).DeltaRElectronJet = cms.double(fatJetRadius) # default is 0.4
#     if useLegacyTaggers:
#         # Set the cone size for the jet-track association to the jet radius
#         getattr(process,'jetTracksAssociatorAtVertexFatPF'+postfix).coneSize = cms.double(fatJetRadius) # default is 0.4
#         getattr(process,'secondaryVertexTagInfosFatPF'+postfix).trackSelection.jetDeltaRMax = cms.double(fatJetRadius)   # default is 0.3
#         getattr(process,'secondaryVertexTagInfosFatPF'+postfix).vertexCuts.maxDeltaRToJetAxis = cms.double(fatJetRadius) # default is 0.4
#         # Set the jet-SV dR to the jet radius
#         getattr(process,'inclusiveSecondaryVertexFinderTagInfosFatPF'+postfix).vertexCuts.maxDeltaRToJetAxis = cms.double(fatJetRadius) # default is 0.4
#         getattr(process,'inclusiveSecondaryVertexFinderTagInfosFatPF'+postfix).extSVDeltaRToJet = cms.double(fatJetRadius) # default is 0.3
#         # Set the JP track dR cut to the jet radius
#         process.jetProbabilityComputerFat = process.jetProbabilityComputer.clone( deltaR = cms.double(fatJetRadius) ) # default is 0.3
#         getattr(process,'jetProbabilityBJetTagsFatPF'+postfix).jetTagComputer = cms.string('jetProbabilityComputerFat')
#         # Set the JBP track dR cut to the jet radius
#         process.jetBProbabilityComputerFat = process.jetBProbabilityComputer.clone( deltaR = cms.double(fatJetRadius) ) # default is 0.4
#         getattr(process,'jetBProbabilityBJetTagsFatPF'+postfix).jetTagComputer = cms.string('jetBProbabilityComputerFat')
#         # Set the CSVv2 track dR cut to the jet radius
#         process.combinedSecondaryVertexV2ComputerFat = process.combinedSecondaryVertexV2Computer.clone()
#         process.combinedSecondaryVertexV2ComputerFat.trackSelection.jetDeltaRMax = cms.double(fatJetRadius) # default is 0.3
#         process.combinedSecondaryVertexV2ComputerFat.trackPseudoSelection.jetDeltaRMax = cms.double(fatJetRadius) # default is 0.3
#         getattr(process,'combinedInclusiveSecondaryVertexV2BJetTagsFatPF'+postfix).jetTagComputer = cms.string('combinedSecondaryVertexV2ComputerFat')
#     else:
#         # Set the cone size for the jet-track association to the jet radius
#         getattr(process,'pfImpactParameterTagInfosFatPF'+postfix).maxDeltaR = cms.double(fatJetRadius) # default is 0.4
#         getattr(process,'pfSecondaryVertexTagInfosFatPF'+postfix).trackSelection.jetDeltaRMax = cms.double(fatJetRadius)   # default is 0.3
#         getattr(process,'pfSecondaryVertexTagInfosFatPF'+postfix).vertexCuts.maxDeltaRToJetAxis = cms.double(fatJetRadius) # default is 0.4
#         # Set the jet-SV dR to the jet radius
#         getattr(process,'pfInclusiveSecondaryVertexFinderTagInfosFatPF'+postfix).vertexCuts.maxDeltaRToJetAxis = cms.double(fatJetRadius) # default is 0.4
#         getattr(process,'pfInclusiveSecondaryVertexFinderTagInfosFatPF'+postfix).extSVDeltaRToJet = cms.double(fatJetRadius) # default is 0.3
#         # Set the JP track dR cut to the jet radius
#         process.candidateJetProbabilityComputerFat = process.candidateJetProbabilityComputer.clone( deltaR = cms.double(fatJetRadius) ) # default is 0.3
#         getattr(process,'pfJetProbabilityBJetTagsFatPF'+postfix).jetTagComputer = cms.string('candidateJetProbabilityComputerFat')
#         # Set the JBP track dR cut to the jet radius
#         process.candidateJetBProbabilityComputerFat = process.candidateJetBProbabilityComputer.clone( deltaR = cms.double(fatJetRadius) ) # default is 0.4
#         getattr(process,'pfJetBProbabilityBJetTagsFatPF'+postfix).jetTagComputer = cms.string('candidateJetBProbabilityComputerFat')
#         # Set the CSVv2 track dR cut to the jet radius
#         process.candidateCombinedSecondaryVertexV2ComputerFat = process.candidateCombinedSecondaryVertexV2Computer.clone()
#         process.candidateCombinedSecondaryVertexV2ComputerFat.trackSelection.jetDeltaRMax = cms.double(fatJetRadius) # default is 0.3
#         process.candidateCombinedSecondaryVertexV2ComputerFat.trackPseudoSelection.jetDeltaRMax = cms.double(fatJetRadius) # default is 0.3
#         if hasattr(process,'pfCombinedInclusiveSecondaryVertexV2BJetTagsFatPF'+postfix):
#             getattr(process,'pfCombinedInclusiveSecondaryVertexV2BJetTagsFatPF'+postfix).jetTagComputer = cms.string('candidateCombinedSecondaryVertexV2ComputerFat')

#-------------------------------------
process.btagana = bTagAnalyzer.clone()
# if useLegacyTaggers:
#     process.btagana = bTagAnalyzerLegacy.clone()
# The following combinations should be considered:
# For b-tagging performance measurements:
#   process.btagana.useSelectedTracks    = True
#   process.btagana.useTrackHistory      = False (or True for Mistag systematics with GEN-SIM-RECODEBUG samples)
#   produceJetTrackTree  = False
#   process.btagana.produceAllTrackTree  = False
#   process.btagana.producePtRelTemplate = False (or True for PtRel fit studies)
# or data/MC validation of jets, tracks and SVs:
#   process.btagana.useSelectedTracks    = False (or True for JP calibration)
#   process.btagana.useTrackHistory      = False
#   produceJetTrackTree  = True
#   process.btagana.produceAllTrackTree  = False
#   process.btagana.producePtRelTemplate = False
# or general tracks, PV and jet performance studies:
#   process.btagana.useSelectedTracks    = True
#   process.btagana.useTrackHistory      = False
#   produceJetTrackTree  = False
#   process.btagana.produceAllTrackTree  = True
#   process.btagana.producePtRelTemplate = False
#------------------
#Handle groups
for requiredGroup in process.btagana.groups:
   for storedGroup in btagana_tmp.groups:
     if (requiredGroup.group == storedGroup.group):
       requiredGroup.store = storedGroup.store

process.btagana.MaxEta                = maxJetEta ## for extended forward pixel coverage
process.btagana.MinPt                 = minJetPt
process.btagana.tracksColl            = cms.InputTag(trackSource)
process.btagana.useSelectedTracks     = useSelectedTracks ## False if you want to run on all tracks : for commissioning studies
process.btagana.useTrackHistory       = useTrackHistory ## Can only be used with GEN-SIM-RECODEBUG files
process.btagana.produceJetTrackTruthTree = useTrackHistory ## can only be used with GEN-SIM-RECODEBUG files and when useTrackHistory is True
process.btagana.produceAllTrackTree   = produceAllTrackTree ## True if you want to run info for all tracks : for commissioning studies
process.btagana.producePtRelTemplate  = producePtRelTemplate  ## True for performance studies
#------------------
process.btagana.runTagVariables     = runTagVariables  ## True if you want to run TagInfo TaggingVariables
process.btagana.runCSVTagVariables  = runCSVTagVariables   ## True if you want to run CSV TaggingVariables
process.btagana.runCSVTagTrackVariables  = runCSVTagTrackVariables   ## True if you want to run CSV Tagging Track Variables
process.btagana.runPrunedDeepFlavourTaggers = runPrunedDeepFlavourTaggers
process.btagana.runDeepFlavourTagVariables = runDeepFlavourTagVariables
process.btagana.runDeepDoubleXTagVariables = runDeepDoubleXTagVariables
process.btagana.runDeepBoostedJetTagVariables = runDeepBoostedJetTagVariables
process.btagana.primaryVertexColl     = cms.InputTag(pvSource)
process.btagana.Jets                  = cms.InputTag(patJetSource)
process.btagana.muonCollectionName    = cms.InputTag(muSource)
process.btagana.patMuonCollectionName = cms.InputTag(patMuons)
process.btagana.patElecCollectionName = cms.InputTag(patElecs)
process.btagana.use_ttbar_filter      = cms.bool(useTTbarFilter)
#process.btagana.triggerTable          = cms.InputTag('TriggerResults::HLT') # Data and MC
process.btagana.triggerTable          = cms.InputTag(trigresults) # Data and MC
process.btagana.genParticles          = cms.InputTag(genParticles)
process.btagana.candidates            = cms.InputTag(pfCandidates)
process.btagana.runJetVariables     = runJetVariables
process.btagana.runQuarkVariables   = runQuarkVariables
process.btagana.runHadronVariables  = runHadronVariables
process.btagana.runGenVariables     = runGenVariables
process.btagana.runPFElectronVariables = runPFElectronVariables
process.btagana.runPFMuonVariables = runPFMuonVariables
process.btagana.runPatMuons = runPatMuons
process.btagana.runPatElecs = runPatElecs
process.btagana.runCTagVariables = runCTagVariables
process.btagana.runEventInfo = runEventInfo
# process.btagana.runOnData = cms.bool(runOnData)

# if runOnData:
#   process.btagana.runHadronVariables  = False
#   process.btagana.runQuarkVariables   = False
#   process.btagana.runGenVariables     = False

# if runCTagVariables:
#     process.btagana.runEventInfo = True

if not process.btagana.useTrackHistory  or not produceJetTrackTree:
    process.btagana.produceJetTrackTruthTree = False

# if process.btagana.useTrackHistory:
#     process.load('SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi')
#     process.load('SimTracker.TrackerHitAssociation.tpClusterProducer_cfi')

# if runFatJets:
#     process.btaganaFatJets = process.btagana.clone(
#         runEventInfo      = cms.bool(not processStdAK4Jets),
#         allowJetSkipping    = cms.bool(False),
#         runTagVariables     = runTagVariables,
#         runDeepFlavourTagVariables = cms.bool(False),
#         deepFlavourJetTags = cms.string(''),
#         deepFlavourNegJetTags = cms.string(''),
#         runTagVariablesSubJets = runTagVariablesSubJets,
#         runDeepDoubleXTagVariables = runDeepDoubleXTagVariables,
#         runDeepBoostedJetTagVariables = runDeepBoostedJetTagVariables,
#         useSelectedTracks   = cms.bool(True),
#         maxDeltaR           = cms.double(fatJetRadius),
#         R0                  = cms.double(fatJetRadius),
#         maxSVDeltaRToJet    = cms.double(fatJetRadius-(0.1+(fatJetRadius-0.8)*(0.4/0.7))), # linear interpolation from 0.7 at R=0.8 to 1.0 at R=1.5
#         doubleSVBJetTags    = cms.string('pfBoostedDoubleSecondaryVertex' + ('CA15' if algoLabel=='CA' else 'AK8') + 'BJetTags'),
#         distJetAxis         = cms.double(9999.),
#         decayLength         = cms.double(9999.),
#         deltaR              = cms.double(0.8),
#         BranchNamePrefix    = cms.string('FatJetInfo'),
#         Jets                = cms.InputTag(patFatJetSource),
#         SubJets             = cms.VInputTag(),
#         SubJetLabels        = cms.vstring(),
#         runFatJets          = cms.bool(True),
#         runSubJets          = runSubJets,
#         svComputer          = cms.string('combinedSecondaryVertexV2ComputerFat' if useLegacyTaggers else 'candidateCombinedSecondaryVertexV2ComputerFat'),
#         bdsvTagInfos        = cms.string('pfBoostedDoubleSV' + ('CA15' if algoLabel=='CA' else 'AK8')),
#         use_ttbar_filter    = cms.bool(False)
#     )
#     if useSoftDrop:
#         process.btaganaFatJets.SubJets.append( cms.InputTag(patSubJetSourceSoftDrop) )
#         process.btaganaFatJets.SubJetLabels.append( 'SoftDropPuppi' )
#     if usePruned:
#         process.btaganaFatJets.SubJets.append( cms.InputTag('selectedPatJetsPrunedFatPFPacked:SubJets') )
#         process.btaganaFatJets.SubJetLabels.append( 'Pruned' )

# if doBoostedCommissioning:
#     process.btaganaFatJets.runHadronVariables = True
#     process.btaganaFatJets.runQuarkVariables = True
#     process.btaganaFatJets.runPFMuonVariables = True
#     process.btaganaFatJets.runCSVTagVariables = True
#     process.btaganaFatJets.runCSVTagTrackVariables = True
#     process.btaganaFatJets.runCSVTagVariablesSubJets = True
#     process.btaganaFatJets.runDeepDoubleXTagVariables = True
#     process.btaganaFatJets.runDeepBoostedJetTagVariables = True
#     print "**********NTuples will be made for boosted b tag commissioning. The following switches will be reset:**********"
#     print "runHadronVariables set to '",process.btaganaFatJets.runHadronVariables,"'"
#     print "runQuarkVariables set to '",process.btaganaFatJets.runQuarkVariables,"'"
#     print "runPFMuonVariables set to '",process.btaganaFatJets.runPFMuonVariables,"'"
#     print "For fat jets: runCSVTagVariables set to '",process.btaganaFatJets.runCSVTagVariables,"'"
#     print "For fat jets: runCSVTagTrackVariables set to '",process.btaganaFatJets.runCSVTagTrackVariables,"'"
#     print "For subjets:  runCSVTagVariablesSubJets set to '",process.btaganaFatJets.runCSVTagVariablesSubJets,"'"
#     print "For fat jets: runDeepDoubleXTagVariables set to '",process.btaganaFatJets.runDeepDoubleXTagVariables,"'"
#     print "For fat jets: runDeepBoostedJetTagVariables set to '",process.btaganaFatJets.runDeepBoostedJetTagVariables,"'"
#     print "********************"

# if process.btagana.produceJetTrackTruthTree:
#     process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")
#     process.load("SimTracker.TrackHistory.TrackHistory_cff")
#     process.load("SimTracker.TrackHistory.TrackClassifier_cff")
#     process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")
#     process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cfi")


process.btagana.TriggerPathNames = cms.vstring("HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_*",
					       "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_*")
# process.btagana.TriggerPathNames = cms.vstring()

#---------------------------------------

#---------------------------------------
## Trigger selection !
#import HLTrigger.HLTfilters.triggerResultsFilter_cfi as hlt
#process.JetHLTFilter = hlt.triggerResultsFilter.clone(
#    triggerConditions = cms.vstring(
#        "HLT_PFJet80_v*"
#    ),
#    hltResults = cms.InputTag("TriggerResults","","HLT"),
#    l1tResults = cms.InputTag( "" ),
#    throw = cms.bool( False ) #set to false to deal with missing triggers while running over different trigger menus
#)
#---------------------------------------

#---------------------------------------
## Optional MET filters:
## https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFilters
#process.load("RecoMET.METFilters.metFilters_cff")
#process.trackingFailureFilter.VertexSource = cms.InputTag('goodOfflinePrimaryVertices')
#---------------------------------------

#---------------------------------------
## Event counter
from RecoBTag.PerformanceMeasurements.eventcounter_cfi import eventCounter
process.allEvents = eventCounter.clone()
process.selectedEvents = eventCounter.clone()
#---------------------------------------

#---------------------------------------
## Define event filter sequence
process.filtSeq = cms.Sequence(
    #process.JetHLTFilter*
    #process.noscraping
    process.primaryVertexFilter
)


## Define analyzer sequence
process.analyzerSeq = cms.Sequence(process.btagana)
# if processStdAK4Jets:
    # process.analyzerSeq += process.btagana
# if runFatJets:
#     process.analyzerSeq += process.btaganaFatJets
# if processStdAK4Jets and useTTbarFilter:
#     process.analyzerSeq.replace( process.btagana, process.ttbarselectionproducer * process.ttbarselectionfilter * process.btagana )
#---------------------------------------

#Trick to make it work in 9_1_X
# process.tsk = cms.Task()
# for mod in process.producers_().itervalues():
#     process.tsk.add(mod)
# for mod in process.filters_().itervalues():
#     process.tsk.add(mod)

process.p = cms.Path(
    process.allEvents
    * process.filtSeq
    * process.selectedEvents
    * process.analyzerSeq#,
    # process.tsk
)

process.analysisNTupleEndPath = cms.EndPath(process.analyzerSeq)

# Delete predefined output module (needed for running with CRAB)
del process.out

# open('pydump.py','w').write(process.dumpPython())
