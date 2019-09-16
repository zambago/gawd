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

#get data for app
np.random.seed(42)
random_x=np.random.randint(1,101,100)
random_y=np.random.randint(1,101,100)

#Add styling to app. Option to use external stylsheet
colors = {'background':'#a7cef2', 'text':'#7FDBFF'}


#Use dash html components to diplay html on dash
app.layout = html.Div(children=[
             html.H1("Hello Kedumetse!", style={'textAlign':'left'
                                                }),

 # Div that creates a Navigation tab in dasbboard
            html.Div(
            [
                html.H2("Welcome to the New Vula Dashboard"),
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
    #create a dropdown that menu item
            dcc.Dropdown(
        options=[
            {'label': 'Assignment 1', 'value': 'Ass1'},
            {'label': 'Select Assignment', 'value': 'Select'},
            {'label': 'Assignment 2', 'value': 'Ass2'},
            {'label': 'Assignment 3', 'value': 'Ass3'}
        ],
        multi=True,
        value="Select"
    ),
        dcc.Dropdown(
        options=[
            {'label': 'Highest Score', 'value': 'HS'},
            {'label': 'View Progress', 'value': 'VP'},
            {'label': 'DP Needed', 'value': 'DP'}
        ],
        multi=True,
        value="VP"
    ),

# Display plot using dcc graph_objs
             dcc.Graph(id="plotfromdata",
                        figure={'data':[go.Scatter(x=random_x, y=random_y,mode='markers',
                        marker={'size':12,'color':colors['background']})],
                        'layout':go.Layout(title='My Personal Workspace', xaxis={'title':'xaxis title'})}

)], style={'margin':'50px'})

if __name__ == '__main__':
    app.run_server()
