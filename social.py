"""
A simple learning analytics dashboard for programming assignment feedback.

"""

#Import python libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd

#Initialise dash application
app= dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[
             html.H1("Hello Kedumetse!", style={'textAlign':'left'
                                                }),
             html.Br(),

 # Div that creates a Navigation tab in dasbboard
            html.Div(
            [
                html.H2("Welcome to the New Vula Dashboard"),
                html.Br(),
                dbc.Tabs(
                    [
                        dbc.Tab(
                            label="Overview",
                            style={"padding": "10px"},
                        ),
                        dbc.Tab(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.P(
                                            "View Your Common Error",
                                            className="card-text",
                                        ),
                                        dbc.Button("Click here", color="success"),
                                    ]
                                )
                            ),
                            label="Analytics",
                            style={"padding": "10px"},
                        ),
                        dbc.Tab(
                            label="Social",
                            style={"padding": "10px"},
                            ),
                    ]
                ),
            ]
        ),
#Div that shows results of submitted programming assignments
                html.Div([
                    dbc.Row([
                        dbc.Col(
                        "Top Friend Display",
                        style={"height": "100px", "border-style": "solid"},
                        ),
                    ]),
                dbc.Row([
                    dbc.Col(
                    "Summary of Assignment Submissions",
                    style={"height": "100px", "border-style": "solid"},
                    ),
                ]),
                ]),
                ], style={'margin':'50px'})

if __name__ == '__main__':
    app.run_server()
