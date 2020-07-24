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
                         width={"size": 12, "offset": 0}),
                 id="macd-row-1"),
         dbc.Row(dbc.Col([html.Div(
         "Take into account the differences in values and the short-term exponential \
         class, connections between them by examining the convergence and divergence \
         of large moving. MACD is presented in the form of two lines: MACD and the \
         so-called signal. You can proceed to the recognition of divergences between \
         the connector and the price chart."
         ),
         html.P("")])),
        dbc.Row(dbc.Col(html.Div("Select the company to analyze:"),
                                 width={"size": 6, "offset": 3}),
                         id="bb-row-2"),
         dbc.Row(dbc.Col(html.Div([
                            dcc.Dropdown(id='dropdown-so',
                                         options=KmeanOptions().wse_options_for_indicators(),
                                         value='11B')
                                  ]),
             width={"size": 6, "offset": 3}),
             id="bb-row-3"),
         dbc.Row(dbc.Col([html.Div([dcc.Graph(id='macd-plot'),
                                    ])]),
                 id="bb-row-4"),
         dbc.Row(dbc.Col([html.Div(id="update-table")],
                         width={"size": 6,
                                "offset": 3}),
                 id="bb-row-5")
         ])])