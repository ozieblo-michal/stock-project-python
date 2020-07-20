import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
#from dash.dependencies import Input, Output
#from app import app

from assets.navbar import Navbar
from assets.sidebar import Sidebar

navbar = Navbar()
sidebar = Sidebar()

CONTENT_STYLE = {
    "margin-top": "2rem",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "1rem 1rem",
}

layout = html.Div([


    dbc.Container(
        [
navbar,
            dbc.Row(
            [dbc.Col(
                [
                    sidebar,
                    html.H2("Heading"),
                 html.P(
                     """\
Donec id elit non mi porta gravida at eget metus.Fusce dapibus, tellus ac cursus
commodo, tortor mauris condimentumnibh, ut fermentum massa justo sit amet risus
. Etiam porta semmalesuada magna mollis euismod. Donec sed odio dui. Donec id
elit nonmi porta gravida at eget metus. Fusce dapibus, tellus ac cursuscommodo,
tortor mauris condimentum nibh, ut fermentum massa justo sitamet risus. Etiam
porta sem malesuada magna mollis euismod. Donec sedodio dui."""
                 ),
                 dbc.Button("View details",
                            color="secondary")], md=4),
dcc.Link('Go to App 2', href='/apps/app2')])],
        className="mt-4"
    )

], style=CONTENT_STYLE)