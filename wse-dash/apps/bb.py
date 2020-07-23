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
                 id="bb-row-0"),
         dbc.Row(dbc.Col(html.Div(html.H1("BOLLINGER BANDS")),
                         width={"size": 6, "offset": 3}),
                 id="bb-row-1"),
         dbc.Row(dbc.Col(html.Div(html.H3("Description:")),
                         width={"size": 6, "offset": 3}),
                 id="bb-row-2"),
         dbc.Row(dbc.Col(html.Div("""\
                                    The set consists of three elements. The first (and also the middle, if
                                    you look at the resulting whole plot) is the moving average (SMA) with
                                    a default value of 20. Two other components to the control lines, which
                                    are drawn below and superior. Lower band to SMA minus two standard deviations.
                                    Combined top band for SMA plus two standard deviations. There are opinions
                                    that the standard value deviation is 2.5 thanks to which 99% of the price
                                    action is between two ribbons, which means that the external injection
                                    becomes a very significant signal.
                                    """),
                         width={"size": 6, "offset": 3}),
                 id="bb-row-3"),
         dbc.Row(dbc.Col(html.Div(html.H4("Select the company to Bollinger Bands analyze:")),
                         width={"size": 6, "offset": 3}),
                 id="bb-row-4"),
         dbc.Row(dbc.Col(html.Div([
                            dcc.Dropdown(id='dropdown-so',
                                         options=KmeanOptions().wse_options_for_indicators(),
                                         value='11B'),
             html.Div(id='dd-output-container')]),
             width={"size": 6, "offset": 3}),
             id="bb-row-5"),
         dbc.Row(dbc.Col(dbc.Button("Analyze",
                                    color="primary",
                                    block=True),
                         width={"size": 6, "offset": 3}),
                 id="bb-row-6"),
         dbc.Row(dbc.Col(html.Div("Results"),
                         width={"size": 6,
                                "offset": 3}),
                 id="bb-row-7"),
         dbc.Row(dbc.Col(html.Div(html.H2(dcc.Graph(id='bb-plot')))),
                 id="bb-row-8"),
         dbc.Row(dbc.Col(dbc.Button("Export the report",
                                    color="primary",
                                    block=True),
                         width={"size": 6,
                                "offset": 3}),
                 id="bb-row-9")]
    )
])