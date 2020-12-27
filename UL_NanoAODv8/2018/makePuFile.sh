dasgoclient -query 'file dataset=/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL18_106X_upgrade2018_realistic_v11_L1v1-v2/PREMIX' > pu.py
cat pu.py | sed "s:^:':" | sed "s:$:',:" | sed '1ipuListFull=[' | sed '$a]' > pu2.py
mv pu2.py pu.py
