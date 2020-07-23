import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

df = pd.read_csv('/Users/mateuszjeczarek/Documents/GitHub/stock-project-python/wse-dash/databases/csv-files/mwig40_d.csv')

df['MA20'] = df['Zamkniecie'].rolling(window=20).mean()

df['20dSTD'] = df['Zamkniecie'].rolling(window=20).std()

df['Upper'] = df['MA20'] + (df['20dSTD']*2)
df['Lower'] = df['MA20'] - (df['20dSTD']*2)

df['Data'] = pd.to_datetime(df['Data'])

df = df[df['Data'] > (df.Data.max() - pd.Timedelta('90 day'))]

class Subplots:

    def subplots(self):

        fig = make_subplots(vertical_spacing = 0, rows=1, cols=1)

        fig.add_trace(go.Candlestick(x=df['Data'],
                                    open=df['Otwarcie'],
                                    high=df['Najwyzszy'],
                                    low=df['Najnizszy'],
                                    close=df['Zamkniecie']))

        fig.add_trace(go.Scatter(x=df['Data'], y = df['MA20'],
                                name="MA20 Line"))

        fig.add_trace(go.Scatter(x=df['Data'], y = df['Upper'],
                                name="Upper Line"))

        fig.add_trace(go.Scatter(x=df['Data'], y = df['Lower'],
                                name="Lower Line"))

        fig.update_layout(
                    title_text="Bollinger Bands Plot",
                    #autosize=True,
                    width=1300,
                    height=800,
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
