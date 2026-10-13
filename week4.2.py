import csv
import math
import numpy as np
from scipy import stats

files = ["/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/data1.csv",
         "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/data2.csv",
         "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/data3.csv",
         "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/data4.csv",
         "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/data5.csv",
         "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/data6.csv",
         "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/data7.csv",
         "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/data8.csv",
         "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/data9.csv",
         "/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/data10.csv"
    
]

all_data = []

for filename in files:
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
             try:
                 IDnumber = int(row[0])
                 mean = float(row[1])
                 standardDeviation = float(row[2])                

             except ValueError:
                    print("Error: value must be a number")
                    continue

             all_data.append((IDnumber, mean, standardDeviation))

   


# list of all the possible IDs
IDs = [211, -211, 321, -321, 2212, -2212, 3122, -3122, 3312, -3312, 3334, -3334]

for IDnumber in IDs :
   means = []
   for row in all_data:
        if row[0] == IDnumber:
            means.append(row[1])

   if len(means) > 0:
         Mean = np.mean(means)
         StandardDeviation = np.std(means)
         skew = stats.skew(means)

         print(IDnumber, Mean, StandardDeviation, skew)



 