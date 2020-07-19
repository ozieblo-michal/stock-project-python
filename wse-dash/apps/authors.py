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
                            index number: 89338
                     """),
                 html.P("""\
                            A graduate of the University of Warsaw, currently a post-graduate student of data
                            engineering - big data at the Warsaw School of Economics. He started his professional 
                            career in the insurance sector (Generali, Warta), where he dealt with sales force 
                            settlements. Then he worked as a data analyst in projects for companies in the FMCG 
                            industry. Currently associated with the banking sector as a data warehouse analyst 
                            responsible for automation of bonus system accounting.
                        """),
                 ])
            ])
        ],
        className="mt-4"
    )
])
