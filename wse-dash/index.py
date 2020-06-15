import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1, app2, homepage, rsi





app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/homepage':
        return homepage.layout
    elif pathname == '/authors':
        return homepage.layout
    elif pathname == '/so':
        return app1.layout
    elif pathname == '/rsi':
        return rsi.layout
    elif pathname == '/macd':
        return app1.layout
    elif pathname == '/bb':
        return app1.layout
    elif pathname == '/kmean':
        return app2.layout
    elif pathname == '/nn':
        return app2.layout
    elif pathname is None:
        return '404'
    else:
        return homepage.layout

if __name__ == '__main__':
    app.run_server(debug=True)