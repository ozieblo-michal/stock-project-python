import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from databases.wsedfIntoDict import KmeanOptions

from assets.navbar import Navbar

navbar = Navbar()

layout = html.Div([
    navbar,
    dbc.Container(
        [dbc.Row(dbc.Col(html.Div(),
                         width={"size": 6, "offset": 3}),
                 id="so-row-0"),
         dbc.Row(dbc.Col(html.Div(html.H1("STOCHASTIC OSCILLATOR")),
                         width={"size": 6, "offset": 3}),
                 id="so-row-1"),
         dbc.Row(dbc.Col(html.Div("Description"),
                         width={"size": 6, "offset": 3}),
                 id="so-row-2"),
         dbc.Row(dbc.Col(html.Div([
             dcc.Dropdown(
                 id='dropdown-so',
                 options=KmeanOptions().wse_options_for_indicators()
             ),
             html.Div(id='dd-output-container')
         ]), width={"size": 6, "offset": 3}),
             id="so-row-3"),
         dbc.Row(dbc.Col(html.Div("Run the analysis button"),
                         width={"size": 6, "offset": 3}),
                 id="so-row-4"),
         dbc.Row(dbc.Col(html.Div("Results"),
                         width={"size": 6, "offset": 3}),
                 id="so-row-5"),
         dbc.Row(dbc.Col(html.Div("Plot candles"),
                         width={"size": 6, "offset": 3}),
                 id="so-row-6"),
         dbc.Row(dbc.Col(html.Div("Plot SO"),
                         width={"size": 6, "offset": 3}),
                 id="so-row-7"),
         dbc.Row(dbc.Col(html.Div("Export the report"),
                         width={"size": 6, "offset": 3}),
                 id="so-row-8")]
    )
])