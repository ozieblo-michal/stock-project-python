import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from assets.navbar import Navbar

navbar = Navbar()

layout = html.Div([
    navbar,
    dbc.Container(
        [dbc.Row(
            html.H1("THE DASHBOARD TO CREATE, ANALYZE AND OPTIMIZE INVESTMENT \
            PORTFOLIO ON THE WARSAW STOCK EXCHANGE MARKET")
            ),
        dbc.Row(
            [dbc.Col(
                [
                 html.P(),
                 html.H3("Overview"),
                 html.P(
                     """\
                        The tool for stock traders eager to maintain a view of \
                        the WSE market in order to recognize, analyze, and \
                        respond to market changes using technical analysis \
                        indicators and basic unsupervised clustering algorythm.
                     """),
                 html.H3("Main goal"),
                 html.P(
                     """\
                        Identify trends in equity securities prices movement \
                        using RSI, Stochastic Oscillator, MACD and Bollinger \
                        Bands indicators and also an unsupervised K-mean \
                        clustering to market sectors to create opportunities \
                        for capital gains.
                     """),
                 html.H3("Partial goals/Objectives"),
                 html.Ul(
                     [html.Li("Easy download of data about WSE stocks."),
                     html.Li("Visualize stocks performance to allow quick \
                     analysis."),
                     html.Li("Provide factors for price changes."),
                     html.Li("Generate investment models based on clusters \
                     detected by unsupervised learning"),
                     html.Li("Monitoring of the conducted investment portfolio")]),
                 html.H3("How to use it?"),
                 html.Ol(
                     [html.Li("Click the below button in order to download \
                     recent stock data from Stooq.com website"),
                     html.Li("[NOT DONE YET] Check trending companies from \
                     the below newly generated table for the incoming session \
                     based on technical analysis."),
                     html.Li("Check in details visualizations related with \
                     each market indicator from the navigation bar menu above."),
                     html.Li("Check related companies based on price movements \
                     via K-mean clustering from the navigation bar menu above \
                     [IN PROGRESS, DONE ONLY FOR mWIG40 AT THE MOMENT]."),
                     html.Li("[NOT DONE YET] Maintain your own portfolio by \
                     save of your transactions data, giving you the extra \
                     personalized signals.")]
                 )])]),
            dbc.Row([dbc.Col([
                html.P(""),
            # in the short future:
            # generate a dataframe with notification if
            # technical analyses will indicate signals to buy or sell
                dbc.Button("Download last stock prices",
                           id="run-scrapper-and-find-best-comp",
                           block=True,
                           size="lg",
                           color="secondary"),
                           html.Div(id='hidden-div', style={'display':'none'})
                           ],
                           width={"size": 6, "offset": 3})])],
                           className="mt-4")])
