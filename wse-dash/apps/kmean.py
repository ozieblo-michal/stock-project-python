import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dataTransformations.kmean_and_sil_plots import Subplots

from assets.navbar import Navbar

navbar = Navbar()

textareas = html.Div([dbc.Textarea(className="mb-3",
                                   placeholder="Donec id elit non mi porta gravida at eget metus.")])

layout = html.Div([navbar,
                   dbc.Container(
                       [dbc.Row(
                           [dbc.Col([
                               html.H1("Grouping of related economy sectors using the K-mean clustering algorythm")],
                               md=6),
                            dbc.Col([html.P(),
                                     html.H2("Description"),
                                     html.P("""\
                                                Donec id elit non mi porta gravida at eget metus.Fusce dapibus, tellus ac cursus
                                                commodo, tortor mauris condimentumnibh, ut fermentum massa justo sit amet risus
                                                . Etiam porta semmalesuada magna mollis euismod. Donec sed odio dui. Donec id
                                                elit nonmi porta gravida at eget metus. Fusce dapibus, tellus ac cursuscommodo,
                                                tortor mauris condimentum nibh, ut fermentum massa justo sitamet risus. Etiam
                                                porta sem malesuada magna mollis euismod. Donec sedodio dui.
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
                           dbc.Row([
                                dbc.Button("Open collapse", id="collapse-button-k-plots",
                                           className="mb-3", color="primary"),
                                html.Div([
                                    dbc.Collapse(
                                        dbc.Card(
                                            dbc.CardBody([
                                                    dcc.Graph(figure=Subplots().subplots())
                                            ]), style={"height": "80vh", "width": "80vh"}
                                        ),id="collapse-k-plots")
                                ])
                           ], justify="center", align="center", className="h-50"),
                           dbc.Row([
                                html.H3("Number of clusters:"),
                                html.Div([dbc.Input(id="input", placeholder="Type the number of K", type="text"),
                                          html.Br(),
                                          html.P(id="output")])], justify="center", align="center", className="h-50"),
                            html.Br(),
                            dbc.Row([
                               html.Div([
                                   # dcc.Input(id='csv-files-loc', style={'fontSize': 12}),
                                   html.Button(id='submit-button', children='Run clusters searching'),
                                   dbc.Collapse(
                                       dbc.Card(dbc.CardBody([
                                               html.Iframe(id='datatable',
                                               sandbox='',
                                               style={'height': '80vh', 'width': 720}),
                                        dbc.Button("Download the result as a CSV file", color="secondary", block=True)
                                       ])),id="collapse-clusters"),
                               ]),
                             ], justify="center", align="center", className="h-50")],
                       className="mt-4")])

# to do:
#        cross validation of k-mean algorythm
# wyniki jako wysuwany kontener?
# loading animation