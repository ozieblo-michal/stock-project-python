import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

df = pd.read_csv('/Users/mateuszjeczarek/Documents/GitHub/stock-project-python/wse-dash/databases/csv-files/mwig40_d.csv')

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

df['Data'] = pd.to_datetime(df['Data'])

df = df[df['Data'] > (df.Data.max() - pd.Timedelta('90 day'))]

class Subplots:

    def subplot_1(self):

        fig = make_subplots(vertical_spacing=0, rows=1, cols=1)

        fig.add_trace(go.Candlestick(x=df['Data'],
                                     open=df['Otwarcie'],
                                     high=df['Najwyzszy'],
                                     low=df['Najnizszy'],
                                     close=df['Zamkniecie']))

        fig.add_trace(go.Scatter(x=df['Data'], y=df['Zamkniecie'],
                                 name="Close Price"),
                      row=1,
                      col=1)

        fig.add_trace(
            go.Scatter(
                mode='markers',
                marker_symbol='triangle-up',
                x=df['Data'],
                y=df['Buy_Signal_price'],
                marker=dict(
                    color='rgba(85, 185, 39, 1)',
                    size=20
                ),
                name='Buy Signal Price'),
            row=1,
            col=1)

        fig.add_trace(
            go.Scatter(
                mode='markers',
                marker_symbol='triangle-down',
                x=df['Data'],
                y=df['Sell_Signal_price'],
                marker=dict(
                    color='rgba(185, 39, 39, 1)',
                    size=20
                ),
                name='Sell Signal Price'),
            row=1,
            col=1)

        fig.update_layout(
            title_text="Visually the stock buy and sell signal",
            #autosize=True,
            width=1290,
            height=800,
            showlegend=True,
        )

        return fig

    def subplot_2(self):

        fig = make_subplots(vertical_spacing=0, rows=1, cols=1)

        fig.add_trace(go.Scatter(x=df['Data'], y=df['MACD'],
                                 name="MACD Line"),
                      row=1,
                      col=1)

        fig.add_trace(go.Scatter(x=df['Data'], y=df['Signal Line'],
                                 name="Signal Line"),
                      row=1,
                      col=1)

        fig.update_layout(xaxis=dict(zerolinecolor='black', showticklabels=False),
                          xaxis2=dict(showticklabels=False),
                          xaxis_rangeslider_visible=False)

        fig.update_layout(
            title_text="Visually the MACD and Signal Line",
            #autosize=True,
            width=1290,
            height=500,
            showlegend=True,
        )

        fig.update_layout(
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=7,
                             label="7d",
                             step="day",
                             stepmode="backward"),
                        dict(count=14,
                             label="14d",
                             step="day",
                             stepmode="backward"),
                        dict(count=21,
                             label="21d",
                             step="day",
                             stepmode="backward"),
                        dict(count=1,
                             label="1m",
                             step="month",
                             stepmode="backward"),
                        dict(count=2,
                             label="2m",
                             step="month",
                             stepmode="backward"),
                        dict(step="all")
                    ])
                ),
                rangeslider=dict(
                    visible=True
                ),
                type="date"
            )
        )
        return fig
