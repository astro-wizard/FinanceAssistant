# -*- coding: utf-8 -*-

"""
FinanceAssistant.app.py
---------
app.py is the Finance Assistant Dash application.


Created : 28 December 2023
Last Modified : 8 February 2023
"""


import dash
from dash import Dash
from dash import html
import dash_bootstrap_components as dbc
import dotenv
dotenv.load_dotenv()


app = Dash(__name__,
           use_pages=True,
           pages_folder="dashboard/pages",
           assets_folder="dashboard/assets",
           external_stylesheets=[dbc.themes.SANDSTONE, dbc.icons.FONT_AWESOME],
           )


sidebar = html.Div(
    [
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fas fa-home me-2"), html.Span("Home")],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-chart-simple me-2"),
                        html.Span("Market"),
                    ],
                    href="/market",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)


app.title = "StockSavvy"
server = app.server
app.config.suppress_callback_exceptions = True


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("About", href="/about"), ),
    ],
    brand="StockSavvy",
    brand_href="#",
    color="primary",
    dark=True,
    style={"margin": 0, "height": "7vh", }
)


app.layout = html.Div([
    navbar,
    html.Div(
        [
            sidebar,
            dash.page_container
        ],
        className="content",
    ),
])


if __name__ == "__main__":
    app.run_server(debug=False)
