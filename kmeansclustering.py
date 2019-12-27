from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from sklearn.cluster import KMeans

from parameters import Parameters

import numpy as np
import pandas as pd

name_abbreviation_mWIG40_dict = {
    'mWIG40': 'mWIG40',
    '11_bit_studios': '11B',
    'Asseco_Poland': 'ACP',
    'Amica': 'AMC',
    'Grupa_Azoty': 'ATT',
    'Budimex': 'BDX',
    'Benefit_Systems': 'BFT',
    'Bank_Handlowy_w_Warszawie': 'BHW',
    'BNP_Paribas_Bank_Polska': 'BNP',
    'Boryszew': 'BRS',
    'Inter_Cars': 'CAR',
    'Ciech': 'CIE',
    'CI_Games': 'CIG',
    'Celon_Pharma': 'CLN',
    'Comarch': 'CMR',
    'Develia': 'DVL',
    'AmRest_Holdings': 'EAT',
    'Echo_Investment': 'ECH',
    'Enea': 'ENA',
    'Energa': 'ENG',
    'Eurocash': 'EUR',
    'Fabryka_Maszyn_Famur': 'FMF',
    'Fabryki_Mebli_Forte': 'FTE',
    'Giełda_Papierów_Wartościowych_w_Warszawie': 'GPW',
    'Globe_Trade_Centre': 'GTC',
    'Getin_Holding': 'GTN',
    'ING_Bank_Śląski': 'ING',
    'Kernel_Holding': 'KER',
    'Kruk': 'KRU',
    'Grupa_Kęty': 'KTY',
    'LiveChat_Software': 'LVC',
    'Lubelski_Węgiel_Bogdanka': 'LWB',
    'Mabion': 'MAB',
    'Bank_Millennium': 'MIL',
    'Orbis': 'ORB',
    'PKP_Cargo': 'PKP',
    'PlayWay': 'PLW',
    'Stalprodukt': 'STP',
    'Ten_Square_Games': 'TEN',
    'VRG': 'VRG',
    'Wirtualna_Polska_Holding': 'WPL'
}

class KMeansClustering:

    def kMeansClustering(self):

        abbreviations_of_companies = list(name_abbreviation_mWIG40_dict.values())

        movements = Parameters(abbreviations_of_companies)

        daily_movement = movements.daily_movement()
        df_array = daily_movement.to_numpy().T #ważne
        df_array[np.isnan(df_array)] = 0

        normalizer = Normalizer()
        kmeans = KMeans(n_clusters = 14,max_iter = 1000)
        pipeline = make_pipeline(normalizer,kmeans)

        pipeline.fit(df_array)
        labels = pipeline.predict(df_array)

        df = pd.DataFrame({'Labels':labels,
                           'Companies':daily_movement.columns}).sort_values(by=['Labels'],
                                                                            axis = 0)

        return print(df)

# x = KMeansClustering()
# x.kMeansClustering()