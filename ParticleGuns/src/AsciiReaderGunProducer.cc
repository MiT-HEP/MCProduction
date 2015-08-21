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
using namespace gen;

// -- Constructor
AsciiReaderGunProducer::AsciiReaderGunProducer(const edm::ParameterSet& pset) :
	Py8GunBase(pset)
{
  edm::ParameterSet pgun_params =  pset.getParameter<edm::ParameterSet>("PGunParameters") ;

  fileName = pgun_params.getParameter<string>("fileName");
  
  // -- keep track of the "original informations"

  fVerbosity = pset.getUntrackedParameter<int>( "Verbosity",0 ) ;
  // after configuration
  beginJob();

}

AsciiReaderGunProducer::~AsciiReaderGunProducer() {
  endJob();
}


bool AsciiReaderGunProducer::generatePartonsAndHadronize()
{
  fMasterGen->event.reset();

  // event loop (well, another step in it...)
  // no need to clean up GenEvent memory - done in HepMCProduct
   
  // here re-create fEvt (memory)
  //
  //fEvt = new HepMC::GenEvent() ;
   
  // now actualy, cook up the event from PDGTable and parameters

  // 1st, primary vertex
  //HepMC::GenVertex* Vtx = new HepMC::GenVertex(HepMC::FourVector(0.,0.,0.));

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

  int barcode = 1 ;
  unsigned int np =1 ; ss >> np;

  for (unsigned int ip=0; ip < np; ++ip) {
    int particleID ; ss >> particleID  ;
    double pt  ; ss >> pt;
    double eta ; ss >> eta;
    double phi ; ss >> phi;
    double mass = (fMasterGen->particleData).m0( particleID );

    // Translate to a TLorentzVector for the Math
    TLorentzVector lv;
    lv.SetPtEtaPhiM(pt,eta,phi,mass);
    double px     = lv.Px() ;
    double py     = lv.Py() ;
    double pz     = lv.Pz() ;
    double ee     = lv.Energy() ;

    if( 1<= fabs(particleID) && fabs(particleID) <= 6) // quarks
	(fMasterGen->event).append( particleID, 23, 101, 0, px, py, pz, ee, mass ); 
    else if (fabs(particleID) == 21)                   // gluons
	(fMasterGen->event).append( 21, 23, 101, 102, px, py, pz, ee, mass );
    else                                               // other
	(fMasterGen->event).append( particleID, 1, 0, 0, px, py, pz, ee, mass ); 

    ++barcode ;

  }

   if ( !fMasterGen->next() ) return false;

   event().reset(new HepMC::GenEvent);
   return toHepMC.fill_next_event( fMasterGen->event, event().get() );

}

void AsciiReaderGunProducer::beginJob()
{
	ascii.open(fileName.c_str() );
}

void AsciiReaderGunProducer::endJob()
{
	ascii.close();
}


