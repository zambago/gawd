"""
A simple learning analytics dashboard for programming assignment feedback.

"""

#Import python libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction
import numpy as np
import pandas as pd

#Initialise dash application
app= dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#get data for app
np.random.seed(42)
random_x=np.random.randint(1,101,100)
random_y=np.random.randint(1,101,100)

#data for marks vs assignment submitted graph
xvalues = [1,2,3,4,5,6,7,8,9,10]
yvalues = np.random.randint(1,101,10)

#data for number of submissions per assignments

trace1_value = np.random.randint(1,31,10)
trace2_value = np.random.randint(1,20,10)
trace3_value = np.random.randint(1,21,10)

#Define Traces for second Graph
trace1 = go.Bar(x=xvalues, y=trace1_value,name='Assignment1', marker={'color':'#eb34db'})
trace2 = go.Bar(x=xvalues, y=trace2_value,name='Assignment2', marker={'color':'#34eb3d'})
trace3 = go.Bar(x=xvalues, y=trace3_value,name='Assignment3', marker={'color':'#eb8634'})


#Add styling to app. Option to use external stylsheet
colors = {'background':'#a7cef2', 'text':'#7FDBFF'}

#Use dash html components to diplay html on dash
app.layout = html.Div(children=[
             html.H1("Hello Kedumetse!", style={'textAlign':'left'
                                                }),
             html.Br(),

 # Div that creates a Navigation tab in dasbboard
            html.Div(
            [
                html.H2("Below is an overview of your dashboard"),
                html.Br(),
                dbc.Tab(
                        label="Overview",
                        style={"padding": "10px"},
                        ),
                        dbc.Tab(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.P(
                                            "View Your Common Error from submitted Assignments",
                                            className="card-text",
                                        ),
                                        dbc.Button("Click here", color="success"),
                                    ]
                                )
                            ),

                        ),
                        ]),

#Row that displays different data to user
            html.Div([
                            html.Div(
                                [html.H6(id="countdownText"), html.P("Time Till Next Dateline: 13 Days")],
                                id="countdown",
                                className="mini_container",
                                style={"padding": "20px"},
                            ),
                                html.Div(
                                    [html.H6(id="highestscoreText"), html.P("Your Highest Score: 80%")],
                                    id="highestscore",
                                    className="mini_container",
                                    style={"padding": "20px"},
                            ),
                                html.Div(
                                    [html.H6(id="averagescoreText"), html.P("Your Average Score: 78%")],
                                    id="averagescore",
                                    className="mini_container",
                                    style={"padding": "20px"},
                            ),
                                html.Div(
                                    [html.H6(id="dpneededText"), html.P("DP Needed: 67%")],
                                    id="dpneeded",
                                    className="mini_container",
                                    style={"padding": "20px"},
                            ),
                             ],
                                 id="info-container",
                                 className="row container-display",
                                 style={"align": "center"},

                            ),

# Div with link to more resources
               html.Div(
                    [
                        html.A(
                            html.Button("Recommended Learning Resources", id="learn-more-button"),
                            href="https://www.linkedin.com",
                        ),
                    ],
                    id="resourcebutton",
                    style={"margin-bottom": "25px", "float":"right"},
                ),
    #create a dropdown that menu item
            dcc.Dropdown(id='mark_picker',
        options=[
            {'label': 'Your Score Per Assignment', 'value': 'your_score'},
            {'label': 'Select Visualisation', 'value': 'Select'},
            {'label': 'Average Class Score Per Assignment', 'value': 'class_score'}
        ],
        multi=True,
        value="Select"
    ),
        dcc.Dropdown(id='submission_picker',
        options=[
            {'label': 'Your Submissions Per Assignment', 'value': 'YS'},
            {'label': 'Submission Per Assignment Visualisation', 'value': 'SA'},
            {'label': 'Average Class Submissions Per Assignment', 'value': 'CS'}
        ],
        multi=True,
        value="SA"
    ),

# Display plot using dcc graph_objs
             dcc.Graph(id="plotfromdata",
                        figure={'data':[go.Bar(x=xvalues, y=yvalues)],
                        'layout':go.Layout(title='MARKS VS ASSIGNMENTS SUBMITTED', xaxis={'title':'Assignments'},yaxis={'title':'Marks'})}

                        ),

            dcc.Graph(id="plotfromdata-2",
                       figure = {'data':[trace1,trace2,trace3],
                       'layout':go.Layout(title='NUMBER OF SUBMISSIONS PER ASSIGNMENT', xaxis={'title':'Assignments'},yaxis={'title':'No of Submissions'})}


            )], style={'margin':'120px'})

if __name__ == '__main__':
    app.run_server()
