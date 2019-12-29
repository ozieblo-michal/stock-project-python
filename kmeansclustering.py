from parameters import Parameters, name_abbreviation_mWIG40_dict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs
from matplotlib import style

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# K-means:
# The clustering algorithm tries to partition a set of points into K sets (clusters)
# such that the points in each cluster tend to be near each other.
# It is unsupervised because the points have no external classification.

sectors_mWIG40_dict = {
    'mWIG40':'MARKET INDICATOR',
    '11B':'GAMING',
    'ACP':'IT',
    'AMC':'AGD',
    'ATT':'CHEMICALS',
    'BDX':'INFRASTRUCTURE',
    'BFT':'SERVICES',
    'BHW':'BANK',
    'BNP':'BANK',
    'BRS':'CHEMICALS AND CAR PARTS',
    'CAR':'CAR PARTS',
    'CIE':'CHEMICALS',
    'CIG':'GAMING',
    'CLN':'BIOTECH',
    'CMR':'IT',
    'DVL':'CONSTRUCTION DEVELOPER',
    'EAT':'FOOD INDUSTRY',
    'ECH':'CONSTRUCTION DEVELOPER',
    'ENA':'ENERGETICS',
    'ENG':'ENERGETICS',
    'EUR':'FOOD INDUSTRY',
    'FMF':'MINING INDUSTRY',
    'FTE':'FURNITURE',
    'GPW':'STOCK EXCHANGE',
    'GTC':'CONSTRUCTION DEVELOPER',
    'GTN':'BANK',
    'ING':'BANK',
    'KER':'FOOD INDUSTRY',
    'KRU':'VINDICATION',
    'KTY':'METAL PROCESSING',
    'LVC':'IT',
    'LWB':'MINING INDUSTRY',
    'MAB':'BIOTECH',
    'MIL':'BANK',
    'ORB':'HOSPITALITY',
    'PKP':'RAILWAYS',
    'PLW':'GAMING',
    'STP':'METAL PROCESSING',
    'TEN':'GAMING',
    'VRG':'CLOTHES',
    'WPL':'IT'
}

class KMeansClustering:

    def kMeansClustering(self):

        abbreviations_of_companies = list(name_abbreviation_mWIG40_dict.values())

        movements = Parameters(abbreviations_of_companies)

        daily_movement = movements.daily_movement()

        # a dataframe to an array and the transpose of a matrix
        df_array = daily_movement.to_numpy().T

        # impact on the result, but not significant on a large scale.
        # zero means no change in the price of the item on a given day.
        df_array[np.isnan(df_array)] = 0

        style.use("seaborn-pastel")

        # make_blobs() is used to generate sample points
        # around c centers (randomly chosen)
        X, y = make_blobs(n_samples=400,
                          centers=10,
                          cluster_std=1,
                          n_features=2)

        plt.scatter(X[:, 0],
                    X[:, 1],
                    s=5,
                    color='r')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()
        # clear the figure
        plt.clf()
        # more about: https://www.geeksforgeeks.org/ml-determine-the-optimal-value-of-k-in-k-means-clustering/

        # Elbow Method For Optimal k
        sum_of_squared_distances = []
        K = range(1, 16)

        for k in K:
            km = KMeans(n_clusters=k)
            km = km.fit(df_array)
            sum_of_squared_distances.append(km.inertia_)

        plt.plot(K, sum_of_squared_distances, 'bx-')
        plt.xlabel('k')
        plt.ylabel('Sum_of_squared_distances')
        plt.title('Elbow Method For Optimal k')
        plt.show()
        plt.clf()
        # more about: https://blog.cambridgespark.com/how-to-determine-the-optimal-number-of-clusters-for-k-means-clustering-14f27070048f

        normalizer = Normalizer()
        kmeans = KMeans(n_clusters = 10,
                        max_iter = 1000)
        pipeline = make_pipeline(normalizer,kmeans)
        pipeline.fit(df_array)
        labels = pipeline.predict(df_array)

        x = list(name_abbreviation_mWIG40_dict.values())
        y =[]

        for i in x:
            y.append(sectors_mWIG40_dict[i])
        print(y)

        df = pd.DataFrame({'Labels':labels,
                           'Companies':daily_movement.columns,
                           'Economic sector':y}).sort_values(by=['Labels','Economic sector'], axis = 0)

        return print(df)

x = KMeansClustering()
x.kMeansClustering()