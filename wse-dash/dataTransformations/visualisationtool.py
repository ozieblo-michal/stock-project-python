import pandas as pd
import matplotlib.pyplot as plt
import os
import plotly.graph_objects as go

from parameters import Parameters
from pandas.plotting import register_matplotlib_converters # vis_volume_stock function requirement, due to future Pandas update

path = '/Users/michalozieblo/Desktop/stock-project-python/csv-files'
database = pd.read_csv(os.path.join(path,r'database.csv'), index_col=[0])

class Visualisationtool:

    def __init__(self):
        pass

    def vis_high_price(self, abbreviations_of_companies):
        data_to_plot = Parameters(abbreviations_of_companies).high_price()
        data_to_plot.plot()
        plt.grid(color='black',
                 linestyle='-.',
                 linewidth=0.5)

        plt.title('High price: %s' % abbreviations_of_companies)
        plt.xlabel('Date')
        plt.ylabel('Price')

        return plt.show()

    def vis_low_price(self, abbreviations_of_companies):
        data_to_plot = Parameters(abbreviations_of_companies).low_price()
        data_to_plot.plot()
        plt.grid(color='black',
                 linestyle='-.',
                 linewidth=0.5)

        plt.title('Low price: %s' % abbreviations_of_companies)
        plt.xlabel('Date')
        plt.ylabel('Price')

        return plt.show()

    def vis_open_price(self, abbreviations_of_companies):
        data_to_plot = Parameters(abbreviations_of_companies).open_price()
        data_to_plot.plot()
        plt.grid(color='black',
                 linestyle='-.',
                 linewidth=0.5)

        plt.title('Open price: %s' % abbreviations_of_companies)
        plt.xlabel('Date')
        plt.ylabel('Price')

        return plt.show()

    def vis_close_price(self, abbreviations_of_companies):
        data_to_plot = Parameters(abbreviations_of_companies).close_price()
        data_to_plot.plot()
        plt.grid(color='black',
                 linestyle='-.',
                 linewidth=0.5)

        plt.title('Close price: %s' % abbreviations_of_companies)
        plt.xlabel('Date')
        plt.ylabel('Price')

        return plt.show()

    def vis_volume_stock(self, abbreviations_of_companies):

        register_matplotlib_converters()

        list_volume_stock = Parameters(abbreviations_of_companies).volume_stock()
        fig, axs = plt.subplots(len(list_volume_stock),1)
        for i, df in enumerate(list_volume_stock):
            axs.bar(df.index, df.values.flatten())
            axs.set_title('Volume stock %s' % abbreviations_of_companies[i])
        plt.gcf().autofmt_xdate()
        return plt.show()

    # fakap z osią X dla kilku plotów
    # dać wersje z lineplotem

    # https://www.semicolonworld.com/question/58756/datetime-x-axis-matplotlib-labels-causing-uncontrolled-overlap
    # data_to_plot.plot(kind='bar') # problem: etykieta dla każdego labela
    # https://stackoverflow.com/questions/25440008/python-pandas-flatten-a-dataframe-to-a-list
    # dodac kolorek zielony/czerowny byki/niedzwiedzie >> barplot?

    def vis_daily_movement(self, abbreviations_of_companies): #ta sama nazwa, bierze input z test-fieldu tak jak w parameters
        data_to_plot = Parameters(abbreviations_of_companies).daily_movement()
        data_to_plot.plot() # tu nie trzeba labelki, bo zasysa z df'a
        plt.grid(color='black',
                 linestyle='-.',
                 linewidth=0.5)
        plt.title('Daily movement: %s' % abbreviations_of_companies)
        plt.xlabel('Date')
        plt.ylabel('Price')
        return plt.show()

    def candlestick(self, abbreviations_of_companies):

        print(abbreviations_of_companies)

        for i in abbreviations_of_companies:

            i = ["%s" % i] # " " to read as a word!

            print('test: ', i)

            df_open_price = Parameters(i).open_price()
            df_high_price = Parameters(i).high_price()
            df_low_price = Parameters(i).low_price()
            df_close_price = Parameters(i).close_price()

            fig = go.Figure(data=[go.Candlestick(x=df_open_price.index,
                                                     open=df_open_price.values.flatten(),
                                                     high=df_high_price.values.flatten(),
                                                     low=df_low_price.values.flatten(),
                                                     close=df_close_price.values.flatten())
                                  ])

    if __init__ == "__main__":
        print("Visualisationtool run directly")
    else:
        print("Visualisationtool imported into another module")