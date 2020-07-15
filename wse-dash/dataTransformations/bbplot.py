import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('/Users/mateuszjeczarek/PycharmProjects/stock-project-python-new_master/wse-dash/databases/csv-files/mwig40_d.csv')

df['MA20'] = df['Zamkniecie'].rolling(window=20).mean()

df['20dSTD'] = df['Zamkniecie'].rolling(window=20).std()

df['Upper'] = df['MA20'] + (df['20dSTD']*2)
df['Lower'] = df['MA20'] - (df['20dSTD']*2)

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
                    title_text="Bollinger Bands",
                    autosize=True,
                    showlegend=True,
                    )

        fig.update_layout(
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                             label="1m",
                             step="month",
                             stepmode="backward"),
                        dict(count=6,
                             label="6m",
                             step="month",
                             stepmode="backward"),
                        dict(count=1,
                             label="YTD",
                             step="year",
                             stepmode="todate"),
                        dict(count=1,
                             label="1y",
                             step="year",
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