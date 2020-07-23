import pandas as pd
import numpy as np
import os
import sys
from numpy import inf
import timeit

# Need database.cvs file, which is a return from databasecreator.py run

# `path` - Path to .csv files with historical values for each company.
path = '/Users/michalozieblo/Desktop/stock-project-python/csv-files'

class Parameters:

    '''
    Functions (described separately below):
    `__init__`
    `daily_movement`
    `high_price`
    `low_price`
    `open_price`
    `close_price`
    `volume_stock`
    `sum_of_movements`
    '''

    def __init__(self, abbreviations_of_companies):

        """
        :param abbreviations_of_companies: Abbreviation(s) of tested companies as list with string object(s).

        `list_source_df` - List of dataframes with historical data values, not from the main "master" database, \
                           but for each single raw data for them.

        `source_df` - Temporary dataframe with historical data for the company, used in a loop.
        """

        self.abbreviations_of_companies = abbreviations_of_companies
        self.list_source_df = []

        start = timeit.default_timer()

        if len(self.abbreviations_of_companies) > 0: # if more than one company selected
            for i in self.abbreviations_of_companies:
                self.source_df = pd.read_csv(os.path.join(path,r'%s_d.csv' % i),
                                             delimiter=',',
                                             index_col=[0]) # important
                self.source_df.index = pd.to_datetime(self.source_df.index)
                self.list_source_df.append(self.source_df)

        else:
            self.source_df = pd.read_csv(os.path.join(path,r'%s_d.csv' % abbreviations_of_companies),
                                         delimiter=',',
                                         index_col=[0]) # index is important here
            self.source_df.index = pd.to_datetime(self.source_df.index)
            self.list_source_df.append(self.source_df)

        stop = timeit.default_timer()
        print('-----------------------------------------')
        print('Initialization run time: ', stop - start)

    def daily_movement(self):

        '''
        `database` - Dataframe with the main database with all data.

        `list_price_subtract` - List with result(s) of subtracting the opening price logarithm \
                                and the closing price logarithm.

        `column_headlines` - Var (type list) for a loop to rename column names with specific company prefix.

        `open_price_subtract` - result of subtracting the opening price logarithm \
                                and the closing price logarithm of each single company.

        `daily_movement` - Concatenated dataframe with daily movement for each selected company \
                           (input, var abbreviations_of_companies). Return var.

        "You can think about and perhaps experiment to see if you should scale all variables together \
        (meaning one global min and max in the dataset), or whether to scale the individual columns/features \
        of your dataset, so each one lies in the given range.

        A tip for financial data is to use the log returns - that means to take your raw prices, compute \
        the logarithm of those values, then take the difference between the closing prices of each day.

        The reason for this is to because the resulting values are normally distributed, which is an underlying \
        assumption of many models you will subsequently use (Boosting, ARIMA, GARCH for volatilities etc.). \
        There are also other reasons of convenience."

        Source and more about:
        https://datascience.stackexchange.com/questions/40142/how-to-normalize-data-of-a-different-nature

        :return: daily_movement
        '''

        start = timeit.default_timer()

        try:
            database = pd.read_csv(os.path.join(path, r'database.csv'),
                                   delimiter=',',
                                   index_col=[0])  # proper set of the index is important
        except FileNotFoundError:
            print("Error: Dataframe based on database.csv cannot be loaded. Source file do not found. \n ",
                  "Run databasecreator.py")
            sys.exit(1)

        list_price_subtract = []
        column_headlines = []

        # take raw prices, compute the logarithm of those values, then take the difference between \
        # the closing prices of each day
        for i in self.abbreviations_of_companies:
            open_price = database['Open_price_%s' % i]
            close_price = database['Close_price_%s' % i]

            open_price = np.log(open_price)
            close_price = np.log(close_price)

            open_price[open_price == -inf] = 0
            close_price[close_price == -inf] = 0

            open_price_subtract = open_price.sub(close_price)
            list_price_subtract.append(open_price_subtract)
            column_headlines.append('Daily_movement_%s' % i)

        daily_movement = pd.concat(list_price_subtract, axis=1)
        daily_movement.columns = column_headlines

        stop = timeit.default_timer()
        print('-----------------------------------------')
        print('daily_movement run time: ', stop - start)

        return daily_movement

    def high_price(self):

        '''
        vars:

        `high_price` - Dataframe with high price for each day for a single company, used in a loop. Return var.

        `df_high_price` - Dataframe with high prices concat based on the index.

        `list_high_price` - List of `high_price` dataframes for each company.
        `column_headlines` - Var (type list) for a loop to rename column names with specific company prefix.

        :return: df_high_price
        '''

        list_high_price = []
        column_headlines = []

        start = timeit.default_timer()

        for i in self.list_source_df:
            high_price = i['Najwyzszy']
            list_high_price.append(high_price)

        for i in self.abbreviations_of_companies:
            column_headlines.append('Max_price_%s' % i)

        df_high_price = pd.concat(list_high_price, axis=1)
        df_high_price.columns = column_headlines

        print('-----------------------------------------')
        print('Dataframe head, First 5 rows: \n',
              df_high_price.head())
        print('-----------------------------------------')
        print(df_high_price.describe())
        print('-----------------------------------------')
        print(df_high_price.dtypes)
        print('-----------------------------------------')
        print('Is NaN?: \n',
              df_high_price.isna())
        print('-----------------------------------------')
        print('Rows with NaN: \n',
              df_high_price[df_high_price.isnull().any(axis=1)])

        stop = timeit.default_timer()
        print('-----------------------------------------')
        print('df_high_price run time: ', stop - start)

        return df_high_price

    def low_price(self):

        '''
        vars:
        `list_low_price`
        `column_headlines`
        `low_price`
        `df_low_price`

        :return: df_low_price
        '''

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

        '''
        var:
        `list_open_price`
        `column_headlines`
        `open_price`
        `df_open_price`

        :return: df_open_price
        '''

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

        '''
        var:
        `list_close_price`
        `column_headlines`
        `close_price`
        `df_close_price`

        :return: df_close_price
        '''

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

        '''
        `list_volume_stock`
        `volume_stock`

        :return: list_volume_stock
        '''

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



    def sum_of_movements(self):

        '''
        :return: `result`
        '''

        database = pd.read_csv(os.path.join(path,r'database.csv')) # sprawdz to wzgledem tego co sie dzieje doslownie funkcje wyzej

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
        print("ADMIN INFO: Parameters.py run directly.")
    else:
        print("ADMIN INFO: Parameters.py imported into another module.")

    # zastosuj do nazw klucze do slownika :)
