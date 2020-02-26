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

opts.register('logs', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'create log files configured via MessageLogger')

opts.register('doTrackV0', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'Use TrackingV0 instead of V2')

opts.register('runCMSSW11Sample', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'Use setup for CMSSW 11')

opts.register('wantSummary', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'show cmsRun summary at job completion')

opts.register('dumpPython', None,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'Path to python file with content of cms.Process')

opts.register('htrk', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'added monitoring histograms for selected Tracks and Vertices')

opts.register('skimTracks', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'skim original collection of generalTracks (only tracks associated to first N pixel vertices)')

opts.parseArguments()

if opts.doTrackV0:
    if opts.runCMSSW11Sample:
        # use the following two lines for tracking V2 setup
        from RecoBTag.PerformanceMeasurements.step3_TrackingV0_11_0_0_samples import cms, process
        # process.load("RecoBTag.PerformanceMeasurements.BTagHLT_stripped_cff")
    else:
        # use the following two lines for tracking V0 setup
        from RecoBTag.PerformanceMeasurements.step3_TrackingV0_11_0_0 import cms, process
        # process.load("RecoBTag.PerformanceMeasurements.BTagHLT_stripped_cff")
else:
    if opts.runCMSSW11Sample:
        # use the following two lines for tracking V2 setup
        from RecoBTag.PerformanceMeasurements.step3_TrackingV2_11_0_0_samples import cms, process
        # process.load("RecoBTag.PerformanceMeasurements.BTagHLT_stripped_trackV2_cff")
    else:
        # use the following two lines for tracking V2 setup
        from RecoBTag.PerformanceMeasurements.step3_TrackingV2_11_0_0 import cms, process
        # process.load("RecoBTag.PerformanceMeasurements.BTagHLT_stripped_trackV2_cff")

# process.load("RecoBTag.PerformanceMeasurements.BTagHLT_stripped_trackV2_cff")
process.load("RecoBTag.PerformanceMeasurements.BTagHLT_stripped_trackV2_LikeOffline11_cff")

# remove cms.EndPath for EDM output
del process.HLTOutput

# remove cms.EndPath for DQM output
del process.DQMFileSaverOutput

# reset path to EDM input files
process.source.fileNames = []
process.source.secondaryFileNames = []

# process.maxEvents = cms.untracked.PSet(
#     input = cms.untracked.int32(-1)
# )



###
### Sequence for HLT(-like) AK4-{PF,Calo} Jets
###
process.ak4PFJetsCorrected.correctors = ['ak4PFL1FastL2L3Corrector']

process.ak4CaloL1FastjetCorrector = cms.EDProducer('L1FastjetCorrectorProducer',
  algorithm = cms.string('AK4Calo'),
  level = cms.string('L1FastJet'),
  srcRho = cms.InputTag('fixedGridRhoFastjetAll'),
)
process.ak4CaloL2RelativeCorrector = cms.EDProducer('LXXXCorrectorProducer',
  algorithm = cms.string('AK4Calo'),
  level = cms.string('L2Relative'),
)
process.ak4CaloL3AbsoluteCorrector = cms.EDProducer('LXXXCorrectorProducer',
  algorithm = cms.string('AK4Calo'),
  level = cms.string('L3Absolute'),
)
process.ak4CaloL1FastL2L3Corrector = cms.EDProducer('ChainedJetCorrectorProducer',
  correctors = cms.VInputTag('ak4CaloL1FastjetCorrector', 'ak4CaloL2RelativeCorrector', 'ak4CaloL3AbsoluteCorrector'),
)
process.ak4CaloJetsCorrected = cms.EDProducer('CorrectedCaloJetProducer',
  correctors = cms.VInputTag('ak4CaloL1FastL2L3Corrector'),
  src = cms.InputTag('ak4CaloJets'),
)
process.ak4CaloJetsSeq = cms.Sequence(
    process.ak4CaloL1FastjetCorrector
  * process.ak4CaloL2RelativeCorrector
  * process.ak4CaloL3AbsoluteCorrector
  * process.ak4CaloL1FastL2L3Corrector
  * process.ak4CaloJetsCorrected
)
process.reconstruction *= process.ak4CaloJetsSeq



# Input source
# process.source = cms.Source("PoolSource",
#     fileNames = cms.untracked.vstring(
# "file:/eos/cms/store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/A7DE6079-B3AE-4743-A5F3-2050EDEB8383.root"
# ),
#     secondaryFileNames = cms.untracked.vstring()
# )
# process.options = cms.untracked.PSet(
# )


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



