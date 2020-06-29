import FWCore.ParameterSet.Config as cms

def customize_HLT_trkIter2GlobalPtSeedXX(process,ptVal=0.9):

  ptStr = str(ptVal).replace(".","p")

  setattr(process,"hltIter2PFlowPixelTrackingRegionsGlobalPtSeed"+ptStr,
          cms.EDProducer( 'GlobalTrackingRegionWithVerticesEDProducer',
                          RegionPSet = cms.PSet( 
                            useFixedError = cms.bool( True ),
                            nSigmaZ = cms.double( 4.0 ),
                            VertexCollection = cms.InputTag( 'hltTrimmedPixelVertices' ),
                            beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
                            useFoundVertices = cms.bool( True ),
                            fixedError = cms.double( 0.2 ),
                            sigmaZVertex = cms.double( 3.0 ),
                            useFakeVertices = cms.bool( False ),
                            ptMin = cms.double( ptVal ),
                            originRadius = cms.double( 0.05 ),
                            precise = cms.bool( True ),
                            useMultipleScattering = cms.bool( False )
                          )
                        )
        )
          
  process.hltIter2PFlowPixelHitDoublets.trackingRegions = 'hltIter2PFlowPixelTrackingRegionsGlobalPtSeed'+ptStr

  process.HLTIterativeTrackingIteration2.replace(
    process.hltIter2PFlowPixelTrackingRegions,
    getattr(process,"hltIter2PFlowPixelTrackingRegionsGlobalPtSeed"+ptStr)
  )

  return process


def customize_HLT_trkIter2GlobalPtSeedXXForBTag(process,ptVal=0.9):

  ptStr = str(ptVal).replace(".","p")
  
  setattr(process,"hltIter2PFlowPixelTrackingRegionsGlobalPtSeed"+ptStr+"ForBTag",
          cms.EDProducer( 'GlobalTrackingRegionWithVerticesEDProducer',
                          RegionPSet = cms.PSet( 
                            useFixedError = cms.bool( True ),
                            nSigmaZ = cms.double( 0.0 ),
                            VertexCollection = cms.InputTag( 'hltFastPVPixelVertices' ),
                            beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
                            useFoundVertices = cms.bool( True ),
                            fixedError = cms.double( 0.2 ),
                            sigmaZVertex = cms.double( 3.0 ),
                            useFakeVertices = cms.bool( False ),
                            ptMin = cms.double( ptVal ),
                            originRadius = cms.double( 0.3 ),
                            precise = cms.bool( True ),
                            useMultipleScattering = cms.bool( False )
                          )
                        )
        )

  process.hltIter2PFlowPixelHitDoubletsForBTag.trackingRegions = 'hltIter2PFlowPixelTrackingRegionsGlobalPtSeed'+ptStr+'ForBTag'

  process.HLTIterativeTrackingIteration2ForBTag.replace(
    process.hltIter2PFlowPixelTrackingRegionsForBTag,
    getattr(process,"hltIter2PFlowPixelTrackingRegionsGlobalPtSeed"+ptStr+"ForBTag")
  )

  return process


def customize_HLTDeepCSVPF(process,ptVal=0.9):

  ptStr = str(ptVal).replace(".","p")

  setattr(process,"hltDeepBLifetimeTagInfosPFPtCut"+ptStr,
          cms.EDProducer("CandIPProducer",
                         candidates = cms.InputTag("hltParticleFlow"),
                         computeGhostTrack = cms.bool(True),
                         computeProbabilities = cms.bool(True),
                         ghostTrackPriorDeltaR = cms.double(0.03),
                         jetDirectionUsingGhostTrack = cms.bool(False),
                         jetDirectionUsingTracks = cms.bool(False),
                         jets = cms.InputTag("hltPFJetForBtag"),
                         maxDeltaR = cms.double(0.4),
                         maximumChiSquared = cms.double(5.0),
                         maximumLongitudinalImpactParameter = cms.double(17.0),
                         maximumTransverseImpactParameter = cms.double(0.2),
                         minimumNumberOfHits = cms.int32(3),
                         minimumNumberOfPixelHits = cms.int32(2),
                         minimumTransverseMomentum = cms.double(ptVal),
                         primaryVertex = cms.InputTag("hltVerticesPFFilter"),
                         useTrackQuality = cms.bool(False)
                       )
        )

  process.hltDeepSecondaryVertexTagInfosPF.trackIPTagInfos = "hltDeepBLifetimeTagInfosPFPtCut"+ptStr 

  process.HLTBtagDeepCSVSequencePF.replace(
    process.hltDeepBLifetimeTagInfosPF,
    getattr(process,"hltDeepBLifetimeTagInfosPFPtCut"+ptStr)
  )


  setattr(process,"hltDeepInclusiveVertexFinderPFPtCut"+ptStr,    
          cms.EDProducer("InclusiveCandidateVertexFinder",
                         beamSpot = cms.InputTag("hltOnlineBeamSpot"),
                         clusterizer = cms.PSet(
                           clusterMaxDistance = cms.double(0.05),
                           clusterMaxSignificance = cms.double(4.5),
                           clusterMinAngleCosine = cms.double(0.5),
                           distanceRatio = cms.double(20.0),
                           seedMax3DIPSignificance = cms.double(9999.0),
                           seedMax3DIPValue = cms.double(9999.0),
                           seedMin3DIPSignificance = cms.double(1.2),
                           seedMin3DIPValue = cms.double(0.005)
                         ),
                         fitterRatio = cms.double(0.25),
                         fitterSigmacut = cms.double(3.0),
                         fitterTini = cms.double(256.0),
                         maxNTracks = cms.uint32(30),
                         maximumLongitudinalImpactParameter = cms.double(0.3),
                         maximumTimeSignificance = cms.double(3.0),
                         minHits = cms.uint32(8),
                         minPt = cms.double( ptVal ),
                         primaryVertices = cms.InputTag("hltVerticesPFFilter"),
                         tracks = cms.InputTag("hltParticleFlow"),
                         useDirectVertexFitter = cms.bool(True),
                         useVertexReco = cms.bool(True),
                         vertexMinAngleCosine = cms.double(0.95),
                         vertexMinDLen2DSig = cms.double(2.5),
                         vertexMinDLenSig = cms.double(0.5),
                         vertexReco = cms.PSet(
                           finder = cms.string('avr'),
                           primcut = cms.double(1.0),
                           seccut = cms.double(3.0),
                           smoothing = cms.bool(True)
                         )
                       )
  )

  process.hltDeepInclusiveSecondaryVerticesPF.secondaryVertices = "hltDeepInclusiveVertexFinderPFPtCut"+ptStr

  process.HLTBtagDeepCSVSequencePF.replace(
    process.hltDeepInclusiveVertexFinderPF,
    getattr(process,"hltDeepInclusiveVertexFinderPFPtCut"+ptStr)
  )


  return process


