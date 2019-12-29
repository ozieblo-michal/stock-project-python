import pandas as pd
import os

from parameters import name_abbreviation_mWIG40_dict
from parameters import path

class DatabaseCreator:

    def __init__(self):
        pass

    def database_creator(self):

        abbreviation_values = name_abbreviation_mWIG40_dict.values()

        pre_column_names = ['Open_price', 'Max', 'Min', 'Close_price', 'Volume']
        df_to_merge_list = []

        for j in abbreviation_values:

            column_names_with_suffix = [(column_headline + '_%s' % j) for column_headline in pre_column_names]

            df_to_merge = pd.read_csv(os.path.join(path,r'%s_d.csv' % j),
                                      delimiter=',',
                                      index_col='Data') # important

            df_to_merge.index = pd.to_datetime(df_to_merge.index)

            df_to_merge.columns = column_names_with_suffix
            df_to_merge.index.names = ['Date']

            df_to_merge_list.append(df_to_merge)

        database = pd.concat(df_to_merge_list,
                                 axis=1,
                                 sort=True)  # important

        print('poszlo')
        return database.to_csv(os.path.join(path,r'database.csv'))

    if __init__ == "__main__":
        print("DatabaseCreator run directly")
    else:
        print("DatabaseCreator imported into another module")

a = DatabaseCreator()
a.database_creator()