//
// Package:    MCProduction/AsciiReaderInfo
// Class:      AsciiReaderInfo
// 
// Original Author:  Andrea Carlo Marini
//         Created:  Fri, 21 Aug 2015 07:26:35 GMT
//


// system include files
#include <memory>
#include <string>
#include <fstream>
#include <sstream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"


//
// class declaration
//

class AsciiReaderInfo : public edm::EDProducer {
   public:
      explicit AsciiReaderInfo(const edm::ParameterSet&);
      ~AsciiReaderInfo(){}

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() override;
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      
      // ----------member data ---------------------------
      int fVerbosity;
      std::string fileName;
      std::ifstream ascii;


};

