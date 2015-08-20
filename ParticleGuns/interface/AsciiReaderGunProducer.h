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

#include <memory>
#include "boost/shared_ptr.hpp"
#include <fstream>
#include <sstream>


namespace edm {
  
  class AsciiReaderGunProducer : public one::EDProducer<one::WatchRuns, EndRunProducer> {
  
  public:
    AsciiReaderGunProducer(const ParameterSet &);
    virtual ~AsciiReaderGunProducer();

    void beginRun(const edm::Run&, const edm::EventSetup&) override;
    void endRun(const edm::Run& r, const edm::EventSetup&) override;
    void endRunProduce(edm::Run& r, const edm::EventSetup&) override;
    
    //---
    void beginJob() override;
    void endJob() override;

  private:
   
    virtual void produce(Event & e, const EventSetup& es) override;
    std::ifstream ascii;
    
  protected :
  
    // data members
    
    std::string fileName ; 

    HepMC::GenEvent* fEvt;

    ESHandle<HepPDT::ParticleDataTable> fPDGTable ;

    int  fVerbosity ;
     // format in the file should be pdgid pt eta phi m

  };
} 

#endif