# skimming of tracks
if opts.skimTracks:

   ###
   ### redefine GeneralTracks, selecting a subset of tracks associated to N pixel vertices
   ###  - each track is associated to the pixel vertex which is closest to it in Z
   ###  - the track is retained only if the associated pixel vertex is one of the first N of the vertex collection (ranking is based on sum-pT2)
   ###
   # clone original collection of generalTracks
   process.generalTracksOriginal = process.generalTracks.clone()

   # re-order (see ranker) and restrict the original list of pixel vertices similarly
   # to what was done at HLT in Run-2 (see hltTrimmedPrimaryVertices in 2018 HLT Menu)
   process.hltTrimmedPixelVertices = cms.EDProducer('PixelVerticesSelector',

     src = cms.InputTag('pixelVertices'),

     minSumPt2 = cms.double( 0.0 ),
     minSumPt2FractionWrtMax = cms.double( 0.3 ),

     # criterion to rank pixel vertices
     # (utilizes PVClusterComparer to compute
     # the vertex SumPtSquared f.o.m. using a sub-set of tracks)
     ranker = cms.PSet(
       track_chi2_max = cms.double( 20.0 ),
       track_pt_max = cms.double( 20.0 ),
       track_prob_min = cms.double( -1.0 ),
       track_pt_min = cms.double( 1.0 )
     ),

     # retain only first N vertices
     maxNVertices = cms.int32( -1 ),
   )

   # updated collection of generalTracks
   #  - redefine the module "generalTracks", so that downstream modules
   #    automatically use this updated collection
   #    (instead of the original "generalTracks" collection)
   #  - new set of generalTracks contains only the input tracks
   #    associated to one of the first N pixel vertices
   process.generalTracks = cms.EDProducer('TracksClosestToFirstVerticesSelector',

     tracks = cms.InputTag('generalTracksOriginal'),
     vertices = cms.InputTag('hltTrimmedPixelVertices'),

     # retain only tracks associated to one of the first N vertices
     maxNVertices = cms.int32( 10 ),

     # track-vertex association: max delta-Z between track and z-closest vertex
     maxDeltaZ = cms.double( 0.2 ),
   )

   # insert updated generalTracks into tracking sequence and related task
   process.globalreco_tracking.replace(process.generalTracks, cms.Sequence(
      (process.generalTracksOriginal
     +(process.reconstruction_pixelTrackingOnly * process.hltTrimmedPixelVertices))
     * process.generalTracks
   ))

   process.generalTracksTask.add(process.generalTracksOriginal, process.hltTrimmedPixelVertices)






process.noFilter_PFDeepCSV = cms.Path(process.HLTBtagDeepCSVSequencePF)


# process.hltOutput = cms.OutputModule( "PoolOutputModule",
#      fileName = cms.untracked.string( "hltoutput_hlt.root" ),
#      fastCloning = cms.untracked.bool( False ),
#      outputCommands = cms.untracked.vstring(
#         'drop *',
#         # 'keep *_particleFlowTmp*_*_*',
#          # 'keep *_ak4PFJets*_*_*',
#          # 'keep *_ak4PFJets*_*_RECO',
#          # 'keep *_ak4GenJets_*_HLT',
#         'keep *_hltDeepCombinedSecondaryVertexBJetTagsInfos_*_*',
#         # # 'keep *_hltDeepCombinedSecondaryVertexBJetTagsInfosCalo_*_*',
#         'keep *_hltDeepCombinedSecondaryVertexBJetTagsPF*_*_*',
#          )
#      )




# max number of events to be processed
process.maxEvents.input = opts.maxEvents

# number of events to be skipped
process.source.skipEvents = cms.untracked.uint32(opts.skipEvents)

# multi-threading settings
process.options.numberOfThreads = cms.untracked.uint32(opts.numThreads if (opts.numThreads > 1) else 1)
process.options.numberOfStreams = cms.untracked.uint32(opts.numStreams if (opts.numStreams > 1) else 1)
if hasattr(process, 'DQMStore'):
   process.DQMStore.enableMultiThread = (process.options.numberOfThreads > 1)

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
     # "file:/eos/cms/store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/A7DE6079-B3AE-4743-A5F3-2050EDEB8383.root",
     # "/store/relval/CMSSW_11_0_0/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/110X_mcRun4_realistic_v2_2026D49noPU-v2/20000/26BAF436-18BA-4843-95E6-100394440248.root",
     "/store/relval/CMSSW_11_0_0/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/F4CA9166-52A2-474F-8D30-9B70B4B28361.root",
     # /RelValTTbar_14TeV/CMSSW_11_0_0_pre13-110X_mcRun4_realistic_v2_2026D49noPU-v1/GEN-SIM-DIGI-RAW",
     # "/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/D7F3470F-864E-944B-922E-7178756F4652.root",
   ]


# dump content of cms.Process to python file
if opts.dumpPython is not None:
   open(opts.dumpPython, 'w').write(process.dumpPython())



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
        options_to_change.update([i for i in variableDict[var].runOptions])
      found=True
      break
  if(not found):
    print('WARNING: The group ' + requiredGroup + ' was not found')




# print "Running on data: %s"%('True' if options.runOnData else 'False')
# print "Running with globalTag: %s"%(options.globalTag)
# print "Running with globalTag: %s"%("auto:phase2_realistic_T14")

# trigresults='TriggerResults::HLT'
# trigresults='TriggerResults'

# if options.inputFiles:
#     process.source.fileNames = options.inputFiles



