import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dataTransformations.kmean_and_sil_plots import Subplots

from databases.wsedfIntoDict import KmeanOptions

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
                                                  dbc.Card(dcc.Checklist(options=KmeanOptions().wig20_options_for_kmean(),
                                                  value=[d['value'] for d in KmeanOptions().wig20_options_for_kmean() if 'value' in d],
                                                                         labelStyle={'display': 'block'})),
                                                  id="collapse")]),
                                    html.Div([dbc.Button("mWIG40", id="collapse-button-mWIG40",
                                                         className="mb-3", color="primary"),
                                              dbc.Collapse(
                                                  dbc.Card(dcc.Checklist(options=KmeanOptions().mwig40_options_for_kmean(),
                                                                         value=[d['value'] for d in KmeanOptions().mwig40_options_for_kmean() if 'value' in d],
                                                                         labelStyle={'display': 'block'})),
                                                  id="collapse2")]),
                                    html.Div([dbc.Button("sWIG80", id="collapse-button-sWIG80",
                                                         className="mb-3", color="primary"),
                                              dbc.Collapse(
                                                  dbc.Card(dcc.Checklist(options=KmeanOptions().swig80_options_for_kmean(),
                                                                         value=[d['value'] for d in KmeanOptions().swig80_options_for_kmean() if 'value' in d],
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