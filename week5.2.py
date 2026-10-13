import math
import matplotlib.pyplot as plt
import numpy as np


def openfile(filename):
    data = []

    with open(filename, "r") as infile:
        next(infile)

        for line in infile:
            values = line.split()

            if len(values) == 4:
                try:
                    x = float(values[0])
                    y = float(values[1])
                    z = float(values[2])
                    particle_id = int(values[3])
                except ValueError:
                    print("Error: value must be a number")
                    continue

                data.append((x, y, z, particle_id))

    return data


# Files


filenames = [

    "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/Practical/output-Set1.txt",
    "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/Practical/output-Set2.txt",
    "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/Practical/output-Set3.txt",
    "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/Practical/output-Set4.txt",
    "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/Practical/output-Set5.txt",
    "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/Practical/output-Set6.txt",
    "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/Practical/output-Set7.txt",
    "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/Practical/output-Set8.txt",
    "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/Practical/output-Set9.txt",
    "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/Practical/output-Set10.txt"
]

#define the bins and add a maximum
bin_width = 0.1
max_momentum = 10.0 

bins = np.arange(0, max_momentum + bin_width, bin_width)

all_differences = []

for filename in filenames:

    data = openfile(filename)

    momenta_ID1 = []
    momenta_ID2 = []

    # Calculate momentum for each particle
    for x, y, z, particle_id in data:

        momentum = math.sqrt(x**2 + y**2 + z**2)

        if particle_id == 3312:     #change the ID to the one that gets analysed 
            momenta_ID1.append(momentum)

        elif particle_id == -3312:   #change ID to match the first one
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

# Bin centres
bin_centers = (bins[:-1] + bins[1:]) / 2

# Plot
plt.figure()

plt.errorbar(
    bin_centers,
    mean_difference,
    yerr=std_difference,
    fmt='o',
    markersize=3,
    capsize=3
)

plt.axhline(0, color='black', linewidth=1)

plt.xlabel("Momentum")
plt.ylabel("Normalized distribution: 3312 - (-3312)")
plt.title("Difference between momentum distributions of 3312 and -3312")
plt.grid()
plt.tight_layout()
plt.savefig("weighted_momentum_distribution_difference.png")
plt.show()
plt.close()