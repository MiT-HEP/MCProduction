cmsDriver.py \
	MCProduction/ParticleGuns/python/AsciiReader_cfi.py \
	--mc \
	--eventcontent AODSIM \
	--datatier AODSIM \
	--pileup 2015_25ns_Startup_PoissonOOTPU \
	--pileup_input /store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/40002/FA6ABD01-8CAF-E411-A541-001E67396D10.root,/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/40002/FA6AEBB3-74AF-E411-B863-001E67A3FE66.root,/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/40002/FAE2833C-81AF-E411-B046-B083FED76520.root,/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/40002/FAEC3E3C-94AF-E411-BE22-0CC47A0AD6AA.root,/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/40002/FCDB6A8F-88AF-E411-B36A-848F69FD2817.root,/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/40002/FCE177C6-7AAF-E411-AA9A-003048642BAD.root,/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/40002/FE0DEBA3-79AF-E411-B39B-008CFA11139C.root,/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/40002/FE156415-8CAF-E411-BFDA-0CC47A0AD6FE.root,/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/40002/FE1CA9E6-7DAF-E411-8B34-782BCB1E2A3B.root,/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/40002/FE606C9D-88AF-E411-A5A8-0025902D959A.root,/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/40002/FECD6553-6CAF-E411-BF60-7845C4FC3758.root,/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/40002/FED4CE94-0BAF-E411-9E06-003048344C28.root \
	--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
	--conditions MCRUN2_74_V9 \
	--magField 38T_PostLS1 \
	--step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:@frozen25ns,RAW2DIGI,L1Reco,RECO \
	--python_filename step12.py  \
	--no_exec \
	--fileout file:step2.root \
	-n $(cat embedding.txt | grep -v '^#' | wc -l  )


	#--pileup_input dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM \
	#--pileup_input das:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM \
