import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('/Users/mateuszjeczarek/PycharmProjects/stock-project-python-new_master/wse-dash/databases/csv-files/mwig40_d.csv')

#Calculate the MACD and signal line indicators
#Calculate the short term exponential moving average (EMA)
ShortEMA = df.Zamkniecie.ewm(span=12, adjust=False).mean()

#Calcualte the long term exponential moving average (EMA)
LongEMA = df.Zamkniecie.ewm(span=26, adjust=False).mean()

#Calculate the MACD line
MACD = ShortEMA - LongEMA

#Calculate the signal line
signal = MACD.ewm(span=9, adjust=False).mean()

# Create new columns for the data
df['MACD'] = MACD
df['Signal Line'] = signal

# Create a function to signal when to buy and sell an asset
def buy_sell(signal):
    Buy = []
    Sell = []
    flag = -1

    for i in range(0, len(signal)):
        if signal['MACD'][i] > signal['Signal Line'][i]:
            Sell.append(np.nan)
            if flag != 1:
                Buy.append(signal['Zamkniecie'][i])
                flag = 1
            else:
                Buy.append(np.nan)
        elif signal['MACD'][i] < signal['Signal Line'][i]:
            Buy.append(np.nan)
            if flag != 0:
                Sell.append(signal['Zamkniecie'][i])
                flag = 0
            else:
                Sell.append(np.nan)
        else:
            Buy.append(np.nan)
            Sell.append(np.nan)

    return (Buy, Sell)

# Create buy and sell column
a = buy_sell(df)
df['Buy_Signal_price'] = a[0]
df['Sell_Signal_price'] = a[1]

MACD = df['MACD']

class Subplots:

    def subplots(self):

#        fig = plt.figure(figsize=(12.2, 4.5))
#        plt.scatter(df.index, df['Buy_Signal_price'], color='green', label='Buy', marker='^', alpha=1)
#        plt.scatter(df.index, df['Sell_Signal_price'], color='red', label='Sell', marker='v', alpha=1)
#        plt.plot(df['Zamkniecie'], label='Close Price', alpha = 0.35)
#        plt.title('Close Price Buy & Sell Signal')
#        plt.xticks(rotation = 45)
#        plt.xlabel('Date')
#        plt.ylabel('Close Price')
#        plt.legend(loc = 'upper left')

        fig = make_subplots(vertical_spacing = 0, rows=2, cols=1, row_heights=[0.5, 0.5])

        fig.add_trace(go.Candlestick(x=df['Data'],
                                      open=df['Otwarcie'],
                                      high=df['Najwyzszy'],
                                      low=df['Najnizszy'],
                                      close=df['Zamkniecie']))

        fig.add_trace(go.Scatter(x=df['Data'], y = df['MACD'],
                                 name="MACD Line"),
                                 row=2,
                                 col=1)

        fig.add_trace(go.Scatter(x=df['Data'], y = df['Signal Line'],
                                 name="Signal Line"),
                                 row=2,
                                 col=1)

        fig.update_layout(xaxis=dict(zerolinecolor='black', showticklabels=False),
                          xaxis2=dict(showticklabels=False),
                          xaxis_rangeslider_visible=False)

        fig.update_xaxes(showline=True,
                         linewidth=1,
                         linecolor='black',
                         mirror=False)

        fig.update_layout(
                   title_text="MACD",
                   autosize=True,
                   showlegend=True,
                   )

        return fig

        # Add range slider - pojawia się problem z implementacją w przypadku kiedy mamy dwa wykresy
        # fig.update_layout(
        #    xaxis=dict(
        #        rangeselector=dict(
        #            buttons=list([
        #                dict(count=1,
        #                     label="1m",
        #                     step="month",
        #                     stepmode="backward"),
        #                dict(count=6,
        #                     label="6m",
        #                     step="month",
        #                     stepmode="backward"),
        #                dict(count=1,
        #                     label="YTD",
        #                     step="year",
        #                     stepmode="todate"),
        #                dict(count=1,
        #                     label="1y",
        #                     step="year",
        #                     stepmode="backward"),
        #                dict(step="all")
        #            ])
        #        ),
        #        rangeslider=dict(
        #            visible=True
        #        ),
        #        type="date"
        #    )
        # )
