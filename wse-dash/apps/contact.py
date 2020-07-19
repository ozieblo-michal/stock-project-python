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
                            CONTACT CONTACT
                        """),
                 #dbc.Button("View details",color="secondary")
                ]
            #, md=4
                 ),
            dbc.Col(
                [html.H2("Mateusz Jęczarek"),
                 html.P("""\
                            index number: 89338
                        """),
                 html.P("""\
                            e-mail adress: mateusz.jeczarek@gmail.com
                            phone number: 728-326-989
                        """),
                 ])
            ])
        ],
        className="mt-4"
    )
])
