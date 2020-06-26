from dataTransformations.parameters import Parameters
from dataTransformations.dict_stock_project import name_abbreviation_mWIG40_dict

from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import silhouette_score

import plotly.graph_objs as go

class SilhouettePlot:

    def silhouettePlot(self):

        '''
        :return: fig - the Silhouette plot
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

        # Metoda Silhouette'a:

        sil = []
        kmax = 22

        # dissimilarity would not be defined for a single cluster, thus, minimum number of clusters should be 2
        for k in range(2, kmax + 1):
            kmeans = KMeans(n_clusters=k).fit(norm_movements)
            labels = kmeans.labels_
            sil.append(silhouette_score(norm_movements,
                                        labels,
                                        metric='euclidean'))

        x = range(1, 22)

        # fig = plt.figure(figsize=(8,6))
        # plt.plot(x,
        #          sil,
        #          linestyle='--',
        #          marker='o')
        # plt.title('The Silhouette Method')
        # plt.xlabel('k')
        # plt.ylabel('Silhouette score')
        # plt.show()

        data = go.Scatter(x=list(x), y=sil)


        return data

# x = SilhouettePlot()
# x.silhouettePlot()