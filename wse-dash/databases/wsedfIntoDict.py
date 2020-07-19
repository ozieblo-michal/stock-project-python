import pandas as pd

# spolki z infosfera

class KmeanOptions:

    def __init__(self):
        pass

    def wig20_options_for_kmean(self):

        wig20_df = pd.read_csv('/Users/michalozieblo/Desktop/wse-dash/databases/wse_wig20.csv',
                               delimiter=";")

        wig20Abbrev = dict(zip(wig20_df['Nazwa giełdowa'],
                               wig20_df['Ticker']))

        wig20_options_for_kmean = []

        for key, value in wig20Abbrev.items():
            tmp_dict_1 = {'label': key}
            tmp_dict_2 = {'value': value}
            tmp_dict_3 = {**tmp_dict_1, **tmp_dict_2}
            wig20_options_for_kmean.append(tmp_dict_3)

        return wig20_options_for_kmean

    def mwig40_options_for_kmean(self):

        mwig40_df = pd.read_csv('/Users/michalozieblo/Desktop/wse-dash/databases/wse_mwig40.csv',
                                delimiter=";")

        mwig40Abbrev = dict(zip(mwig40_df['Nazwa giełdowa'],
                                mwig40_df['Ticker']))

        mwig40_options_for_kmean = []

        for key, value in mwig40Abbrev.items():
            tmp_dict_1 = {'label': key}
            tmp_dict_2 = {'value': value}
            tmp_dict_3 = {**tmp_dict_1, **tmp_dict_2}
            mwig40_options_for_kmean.append(tmp_dict_3)

        return mwig40_options_for_kmean

    def swig80_options_for_kmean(self):

        swig80_df = pd.read_csv('/Users/michalozieblo/Desktop/wse-dash/databases/wse_swig80.csv',
                                delimiter=";")

        swig80Abbrev = dict(zip(swig80_df['Nazwa giełdowa'],
                                swig80_df['Ticker']))

        swig80_options_for_kmean = []

        for key, value in swig80Abbrev.items():
            tmp_dict_1 = {'label': key}
            tmp_dict_2 = {'value': value}
            tmp_dict_3 = {**tmp_dict_1, **tmp_dict_2}
            swig80_options_for_kmean.append(tmp_dict_3)

        return swig80_options_for_kmean

    def wse_options_for_indicators(self):

        wse_df = pd.read_csv('/Users/michalozieblo/Desktop/wse-dash/databases/wseDataframe.csv',
                             delimiter=";")

        wseAbbrev = dict(zip(wse_df['Nazwa giełdowa'],
                             wse_df['Ticker']))

        wse_options_for_kmean = []

        for key, value in wseAbbrev.items():
            tmp_dict_1 = {'label': key}
            tmp_dict_2 = {'value': value}
            tmp_dict_3 = {**tmp_dict_1, **tmp_dict_2}
            wse_options_for_kmean.append(tmp_dict_3)

        return wse_options_for_kmean