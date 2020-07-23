import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from assets.navbar import Navbar

navbar = Navbar()

layout = html.Div([
    navbar,
    dbc.Container(
        [dbc.Row(
            [dbc.Col(
                [html.H2("Michał Oziębło"),
                 html.P("index number: 73754"),
                 html.P("e-mail adress: ozieblo.michal@icloud.com"),
                 html.P("phone number: +48 792 784 044")
                 # to do: add LinkedIn and GitHub icons with hyperlinks,
                 # bold text
                ]
                 ),
            dbc.Col(
                [html.H2("Mateusz Jęczarek"),
                 html.P("index number: 89338"),
                 html.P("e-mail adress: mateusz.jeczarek@gmail.com"),
                html.P("phone number: +48 792 784 044")
                # to do: add LinkedIn and GitHub icons with hyperlinks,
                # bold text
                 ])
            ])
        ],
        className="mt-4"
    )
])
