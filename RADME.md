This is simple python script for energy and sensitivity calibration of radiacode devices (can be used for any spectrometer).

usage:

0) set sensitivity_calibration in the code to "False"
1) open your spectrum file of known isotopes in software like InterSpec and identify main peaks. 
2) type channel number (before calibration appears as energy in InterSpec) and real energies specific for each isotope in energy_channels table in the code. In this step multiple isotops of unknown activities can be used.

3) launch the code with input .csv spectrum file name as parameter
4) energy calibrated spectrum is exported as "processed.csv"
5) now you have energy calibrated spectrum ready to be viewed in e.g. InterSpec

6) if you want sensitivity calibration you will need spectrum of sample with known ratios between isotopes (in this step it is critical to not have unknown mix)
7) process the spectrum by the python script as before and open it in InterSpec
8) compute peaks area
9) type mean energy and peak area in area_data table in the script (if you are not using natural uranium ore as sample you will need to adjust emission probalitity of each energy, [keep in mind that this is not activity because diffecent isotopes can emmit different energies])
10) set sensitivity_calibration to "True"
11) process your unprocessed spectrum as before
12) now you have energy and sensitity calibrated spectrum
