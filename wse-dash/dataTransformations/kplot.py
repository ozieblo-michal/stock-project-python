from dataTransformations.parameters import Parameters
from dataTransformations.dict_stock_project import name_abbreviation_mWIG40_dict

from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
import numpy as np

import dash_core_components as dcc
import plotly.graph_objs as go

class KMeansPlot:

    def kMeansPlot(self):

        '''
        :return: fig plot of optimal K value
        '''

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
        norm_movements = normalize(norm_movements,
                                   axis=0)

        # data transpose due to the KMean algorythm specific construction (calculation on columns, not rows):
        norm_movements = norm_movements.transpose()

        # print of control information about data shape:
        print('daily_movement_object shape: ',
              daily_movement_object.shape)
        print('norm_movements shape: ',
              norm_movements.shape)

        # Test element-wise for Not a Number (NaN), return result as a bool array, change for 0 if True
        # (Impact on the result, but not significant on a large scale. Zero means no change in the price of the item \
        # on a given day):
        norm_movements[np.isnan(norm_movements)] = 0

        # Elbow Method For Optimal k
        sum_of_squared_distances = []
        K = range(1, 22)

        for k in K:
            km = KMeans(n_clusters=k).fit(norm_movements)
            sum_of_squared_distances.append(km.inertia_)


        # fig = plt.figure(figsize=(8,6))
        # plt.plot(K, sum_of_squared_distances,
        #          'bx-')
        # plt.xlabel('k')
        # plt.ylabel('Sum_of_squared_distances')
        # plt.title('Elbow Method For Optimal k')
        # plt.show()

        data = go.Scatter(x=list(K),y=sum_of_squared_distances)

        return data

# x = KMeansPlot()
# x.kMeansPlot()