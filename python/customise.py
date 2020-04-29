import FWCore.ParameterSet.Config as cms

def customize_HLT_trkIter2GlobalPtSeed0p9(process):

  process.hltIter2PFlowPixelTrackingRegionsGlobalPtSeed0p9 = cms.EDProducer( 'GlobalTrackingRegionWithVerticesEDProducer',
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( 'hltTrimmedPixelVertices' ),
      beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 0.2 ),
      sigmaZVertex = cms.double( 3.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 0.9 ),
      originRadius = cms.double( 0.05 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False )
    )
  )

  process.hltIter2PFlowPixelHitDoublets.trackingRegions = 'hltIter2PFlowPixelTrackingRegionsGlobalPtSeed0p9'

  process.HLTIterativeTrackingIteration2.replace(
    process.hltIter2PFlowPixelTrackingRegions,
    process.hltIter2PFlowPixelTrackingRegionsGlobalPtSeed0p9
  )

  return process


def customize_HLT_trkIter2GlobalPtSeed0p9ForBTag(process):
  process.hltIter2PFlowPixelTrackingRegionsGlobalPtSeed0p9ForBTag = cms.EDProducer( 'GlobalTrackingRegionWithVerticesEDProducer',
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 0.0 ),
      VertexCollection = cms.InputTag( 'hltFastPVPixelVertices' ),
      beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 0.2 ),
      sigmaZVertex = cms.double( 3.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 0.9 ),
      originRadius = cms.double( 0.3 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False )
    )
  )

  process.hltIter2PFlowPixelHitDoubletsForBTag.trackingRegions = 'hltIter2PFlowPixelTrackingRegionsGlobalPtSeed0p9ForBTag'

  process.HLTIterativeTrackingIteration2ForBTag.replace(
    process.hltIter2PFlowPixelTrackingRegionsForBTag,
    process.hltIter2PFlowPixelTrackingRegionsGlobalPtSeed0p9ForBTag
  )

  return process
