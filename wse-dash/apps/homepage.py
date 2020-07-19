import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
#from dash.dependencies import Input, Output
#from app import app

from assets.navbar import Navbar

navbar = Navbar()

layout = html.Div([

    navbar,
    dbc.Container(
        [dbc.Row(
            html.H1("THE DASHBOARD TO CREATE, ANALYZE AND OPTIMIZE INVESTMENT PORTFOLIO ON THE WARSAW STOCK EXCHANGE MARKET")
            ),
        dbc.Row(
            [dbc.Col(
                [
                 html.H3("Overview"),
                 html.P(
                     """\
                        For stock traders eager to maintain a view of the market in order to recognize, 
                        analyze, and respond to market changes.
                     """),
                 html.H3("Main goal"),
                 html.P(
                     """\
                        Identify trends in equity securities prices movement using a standard technical analysis 
                        and unsupervised algorithms to create opportunities for capital gains.
                     """),
                 html.H3("Partial goals/Objectives"),
                 html.Ul(
                     [html.Li("Visualize stocks performance to allow quick analysis."),
                     html.Li("Provide factors for price changes."),
                     html.Li("Generate investment models based on clusters detected by unsupervised learning"),
                     html.Li("Monitoring of the conducted investment portfolio")]
                 ),
                 ], md=7),
                dbc.Col(
                    [
                     dcc.Graph(figure={"data": [{"x": [1, 2, 3],
                                                 "y": [1, 4, 9]}]})])]
        ),
            dbc.Row([dbc.Col([
                dbc.Button("Search valuable companies for today",
                           id="run-scrapper-and-find-best-comp",
                           color="secondary"),

html.Div(id='hidden-div', style={'display':'none'})

            ],
                md=8)
            ])
        ],
        className="mt-4"
    ),
])