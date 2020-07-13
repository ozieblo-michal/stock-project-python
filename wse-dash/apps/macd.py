import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np


from assets.navbar import Navbar

navbar = Navbar()

textareas = html.Div([dbc.Textarea(className="mb-3",
                                   placeholder="Donec id elit non mi porta gravida at eget metus.")])

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

# Add range slider - pojawia się problem z implementacją w przypadku kiedy mamy dwa wykresy
#fig.update_layout(
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
#)

layout = html.Div([navbar,
                   dbc.Container(
                       [dbc.Row(
                           [dbc.Col([
                               html.H1("Moving Average Convergence / Divergence")],
                               md=6),
                            dbc.Col([html.P(),
                                     html.H2("Description"),
                                     html.P("""\
                                                Take into account the differences in values and the short-term exponential 
                                                class, connections between them by examining the convergence and divergence 
                                                of large moving. MACD is presented in the form of two lines: MACD and the 
                                                so-called signal. You can proceed to the recognition of divergences between 
                                                the connector and the price chart.
                                            """)])]),
                           dbc.Row([html.H3("Selected companies:"),
                                    html.Div([dbc.Button("WIG20", id="collapse-button",
                                                         className="mb-3", color="primary"),
                                              dbc.Collapse(
                                                  dbc.Card(dcc.Checklist(options=[{'label': 'ALIOR', 'value': 'ALR'},
                                                                                  {'label': 'PEKAO', 'value': 'PEO'},
                                                                                  {'label': 'SANPL', 'value': 'SPL'},
                                                                                  {'label': 'CCC', 'value': 'CCC'},
                                                                                  {'label': 'CDPROJEKT', 'value': 'CDR'},
                                                                                  {'label': 'CYFRPLSAT', 'value': 'CPS'},
                                                                                  {'label': 'ENERGA', 'value': 'ENG'},
                                                                                  {'label': 'EUROCASH', 'value': 'EUR'},
                                                                                  {'label': 'LOTOS', 'value': 'LTS'},
                                                                                  {'label': 'JSW', 'value': 'JSW'},
                                                                                  {'label': 'KGHM', 'value': 'KGH'},
                                                                                  {'label': 'LPP', 'value': 'LPP'},
                                                                                  {'label': 'MBANK', 'value': 'MBK'},
                                                                                  {'label': 'ORANGEPL', 'value': 'OPL'},
                                                                                  {'label': 'PKOBP', 'value': 'PKO'},
                                                                                  {'label': 'PGE', 'value': 'PGE'},
                                                                                  {'label': 'PKNORLEN', 'value': 'PKN'},
                                                                                  {'label': 'PGNIG', 'value': 'PGN'},
                                                                                  {'label': 'PZU', 'value': 'PZU'},
                                                                                  {'label': 'TAURONPE', 'value': 'TPE'}],
                                                  value=['ALR', 'PEO', 'SPL', 'CCC', 'CDR', 'CPS', 'ENG', 'EUR', 'LTS',
                                                         'JSW', 'KGH', 'LPP', 'MBK', 'OPL', 'PKO', 'PGE', 'PKN', 'PGN',
                                                         'PZU', 'TPE'],
                                                                         labelStyle={'display': 'block'})),
                                                  id="collapse")]),
                                    html.Div([dbc.Button("mWIG40", id="collapse-button-mWIG40",
                                                         className="mb-3", color="primary"),
                                              dbc.Collapse(
                                                  dbc.Card(dcc.Checklist(options=[{'label': 'ALIOR', 'value': '11B'},
                                                                                  {'label': 'PEKAO', 'value': 'ACP'},
                                                                                  {'label': 'SANPL', 'value': 'AMC'},
                                                                                  {'label': 'CCC', 'value': 'ASE'},
                                                                                  {'label': 'CDPROJEKT', 'value': 'ATT'},
                                                                                  {'label': 'CYFRPLSAT', 'value': 'BDX'},
                                                                                  {'label': 'ENERGA', 'value': 'BFT'},
                                                                                  {'label': 'EUROCASH', 'value': 'BHW'},
                                                                                  {'label': 'LOTOS', 'value': 'BNP'},
                                                                                  {'label': 'JSW', 'value': 'CAR'},
                                                                                  {'label': 'KGHM', 'value': 'CIE'},
                                                                                  {'label': 'LPP', 'value': 'CLN'},
                                                                                  {'label': 'MBANK', 'value': 'CMR'},
                                                                                  {'label': 'ORANGEPL', 'value': 'DOM'},
                                                                                  {'label': 'PKOBP', 'value': 'DVL'},
                                                                                  {'label': 'PGE', 'value': 'EAT'},
                                                                                  {'label': 'PKNORLEN', 'value': 'ECH'},
                                                                                  {'label': 'PGNIG', 'value': 'ENA'},
                                                                                  {'label': 'PZU', 'value': 'ENG'},
                                                                                  {'label': 'TAURONPE', 'value': 'EUR'},
                                                                                  {'label': 'ALIOR', 'value': 'FMF'},
                                                                                  {'label': 'PEKAO', 'value': 'FTE'},
                                                                                  {'label': 'SANPL', 'value': 'GPW'},
                                                                                  {'label': 'CCC', 'value': 'GTC'},
                                                                                  {'label': 'CDPROJEKT', 'value': 'ING'},
                                                                                  {'label': 'CYFRPLSAT', 'value': 'KER'},
                                                                                  {'label': 'ENERGA', 'value': 'KRU'},
                                                                                  {'label': 'EUROCASH', 'value': 'KTY'},
                                                                                  {'label': 'LOTOS', 'value': 'LVC'},
                                                                                  {'label': 'JSW', 'value': 'LWB'},
                                                                                  {'label': 'KGHM', 'value': 'MAB'},
                                                                                  {'label': 'LPP', 'value': 'MIL'},
                                                                                  {'label': 'MBANK', 'value': 'NEU'},
                                                                                  {'label': 'ORANGEPL', 'value': 'PKP'},
                                                                                  {'label': 'PKOBP', 'value': 'PLW'},
                                                                                  {'label': 'PGE', 'value': 'STP'},
                                                                                  {'label': 'PKNORLEN', 'value': 'TEN'},
                                                                                  {'label': 'PGNIG', 'value': 'VRG'},
                                                                                  {'label': 'PZU', 'value': 'WPL'}],
                                                  value=['11B', 'ACP', 'AMC', 'ASE', 'ATT', 'BDX', 'BFT', 'BHW', 'CAR',
                                                         'CIE', 'CLN', 'CMR', 'DOM', 'DVL', 'EAT', 'ECH', 'ENA', 'ENG',
                                                         'EUR', 'FMF', 'FTE', 'GPW', 'GTC', 'ING', 'KER', 'KRU', 'KTY',
                                                         'LVC', 'LWB', 'MAB', 'MIL', 'NEU', 'PKP', 'PLW', 'STP', 'TEN',
                                                         'VRG', 'WPL'],
                                                  labelStyle={'display': 'block'})), id="collapse2")]),
                                    html.Div([dbc.Button("mWIG80", id="collapse-button-mWIG80",
                                                         className="mb-3", color="primary"),
                                              dbc.Collapse(
                                                  dbc.Card(dcc.Checklist(options=[{'label': 'ALIOR', 'value': '11B'},
                                                                                  {'label': 'PEKAO', 'value': 'ACP'},
                                                                                  {'label': 'SANPL', 'value': 'AMC'}],
                                                                         value=['11B', 'ACP', 'AMC'],
                                                                         labelStyle={'display': 'block'})),
                                                  id="collapse3")])
                                    ], justify="center", align="center", className="h-50"),
                           dcc.Graph(figure=fig),
                            html.Br()],
                       className="mt-4")])

# to do:
#        cross validation of k-mean algorythm
# wyniki jako wysuwany kontener?
# loading animation
