import numpy as np
import sys

# VALUES IN THIS AREA SHOULD BE EDITED ACCORDING TO THE DETECTOR
sensitivity_calibration = True
last_value_zero = True # replace last value with zero (last value is usually high which prevents it from displaing corectly in linear scale)
ec = 3 #energy calibration polymon degree
sc = 4 #sensitivity calibration polynom degree

energy_channels = [
	#energy in kEV; channel on detector
	[26, 6.9], #241Am
	[60, 25], #241Am
	[186, 76], #226Ra
	[242, 98], #214Pb
	[295, 119], #214Pb
	[352, 142], #214Pb
	[609, 242], #214Bi
	[1120, 433], #214Bi
	[1461, 553], #40K
	[1765, 661], #214Bi
	[2204, 805], #214Bi
	[2614, 945], #208Tl 
]

area_data = [
	#peak mean energy; emission probability; peak area; sensitivity (computed later, should be zero now)
	[20, 0.0357, 1320000, 0], #this value is actually made up to correct low energies while there is no suitable low enegry peak at low energy
	[186, 0.0357, 631912, 0], #226Ra
	[242, 0.0726, 910879, 0], #214Pb
	[295, 0.1847, 1403782, 0], #214Pb
	[352, 0.3572, 2008639, 0], #214Pb
	[609, 0.4544, 949801, 0], #214Bi
	[1120, 0.149, 112825, 0], #214Bi
	[1765, 0.1529, 54436, 0], #214Bi
	[2204, 0.0492, 8014, 0], #214Bi
]
# END OF INPUT DATA AREA, REST OF THE CODE SHOULD NOT BE EDITED







#energy polynomial
channels = np.array([row[1] for row in energy_channels])  
energies = np.array([row[0] for row in energy_channels])  
energy_coeffs = np.polyfit(channels, energies, ec)  # polynomial fit

#sensitivity polynomial
energy = np.array([row[0] for row in area_data])  
probability = np.array([row[1] for row in area_data])
area = np.array([row[2] for row in area_data])
sensitivity = np.array([row[3] for row in area_data])
sensitivity = (probability*sum(area))/area
sensitivity_coeffs = np.polyfit(energy, sensitivity, sc)  # polynomial fit

#load spectrum as array
spectrum = np.genfromtxt(sys.argv[1], delimiter=',', dtype=float)

#energy calibration processing whole column as vector
unmodified = spectrum[:, 0]
spectrum[:, 0] = np.polyval(energy_coeffs, unmodified)

#sensitivity calibration
if sensitivity_calibration == True :
	energy_calibrated_energy = spectrum[:, 0]
	energy_calibrated_data = spectrum[:, 1]
	spectrum[:, 1] = energy_calibrated_data*np.polyval(sensitivity_coeffs, energy_calibrated_energy)
	

#replacing the last value with zero
if last_value_zero == True :
	spectrum[spectrum.shape[0]-1, 1] = 0

#saving array as csv file
np.savetxt('processed.csv', spectrum, delimiter=',')