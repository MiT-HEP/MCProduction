#ifndef AsciiReaderGunProducer_H
#define AsciiReaderGunProducer_H

#include <string>
#include "HepPDT/defs.h"
#include "HepPDT/TableBuilder.hh"
#include "HepPDT/ParticleDataTable.hh"

#include "HepMC/GenEvent.h"

#include "FWCore/Framework/interface/one/EDProducer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include <memory>
#include "boost/shared_ptr.hpp"
#include <fstream>
#include <sstream>

#include "GeneratorInterface/Pythia8Interface/interface/Py8GunBase.h"
#include "GeneratorInterface/Core/interface/GeneratorFilter.h"
#include "GeneratorInterface/ExternalDecays/interface/ExternalDecayDriver.h"

namespace gen {

  class AsciiReaderGunProducer : public Py8GunBase {
//public one::EDProducer<one::WatchRuns, EndRunProducer> {
  
  public:
    AsciiReaderGunProducer(const edm::ParameterSet &);
    virtual ~AsciiReaderGunProducer();

    bool generatePartonsAndHadronize() override;
    const char* classname() const override { return "AsciiReaderGunProducer";}


    //--- open and close the ascii file stream
    void beginJob() ;
    void endJob() ;

  private:
   
    std::ifstream ascii;
    
  protected :
  
    // data members
    
    std::string fileName ; 

    int  fVerbosity ;
     // format in the file should be pdgid pt eta phi m

  };

  
  typedef edm::GeneratorFilter<gen::AsciiReaderGunProducer, gen::ExternalDecayDriver> AsciiReaderGun;
} 

#endif
