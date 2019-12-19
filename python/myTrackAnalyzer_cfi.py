import FWCore.ParameterSet.Config as cms

myTrackAnalyzer = cms.EDAnalyzer("MyTrackAnalyzer",
    tracks = cms.InputTag('generalTracks'),
)
