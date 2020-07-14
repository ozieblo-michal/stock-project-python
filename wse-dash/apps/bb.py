import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

from databases.wsedfIntoDict import KmeanOptions

from assets.navbar import Navbar

navbar = Navbar()

textareas = html.Div([dbc.Textarea(className="mb-3",
                                   placeholder="Donec id elit non mi porta gravida at eget metus.")])

df = pd.read_csv('/Users/mateuszjeczarek/PycharmProjects/stock-project-python-new_master/wse-dash/databases/csv-files/mwig40_d.csv')

df['MA20'] = df['Zamkniecie'].rolling(window=20).mean()

df['20dSTD'] = df['Zamkniecie'].rolling(window=20).std()

df['Upper'] = df['MA20'] + (df['20dSTD']*2)
df['Lower'] = df['MA20'] - (df['20dSTD']*2)

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

layout = html.Div([navbar,
                   dbc.Container(
                       [dbc.Row(
                           [dbc.Col([
                               html.H1("Bollinger Bands")],
                               md=6),
                               dbc.Col([html.P(),
                                        html.H2("Description"),
                                        html.P("""\
                                                The set consists of three elements. The first (and also the middle, if 
                                                you look at the resulting whole plot) is the moving average (SMA) with 
                                                a default value of 20. Two other components to the control lines, which 
                                                are drawn below and superior. Lower band to SMA minus two standard deviations. 
                                                Combined top band for SMA plus two standard deviations. There are opinions 
                                                that the standard value deviation is 2.5 thanks to which 99% of the price 
                                                action is between two ribbons, which means that the external injection 
                                                becomes a very significant signal. 
                                            """)])]),
                           dbc.Row([html.H3("Selected companies:"),
                                    html.Div([dbc.Button("WIG20", id="collapse-button",
                                                         className="mb-3", color="primary"),
                                              dbc.Collapse(
                                                  dbc.Card(
                                                      dcc.Checklist(options=KmeanOptions().wig20_options_for_kmean(),
                                                                    value=[d['value'] for d in
                                                                           KmeanOptions().wig20_options_for_kmean() if
                                                                           'value' in d],
                                                                    labelStyle={'display': 'block'})),
                                                  id="collapse")]),
                                    html.Div([dbc.Button("mWIG40", id="collapse-button-mWIG40",
                                                         className="mb-3", color="primary"),
                                              dbc.Collapse(
                                                  dbc.Card(
                                                      dcc.Checklist(options=KmeanOptions().mwig40_options_for_kmean(),
                                                                    value=[d['value'] for d in
                                                                           KmeanOptions().mwig40_options_for_kmean() if
                                                                           'value' in d],
                                                                    labelStyle={'display': 'block'})),
                                                  id="collapse2")]),
                                    html.Div([dbc.Button("sWIG80", id="collapse-button-sWIG80",
                                                         className="mb-3", color="primary"),
                                              dbc.Collapse(
                                                  dbc.Card(
                                                      dcc.Checklist(options=KmeanOptions().swig80_options_for_kmean(),
                                                                    value=[d['value'] for d in
                                                                           KmeanOptions().swig80_options_for_kmean() if
                                                                           'value' in d],
                                                                    labelStyle={'display': 'block'})),
                                                  id="collapse3")])
                                    ], justify="center", align="center", className="h-50"),
                           dcc.Graph(figure=fig),
                            html.Br()],
                       className="mt-4")])
