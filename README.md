Sherin Gelbert i6378000

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
3. install matplot library
4. download the code

The code is divided into smaller codes.
week2.py -> calculates the total momentum of each appended molecule
week3.py --> calculates the average count of one molecule for one file
week4.2.py --> calculates for all 10 files the average count, standard deviation and skewness of each molecule 
week4.3.py --> takes the average count and standard deviation form the week4.2.py code and calculates the statistical uncertainty with a sigma 3 trash hold & compares the two paired up molecules (211 & -211 , 321 & -321, ...)  for significants 
week5.2.py --> calculates the momentum of each molecule and then calculates the weighted average and difference between the molecule pairs and plots the difference in distribution as a function of momentum

1. Question :
ID : (average , standard deviation)

211: (19.949512337472093, 0.03106576179376466),   
-211: ( 19.917215586208876, 0.030237707990851567), 
321: (2.509148587261694 ,0.00452871814381463),
-321: (2.503457511371118 ,0.005221255159721487),
2212: (1.2080342879254498, 0.0017990168407428311),
-2212: (1.1841612630913216, 0.0022883792488439174),
3122: (0.27659863110414984, 0.0010192634693903732),
-3122: (0.2716960275676958 ,0.00093481236740067559),
3312: (0.03944121369079915 ,0.0002691186769131287),
-3312: (0.039000539692252666,0.00038182902623205926),
3334: (0.001187098532890652, 3.953746458174925e-05),
-3334: (0.0011515851608191005, 4.818729437508508e-05)

2. Question :

To calculate the significants, the difference between the means was calculated.
And the difference between the uncertainty using the formular:
A) sigma_difference = math.sqrt(sigma1**2 + sigma2**2)
B) sigma_difference2 = math.sqrt(abs(sigma1**2 - sigma2**2))

And then it was calcuated, how many sigma_difference were subtarcted from the difference of the mean until it reached zero.

A) 211 vs -211: Number of sigma: 1 --> They are statistically consistant.
B) 211 vs -211: Number of sigma: 0 --> They are statistically consistant.

Overall it can be said, taht this pair is statistically consitsnat as both calculations give the same answer.

A) 321 vs -321: Number of sigma: 1 --> They are statistically consistant.
B) 321 vs -321: Number of sigma: 0 --> They are statistically consistant.

This can also be seen in the pair of 321 and -321.

A) 2212 vs -2212: Number of sigma: 9 --> They are not statistically consistant
B) 2212 vs -2212: Number of sigma: 0 --> They are statistically consistant.

For this pair it is harder to give a defined answer, as the first calculations showes a sigma of 9, this indicateds its rather not statistically significant.

A) 3122 vs -3122: Number of sigma: 4 --> They are not statistically consistant
B) 3122 vs -3122: Number of sigma: 0 --> They are statistically consistant.

For this pair also one calculation showesm, that it is not statistically consistant, hwoever it is closer to 3 than the other pair, so one could say that it is still signifcantly consistant.

A) 3312 vs -3312: Number of sigma: 1 --> They are statistically consistant.
B) 3312 vs -3312: Number of sigma: 0 --> They are statistically consistant.

the pair is staitistically consistant.

A) 3334 vs -3334: Number of sigma: 1 --> They are statistically consistant.
B) 3334 vs -3334: Number of sigma: 0 --> They are statistically consistant.

the pair is statistically signifcant. 


Lastly I took the difference between the two averges and calculated the weighted avergae difference (Diff) and its uncertainty. 

for p1, p2 in pairs:
    mean1, err1 = data[p1]
    mean2, err2 = data[p2]
    
    diff = mean1 - mean2
    err_diff = (err1**2 + err2**2)**0.5
    
    w = 1.0 / (err_diff**2)
    sum_w_diff += w * diff
    sum_w += w
    
    results.append((p1, p2, diff, err_diff))

weighted_avg_diff = sum_w_diff / sum_w
weighted_err_diff = 1.0 / (sum_w**0.5)

--> meaning : 
1.calculated the difference between two measurements
2.calculated the uncertainties, assuming the two measurements are independent
3.calculated the inverse-variance weight
4.calculated the weighted average difference
5.calculated the uncertainty of the weighted average

these are my results : 

Pair (211, -211): Diff = 0.0322968 ± 0.0433521
Pair (321, -321): Diff = 0.0056911 ± 0.0069116
Pair (2212, -2212): Diff = 0.0238730 ± 0.0029109
Pair (3122, -3122): Diff = 0.0049026 ± 0.0013830
Pair (3312, -3312): Diff = 0.0004407 ± 0.0004671
Pair (3334, -3334): Diff = 0.0000355 ± 0.0000623

3. Question :

my calculations looked like this:

for x, y, z, particle_id in data:

        momentum = math.sqrt(x**2 + y**2 + z**2)

        if particle_id == 3122:     #change the ID to the one that gets analysed 
            momenta_ID1.append(momentum)

        elif particle_id == -3122:   #change ID to match the first one
            momenta_ID2.append(momentum)

    # Histogram using the same bins
    counts_ID1, _ = np.histogram(momenta_ID1, bins=bins)
    counts_ID2, _ = np.histogram(momenta_ID2, bins=bins)

    # Normalize each distribution by the total number of particles
    if len(momenta_ID1) > 0:
        counts_ID1 = counts_ID1 / len(momenta_ID1)
    else:
        counts_ID1 = np.full(len(bins) - 1, np.nan)

    if len(momenta_ID2) > 0:
        counts_ID2 = counts_ID2 / len(momenta_ID2)
    else:
        counts_ID2 = np.full(len(bins) - 1, np.nan)

    # Difference between normalized distributions
    difference = counts_ID1 - counts_ID2

    all_differences.append(difference)


# Convert to NumPy array
all_differences = np.array(all_differences)

# Calculate mean and spread in each momentum bin
mean_difference = np.nanmean(all_differences, axis=0)
std_difference = np.nanstd(all_differences, axis=0, ddof=1)

To answer the question, I analysed the plots (see graphs "Difference between momentum distributions of ID1 and ID2"). If the error bar *3 crossed the zero line, then plot showed no asymmetry between the molecules.

