import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from assets.navbar import Navbar

# to do: add photos, merge with Contact page

navbar = Navbar()

layout = html.Div([
    navbar,
    dbc.Container(
        [dbc.Row(
            [dbc.Col(
                [html.H2("Michał Oziębło"),
                 html.P("""\
                            index: 73754
                     """),
                 html.P("""\
                            Centralized Monitoring Analyst in AstraZeneca Pharma Poland. Michał studied Biotechnology at the University of Warsaw,\
                            Finance and accounting at the SGH Warsaw School of Economics and is now enroled into Data Engineering post-graduate studies,\
                            also at the SGH. His MSc theses were about in vitro characterization of stem cells from an adiposte tissue and their potention to myogenic\
                            differentiation, and about valuation and growth strategies for biotech companies. He worked among others in MedImmune, MSD \
                            and BNP Paribas Securities Services.
                        """),
                ]
                 ),
            dbc.Col(
                [html.H2("Mateusz Jęczarek"),
                 html.P("""\
                            index: 89338
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
            ]),
        dbc.Row(
            [dbc.Col(
                [
                 html.P("E-mail: ozieblo.michal@icloud.com"),
                 html.P("Mobile: +48 792 784 044")
                 # to do: add LinkedIn and GitHub icons with hyperlinks,
                 # bold text
                ]
                 ),
            dbc.Col(
                [
                 html.P("E-mail: mateusz.jeczarek@gmail.com"),
                html.P("Mobile: +48 792 784 044")
                # to do: add LinkedIn and GitHub icons with hyperlinks,
                # bold text
                 ])
            ])
        ],
        className="mt-4"
    )
])
