"""
A simple app prototype learning analytics dashboard for programming assignment feedback.
Requires dash-bootstrap-components 0.3.0 or later
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
             html.H1("Hello Kedumetse!", style={'textAlign':'center'
                                                }),
             html.Div("Welcome to the New Vula Dashboard"),

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
                                            "This tab has a card!",
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

# Display plot using dcc graph_objs
             dcc.Graph(id="plotfromdata",
                        figure={'data':[go.Scatter(x=random_x, y=random_y,mode='markers',
                        marker={'size':12,'color':colors['background']})],
                        'layout':go.Layout(title='My Personal Workspace', xaxis={'title':'xaxis title'})}

),
dcc.Graph(id="plotfromdata2",
           figure={'data':[go.Scatter(x=random_x, y=random_y,mode='markers',
           marker={'size':12,'color':colors['background']})],
           'layout':go.Layout(title='My Personal Workspace', xaxis={'title':'xaxis title'})}

)], style={'margin':'50px'})

if __name__ == '__main__':
    app.run_server()
