import FWCore.ParameterSet.Config as cms
from RecoBTag.PerformanceMeasurements.bTagAnalyzerCommon_cff import *
from RecoBTag.PerformanceMeasurements.variables_cfi import *
from RecoBTag.PerformanceMeasurements.varGroups_cfi import *
bTagAnalyzer = cms.EDAnalyzer("BTagAnalyzer",
    bTagAnalyzerCommon,
    variableSet,
    groupSet,
    # computers
    svComputer = cms.string('candidateCombinedSecondaryVertexV2Computer'),
    svComputerSubJets = cms.string('candidateCombinedSecondaryVertexV2Computer'),
    slComputer = cms.string('candidateCombinedSecondaryVertexSoftLeptonComputer'),
    # TagInfos (need to omit the 'TagInfos' part from the label)
    deepFlavourTagInfos = cms.string('pfDeepFlavour'),
    deepDoubleXTagInfos = cms.string('pfDeepDoubleX'),
    deepBoostedJetTagInfos = cms.string('pfDeepBoostedJet'),
    ipTagInfos = cms.string('pfImpactParameter'),
    svTagInfos = cms.string('pfInclusiveSecondaryVertexFinder'),
    svNegTagInfos = cms.string('pfInclusiveSecondaryVertexFinderNegative'),
    softPFMuonTagInfos = cms.string('softPFMuons'),
    softPFElectronTagInfos = cms.string('softPFElectrons'),
    bdsvTagInfos = cms.string('pfBoostedDoubleSVAK8'),
    ipTagInfosCTag = cms.string('pfImpactParameter'),
    svTagInfosCTag = cms.string('pfInclusiveSecondaryVertexFinderCvsL'),
    svNegTagInfosCTag = cms.string('pfInclusiveSecondaryVertexFinderNegativeCvsLTagInfos'),
    softPFMuonTagInfosCTag = cms.string('softPFMuons'),
    softPFElectronTagInfosCTag = cms.string('softPFElectrons'),
    # taggers
    deepFlavourJetTags = cms.string('pfDeepFlavourJetTags'),
    deepFlavourNegJetTags = cms.string('pfNegativeDeepFlavourJetTags'),
    deepCSVBJetTags    = cms.string('pfDeepCSVJetTags'),
    deepCSVNegBJetTags = cms.string('pfNegativeDeepCSVJetTags'),
    deepCSVPosBJetTags = cms.string('pfPositiveDeepCSVJetTags'),
    trackCHEBJetTags = cms.string('pfTrackCountingHighEffBJetTags'),
    trackCNegHEBJetTags = cms.string('pfNegativeTrackCountingHighEffBJetTags'),
    trackCHPBJetTags = cms.string('pfTrackCountingHighPurBJetTags'),
    trackCNegHPBJetTags = cms.string('pfNegativeTrackCountingHighPurBJetTags'),
    jetBPBJetTags = cms.string('pfJetBProbabilityBJetTags'),
    jetBPNegBJetTags = cms.string('pfNegativeOnlyJetBProbabilityBJetTags'),
    jetBPPosBJetTags = cms.string('pfPositiveOnlyJetBProbabilityBJetTags'),
    jetPBJetTags = cms.string('pfJetProbabilityBJetTags'),
    jetPNegBJetTags = cms.string('pfNegativeOnlyJetProbabilityBJetTags'),
    jetPPosBJetTags = cms.string('pfPositiveOnlyJetProbabilityBJetTags'),
    simpleSVHighPurBJetTags = cms.string('pfSimpleSecondaryVertexHighPurBJetTags'),
    simpleSVNegHighPurBJetTags = cms.string('pfNegativeSimpleSecondaryVertexHighPurBJetTags'),
    simpleSVHighEffBJetTags = cms.string('pfSimpleSecondaryVertexHighEffBJetTags'),
    simpleSVNegHighEffBJetTags = cms.string('pfNegativeSimpleSecondaryVertexHighEffBJetTags'),
    combinedSVBJetTags = cms.string('pfCombinedSecondaryVertexV2BJetTags'),
    combinedSVPosBJetTags = cms.string('pfPositiveCombinedSecondaryVertexV2BJetTags'),
    combinedSVNegBJetTags = cms.string('pfNegativeCombinedSecondaryVertexV2BJetTags'),
    combinedIVFSVBJetTags = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    combinedIVFSVPosBJetTags = cms.string('pfPositiveCombinedInclusiveSecondaryVertexV2BJetTags'),
    combinedIVFSVNegBJetTags = cms.string('pfNegativeCombinedInclusiveSecondaryVertexV2BJetTags'),
    softPFMuonBJetTags = cms.string('softPFMuonBJetTags'),
    softPFMuonNegBJetTags = cms.string('negativeSoftPFMuonBJetTags'),
    softPFMuonPosBJetTags = cms.string('positiveSoftPFMuonBJetTags'),
    softPFElectronBJetTags = cms.string('softPFElectronBJetTags'),
    softPFElectronNegBJetTags = cms.string('negativeSoftPFElectronBJetTags'),
    softPFElectronPosBJetTags = cms.string('positiveSoftPFElectronBJetTags'),
    doubleSVBJetTags = cms.string('pfBoostedDoubleSecondaryVertexAK8BJetTags'),
    deepDoubleXJetTags = cms.string('pfDeepDouble'),
    massIndDeepDoubleXJetTags = cms.string('pfMassIndependentDeepDouble'),
    deepBoostedJetTags = cms.string('pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags'),
    cMVABJetTags = cms.string('pfCombinedMVABJetTags'),
    cMVAv2BJetTags = cms.string('pfCombinedMVAV2BJetTags'),
    cMVAv2NegBJetTags = cms.string('pfNegativeCombinedMVAV2BJetTags'),
    cMVAv2PosBJetTags = cms.string('pfPositiveCombinedMVAV2BJetTags'),
    CvsBCJetTags = cms.string('pfCombinedCvsBJetTags'),
    CvsBNegCJetTags = cms.string('pfNegativeCombinedCvsBJetTags'),
    CvsBPosCJetTags = cms.string('pfPositiveCombinedCvsBJetTags'),
    CvsLCJetTags = cms.string('pfCombinedCvsLJetTags'),
    CvsLNegCJetTags = cms.string('pfNegativeCombinedCvsLJetTags'),
    CvsLPosCJetTags = cms.string('pfPositiveCombinedCvsLJetTags')
)
