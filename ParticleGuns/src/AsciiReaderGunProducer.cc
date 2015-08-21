// self H
#include "MCProduction/ParticleGuns/interface/AsciiReaderGunProducer.h"

// STL
#include <ostream>

// SimDataFormatns
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"

// FWCore
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

//SimGeneral
#include "SimGeneral/HepPDTRecord/interface/ParticleDataTable.h"

// ROOT
#include "TLorentzVector.h"

// Name spaces
using namespace edm;
using namespace std;

// -- Constructor
AsciiReaderGunProducer::AsciiReaderGunProducer(const edm::ParameterSet& pset) :
	fEvt(0)
{
  edm::ParameterSet pgun_params =  pset.getParameter<edm::ParameterSet>("PGunParameters") ;
  
  fileName = pgun_params.getParameter<string>("fileName");
  
  produces<HepMCProduct>();
  produces<GenEventInfoProduct>();
  produces<GenRunInfoProduct, InRun>();

  // -- keep track of the "original informations"
  produces<unsigned int>("originalRun");
  produces<unsigned int>("originalLumi");
  produces<unsigned int>("originalEvent");

  fVerbosity = pset.getUntrackedParameter<int>( "Verbosity",0 ) ;


}

AsciiReaderGunProducer::~AsciiReaderGunProducer() {}

void AsciiReaderGunProducer::produce(edm::Event &e, const EventSetup& es) {

  if ( fVerbosity > 0 ) {
    LogDebug("AsciiReaderParticleGun") << "AsciiReaderGunProducer : Begin New Event Generation"; 
  }

  // event loop (well, another step in it...)
  // no need to clean up GenEvent memory - done in HepMCProduct
   
  // here re-create fEvt (memory)
  //
  fEvt = new HepMC::GenEvent() ;
   
  // now actualy, cook up the event from PDGTable and parameters

  // 1st, primary vertex
  HepMC::GenVertex* Vtx = new HepMC::GenVertex(HepMC::FourVector(0.,0.,0.));

  // loop over particles

  // read a valid line from the input file
  // make sure to read a line
  string token = "";
  while( token != "" and token[0] != '#' ){
 	 getline ( ascii, token);
 	 if (ascii.eof() ) {
 	   	throw cms::Exception("End Of File")
 	     	<< "Encountered End of File "<< fileName << " while processing entries"<<endl;;
 	 	}
  }
  stringstream ss(token); // convert into a stream
  
  /* line
   * run lumi event np pdgid pt eta phi 
   * 0 0 0 1  11  50. 2.3 3.1
   * 0 0 0 2  11  50. 2.2 3.1 13 52. 2.1 2.2
   */
  auto_ptr<unsigned int> originalRun   ; ss >> (*originalRun  );
  auto_ptr<unsigned int> originalLumi  ; ss >> (*originalLumi );
  auto_ptr<unsigned int> originalEvent ; ss >> (*originalEvent);

  int barcode = 1 ;
  unsigned int np =1 ; ss >> np;

  for (unsigned int ip=0; ip < np; ++ip) {
    int PartID ; ss >> PartID  ;
    double pt  ; ss >> pt;
    double eta ; ss >> eta;
    double phi ; ss >> phi;
    const HepPDT::ParticleData* PData = fPDGTable->particle(HepPDT::ParticleID(abs(PartID))) ;
    double mass   = PData->mass().value() ;

    // Translate to a TLorentzVector for the Math
    TLorentzVector lv;
    lv.SetPtEtaPhiM(pt,eta,phi,mass);
    double px     = lv.Px() ;
    double py     = lv.Py() ;
    double pz     = lv.Pz() ;
    double energy = lv.Energy() ;

    HepMC::FourVector p(px,py,pz,energy) ;
    HepMC::GenParticle* Part = new HepMC::GenParticle(p,PartID,1);

    Part->suggest_barcode( barcode ) ;
    ++barcode ;
    Vtx->add_particle_out(Part);

  }

  fEvt->add_vertex(Vtx) ;
  fEvt->set_event_number(e.id().event()) ;
  fEvt->set_signal_process_id(20) ; 
        
  if ( fVerbosity > 0 ) {
    fEvt->print() ;  
  }

  std::auto_ptr<HepMCProduct> BProduct(new HepMCProduct()) ;
  BProduct->addHepMCData( fEvt );
  e.put(BProduct);

  std::auto_ptr<GenEventInfoProduct> genEventInfo(new GenEventInfoProduct(fEvt));
  e.put(genEventInfo);

  e.put(originalRun,"originalRun");
  e.put(originalLumi,"originalLumi");
  e.put(originalEvent,"originalEvent");

  if ( fVerbosity > 0 ) {
    LogDebug("AsciiGun") << "AsciiReaderGunProducer : Event Generation Done ";
  }
}

void AsciiReaderGunProducer::beginJob()
{
	ascii.open(fileName.c_str() );
}

void AsciiReaderGunProducer::endJob()
{
	ascii.close();
}

void AsciiReaderGunProducer::beginRun(const edm::Run &r, const edm::EventSetup& es ) {
   es.getData( fPDGTable ) ;
}

void AsciiReaderGunProducer::endRun(const Run &run, const EventSetup& es ) {
}

void AsciiReaderGunProducer::endRunProduce(Run &run, const EventSetup& es )
{
   // just create an empty product
   // to keep the EventContent definitions happy
   // later on we might put the info into the run info that this is a PGun
   std::auto_ptr<GenRunInfoProduct> genRunInfo( new GenRunInfoProduct() );
   run.put( genRunInfo );
}

void AsciiReaderGunProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
