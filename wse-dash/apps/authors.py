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
            [dbc.Col(
                [html.H2("Michał Oziębło"),
                 html.P("""\
                            index number: 73754
                     """),
                 html.P("""\
                            Donec id elit non mi porta gravida at eget metus.Fusce dapibus, tellus ac cursus
                            commodo, tortor mauris condimentumnibh, ut fermentum massa justo sit amet risus
                            . Etiam porta semmalesuada magna mollis euismod. Donec sed odio dui. Donec id
                            elit nonmi porta gravida at eget metus. Fusce dapibus, tellus ac cursuscommodo,
                            tortor mauris condimentum nibh, ut fermentum massa justo sitamet risus. Etiam
                            porta sem malesuada magna mollis euismod. Donec sedodio dui.
                        """),
                 #dbc.Button("View details",color="secondary")
                ]
            #, md=4
                 ),
            dbc.Col(
                [html.H2("Mateusz Jęczarek"),
                 html.P("""\
                            Donec id elit non mi porta gravida at eget metus.Fusce dapibus, tellus ac cursus
                            commodo, tortor mauris condimentumnibh, ut fermentum massa justo sit amet risus
                            . Etiam porta semmalesuada magna mollis euismod. Donec sed odio dui. Donec id
                            elit nonmi porta gravida at eget metus. Fusce dapibus, tellus ac cursuscommodo,
                            tortor mauris condimentum nibh, ut fermentum massa justo sitamet risus. Etiam
                            porta sem malesuada magna mollis euismod. Donec sedodio dui.
                        """),
                 ])
            ])
        ],
        className="mt-4"
    )
])