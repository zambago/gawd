"""
A simple learning analytics dashboard high fidelity prototype for programming assignment feedback.
"""

#Import python libraries
import dash
import time
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction
import numpy as np
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#Initialise dash application
app= dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.config['suppress_callback_exceptions'] = True

#get data for app
np.random.seed(42)
random_x=np.random.randint(1,101,100)
random_y=np.random.randint(1,101,100)

#data for marks vs assignment submitted graph
xvalues = [1,2,3,4,5,6,7,8,9,10]
yvalues = np.random.randint(1,101,10)

#data for number of submissions per assignments

trace1_value = np.random.randint(1,20,10)
trace2_value = np.random.randint(1,20,10)
trace3_value = np.random.randint(1,20,10)

#Define Traces for second Graph
trace1 = go.Bar(x=xvalues, y=trace1_value,name='Assignment1', marker={'color':'#eb34db'})
trace2 = go.Bar(x=xvalues, y=trace2_value,name='Assignment2', marker={'color':'#34eb3d'})
trace3 = go.Bar(x=xvalues, y=trace3_value,name='Assignment3', marker={'color':'#eb8634'})


#Add styling to app. Option to use external stylsheet
colors = {'background':'#a7cef2', 'text':'#7FDBFF'}

#Use dash html components to diplay html on dash
app.layout = html.Div(children=[
             dcc.Input(
                    id="my_name",
                    type='text',
                    value='Your Name',
                    style = {'display': 'inline-block', 'width': '30%', 'margin':'auto','font-size':'150%'}
                ),
             html.Div(id="my_newname", style={"border-width": "10px",'width': '30%','font-size':'150%'}),
             html.Br(),
 # Div that creates tabs with a summary of student submissions
             dcc.Tabs(id="tabs", value='tab-1', children=[
                dcc.Tab(label='Overview', value='tab-1',
                        children=[html.Div([
                                        html.Br(),
                                        html.H3("Below is an Summary of your assignment submissions"),
                                        html.Br(),
                                            dbc.Row([
                                                dbc.Col(
                                                dbc.Card(
                                                            dbc.CardBody(
                                                                [
                                                                    html.P(
                                                                        "Overall Performance: Good",
                                                                        className="card-text",
                                                                    ),
                                                                ]
                                                            ),
                                                            style={"width": "200px", "margin":"2em auto", "border-radius": "1em", "padding":"10px"},
                                                        ),
                                                        ),
                                                dbc.Col(
                                                dbc.Card(
                                                            dbc.CardBody(
                                                                [
                                                                    html.P(
                                                                        "Whats due next: Assignment 2",
                                                                        className="card-text",
                                                                    ),
                                                                ]
                                                            ),
                                                            style={"width": "200px", "margin":"2em auto", "border-radius": "1em", "padding":"10px"},
                                                        ),
                                                        ),
                                                dbc.Col(
                                                dbc.Card(
                                                            dbc.CardBody(
                                                                [
                                                                    html.P(
                                                                        "Your Average Score from x Assignments: 78%",
                                                                        className="card-text",
                                                                    ),
                                                                ]
                                                            ),
                                                            style={"width": "200px", "margin":"2em auto", "border-radius": "1em", "padding":"10px"},
                                                        ),
                                                        ),
                                                dbc.Col(
                                                dbc.Card(
                                                            dbc.CardBody(
                                                                [
                                                                    html.P(
                                                                        "Class Average Score: 72%",
                                                                        className="card-text",
                                                                    ),
                                                                ]
                                                            ),
                                                            style={"width": "200px", "margin":"2em auto", "border-radius": "1em", "padding":"10px"},
                                                        ),
                                                        ),
                                                    ]),
                                                dbc.Row([
                                                    dbc.Col(
                                                    dbc.Card(
                                                                dbc.CardBody(
                                                                    [
                                                                        html.P(
                                                                            "Rate of Assignment Submission: 3/hr",
                                                                            className="card-text",
                                                                        ),
                                                                    ]
                                                                ),
                                                                style={"width": "200px", "margin":"2em auto", "border-radius": "1em", "padding":"10px"},
                                                            ),
                                                            ),
                                                    dbc.Col(
                                                    dbc.Card(
                                                                dbc.CardBody(
                                                                    [
                                                                        html.P(
                                                                            "Most Common Errors: Type Error",
                                                                            className="card-text",
                                                                        ),
                                                                    ]
                                                                ),
                                                                style={"width": "200px", "margin":"2em auto", "border-radius": "1em", "padding":"10px"},
                                                            ),
                                                            ),
                                                    dbc.Col(
                                                    dbc.Card(
                                                                dbc.CardBody(
                                                                    [
                                                                        html.P(
                                                                            "DP Needed to Qualify: 67%",
                                                                            className="card-text",
                                                                        ),
                                                                    ]
                                                                ),
                                                                style={"width": "200px", "margin":"2em auto", "border-radius": "1em", "padding":"10px"},
                                                            ),
                                                            ),
                                                        dbc.Col(
                                                        dbc.Card(
                                                                    dbc.CardBody(
                                                                        [
                                                                            html.P(
                                                                                "Your Highest Score: 80%",
                                                                                className="card-text",
                                                                            ),
                                                                        ]
                                                                    ),
                                                                    style={"width": "200px", "margin":"2em auto", "border-radius": "1em", "padding":"10px"},
                                                                ),
                                                                ),
                                                ]),

                                            ]),
                                            ]),
                dcc.Tab(label='Analytics', value='tab-2', children=[html.H3("Select Graph from the Dropdown Menu"),html.Div(
                        dcc.Dropdown(id='mark_picker',
                            options=[
                                {'label':'Score per Assignment', 'value': 'your_score'},
                                {'label':'Number of Submissions Per Assignment', 'value': 'submission_number'}
                            ],
                            value="your_score"
                        ),style={"margin":"30px"},),dcc.Graph(id='graph-content'),]),
                ]),
                dcc.Loading(id="loading-1", children=[html.Div(id="loading-output-1")], type="default"),
                html.Div(id='tabs-content'),

                ],style={'padding':'20',"margin":"130px"})



