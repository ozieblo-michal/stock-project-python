import dash_bootstrap_components as dbc

def Navbar():

    NAVBAR_STYLE = {
    "position": "relative",
    "height": 60,
    "zIndex": "1111"
    }

    navbar = dbc.NavbarSimple(
        [
            dbc.NavItem(dbc.NavLink("About",
                                    href="/homepage")),
            dbc.NavItem(dbc.NavLink("Authors",
                                    href="/authors")),
            # dbc.NavItem(dbc.NavLink("Contact",
            #                         href="/contact")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Technical analysis",
                                         header=True),
                    # dbc.DropdownMenuItem("Stochastic oscillator",
                    #                      href="/so"),
                    dbc.DropdownMenuItem("RSI",
                                         href="/rsi"),
                    dbc.DropdownMenuItem("MACD",
                                         href="/macd"),
                    dbc.DropdownMenuItem("Bollinger Bands",
                                         href="/bb"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Machine learning indicators",
                                         header=True),
                    dbc.DropdownMenuItem("Grouping of related economy sectors [K-mean clustering]",
                                         href="/kmean"),
                    # dbc.DropdownMenuItem("Stock prices prediction [Neural network]",
                    #                      href="/nn"),
                ],
                nav=True,
                in_navbar=True,
                label="Menu",
                right=True
            ),
        ],
        brand="WSE Indicators Dashboard",
        brand_href="/homepage",
        color="primary",
        dark=True,
        style=NAVBAR_STYLE
    )

    return navbar
