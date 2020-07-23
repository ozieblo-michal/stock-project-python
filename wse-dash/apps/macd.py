import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from assets.navbar import Navbar

from databases.wsedfIntoDict import KmeanOptions

navbar = Navbar()

layout = html.Div([
    navbar,
    dbc.Container(
        [dbc.Row(dbc.Col(html.Div(),
                         width={"size": 6, "offset": 3}),
                 id="macd-row-0"),
         dbc.Row(dbc.Col(html.Div(html.H1("MOVING AVERAGE CONVERGENCE / DIVERGENCE (MACD)")),
                         width={"size": 6, "offset": 3}),
                 id="macd-row-1"),
         dbc.Row(dbc.Col(html.Div(html.H3("Description:")),
                         width={"size": 6, "offset": 3}),
                 id="macd-row-2"),
         dbc.Row(dbc.Col(html.Div("""\
                                    Take into account the differences in values and the short-term exponential 
                                    class, connections between them by examining the convergence and divergence 
                                    of large moving. MACD is presented in the form of two lines: MACD and the 
                                    so-called signal. You can proceed to the recognition of divergences between 
                                    the connector and the price chart.
                                    """),
                         width={"size": 6, "offset": 3}),
                 id="macd-row-3"),
         dbc.Row(dbc.Col(html.Div(html.H4("Select the company to MACD analyze:")),
                         width={"size": 6, "offset": 3}),
                 id="macd-row-4"),
         dbc.Row(dbc.Col(html.Div([
                            dcc.Dropdown(id='dropdown-so',
                                         options=KmeanOptions().wse_options_for_indicators(),
                                         value='11B'),
             html.Div(id='dd-output-container')]),
             width={"size": 6, "offset": 3}),
             id="macd-row-5"),
         dbc.Row(dbc.Col(dbc.Button("Analyze",
                                    color="primary",
                                    block=True),
                         width={"size": 6, "offset": 3}),
                 id="macd-row-6"),
         dbc.Row(dbc.Col(html.Div("Results"),
                         width={"size": 6,
                                "offset": 3}),
                 id="macd-row-7"),
         dbc.Row(dbc.Col(html.Div(html.H2(dcc.Graph(id='macd-plot')))),
                 id="macd-row-8"),
         dbc.Row(dbc.Col(dbc.Button("Export the report",
                                    color="primary",
                                    block=True),
                         width={"size": 6,
                                "offset": 3}),
                 id="macd-row-9")]
    )
])

# import dash_core_components as dcc
# import dash_html_components as html
# import dash_bootstrap_components as dbc
#
# from dataTransformations.macdplot import Subplots
#
# from databases.wsedfIntoDict import KmeanOptions
#
# from assets.navbar import Navbar
#
# navbar = Navbar()
#
# layout = html.Div([navbar,
#                    dbc.Container(
#                        [dbc.Row(
#                            [dbc.Col([
#                                html.H1("Moving Average Convergence / Divergence")],
#                                md=6),
#                                dbc.Col([html.P(),
#                                         html.H2("Description"),
#                                         html.P("""\
#                                                 Take into account the differences in values and the short-term exponential
#                                                 class, connections between them by examining the convergence and divergence
#                                                 of large moving. MACD is presented in the form of two lines: MACD and the
#                                                 so-called signal. You can proceed to the recognition of divergences between
#                                                 the connector and the price chart.
#                                             """)])]),
#                            dbc.Row([html.H3("Selected companies:"),
#                                     html.Div([dbc.Button("WIG20", id="collapse-button",
#                                                          className="mb-3", color="primary"),
#                                               dbc.Collapse(
#                                                   dbc.Card(
#                                                       dcc.Checklist(options=KmeanOptions().wig20_options_for_kmean(),
#                                                                     value=[d['value'] for d in
#                                                                            KmeanOptions().wig20_options_for_kmean() if
#                                                                            'value' in d],
#                                                                     labelStyle={'display': 'block'})),
#                                                   id="collapse")]),
#                                     html.Div([dbc.Button("mWIG40", id="collapse-button-mWIG40",
#                                                          className="mb-3", color="primary"),
#                                               dbc.Collapse(
#                                                   dbc.Card(
#                                                       dcc.Checklist(options=KmeanOptions().mwig40_options_for_kmean(),
#                                                                     value=[d['value'] for d in
#                                                                            KmeanOptions().mwig40_options_for_kmean() if
#                                                                            'value' in d],
#                                                                     labelStyle={'display': 'block'})),
#                                                   id="collapse2")]),
#                                     html.Div([dbc.Button("sWIG80", id="collapse-button-sWIG80",
#                                                          className="mb-3", color="primary"),
#                                               dbc.Collapse(
#                                                   dbc.Card(
#                                                       dcc.Checklist(options=KmeanOptions().swig80_options_for_kmean(),
#                                                                     value=[d['value'] for d in
#                                                                            KmeanOptions().swig80_options_for_kmean() if
#                                                                            'value' in d],
#                                                                     labelStyle={'display': 'block'})),
#                                                   id="collapse3")])
#                                     ], justify="center", align="center", className="h-50"),
#                                     html.Div([
#                                         dcc.Graph(id='g1', figure=Subplots().subplot_1())]),
#                                     html.Div([
#                                         dcc.Graph(id='g2', figure=Subplots().subplot_2())]),
#                             html.Br()],
#                        className="mt-4")])
