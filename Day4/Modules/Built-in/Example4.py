#satistics - perform statistical calculations

import statistics

data = [10,20,30,40,50]

#Mean
print("Mean:",statistics.mean(data))

#Median
print("Median:",statistics.median(data))

#Mode
data_mode = [1,2,2,3,4]
print("Mode:",statistics.mode(data_mode))

#Variance
print("Variance:",statistics.variance(data))

#Standard Deviation
print("Standard Deviation:",statistics.stdev(data))