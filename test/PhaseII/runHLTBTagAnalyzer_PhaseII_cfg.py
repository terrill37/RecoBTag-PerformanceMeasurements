### configuration file to re-run customized HLT Menu on RAW

# use the following two lines for tracking V0 setup
from RecoBTag.PerformanceMeasurements.Simone_TrackingV0 import cms, process
process.load("RecoBTag.PerformanceMeasurements.BTagHLT_stripped_cff")

# use the following two lines for tracking V2 setup
# from RecoBTag.PerformanceMeasurements.Simone_TrackingV2 import cms, process
# process.load("RecoBTag.PerformanceMeasurements.BTagHLT_stripped_trackV2PF_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    # input = cms.untracked.int32(250)
)


# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    # "root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19MiniAOD/TTbar_14TeV_TuneCP5_Pythia8/MINIAODSIM/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/F0225E24-F876-D448-8318-2D89795D632F.root",
    # "root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/QCD_Pt_50to80_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3-v1/10000/19286DB0-FDED-5A4D-B5F9-4FCDB39A99CE.root",
    #"root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/QCD_Pt-15to3000_EMEnriched_TuneCP5_13TeV_pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3-v1/50000/BBB89FE4-5C9D-7842-BDE3-C89FF77630B6.root",
"file:/eos/cms/store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/A7DE6079-B3AE-4743-A5F3-2050EDEB8383.root"
# "/TTbar_14TeV_TuneCP5_Pythia8/PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3_ext1-v3/GEN-SIM-DIGI-RAW"
# "root://xrootd-cms.infn.it//store/mc/PhaseIITDRSpring19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/EB1607A3-B053-1E42-B9C5-418657AD9E2A.root",
),
    secondaryFileNames = cms.untracked.vstring()
)
process.options = cms.untracked.PSet(
)


#redefining reconstruction_step
process.reconstruction = cms.Sequence(process.localreco+
    process.globalreco
    +process.particleFlowReco
    +process.ak4PFJets
    +process.fixedGridRhoFastjetAll
    +process.ak4PFL1FastjetCorrector
    +process.ak4PFJetsCorrected
    +process.particleFlowPtrs
    +process.goodOfflinePrimaryVertices
    +process.pfPileUpJME
    +process.pfNoPileUpJME
    +process.ak4PFJetsCHS
    +process.ak4PFCHSL1FastjetCorrector
    +process.ak4PFCHSL2RelativeCorrector
    +process.ak4PFCHSL3AbsoluteCorrector
    +process.ak4PFCHSL1FastL2L3Corrector
    +process.ak4PFJetsCHSCorrected
)


# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
#process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)

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

# process.DQMStore.enableMultiThread = True
process.DQMStore.enableMultiThread = False

# process.options.numberOfStreams = cms.untracked.uint32(4)
# process.options.numberOfThreads = cms.untracked.uint32(4)
process.options.numberOfStreams = cms.untracked.uint32(1)
process.options.numberOfThreads = cms.untracked.uint32(1)



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
print "Running with globalTag: %s"%("auto:phase2_realistic")

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
process.options   = cms.untracked.PSet(
    # wantSummary = cms.untracked.bool(options.wantSummary),
    wantSummary = cms.untracked.bool(False),
    allowUnscheduled = cms.untracked.bool(True)
)


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

process.btagana.MaxEta                = 2.4
process.btagana.MinPt                 = 30
# process.btagana.triggerTable          = cms.InputTag('TriggerResults::HLT') # Data and MC
process.btagana.triggerTable          = cms.InputTag('TriggerResults::RECO2') # Data and MC
process.btagana.primaryVertexColl     = cms.InputTag('hltVerticesPF')
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
from RecoBTag.PerformanceMeasurements.myTrackAnalyzer_cfi import myTrackAnalyzer
process.trackAnalyzer = myTrackAnalyzer.clone()
process.trackAnalyzer.tracks = cms.InputTag('generalTracks')

## Define analyzer sequence
process.analyzerSeq = cms.Sequence(process.btagana)



process.p = cms.Path(
    process.allEvents
    #* process.filtSeq
    * process.selectedEvents
    # * process.analyzerSeq
    * process.trackAnalyzer
)


process.analysisNTupleEndPath = cms.EndPath(process.analyzerSeq)


del process.out

# open('pydump.py','w').write(process.dumpPython())
