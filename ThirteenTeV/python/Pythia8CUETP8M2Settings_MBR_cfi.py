import FWCore.ParameterSet.Config as cms

pythia8CUETP8M2MBRSettingsBlock = cms.PSet(
    pythia8CUETP8M2MBRSettings = cms.vstring(
        'Tune:pp 14',
        'Tune:ee 7',
        'MultipartonInteractions:pT0Ref=2.331083e+00',
        'MultipartonInteractions:ecmPow=2.279277e-01',
        'MultipartonInteractions:expPow=1.692240e+00',
        'ColourReconnection:range=4.647504e+00',
        'Diffraction:PomFlux=5',
        'Diffraction:MBRepsilon = 0.08',
        'Diffraction:MBRdyminDD = 0.',
        'Diffraction:MBRdyminSigDD = 0.001',
        'Diffraction:MBRdyminDDflux = 1.35',
        'Diffraction:probMaxPert = 0.7',
        'Diffraction:pickQuarkPower = -0.15',
        'Diffraction:pickQuarkNorm = 0.65',
        'Diffraction:sigmaRefPomP = 2.115',
        'Diffraction:mRefPomP = 1.',
        'Diffraction:mPowPomP = 0.208',
        'StringPT:sigma = 0.09',
        'StringPT:enhancedFraction = 0.2',
        'StringPT:enhancedWidth = 5.0',
        )
    )