def customize_CaloJet(process,ptVal=0.9): #FIXME

  ptStr = str(ptVal).replace(".","p")

  setattr(process,"hltDeepCombinedSecondaryVertexBJetTagsInfosCalo"+ptStr,
         cms.EDProducer("TrackDeepNNTagInfoProducer",
                        computer = cms.PSet(
                            SoftLeptonFlip = cms.bool(False),
                            charmCut = cms.double(1.5),
                            correctVertexMass = cms.bool(True),
                            minimumTrackWeight = cms.double(0.5), 
                            pseudoMultiplicityMin = cms.uint32(2),
                            pseudoVertexV0Filter = cms.PSet(
                                k0sMassWindow = cms.double(0.05)
                            ),
                            trackFlip = cms.bool(False),
                            trackMultiplicityMin = cms.uint32(2), 
                            trackPairV0Filter = cms.PSet(
                                k0sMassWindow = cms.double(0.03) 
                            ), 
                            trackPseudoSelection = cms.PSet(
                                     a_dR = cms.double(-0.001053),
                                     a_pT = cms.double(0.005263),
                                     b_dR = cms.double(0.6263),
                                     b_pT = cms.double(0.3684),
                                     jetDeltaRMax = cms.double(0.3),
                                     maxDecayLen = cms.double(5.0),
                                     maxDistToAxis = cms.double(0.07),
                                     max_pT = cms.double(500.0),
                                     max_pT_dRcut = cms.double(0.1),
                                     max_pT_trackPTcut = cms.double(3.0),
                                     min_pT = cms.double(120.0),
                                     min_pT_dRcut = cms.double(0.5),
                                     normChi2Max = cms.double(99999.9),
                                     pixelHitsMin = cms.uint32(0),
                                     ptMin = cms.double(0.0),
                                     qualityClass = cms.string('any'),
                                     sip2dSigMax = cms.double(99999.9),
                                     sip2dSigMin = cms.double(2.0),
                                     sip2dValMax = cms.double(99999.9),
                                     sip2dValMin = cms.double(-99999.9),
                                     sip3dSigMax = cms.double(99999.9),
                                     sip3dSigMin = cms.double(-99999.9),
                                     sip3dValMax = cms.double(99999.9),
                                     sip3dValMin = cms.double(-99999.9),
                                     totalHitsMin = cms.uint32(0),
                                     useVariableJTA = cms.bool(False)
                            ),
                            trackSelection = cms.PSet(
                                     a_dR = cms.double(-0.001053),
                                     a_pT = cms.double(0.005263),
                                     b_dR = cms.double(0.6263),
                                     b_pT = cms.double(0.3684),
                                     jetDeltaRMax = cms.double(0.3),
                                     maxDecayLen = cms.double(5.0),
                                     maxDistToAxis = cms.double(0.07),
                                     max_pT = cms.double(500.0),
                                     max_pT_dRcut = cms.double(0.1),
                                     max_pT_trackPTcut = cms.double(3.0),
                                     min_pT = cms.double(120.0),
                                     min_pT_dRcut = cms.double(0.5),
                                     normChi2Max = cms.double(99999.9),
                                     pixelHitsMin = cms.uint32(0),
                                     ptMin = cms.double(0.0),
                                     qualityClass = cms.string('any'),
                                     sip2dSigMax = cms.double(99999.9),
                                     sip2dSigMin = cms.double(-99999.9),
                                     sip2dValMax = cms.double(99999.9),
                                     sip2dValMin = cms.double(-99999.9),
                                     sip3dSigMax = cms.double(99999.9),
                                     sip3dSigMin = cms.double(-99999.9),
                                     sip3dValMax = cms.double(99999.9),
                                     sip3dValMin = cms.double(-99999.9),
                                     totalHitsMin = cms.uint32(0),
                                     useVariableJTA = cms.bool(False)
                            ),
                            trackSort = cms.string('sip2dSig'),
                                     useTrackWeights = cms.bool(True),
                                     vertexFlip = cms.bool(False)
                        ),
                        svTagInfos=cms.InputTag("hltInclusiveSecondaryVertexFinderTagInfos")
          )
        )
    
  process.hltDeepCombinedSecondaryVertexBJetTagsCalo.src = "hltDeepCombinedSecondaryVertexBJetTagsInfosCalo"+ptStr 

  process.HLTBtagDeepCSVSequenceL3.replace(
    process.hltDeepCombinedSecondaryVertexBJetTagsInfosCalo,
    getattr(process,"hltDeepCombinedSecondaryVertexBJetTagsInfosCalo"+ptStr)
 )
   

  return process



