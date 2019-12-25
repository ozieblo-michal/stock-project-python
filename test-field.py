from visualisationtool import Visualisationtool
# from parameters import Parameters

abbreviations_of_companies = input("Enter abbreviations of companies: ").split()

x = Visualisationtool()
x.vis_close_price(abbreviations_of_companies)
x.vis_daily_movement(abbreviations_of_companies)
x.vis_high_price(abbreviations_of_companies)
x.vis_open_price(abbreviations_of_companies)
x.vis_volume_stock(abbreviations_of_companies)

# muminek = Parameters(x)
# muminek.daily_movement()