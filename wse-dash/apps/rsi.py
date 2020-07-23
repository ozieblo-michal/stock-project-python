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
         dbc.Row(dbc.Col([html.Div(
         "The RSI is a momentum oscillator intended \
         to graph the actual and historical strength or weakness of analyzed \
         securities or the market based on closing prices during a recent \
         trading period."
         ),
         html.Div(
         "The nearer indicators value is to 0, the weaker the momentum is for price movements. \
         Oppositely an RSI closer to 100 shows a signal of a stronger momentum period. As stated \
         by author - John Welles Wilder Jr., any number above threshold equal 70 should be \
         assessed as overbought and below 30 as oversold. An relative strength index between 30 \
         and 70 should be considered as neutral and around 50 like no trend."
         ),
         html.P("")])),
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
