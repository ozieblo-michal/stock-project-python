import pandas as pd
import matplotlib.pyplot as plt
import os

from parameters import Parameters # abbreviations_of_companies!!!
from pandas.plotting import register_matplotlib_converters #barplotcase

path = '/Users/michalozieblo/Desktop/stock-project-python/csv-files'
database = pd.read_csv(os.path.join(path,r'database.csv'), index_col=[0])

class Visualisationtool:

    def __init__(self):
        pass

    def vis_high_price(self, abbreviations_of_companies):
        data_to_plot = Parameters(abbreviations_of_companies).high_price()
        data_to_plot.plot()
        plt.grid(color='black', linestyle='-.', linewidth=0.5)
        return plt.show()

    def vis_low_price(self, abbreviations_of_companies):
        data_to_plot = Parameters(abbreviations_of_companies).low_price()
        data_to_plot.plot()
        plt.grid(color='black', linestyle='-.', linewidth=0.5)
        return plt.show()

    def vis_open_price(self, abbreviations_of_companies):
        data_to_plot = Parameters(abbreviations_of_companies).open_price()
        data_to_plot.plot()
        plt.grid(color='black', linestyle='-.', linewidth=0.5)
        return plt.show()

    def vis_close_price(self, abbreviations_of_companies):
        data_to_plot = Parameters(abbreviations_of_companies).close_price()
        data_to_plot.plot()
        plt.grid(color='black', linestyle='-.', linewidth=0.5)
        return plt.show()

    def vis_volume_stock(self, abbreviations_of_companies):
        register_matplotlib_converters() # zabezpieczenie, pandas po update przestalby ogarniax oś x
        list_volume_stock = Parameters(abbreviations_of_companies).volume_stock() #ok
        fig, axs = plt.subplots(len(list_volume_stock),1)
        for i, df in enumerate(list_volume_stock):
            axs[i].bar(df.index, df.values.flatten())
            axs[i].set_title('%s' % abbreviations_of_companies[i])
        plt.gcf().autofmt_xdate()
        return plt.show()

        # https://www.semicolonworld.com/question/58756/datetime-x-axis-matplotlib-labels-causing-uncontrolled-overlap
        # data_to_plot.plot(kind='bar') # problem: etykieta dla każdego labela
        # https://stackoverflow.com/questions/25440008/python-pandas-flatten-a-dataframe-to-a-list
        # dodac kolorek zielony/czerowny byki/niedzwiedzie

    def vis_daily_movement(self, abbreviations_of_companies): #ta sama nazwa, bierze input z test-fieldu tak jak w parameters
        data_to_plot = Parameters(abbreviations_of_companies).daily_movement()
        data_to_plot.plot() # tu nie trzeba labelki, bo zasysa z df'a
        plt.grid(color='black', linestyle='-.', linewidth=0.5)
        plt.title('Daily movement: %s' % abbreviations_of_companies)
        plt.xlabel('Date')
        plt.ylabel('Price')
        return plt.show()

    if __init__ == "__main__":
        print("Visualisationtool run directly")
    else:
        print("Visualisationtool imported into another module")

# Your main and only problem is that the "dates" are strings. If you convert your strings to dates the plot will look as expected.
# You are doing that already inside the dataframe, but then do not use that column in any of the further code.
# TO DO: tytuly plotow i osi itd