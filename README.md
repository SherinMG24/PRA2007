Sherein Gelbert i6378000

Chemistry: Simulating molecular emissions in a combustion reaction

Questions:
1. What are the average counts of each molecular species and their statistical uncertainties?
2. Is there any asymmetry between the normal and the variant molecule?
3. Is there any asymmetry as a function of their momentum?

Input Structure:
The header contains
- event ID: ID of the experiment or simulation run
- number of molecules tracked: Total number of molecules observed in this run
Each row after the header gives:
- 3D momentum components (px, py, pz in 10-23kg m/s), 
- an integer ID representing the molecule or isotope

Molecule ID     Molecule type
211             Carbon monoxide
-211            Carbon-13 monoxide
321             Nitric oxide
-321            Ionised NO
2212            Water
-2212           Heavy water (D2O)
3122            Methane (CH4)
-3122           Methyl ion (CH3-)
3312            Ethylene (C2H4)
-3312           Ionised ethylene (C2H3-)
3334            Ozone (O3)
-3334           Superoxide anion (O2-)

Requirements:
1. install python and VisualStudio
2. install numpy
3. install matplotlibary

