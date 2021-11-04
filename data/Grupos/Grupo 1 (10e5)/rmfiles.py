import os

def rmfiles(folder):
	data_f = os.listdir(folder)
	for fol in data_f:
		folders = os.path.join(folder, fol)
		files = os.listdir(folders)
		no_rm = ['Nmass.txt', 'OrbitalElements0001.txt', 'OrbitalElements0999.txt', 
		'OrbitalElements1000.txt', 'PltAllGraph0001.txt', 'PltAllGraph1000.txt', 'Parameters.txt']
		for f in files:
			if f in no_rm:
				continue
			
			os.remove(os.path.join(folder, fol, f))


f1 = 'Distance (AU)'
f2 = 'Eccentricity'
f3 = 'Mass (M_earth)'

rmfiles(f1)
rmfiles(f2)
rmfiles(f3)