#Callbacks to update Dashboard

#Callback to update output div for student name
@app.callback(Output(component_id="my_newname" , component_property="children"),
                    [Input(component_id="my_name", component_property="value")])
def update_name_output(input_value):
    return "Welcome to Your New Dashboard: {}".format(input_value)

#Calback to start a spinner if components take too long to load when tabs are clicked
@app.callback(Output("loading-output-1", "children"), [Input("tabs", "value")])
def input_triggers_spinner(value):
    time.sleep(1)
    return value

#Call back to update the tabs div when tabs are clicked

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == "tab-2":
        return html.H3("test")
    elif tab == "tab-1":
            return html.H3('test2')

#Callback to update graph on analytics page when dropdown menu is selected
@app.callback(Output('graph-content', 'figure'),
              [Input('mark_picker', 'value')])
def render_graph(dropdown):
    if dropdown == 'submission_number':
        return {'data':[{'x': xvalues, 'y': yvalues,'type': 'line', 'name': 'Performance'},
                        ],'layout':{"title": {"text": "Your Performance Over Time"},
                            "xaxis":{"title":"Assignment Number"},
                            "yaxis":{"title":"Average Score"}

                        }}
    elif dropdown == 'your_score':
        return {'data':[{'x': xvalues, 'y': yvalues,'type': 'bar', 'name': 'Your Score'},
                        {'x': xvalues, 'y': yvalues,'type': 'bar', 'name': 'Average Class Score'},
                        ],'layout':{"title": {"text": "Your Score Per Assignment vs Average Class Score"},
                                        "xaxis":{"title":"Assignment Number"},
                                        "yaxis":{"title":"Average Score"}
                                        } }


if __name__ == '__main__':
    app.run_server()
