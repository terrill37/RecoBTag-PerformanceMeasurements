// -*- C++ -*-
//
// Package:    MyTrackAnalyzer
// Class:      MyTrackAnalyzer
//
/**\class MyTrackAnalyzer MyTrackAnalyzer.cc RecoBTag/PerformanceMeasurements/plugins/MyTrackAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

#include "TH1D.h"

#include <DataFormats/TrackReco/interface/Track.h>

//
// class declaration
//

// FWK
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

// Formats
#include "DataFormats/Common/interface/Handle.h"

using namespace edm;
using namespace reco;
using namespace std;

class MyTrackAnalyzer : public edm::EDAnalyzer {
   public:
      explicit MyTrackAnalyzer(const edm::ParameterSet&);
      ~MyTrackAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------
      edm::Service<TFileService> fs;
      edm::EDGetTokenT<std::vector<reco::Track>> inputTracksToken_;

      TH1D *hTrackPt_outer;
      TH1D *hTrackEta_outer;
      TH1D *hTrackPhi_outer;
      TH1D *hTrackPt;
      TH1D *hTrackEta;
      TH1D *hTrackPhi;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
MyTrackAnalyzer::MyTrackAnalyzer(const edm::ParameterSet& iConfig):
inputTracksToken_(consumes<std::vector<reco::Track>>(iConfig.getParameter<edm::InputTag>("tracks")))
{
   hTrackEta_outer = fs->make<TH1D>("hTrackEta_outer","Track Eta_outer", 500, -5., 5.);
   hTrackPt_outer = fs->make<TH1D>("hTrackPt_outer","Track Pt_outer", 500, 0, 5.);
   hTrackPhi_outer = fs->make<TH1D>("hTrackPhi_outer","Track Phi_outer", 600, -3., 3.);
   hTrackEta = fs->make<TH1D>("hTrackEta","Track Eta", 500, -5., 5.);
   hTrackPt = fs->make<TH1D>("hTrackPt","Track Pt", 500, 0, 5.);
   hTrackPhi = fs->make<TH1D>("hTrackPhi","Track Phi", 600, -3., 3.);
}


MyTrackAnalyzer::~MyTrackAnalyzer()
{
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
}


//
// member functions
//

// ------------ method called for each event  ------------
void
MyTrackAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    edm::Handle<std::vector<reco::Track>> tracks;
    iEvent.getByToken(inputTracksToken_, tracks);
    for(std::vector<reco::Track>::const_iterator i_track = tracks->begin(); i_track != tracks->end(); ++i_track){
        hTrackEta_outer->Fill(i_track->outerEta());
        hTrackPt_outer->Fill(i_track->outerPt());
        hTrackPhi_outer->Fill(i_track->outerPhi());
        hTrackEta->Fill(i_track->eta());
        hTrackPt->Fill(i_track->pt());
        hTrackPhi->Fill(i_track->phi());
    }
}


// ------------ method called once each job just before starting event loop  ------------
void
MyTrackAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
MyTrackAnalyzer::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void
MyTrackAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
MyTrackAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
MyTrackAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
MyTrackAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MyTrackAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(MyTrackAnalyzer);
