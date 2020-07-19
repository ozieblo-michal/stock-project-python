import pandas as pd
import os

# source to path to .csv files with historical values for each company
from parameters import path

# dict_stock_project contains dictionaries
from dict_stock_project import name_abbreviation_mWIG40_dict

class DatabaseCreator:

    def __init__(self):
        pass

    def database_creator(self):

        '''
        The first and main process of the whole project. Creates the main database created by concatenation historical \
        data of mWIG40 companies in December 2019 with index based on date. Missed values related with a time before \
        company listing or suspended quotes included.

        abbreviation_values - List of full names of companies from the dictionary.

        pre_column_names - List of target prefix for each column merged with the company name shortcut, \
        translation due to polish names of each column title in source files.

        df_to_merge - Temporary dataframe used in a loop with loaded source data for each single company.

        df_to_merge_list - List of single dataframes with values for each single company.

        column_names_with_suffix - Temporary list used in a loop to create company specific column names.

        database - Dataframe with the main database.

        :return: `database.csv` - The main database.
        '''

        abbreviation_values = name_abbreviation_mWIG40_dict.values()
        pre_column_names = ['Open_price', 'Max', 'Min', 'Close_price', 'Volume']
        df_to_merge_list = []

        for j in abbreviation_values:

            column_names_with_suffix = [(column_headline + '_%s' % j) for column_headline in pre_column_names]

            df_to_merge = pd.read_csv(os.path.join(path,r'%s_d.csv' % j),
                                      delimiter=',',
                                      index_col='Data') # index set based on `Data` column is important to remember

            df_to_merge.index = pd.to_datetime(df_to_merge.index)

            df_to_merge.columns = column_names_with_suffix
            df_to_merge.index.names = ['Date']

            df_to_merge_list.append(df_to_merge)

        database = pd.concat(df_to_merge_list,
                                 axis=1,
                                 sort=True)  # sorting is important to successfull creation of the database

        print('Success! Main database created by concatenation historical data of mWIG40 companies in December 2019 ',
              'with index based on date.\n',
              'Warning! Missed values related with a time before company listing or suspended quotes included!')
        return database.to_csv(os.path.join(path,r'database.csv'))

    if __init__ == "__main__":
        print("ADMIN INFO: DatabaseCreator run directly")
    else:
        print("ADMIN INFO: DatabaseCreator imported into another module")

#instance of the class and main function induction to local run:
dummy_instance_of_DatabaseCreator = DatabaseCreator()
dummy_instance_of_DatabaseCreator.database_creator()