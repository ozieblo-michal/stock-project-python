import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import (Input,
                               Output,
                               State)

from app import app
from apps import (app1,
                  app2,
                  homepage,
                  so,
                  rsi,
                  authors,
                  kmean,
                  contact,
                  macd,
                  bb)

from dataTransformations.kmeansclustering import KMeansClustering

import os
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from plotly.subplots import make_subplots
from datetime import datetime

app.layout = html.Div([dcc.Location(id='url',
                                    refresh=False),
                       html.Div(id='page-content')])

# supports navbar menu
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/homepage':
        return homepage.layout
    elif pathname == '/authors':
        return authors.layout
    elif pathname == '/contact':
        return contact.layout
    elif pathname == '/so':
        return so.layout
    elif pathname == '/rsi':
        return rsi.layout
    elif pathname == '/macd':
        return macd.layout
    elif pathname == '/bb':
        return bb.layout
    elif pathname == '/kmean':
        return kmean.layout
    elif pathname == '/nn':
        return app2.layout
    elif pathname is None:
        return '404'
    else:
        return homepage.layout

# supports ...
@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")])
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# supports ...
@app.callback(
    Output("collapse2", "is_open"),
    [Input("collapse-button-mWIG40", "n_clicks")],
    [State("collapse2", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# supports ...
@app.callback(
    Output("collapse3", "is_open"),
    [Input("collapse-button-sWIG80", "n_clicks")],
    [State("collapse3", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# supports ...
@app.callback(
    Output("output", "children"),
    [Input("input", "value")])
def output_text(value):
    return value

# supports ...
@app.callback(
    Output('datatable','srcDoc'),
    [Input('submit-button','n_clicks')],
    [State('datatable','value')])
def update_datatable(n_clicks, csv_file):
    if n_clicks is not None:
        df = KMeansClustering()
        x = df.kMeansClustering()
        return x.to_html()

# supports ...
@app.callback(
    Output("collapse-k-plots", "is_open"),
    [Input("collapse-button-k-plots", "n_clicks")],
    [State("collapse-k-plots", "is_open")])
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# supports ...
@app.callback(
    Output("collapse-clusters", "is_open"),
    [Input("submit-button", "n_clicks")],
    [State("collapse-clusters", "is_open")])
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# supports run of the scrapper
@app.callback(
    Output('hidden-div', 'children'),
    [Input('run-scrapper-and-find-best-comp', 'n_clicks')])
def run_script_onClick(n_clicks):
    if n_clicks is not None:
        return os.system('/Users/mateuszjeczarek/Documents/GitHub/stock-project-python/wse-dash/scrapper.py')

# supports ...
@app.callback(
    Output('dd-output-container', 'children'),
    [Input('dropdown-so', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

# supports RSI visualizations
@app.callback(
    Output('candle-plot', 'figure'),
    [Input('dropdown-so', 'value')])
def update_output(value):

    path = '/Users/mateuszjeczarek/Documents/GitHub/stock-project-python/wse-dash/wseStocks/data/daily/pl/wse stocks'

    df = pd.read_csv(os.path.join(path, r'%s.txt' % value),
                     delimiter=',',
                     index_col=[0])

    date_index = []

    for i in df['<DATE>']:
        date = datetime.strptime(str(i), '%Y%m%d').strftime('%m/%d/%Y')
        date_index.append(date)

    fig = make_subplots(rows=3,
                        cols=1,
                        subplot_titles=('Title 1', 'Title 2', 'Title 3'),
                        shared_xaxes=True,
                        vertical_spacing=0.1)

    # Window length for moving average
    window_length = 14

    # Get just the adjusted close
    close = df['<CLOSE>']

    # Get the difference in price from previous step
    delta = close.diff()

    # Get rid of the first row, which is NaN since it did not have a previous
    # row to calculate the differences - nope, we need it to compare with common x axis
    delta[1] = 0
    #delta = delta[1:]

    # Make the positive gains (up) and negative gains (down) Series
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    # Calculate the EWMA
    roll_up1 = up.ewm(span=window_length).mean()
    roll_down1 = down.abs().ewm(span=window_length).mean()

    # Calculate the RSI based on EWMA
    RS1 = roll_up1 / roll_down1
    RSI1 = 100.0 - (100.0 / (1.0 + RS1))

    # Calculate the SMA
    roll_up2 = up.rolling(window_length).mean()
    roll_down2 = down.abs().rolling(window_length).mean()

    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))

    fig.add_trace(go.Scatter(x=date_index[-90:-1],
                             y=RSI1[-90:-1],
                             mode='lines',
                             name='RSI EWMA'),
                  row=1, col=1)

    fig.add_trace(go.Scatter(x=date_index[-90:-1],
                             y=RSI2[-90:-1],
                             mode='lines',
                             name='RSI SMA'),
                  row=2, col=1)

    fig.add_trace(go.Candlestick(x=date_index[-90:-1],
                                 open=df[-90:-1]['<OPEN>'],
                                 high=df[-90:-1]['<HIGH>'],
                                 low=df[-90:-1]['<LOW>'],
                                 close=df[-90:-1]['<CLOSE>'],
                                 name='candlesticks'),
                  row=3, col=1)

    fig.update_layout(height=800,
                      title_text="RSI (EWMA and SMA) for the last 90 trading days:")

    return fig

# supports Bollinger Bands vizualizations

@app.callback(
    Output('bb-plot', 'figure'),
    [Input('dropdown-so', 'value')])
def update_output(value):

    path = '/Users/mateuszjeczarek/Documents/GitHub/stock-project-python/wse-dash/wseStocks/data/daily/pl/wse stocks'

    df = pd.read_csv(os.path.join(path, r'%s.txt' % value),
                    delimiter=',',
                    index_col=[0])

    date_index = []

    for i in df['<DATE>']:
        date = datetime.strptime(str(i), '%Y%m%d').strftime('%m/%d/%Y')
        date_index.append(date)

    fig = make_subplots(vertical_spacing=0, rows=1, cols=1)

    window_length_bb = 20

    df['MA20'] = df['<CLOSE>'].rolling(window=window_length_bb).mean()

    df['20dSTD'] = df['<CLOSE>'].rolling(window=window_length_bb).std()

    df['Upper'] = df['MA20'] + (df['20dSTD'] * 2)

    df['Lower'] = df['MA20'] - (df['20dSTD'] * 2)

    fig.add_trace(go.Candlestick(x=date_index[-90:-1],
                                 open=df[-90:-1]['<OPEN>'],
                                 high=df[-90:-1]['<HIGH>'],
                                 low=df[-90:-1]['<LOW>'],
                                 close=df[-90:-1]['<CLOSE>'],
                                 name='candlesticks'))

    fig.add_trace(go.Scatter(x=date_index[-90:-1],
                             y=df[-90:-1]['MA20'],
                             name='MA20 Line'))

    fig.add_trace(go.Scatter(x=date_index[-90:-1],
                             y=df[-90:-1]['Upper'],
                             name='Upper Line'))

    fig.add_trace(go.Scatter(x=date_index[-90:-1],
                             y=df[-90:-1]['Lower'],
                             name="Lower Line"))

    fig.update_layout(
        title_text="Bollinger Bands for the last 90 trading days:",
        width=1200,
        height=800,
        showlegend=True,
    )

    return fig

# supports MACD vizualizations

@app.callback(
    Output('macd-plot', 'figure'),
    [Input('dropdown-so', 'value')])
def update_output(value):

    path = '/Users/mateuszjeczarek/Documents/GitHub/stock-project-python/wse-dash/wseStocks/data/daily/pl/wse stocks'

    df = pd.read_csv(os.path.join(path, r'%s.txt' % value),
                    delimiter=',',
                    index_col=[0])

    date_index = []

    for i in df['<DATE>']:
        date = datetime.strptime(str(i), '%Y%m%d').strftime('%m/%d/%Y')
        date_index.append(date)

    # fig = make_subplots(vertical_spacing=0, rows=2, cols=1)

    fig = make_subplots(rows=2,
                        cols=1,
                        subplot_titles=('Visually the MACD and Signal Line',
                                        'Visually the stock buy and sell signal'
                                        ),
                        shared_xaxes=True,
                        vertical_spacing=0.1)

    # Calculate the MACD and signal line indicators
    # Calculate the short term exponential moving average (EMA)
    ShortEMA = df['<CLOSE>'].ewm(span=12, adjust=False).mean()

    # Calcualte the long term exponential moving average (EMA)
    LongEMA = df['<CLOSE>'].ewm(span=26, adjust=False).mean()

    # Calculate the MACD line
    MACD = ShortEMA - LongEMA

    # Calculate the signal line
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
                    Buy.append(signal['<CLOSE>'][i])
                    flag = 1
                else:
                    Buy.append(np.nan)
            elif signal['MACD'][i] < signal['Signal Line'][i]:
                Buy.append(np.nan)
                if flag != 0:
                    Sell.append(signal['<CLOSE>'][i])
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

    fig.add_trace(go.Scatter(x=date_index[-90:-1],
                             y=df[-90:-1]['MACD'],
                             name="MACD Line"),
                  row=1,
                  col=1)

    fig.add_trace(go.Scatter(x=date_index[-90:-1],
                             y=df[-90:-1]['Signal Line'],
                             name="Signal Line"),
                  row=1,
                  col=1)

    fig.add_trace(go.Candlestick(x=date_index[-90:-1],
                                 open=df[-90:-1]['<OPEN>'],
                                 high=df[-90:-1]['<HIGH>'],
                                 low=df[-90:-1]['<LOW>'],
                                 close=df[-90:-1]['<CLOSE>'],
                                 name='candlesticks'),
                  row=2,
                  col=1)

    fig.add_trace(go.Scatter(x=date_index[-90:-1],
                             y=df[-90:-1]['<CLOSE>'],
                             name="Close Price"),
                  row=2,
                  col=1)

    fig.add_trace(go.Scatter(mode='markers',
                             marker_symbol='triangle-up',
                             x=date_index[-90:-1],
                             y=df[-90:-1]['Buy_Signal_price'],
                             marker=dict(color='rgba(85, 185, 39, 1)',
                                         size=20
                                         ),
                             name='Buy Signal Price'),
                  row=2,
                  col=1)

    fig.add_trace(go.Scatter(mode='markers',
                             marker_symbol='triangle-down',
                             x=date_index[-90:-1],
                             y=df[-90:-1]['Sell_Signal_price'],
                             marker=dict(color='rgba(185, 39, 39, 1)',
                                         size=20
                                         ),
                             name='Sell Signal Price'),
                  row=2,
                  col=1)

    fig.update_layout(
        title_text="Bollinger Bands for the last 90 trading days:",
        width=1200,
        height=1400,
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
