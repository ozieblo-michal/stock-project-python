import pandas as pd
import matplotlib.pyplot as plt
import os

from parameters import Parameters # abbreviations_of_companies!!!

path = '/Users/michalozieblo/Desktop/stock-project-python/csv-files'
database = pd.read_csv(os.path.join(path,r'database.csv'), index_col=[0])

class Visualisationtool:

    def __init__(self):
        pass

    def vis_high_price(self, abbreviations_of_companies):
        data_to_plot = Parameters(abbreviations_of_companies).high_price()
        data_to_plot.plot()
        return plt.show()

    def vis_low_price(self, abbreviations_of_companies):
        data_to_plot = Parameters(abbreviations_of_companies).low_price()
        data_to_plot.plot()
        return plt.show()

    def vis_open_price(self, abbreviations_of_companies):
        data_to_plot = Parameters(abbreviations_of_companies).open_price()
        data_to_plot.plot()
        return plt.show()

    def vis_close_price(self, abbreviations_of_companies):
        data_to_plot = Parameters(abbreviations_of_companies).close_price()
        data_to_plot.plot()
        return plt.show()

    def vis_volume_stock(self, abbreviations_of_companies):
        data_to_plot = Parameters(abbreviations_of_companies).volume_stock()
        data_to_plot.plot()
        return plt.show()

    def vis_daily_movement(self, abbreviations_of_companies): #ta sama nazwa, bierze input z test-fieldu tak jak w parameters
        data_to_plot = Parameters(abbreviations_of_companies).daily_movement()
        data_to_plot.plot()
        return plt.show()

    if __init__ == "__main__":
        print("Visualisationtool run directly")
    else:
        print("Visualisationtool imported into another module")

#Your main and only problem is that the "dates" are strings. If you convert your strings to dates the plot will look as expected. You are doing that already inside the dataframe, but then do not use that column in any of the further code.

# TO DO:
        #     1. napraw to gowno wyzej, ma byc tylko rok na osi x i przedzialki na 12 miesiecy
        #     2. wysylka do repo na backup
        #     3. os dat jakos sensownie, a nie random pointy