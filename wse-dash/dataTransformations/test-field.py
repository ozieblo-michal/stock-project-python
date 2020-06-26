from visualisationtool import Visualisationtool
from parameters import Parameters

#abbreviations_of_companies = input("Enter abbreviations of companies: ").split()

x = Visualisationtool()
abbreviations_of_companies = input("Enter abbreviation of company: ").split()
print(abbreviations_of_companies)
print(type(abbreviations_of_companies[0]))
#x.vis_close_price(abbreviations_of_companies)
#x.candlestick(abbreviations_of_companies)


# # x.vis_daily_movement(abbreviations_of_companies)
#x.vis_high_price(abbreviations_of_companies)
# # x.vis_low_price(abbreviations_of_companies)
x.vis_volume_stock(abbreviations_of_companies)
# #

#muminek = Parameters(abbreviations_of_companies)
#df = muminek.high_price()




# muminek.volume_stock() # lista
#print(muminek.daily_movement())


#
# import pandas as pd
# import os
# from parameters import path
#
# def database_validation():
#     df = pd.read_csv(os.path.join(path, r'database.csv'))
#     print(df.info())
#     for index, row in df.iterrows():
#         while any(row.isna()):
#             print(index)
#             row = row.fillna(0)
#             if any(row.isna()) == False:
#                 break
#
#     # return print(df.head(), df.tail())
#
#
# database_validation()
# #
# # 1. sprawdz kiedy zaczyna sie szereg czasowy dla danej spolki
# # 2. wylap wszystkie nany z tego szeregu czasowego i zastap ffill
# # 3. merge, uzupelnij pozostale zerami
# # :)
