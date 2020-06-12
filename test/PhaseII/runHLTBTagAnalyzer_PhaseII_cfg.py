### configuration file to re-run customized HLT Menu on RAW
###
### command-line arguments
###
import FWCore.ParameterSet.VarParsing as vpo
opts = vpo.VarParsing('analysis')

opts.register('skipEvents', 0,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of events to be skipped')

opts.register('numThreads', 1,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of threads')

opts.register('numStreams', 1,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of streams')

opts.register('gt', None,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'argument of process.GlobalTag.globaltag')

opts.register('logs', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'create log files configured via MessageLogger')

opts.register('reco', 'hltPhase2_TRKv06',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'Which tracking version to run')

opts.register('outName', 'JetTree_mc.root',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'Name of the output root file')

opts.register('wantSummary', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'show cmsRun summary at job completion')

opts.register('dumpPython', None,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'Path to python file with content of cms.Process')

opts.register('trkdqm', True,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'added monitoring histograms for selected Tracks and Vertices')

opts.register('pfdqm', True,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'added monitoring histograms for selected PF-Candidates')



opts.parseArguments()

# flag: skim original collection of generalTracks (only tracks associated to first N pixel vertices)
opt_skimTracks = False

opt_reco = opts.reco
if opt_reco.endswith('_skimmedTracks'):
   opt_reco = opt_reco[:-len('_skimmedTracks')]
   opt_skimTracks = True

if opt_reco == 'hltPhase2_TRKv00':
   from RecoBTag.PerformanceMeasurements.hltPhase2_TRKv00_cfg import cms, process
elif opt_reco == 'hltPhase2_TRKv02':
   from RecoBTag.PerformanceMeasurements.hltPhase2_TRKv02_cfg import cms, process
elif opt_reco == 'hltPhase2_TRKv06':
   from RecoBTag.PerformanceMeasurements.hltPhase2_TRKv06_cfg import cms, process
elif opt_reco == 'hltPhase2_TRKv00_TICL':
   from RecoBTag.PerformanceMeasurements.hltPhase2_TRKv00_TICL_cfg import cms, process
elif opt_reco == 'hltPhase2_TRKv02_TICL':
   from RecoBTag.PerformanceMeasurements.hltPhase2_TRKv02_TICL_cfg import cms, process
elif opt_reco == 'hltPhase2_TRKv06_TICL':
   from RecoBTag.PerformanceMeasurements.hltPhase2_TRKv06_TICL_cfg import cms, process
else:
   raise RuntimeError('invalid argument for option "reco": "'+opt_reco+'"')

# reset path to EDM input files
process.source.fileNames = []
process.source.secondaryFileNames = []



# # skimming of tracks
# if opts.skimTracks:
#    from JMETriggerAnalysis.Common.hltPhase2_skimmedTracks import customize_hltPhase2_skimmedTracks
#    process = customize_hltPhase2_skimmedTracks(process)



process.noFilter_PFDeepCSV = cms.Path(process.HLTBtagDeepCSVSequencePF)
process.noFilter_PFProba = cms.Path(process.HLTBtagProbabiltySequencePF)
process.noFilter_PFBProba = cms.Path(process.HLTBtagBProbabiltySequencePF)
process.schedule.extend([process.noFilter_PFDeepCSV, process.noFilter_PFProba, process.noFilter_PFBProba])

process.noFilter_PFDeepCSVPuppi = cms.Path(process.HLTBtagDeepCSVSequencePFPuppi)
process.noFilter_PFProbaPuppi = cms.Path(process.HLTBtagProbabiltySequencePFPuppi)
process.noFilter_PFBProbaPuppi = cms.Path(process.HLTBtagBProbabiltySequencePFPuppi)
process.schedule.extend([process.noFilter_PFDeepCSVPuppi, process.noFilter_PFProbaPuppi, process.noFilter_PFBProbaPuppi])


# max number of events to be processed
process.maxEvents.input = opts.maxEvents

# number of events to be skipped
process.source.skipEvents = cms.untracked.uint32(opts.skipEvents)

# multi-threading settings
process.options.numberOfThreads = cms.untracked.uint32(opts.numThreads if (opts.numThreads > 1) else 1)
process.options.numberOfStreams = cms.untracked.uint32(opts.numStreams if (opts.numStreams > 1) else 1)

# show cmsRun summary at job completion
process.options.wantSummary = cms.untracked.bool(opts.wantSummary)

# MessageLogger
if opts.logs:
   process.MessageLogger = cms.Service('MessageLogger',
     destinations = cms.untracked.vstring(
       'cerr',
       'logError',
       'logInfo',
       'logDebug',
     ),
     # scram b USER_CXXFLAGS="-DEDM_ML_DEBUG"
     debugModules = cms.untracked.vstring(
       'PixelVerticesSelector',
       'TracksClosestToFirstVerticesSelector',
       'JMETriggerNTuple',
     ),
     categories = cms.untracked.vstring(
       'FwkReport',
     ),
     cerr = cms.untracked.PSet(
       threshold = cms.untracked.string('WARNING'),
       FwkReport = cms.untracked.PSet(
         reportEvery = cms.untracked.int32(1),
       ),
     ),
     logError = cms.untracked.PSet(
       threshold = cms.untracked.string('ERROR'),
       extension = cms.untracked.string('.txt'),
       FwkReport = cms.untracked.PSet(
         reportEvery = cms.untracked.int32(1),
       ),
     ),
     logInfo = cms.untracked.PSet(
       threshold = cms.untracked.string('INFO'),
       extension = cms.untracked.string('.txt'),
       FwkReport = cms.untracked.PSet(
         reportEvery = cms.untracked.int32(1),
       ),
     ),
     logDebug = cms.untracked.PSet(
       threshold = cms.untracked.string('DEBUG'),
       extension = cms.untracked.string('.txt'),
       FwkReport = cms.untracked.PSet(
         reportEvery = cms.untracked.int32(1),
       ),
     ),
   )

# input EDM files [primary]
if opts.inputFiles:
   process.source.fileNames = opts.inputFiles
else:
   process.source.fileNames = [
     "/store/mc/Phase2HLTTDRWinter20DIGI/TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/20000/2FA69DD4-0651-084E-87B6-E5F38B007D5D.root",
   ]




#===========
# Begin BTagAna

###############################
####### Parameters ############
###############################

groups = ["HLTEventInfo","HLTJetInfo","HLTTagVar","HLTJetTrack","HLTJetSV","HLTCSVTagVar"]



from RecoBTag.PerformanceMeasurements.BTagAnalyzer_cff import *
btagana_tmp = bTagAnalyzer.clone()
print('Storing the variables from the following groups:')
options_to_change = set() #store which swtiches we need on
# for requiredGroup in options.groups:
for requiredGroup in groups:
  print(requiredGroup)
  found=False
  for existingGroup in btagana_tmp.groups:
    if(requiredGroup==existingGroup.group):
      existingGroup.store=True
      for var in existingGroup.variables:
        if "CaloJet." in var:
          var = var.split(".")[1]
        if "PFJet." in var:
          var = var.split(".")[1]
        if "PuppiJet." in var:
          var = var.split(".")[1]
        options_to_change.update([i for i in variableDict[var].runOptions])
      found=True
      break
  if(not found):
    print('WARNING: The group ' + requiredGroup + ' was not found')



# update process.GlobalTag.globaltag
if opts.gt is not None:
   process.GlobalTag.globaltag = opts.gt
print "Running with globalTag: %s"%(process.GlobalTag.globaltag)

# fix for AK4PF Phase-2 JECs
process.GlobalTag.toGet.append(cms.PSet(
  record = cms.string('JetCorrectionsRecord'),
  tag = cms.string('JetCorrectorParametersCollection_PhaseIIFall17_V5b_MC_AK4PF'),
  label = cms.untracked.string('AK4PF'),
))

#~ outFilename = 'JetTree_mc.root'
outFilename = opts.outName


## Output file
process.TFileService = cms.Service("TFileService",
   fileName = cms.string(outFilename)
)



#-------------------------------------
from RecoBTag.PerformanceMeasurements.BTagHLTAnalyzer_cff import *
process.btagana = bTagHLTAnalyzer.clone()

#------------------
#Handle groups
for requiredGroup in process.btagana.groups:
   for storedGroup in btagana_tmp.groups:
     if (requiredGroup.group == storedGroup.group):
       requiredGroup.store = storedGroup.store

process.btagana.MaxEta                = 4.5
process.btagana.MinPt                 = 25
# process.btagana.triggerTable          = cms.InputTag('TriggerResults::RECO2') # Data and MC
process.btagana.triggerTable          = cms.InputTag('TriggerResults') # Data and MC
# process.btagana.primaryVertexColl     = cms.InputTag('hltVerticesPF')
process.btagana.primaryVertexColl     = cms.InputTag('offlinePrimaryVertices') #change with new Offline like sequence

process.btagana.runHLTJetVariables     = cms.bool(True)
process.btagana.runOnData = False

process.btagana.PFJets               = cms.InputTag('hltAK4PFCHSJetsCorrected')
process.btagana.PFJetTags            = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsInfos')
process.btagana.PFSVs                = cms.InputTag('hltDeepSecondaryVertexTagInfosPF')
process.btagana.PFJetDeepCSVTags     = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPF:probb')
process.btagana.PFJetBPBJetTags      = cms.InputTag('hltPfJetBProbabilityBJetTags')
process.btagana.PFJetPBJetTags       = cms.InputTag('hltPfJetProbabilityBJetTags')

process.btagana.PuppiJets            = cms.InputTag('hltAK4PuppiJetsCorrected')
process.btagana.PuppiJetTags         = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsInfosPuppi')
process.btagana.PuppiSVs             = cms.InputTag('hltDeepSecondaryVertexTagInfosPFPuppi')
process.btagana.PuppiJetDeepCSVTags  = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPFPuppi:probb')
process.btagana.PuppiJetBPBJetTags   = cms.InputTag('hltPfJetBProbabilityBJetTagsPuppi')
process.btagana.PuppiJetPBJetTags    = cms.InputTag('hltPfJetProbabilityBJetTagsPuppi')
process.btagana.PuppiJetCSVTags      = cms.InputTag('hltCombinedSecondaryVertexBJetTagsPFPuppi')

#---------------------------------------
## Event counter
from RecoBTag.PerformanceMeasurements.eventcounter_cfi import eventCounter
process.allEvents = eventCounter.clone()
process.selectedEvents = eventCounter.clone()
#---------------------------------------

# update JESC via local SQLite file
# from CondCore.CondDB.CondDB_cfi import CondDB
# CondDBJECFile = CondDB.clone(connect = 'sqlite_fip:RecoBTag/PerformanceMeasurements/data/PhaseIIFall17_V5b_MC.db' )
# process.jec = cms.ESSource('PoolDBESSource', CondDBJECFile, toGet = cms.VPSet())
# for _tmp in [
#   'AK4PF',
# #      'AK4PFchs',
# #      'AK4PFPuppi',
# #      'AK8PF',
# #      'AK8PFchs',
# #      'AK8PFPuppi',
# ]:
#   process.jec.toGet.append(
#     cms.PSet(
#       record = cms.string('JetCorrectionsRecord'),
#       tag = cms.string('JetCorrectorParametersCollection_PhaseIIFall17_V5b_MC_'+_tmp),
#       label = cms.untracked.string(_tmp),
#     )
#   )

# Add an ESPrefer to override JEC that might be available from the global tag
# process.es_prefer_jec = cms.ESPrefer('PoolDBESSource', 'jec')

# Tracking Monitoring
if opts.trkdqm:

   if opt_reco in ['HLT_TRKv00', 'HLT_TRKv00_TICL', 'HLT_TRKv02', 'HLT_TRKv02_TICL']:
      process.reconstruction_pixelTrackingOnly_step = cms.Path(process.reconstruction_pixelTrackingOnly)
      process.schedule.extend([process.reconstruction_pixelTrackingOnly_step])

   from JMETriggerAnalysis.Common.TrackHistogrammer_cfi import TrackHistogrammer
   process.TrackHistograms_hltPixelTracks = TrackHistogrammer.clone(src = 'pixelTracks')
   process.TrackHistograms_hltGeneralTracks = TrackHistogrammer.clone(src = 'generalTracks')

   process.trkMonitoringSeq = cms.Sequence(
       process.TrackHistograms_hltPixelTracks
     + process.TrackHistograms_hltGeneralTracks
   )

   if opt_skimTracks:
      process.TrackHistograms_hltGeneralTracksOriginal = TrackHistogrammer.clone(src = 'generalTracksOriginal')
      process.trkMonitoringSeq += process.TrackHistograms_hltGeneralTracksOriginal

   from JMETriggerAnalysis.Common.VertexHistogrammer_cfi import VertexHistogrammer
   process.VertexHistograms_hltPixelVertices = VertexHistogrammer.clone(src = 'pixelVertices')
   process.VertexHistograms_hltPrimaryVertices = VertexHistogrammer.clone(src = 'offlinePrimaryVertices')
   process.VertexHistograms_offlinePrimaryVertices = VertexHistogrammer.clone(src = 'offlineSlimmedPrimaryVertices')

   process.trkMonitoringSeq += cms.Sequence(
       process.VertexHistograms_hltPixelVertices
     + process.VertexHistograms_hltPrimaryVertices
     + process.VertexHistograms_offlinePrimaryVertices
   )

#   from Validation.RecoVertex.PrimaryVertexAnalyzer4PUSlimmed_cfi import vertexAnalysis, pixelVertexAnalysisPixelTrackingOnly
#   process.vertexAnalysis = vertexAnalysis.clone(vertexRecoCollections = ['offlinePrimaryVertices'])
#   process.pixelVertexAnalysis = pixelVertexAnalysisPixelTrackingOnly.clone(vertexRecoCollections = ['pixelVertices'])
#
#   process.trkMonitoringSeq += cms.Sequence(
#       process.vertexAnalysis
#     + process.pixelVertexAnalysis
#   )

   process.trkMonitoringEndPath = cms.EndPath(process.trkMonitoringSeq)
   process.schedule.extend([process.trkMonitoringEndPath])


if opts.pfdqm:

   from JMETriggerAnalysis.Common.pfCandidateHistogrammerRecoPFCandidate_cfi import pfCandidateHistogrammerRecoPFCandidate
   from JMETriggerAnalysis.Common.pfCandidateHistogrammerPatPackedCandidate_cfi import pfCandidateHistogrammerPatPackedCandidate

   _candTags = [
     ('_simPFCands', 'simPFProducer', '', pfCandidateHistogrammerRecoPFCandidate),
     ('_hltPFCands', 'particleFlowTmp', '', pfCandidateHistogrammerRecoPFCandidate),
     ('_hltPuppiCands', 'hltPuppi', '(pt > 0)', pfCandidateHistogrammerRecoPFCandidate),
     #~ ('_offlinePFCands', 'packedPFCandidates', '', pfCandidateHistogrammerPatPackedCandidate),
   ]

   _regTags = [
     ['', ''],
     ['_HB'   , '(0.0<=abs(eta) && abs(eta)<1.5)'],
     ['_HGCal', '(1.5<=abs(eta) && abs(eta)<3.0)'],
     ['_HF'   , '(3.0<=abs(eta) && abs(eta)<5.0)'],
   ]

   _pidTags = [
     ['', ''],
     ['_chargedHadrons', '(abs(pdgId) == 211)'],
     ['_neutralHadrons', '(abs(pdgId) == 130)'],
     ['_photons'       , '(abs(pdgId) ==  22)'],
   ]

   process.pfMonitoringSeq = cms.Sequence()
   for _candTag in _candTags:
     for _regTag in _regTags:
       for _pidTag in _pidTags:
         _modName = 'PFCandidateHistograms'+_candTag[0]+_regTag[0]+_pidTag[0]
         setattr(process, _modName, _candTag[3].clone(
           src = _candTag[1],
           cut = ' && '.join([_tmp for _tmp in [_candTag[2], _regTag[1], _pidTag[1]] if _tmp]),
         ))
         process.pfMonitoringSeq += getattr(process, _modName)

   process.pfMonitoringEndPath = cms.EndPath(process.pfMonitoringSeq)
   process.schedule.extend([process.pfMonitoringEndPath])


# skimming of tracks
if opt_skimTracks:

   from JMETriggerAnalysis.Common.hltPhase2_skimmedTracks import customize_hltPhase2_skimmedTracks
   process = customize_hltPhase2_skimmedTracks(process)


process.p = cms.Path(
    process.allEvents
    * process.selectedEvents
)
process.schedule.extend([process.p])
process.analysisNTupleEndPath = cms.EndPath(process.btagana)
process.schedule.extend([process.analysisNTupleEndPath])

# dump content of cms.Process to python file
if opts.dumpPython is not None:
   open(opts.dumpPython, 'w').write(process.dumpPython())

# print-outs
print '--- runHLTBTagAnalyzer_PhaseII_cfg.py ---\n'
print 'process.maxEvents.input =', process.maxEvents.input
print 'process.source.skipEvents =', process.source.skipEvents
print 'process.source.fileNames =', process.source.fileNames
print 'process.source.secondaryFileNames =', process.source.secondaryFileNames
print 'numThreads =', opts.numThreads
print 'numStreams =', opts.numStreams
print 'logs =', opts.logs
print 'wantSummary =', opts.wantSummary
print 'process.GlobalTag.globaltag =', process.GlobalTag.globaltag
print 'dumpPython =', opts.dumpPython
print 'doTrackHistos =', opts.trkdqm
print 'doParticleFlowHistos =', opts.pfdqm
print 'option: reco =', opt_reco, '(skimTracks = '+str(opt_skimTracks)+')'
print '\n-------------------------------'
