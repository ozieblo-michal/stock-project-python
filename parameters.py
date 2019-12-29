import pandas as pd
import numpy as np
import os

from dict_stock_project import name_abbreviation_mWIG40_dict

path = '/Users/michalozieblo/Desktop/stock-project-python/csv-files'

class Parameters:

    def __init__(self, abbreviations_of_companies):
        self.abbreviations_of_companies = abbreviations_of_companies
        self.list_source_df = []

        if len(self.abbreviations_of_companies) > 0:
            for i in self.abbreviations_of_companies:
                self.source_df = pd.read_csv(os.path.join(path,r'%s_d.csv' % i),
                                             delimiter=',',
                                             index_col=[0]) # important
                self.source_df.index = pd.to_datetime(self.source_df.index)
                self.list_source_df.append(self.source_df)

        else:
            self.source_df = pd.read_csv(os.path.join(path,r'%s_d.csv' % abbreviations_of_companies),
                                         delimiter=',',
                                         index_col=[0]) # important
            self.source_df.index = pd.to_datetime(self.source_df.index)
            self.list_source_df.append(self.source_df)

    def high_price(self):

        list_high_price = []
        column_headlines = []

        for i in self.list_source_df:
            high_price = i['Najwyzszy']
            list_high_price.append(high_price)

        for i in self.abbreviations_of_companies:
            column_headlines.append('Max_price_%s' % i)

        df_high_price = pd.concat(list_high_price, axis=1)
        df_high_price.columns = column_headlines

        return df_high_price

    def low_price(self):

        list_low_price = []
        column_headlines = []

        for i in self.list_source_df:
            low_price = i['Najnizszy']
            list_low_price.append(low_price)

        for i in self.abbreviations_of_companies:
            column_headlines.append('Min_price_%s' % i)

        df_low_price = pd.concat(list_low_price, axis=1)
        df_low_price.columns = column_headlines

        return df_low_price

    def open_price(self):

        list_open_price = []
        column_headlines = []

        for i in self.list_source_df:
            open_price = i['Otwarcie']
            list_open_price.append(open_price)

        for i in self.abbreviations_of_companies:
            column_headlines.append('Open_price_%s' % i)

        df_open_price = pd.concat(list_open_price, axis=1)
        df_open_price.columns = column_headlines

        return df_open_price

    def close_price(self):

        list_close_price = []
        column_headlines = []

        for i in self.list_source_df:
            close_price = i['Zamkniecie']
            list_close_price.append(close_price)

        for i in self.abbreviations_of_companies:
            column_headlines.append('Close_price_%s' % i)

        df_close_price = pd.concat(list_close_price, axis=1)
        df_close_price.columns = column_headlines

        return df_close_price

    def volume_stock(self):

        list_volume_stock = []


        for i in self.list_source_df:
            volume_stock = i['Wolumen']
            list_volume_stock.append(volume_stock)

        # FOR DATAFRAME:
        #
        # column_headlines = []
        # for i in self.abbreviations_of_companies:
        #     column_headlines.append('Wolumen_%s' % i)
        # df_volume_stock = pd.concat(list_volume_stock, axis=1)
        # df_volume_stock.columns = column_headlines

        return list_volume_stock

    # ZROBIC DWIE FUNKCJE, jedna do wizualizacji, druga na wydruk

    def daily_movement(self):

        database = pd.read_csv(os.path.join(path,r'database.csv'),
                               delimiter=',',
                               index_col=[0]) # important

        list_open_close_price = []
        column_headlines = []

        for i in self.abbreviations_of_companies:
            open_price = database['Open_price_%s' % i]
            close_price = database['Close_price_%s' % i]
            open_price_subtract = open_price.sub(close_price)
            list_open_close_price.append(open_price_subtract)
            column_headlines.append('Daily_movement_%s' % i)

        daily_movement = pd.concat(list_open_close_price, axis=1)
        daily_movement.columns = column_headlines

        return daily_movement

    # DODAC TEST NA WYPADEK BRAKU DATABASE

    def sum_of_movements(self):

        database = pd.read_csv(os.path.join(path,r'database.csv'))

        for i in self.abbreviations_of_companies:
            open_price = database['Open_price_%s' % i]
            close_price = pd.Series(database['Close_price_%s' % i])
            open_price_subtract = open_price.sub(close_price)
            price_subtract_sum = np.sum(open_price_subtract)
            x = 'price_subtract_sum for %s: ' % i, price_subtract_sum

            result = []
            result.append(str(x))

        return result

    # ZBADAC DLACZEGO NIE IDZIE TEGO WRZUCIC NA SOLO DO STR(), TYLKO TAK ROZWALONE

    if __init__ == "__main__":
        print("Parameters run directly")
    else:
        print("Parameters imported into another module")

    # zastosuj do nazw klucze do slownika :)