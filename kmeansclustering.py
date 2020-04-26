from parameters import Parameters
from dict_stock_project import name_abbreviation_mWIG40_dict, sectors_mWIG40_dict

from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class KMeansClustering:

    def kMeansClustering(self):

        abbreviations_of_companies = list(name_abbreviation_mWIG40_dict.values())

        movements = Parameters(abbreviations_of_companies)

        daily_movement_object = movements.daily_movement()

        # Replace NaN with 0's:
        daily_movement_object.fillna(0)

        # a dataframe transformation into an array and the transpose of a matrix
        norm_movements = daily_movement_object.to_numpy()

        # Replace NaN with 0's:
        norm_movements[np.isnan(norm_movements)] = 0

        # Normalize samples individually to unit norm:
        norm_movements = normalize(norm_movements, axis=0)

        # data transpose due to the KMean algorythm specific construction (calculation on columns, not rows):
        norm_movements = norm_movements.transpose()

        # print of control information about data shape:
        print('daily_movement_object shape: ',daily_movement_object.shape)
        print('norm_movements shape: ',norm_movements.shape)

        # Test element-wise for Not a Number (NaN), return result as a bool array, change for 0 if True
        # (Impact on the result, but not significant on a large scale. Zero means no change in the price of the item \
        # on a given day):
        norm_movements[np.isnan(norm_movements)] = 0

        # Elbow Method For Optimal k
        sum_of_squared_distances = []
        K = range(1, 22)

        for k in K:
            km = KMeans(n_clusters=k)
            km = km.fit(norm_movements)
            sum_of_squared_distances.append(km.inertia_)

        plt.plot(K, sum_of_squared_distances, 'bx-')
        plt.xlabel('k')
        plt.ylabel('Sum_of_squared_distances')
        plt.title('Elbow Method For Optimal k')
        plt.show()
        plt.clf()

        kmeans = KMeans(n_clusters = 16, # subjective selection of both parameters
                        max_iter = 1500)

        condition = False

        x = list(name_abbreviation_mWIG40_dict.values())

        while not condition:
            kmeans.fit(norm_movements)
            labels = kmeans.predict(norm_movements)

            y = []

            for i in x:
                y.append(sectors_mWIG40_dict[i])

            df = pd.DataFrame({'Labels':labels,
                               'Companies':daily_movement_object.columns,
                               'Economic sector':y}).sort_values(by=['Labels','Economic sector'],axis = 0)

            # condition due to commonly known trend
            ENERGETICS_test = df.loc[df['Economic sector'] == 'ENERGETICS']
            label = ENERGETICS_test['Labels'].to_list()
            condition_ENERGETICS = (len(set(label)) <= 1)
            print('------------------')
            print(label)

            GAMING_test = df.loc[df['Economic sector'] == 'GAMING']
            label = GAMING_test['Labels'].to_list()
            condition_GAMING = (len(set(label)) <= 1)
            print(label)

            print(condition_ENERGETICS, condition_GAMING)
            print('------------------')

            if all([condition_ENERGETICS, condition_GAMING]):
                condition = True

        return print(df)

x = KMeansClustering()
x.kMeansClustering()
