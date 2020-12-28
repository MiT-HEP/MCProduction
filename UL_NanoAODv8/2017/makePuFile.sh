dasgoclient -query 'file dataset=/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL17_106X_mc2017_realistic_v6-v3/PREMIX' > pu.py
cat pu.py | sed "s:^:':" | sed "s:$:',:" | sed '1ipuListFull=[' | sed '$a]' > pu2.py
mv pu2.py pu.py