## Define the output file name
# if options.runOnData :
#     options.outFilename += '_data'
# else :
#     options.outFilename += '_mc'
#
# options.outFilename += '.root'
outFilename = 'JetTree_mc.root'

## Output file
process.TFileService = cms.Service("TFileService",
   # fileName = cms.string(options.outFilename)
   fileName = cms.string(outFilename)
)


## Options and Output Report
# process.options   = cms.untracked.PSet(
#     # wantSummary = cms.untracked.bool(options.wantSummary),
#     wantSummary = cms.untracked.bool(False),
#     allowUnscheduled = cms.untracked.bool(True)
# )


#-------------------------------------
## Output Module Configuration (expects a path 'p')
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent
process.out = cms.OutputModule("PoolOutputModule",
                               # fileName = cms.untracked.string(options.outFilename),
                               fileName = cms.untracked.string(outFilename),
                               # save only events passing the full path
                               SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               # save PAT Layer 1 output; you need a '*' to
                               # unpack the list of commands 'patEventContent'
                               outputCommands = cms.untracked.vstring('drop *', *patEventContent)
                               #outputCommands = cms.untracked.vstring('keep *')
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

# process.btagana.MaxEta                = 2.4
process.btagana.MaxEta                = 4.5
process.btagana.MinPt                 = 30
# process.btagana.triggerTable          = cms.InputTag('TriggerResults::HLT') # Data and MC
process.btagana.triggerTable          = cms.InputTag('TriggerResults::RECO2') # Data and MC
# process.btagana.primaryVertexColl     = cms.InputTag('hltVerticesPF')
process.btagana.primaryVertexColl     = cms.InputTag('offlinePrimaryVertices') #change with new Offline like sequence
# process.btagana.primaryVertexColl     = cms.InputTag('firstStepPrimaryVertices')

process.btagana.runHLTJetVariables     = cms.bool(True)
# process.btagana.runOnData = options.runOnData
process.btagana.runOnData = False

process.btagana.PFJets               = cms.InputTag('ak4PFJetsCHSCorrected')
process.btagana.PFJetTags            = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsInfos')
process.btagana.PFSVs                = cms.InputTag('hltDeepSecondaryVertexTagInfosPF')
# process.btagana.PFJetCSVTags         = cms.InputTag('hltCombinedSecondaryVertexBJetTagsPF')
process.btagana.PFJetDeepCSVTags     = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPF:probb')



#---------------------------------------
## Event counter
from RecoBTag.PerformanceMeasurements.eventcounter_cfi import eventCounter
process.allEvents = eventCounter.clone()
process.selectedEvents = eventCounter.clone()
#---------------------------------------
# Tracking Monitoring
# if opts.htrk:
#     from RecoBTag.PerformanceMeasurements.myTrackAnalyzer_cfi import myTrackAnalyzer
#     process.trackAnalyzer = myTrackAnalyzer.clone()
#     process.trackAnalyzer.tracks = cms.InputTag('generalTracks')

# Tracking Monitoring
if opts.htrk:
   process.reconstruction_pixelTrackingOnly_step = cms.Path(process.reconstruction_pixelTrackingOnly)

   from JMETriggerAnalysis.Common.TrackHistogrammer_cfi import TrackHistogrammer
   process.TrackHistograms_pixelTracks = TrackHistogrammer.clone(src = cms.InputTag('pixelTracks'))
   process.TrackHistograms_generalTracks = TrackHistogrammer.clone(src = cms.InputTag('generalTracks'))

   from JMETriggerAnalysis.Common.VertexHistogrammer_cfi import VertexHistogrammer
   process.VertexHistograms_pixelVertices = VertexHistogrammer.clone(src = cms.InputTag('pixelVertices'))
   process.VertexHistograms_offlinePrimaryVertices = VertexHistogrammer.clone(src = cms.InputTag('offlinePrimaryVertices'))

   process.trkMonitoringSeq = cms.Sequence(
       process.TrackHistograms_pixelTracks
     + process.TrackHistograms_generalTracks
     + process.VertexHistograms_pixelVertices
     + process.VertexHistograms_offlinePrimaryVertices
   )
   process.trkMonitoringEndPath = cms.EndPath(process.trkMonitoringSeq)


## Define analyzer sequence
process.analyzerSeq = cms.Sequence(process.btagana)



process.p = cms.Path(
    process.allEvents
    #* process.filtSeq
    * process.selectedEvents
    # * process.analyzerSeq
    # * process.trackAnalyzer
)
# if opts.htrk:
#     process.p*=process.trackAnalyzer

process.analysisNTupleEndPath = cms.EndPath(process.analyzerSeq)

del process.out

# open('pydump.py','w').write(process.dumpPython())
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
print 'dumpPython =', opts.dumpPython
print 'doTrackHistos =', opts.htrk
print 'doTrackingV0 =', opts.doTrackV0
print 'runCMSSW11Sample =', opts.runCMSSW11Sample
print 'useSkimmedTracks =', opts.skimTracks
print '\n-------------------------------'
