import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import (Input,
                               Output,
                               State)

from app import app
from apps import (app1,
                  app2,
                  homepage,
                  rsi,
                  authors,
                  kmean,
                  contact)

from dataTransformations.kmeansclustering import KMeansClustering


app.layout = html.Div([dcc.Location(id='url',
                                    refresh=False),
                       html.Div(id='page-content')])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/homepage':
        return homepage.layout
    elif pathname == '/authors':
        return authors.layout
    elif pathname == '/contact':
        return contact.layout
    elif pathname == '/so':
        return app1.layout
    elif pathname == '/rsi':
        return rsi.layout
    elif pathname == '/macd':
        return app1.layout
    elif pathname == '/bb':
        return app1.layout
    elif pathname == '/kmean':
        return kmean.layout
    elif pathname == '/nn':
        return app2.layout
    elif pathname is None:
        return '404'
    else:
        return homepage.layout

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse2", "is_open"),
    [Input("collapse-button-mWIG40", "n_clicks")],
    [State("collapse2", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse3", "is_open"),
    [Input("collapse-button-mWIG80", "n_clicks")],
    [State("collapse3", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(Output("output", "children"), [Input("input", "value")])
def output_text(value):
    return value

@app.callback(Output('datatable','srcDoc'),
            [Input('submit-button','n_clicks')],
             [State('datatable','value')])

def update_datatable(n_clicks,csv_file):
    if n_clicks:
        df = KMeansClustering()
        x = df.kMeansClustering()
        return x.to_html()


@app.callback(
    Output("collapse-k-plots", "is_open"),
    [Input("collapse-button-k-plots", "n_clicks")],
    [State("collapse-k-plots", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open




@app.callback(
    Output("collapse-clusters", "is_open"),
    [Input("submit-button", "n_clicks")],
    [State("collapse-clusters", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open




if __name__ == '__main__':
    app.run_server(debug=True)