from sklearn.preprocessing import Normalizer
from parameters import Parameters
import numpy as np
import matplotlib.pyplot as plt

abbreviations_of_companies = input("Enter abbreviations of companies: ").split()

movements = Parameters(abbreviations_of_companies)

x = movements.daily_movement()

df_array = x.to_numpy()

df_array[np.isnan(df_array)] = 0

print(df_array)

normalizer = Normalizer()

norm_movements = normalizer.fit_transform(df_array)

print(norm_movements)
print(norm_movements.min())
print(norm_movements.max())
print(norm_movements.mean())

plt.plot(norm_movements)

plt.show()

print()