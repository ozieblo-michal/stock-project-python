import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from parameters import Parameters

'''
Need parameters.py to run.

It was a test file to properly set up the normalization into kmeanclustering.py (unrelated files to run).
'''

# Take the companies to analyse. Manual input from the user as name abbreviations.
abbreviations_of_companies = input("Enter company/-ies abbreviation(s) (blank space between if multiple, not a coma): ").split()

# instance of Parameters class to obtain daily movement:
movements = Parameters(abbreviations_of_companies)

# daily movement dataframe(s):
daily_movement_object = movements.daily_movement()

# Replace Not a Number (NaN) with 0's:
daily_movement_object.fillna(0)

# Convert the DataFrame to a NumPy array:
df_array = daily_movement_object.to_numpy()

# Test element-wise for NaN, return result as a bool array, change for 0 if True:
df_array[np.isnan(df_array)] = 0

# Normalize samples individually to unit norm:
norm_movements = normalize(df_array, axis=0)

# Simple check of normalization:
print('check after normalization - MIN VALUE (range between -1 and 0): ', norm_movements.min())
print('check after normalization - MAX VALUE (range between 0 and 1): ',norm_movements.max())
print('check after normalization - MEAN VALUE (properly should be near null): ',norm_movements.mean())

# Plot of distribution:
plt.plot(norm_movements)
plt.suptitle("Daily price movements of companies:", fontsize=12)
plt.title("(the result of subtracting the opening price logarithm and the closing price logarithm)", fontsize=8)
plt.gca().legend(abbreviations_of_companies)
plt.show()
