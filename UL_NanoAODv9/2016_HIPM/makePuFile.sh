dasgoclient -query 'file dataset=/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL16_106X_mcRun2_asymptotic_v13-v1/PREMIX' > pu.py
cat pu.py | sed "s:^:':" | sed "s:$:',:" | sed '1ipuListFull=[' | sed '$a]' > pu2.py
mv pu2.py pu.py
