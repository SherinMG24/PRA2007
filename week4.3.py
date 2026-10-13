import math
import numpy as np
from scipy import stats

#the data form week4.2 results
data = {
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
}
#define which apirs get comapired
pairs = [
    (211, -211),
    (321, -321),
    (2212, -2212),
    (3122, -3122),
    (3312, -3312),
    (3334, -3334)
]

SIGMA_THRESHOLD = 3


for p1, p2 in pairs:

    mean1, sigma1 = data[p1]
    mean2, sigma2 = data[p2]

    # Difference between the two measurements
    difference = abs(mean1 - mean2)

    # Uncertainty of the difference adding
    sigma_difference = math.sqrt(sigma1**2 + sigma2**2)

    # Significance, calculkate how mayn sigams until differecne is at zero
    sigma = 0

    while difference > 0:
        difference -= sigma_difference
        sigma += 1
    print(f"{p1} vs {p2}: "
          "Number of sigma:", sigma)
    if sigma <= 3:
        print("They are statistically consistant.")
    else:
         print("They are not statistically consistant")
    
# Uncertainty of the difference subtracting
    sigma_difference2 = math.sqrt(abs(sigma1**2 - sigma2**2))

    # Significance, calculkate how mayn sigams until differecne is at zero
    sigma_ = 0

    while difference > 0:
        difference -= sigma_difference2
        sigma_ += 1
    print(f"{p1} vs {p2}: "
          "Number of sigma:", sigma_)
    if sigma_ <= 3:
        print("They are statistically consistant.")
    else:
        print("They are not statistically consistant")

    
   
results = []
sum_w_diff = 0.0
sum_w = 0.0

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

print("Pairwise Results:")
for p1, p2, d, e in results:
    print(f"Pair ({p1}, {p2}): Diff = {d:.7f} ± {e:.7f}")

print(f"\nFinal Inverse-Variance Weighted Average Difference: {weighted_avg_diff:.7f} ± {weighted_err_diff:.7f}")




#1. differen (avergae of the pairs)
# 2.avergae difference = weighted avergae (differnce events_per_subsample)
#3. diffference uncertainiy = calculaet subsample uncertainty difference

