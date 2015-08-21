#include "FWCore/Framework/interface/MakerMacros.h"

#include "MCProduction/ParticleGuns/interface/AsciiReaderGunProducer.h"

// define modules
using gen::AsciiReaderGun;
DEFINE_FWK_MODULE(AsciiReaderGun);


#include "MCProduction/ParticleGuns/interface/AsciiReaderInfo.h"
DEFINE_FWK_MODULE(AsciiReaderInfo);
