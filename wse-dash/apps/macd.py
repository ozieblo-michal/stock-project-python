import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from dataTransformations.macdplot import Subplots

from databases.wsedfIntoDict import KmeanOptions

from assets.navbar import Navbar

navbar = Navbar()

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
                                    html.Div([
                                        dcc.Graph(id='g1', figure=Subplots().subplot_1())]),
                                    html.Div([
                                        dcc.Graph(id='g2', figure=Subplots().subplot_2())]),
                            html.Br()],
                       className="mt-4")])
