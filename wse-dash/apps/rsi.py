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
                 id="so-row-0"),
         dbc.Row(dbc.Col(html.Div(html.H1("RELATIVE STRENGTH INDEX")),
                         width={"size": 6, "offset": 3}),
                 id="so-row-1"),
         dbc.Row(dbc.Col(html.Div("Select the company to analyze:"),
                         width={"size": 6, "offset": 3}),
                 id="so-row-2"),
         dbc.Row(dbc.Col(html.Div([
                            dcc.Dropdown(id='dropdown-so',
                                         options=KmeanOptions().wse_options_for_indicators(),
                                         value='11B')
                                  ]),
             width={"size": 6, "offset": 3}),
             id="so-row-3"),
         dbc.Row(dbc.Col([html.Div([dcc.Graph(id='candle-plot'),
                                    dcc.Graph(id='tableRSI1'),
                                    dcc.Graph(id='tableRSI2'),
                                    dcc.Graph(id='tableRSI3'),
                                    dcc.Graph(id='tableRSI4')
                                    ])],
                         width={"size": 6,
                                "offset": 3}),
                 id="so-row-6"),
         dbc.Row(dbc.Col([html.Div(id="update-table")],
                         width={"size": 6,
                                "offset": 3}),
                 id="so-row-7")
         ])])