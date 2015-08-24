#include "MCProduction/ParticleGuns/interface/AsciiReaderInfo.h"
#include <iostream>

using namespace edm;
using namespace std;

AsciiReaderInfo::AsciiReaderInfo(const edm::ParameterSet& iConfig)
{

 
   //now do what ever other initialization is needed
   fVerbosity = iConfig.getUntrackedParameter<int>( "Verbosity",0 ) ;
   fileName   = iConfig.getUntrackedParameter<string>( "fileName" ) ;


   //register your products
   //if do put with a label
   produces<uint32_t>("originalRun");
   produces<uint32_t>("originalLumi");
   produces<uint32_t>("originalEvent");
  
}


// ------------ method called to produce the data  ------------
void
AsciiReaderInfo::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   //Use the ExampleData to create an ExampleData2 which 
   // is put into the Event

   string token = "";
   if ( fVerbosity >1) cout <<"[AsciiReader]::[DEBUG] token line: '"<<token<<"'"<<endl;

   while( token == "" or token[0] == '#' ){
          if (ascii.eof() ) {
            	throw cms::Exception("End Of File")
              	<< "Encountered End of File "<< fileName << " while processing entries"<<endl;;
          	}
          getline ( ascii, token);
   	if ( fVerbosity >1) cout <<"[AsciiReader]::[DEBUG] token line: '"<<token<<"'"<<endl;
   }
   stringstream ss(token); // convert into a stream

  int runNum  ; ss >> runNum  ;
  int lumiNum ; ss >> lumiNum ;
  int eventNum; ss >> eventNum;
 
   std::unique_ptr<uint32_t> runNumPtr(new uint32_t);
   std::unique_ptr<uint32_t> lumiNumPtr(new uint32_t);
   std::unique_ptr<uint32_t> eventNumPtr(new uint32_t);

   *runNumPtr  = runNum;
   *lumiNumPtr =lumiNum;
   *eventNumPtr=eventNum;

   iEvent.put(std::move(runNumPtr),"originalRun");
   iEvent.put(std::move(lumiNumPtr),"originalLumi");
   iEvent.put(std::move(eventNumPtr),"originalEvent");
}

// ------------ method called once each job just before starting event loop  ------------
void 
AsciiReaderInfo::beginJob()
{
	if (fVerbosity > 0 ){
		cout <<"[AsciiReaderInfo]::[beginJob] Opening file: "<<fileName<<endl;
	}
	ascii.open(fileName.c_str() );
}

// ------------ method called once each job just after ending the event loop  ------------
void 
AsciiReaderInfo::endJob() {
	if (fVerbosity >0 ){
		cout <<"[AsciiReaderInfo]::[endJob] Closing file: "<<fileName<<endl;
	}
	ascii.close();
}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
AsciiReaderInfo::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

