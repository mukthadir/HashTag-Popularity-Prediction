__author__ = 'hchou006'

import numpy as np
from numpy import genfromtxt

# saving the location of given csv files in different variables
actual_20_days = 'Actual20days.csv'
expected_20_days = 'Expected20days.csv'

actual_15_days = 'Actual15days.csv'
expected_15_days = 'Expected15days.csv'

actual_10_days = 'Actual10days.csv'
expected_10_days = 'Expected10days.csv'


# generating arrays from testing csv files for prediction and comparison
actual_result = genfromtxt(actual_10_days, delimiter= ',')
expected_result = genfromtxt(expected_10_days, delimiter= ',')

# calculating the RMSE of my prediction using true class labels
rmse = np.sqrt(np.mean((expected_result-actual_result)**2))

# saving rmse in a output file
outputFile = 'RMSE10days.txt'
file = open(outputFile, 'w')
file.write('RMSE of my prediction for the given testing data is ' + str(rmse))
file.close()
