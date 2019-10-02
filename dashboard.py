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

# using dommon mark to provide additional resource to students
markdown_text = '''
### Assignment two is mearnt to test your Knowledge on writing functions.

Python is an extreamely versatile language.
Additional resources to help with this assignment can be accessed on [Linkedin Learning](http://linkedin.com/).

'''

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
                    value='Enter your name',
                    style = {'display': 'inline-block', 'width': '30%', 'margin':'auto','font-size':'150%'}
                ),
             html.Div(id="my_newname", style={"border-width": "10px",'width': '30%','font-size':'150%'}),
             html.Br(),
             dcc.Markdown(children=markdown_text, style={"border-style":'solid',"text-align":'center'}),
             html.Br(),

 # Div that creates tabs with a summary of student submissions
            html.Div(
                        [
                html.H2("Below is an Summary of your assignment submissions"),
                html.Br(),
                    dbc.Row([
                        dbc.Col(
                        dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.P(
                                                "Output from Submitted Assignments",
                                                className="card-text",
                                            ),
                                            dbc.CardLink("Click here", href="https://vula.uct.ac.za/portal"),
                                        ]
                                    ),
                                    style={"width": "18rem", 'color':'#F40009'},
                                ),
                                ),
                        dbc.Col(
                        dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.P(
                                                "Next Due Date: 13 Days",
                                                className="card-text",
                                            ),
                                        ]
                                    ),
                                    style={"width": "18rem"},
                                ),
                                ),
                        dbc.Col(
                        dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.P(
                                                "Your Average Score: 78%",
                                                className="card-text",
                                            ),
                                        ]
                                    ),
                                    style={"width": "18rem"},
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
                                    style={"width": "18rem"},
                                ),
                                ),
                            ]),
                        dbc.Row([
                            dbc.Col(
                            dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.P(
                                                    "Rate of Assignment Submission Per Hour: 3",
                                                    className="card-text",
                                                ),
                                            ]
                                        ),
                                        style={"width": "18rem"},
                                    ),
                                    ),
                            dbc.Col(
                            dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.P(
                                                    "Common Errors: Type Error",
                                                    className="card-text",
                                                ),
                                            ]
                                        ),
                                        style={"width": "18rem"},
                                    ),
                                    ),
                            dbc.Col(
                            dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.P(
                                                    "DP Needed: 67%",
                                                    className="card-text",
                                                ),
                                            ]
                                        ),
                                        style={"width": "18rem"},
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
                                            style={"width": "18rem"},
                                        ),
                                        ),
                                ]),
                        ]),
                        html.Br(),

    #create a dropdown that menu item
            dcc.Dropdown(id='mark_picker',
        options=[
            {'label': 'Your Score Per Assignment', 'value': 'your_score'},
            {'label': 'Average Class Score Per Assignment', 'value': 'class_score'}
        ],
        value="your_score"
    ),


# Display plot using dcc graph_objs
             dcc.Graph(id="plotfromdata",
                        figure={'data':[go.Bar(x=xvalues, y=yvalues)],
                        'layout':go.Layout(title='MARKS VS ASSIGNMENTS SUBMITTED', xaxis={'title':'Assignments'},yaxis={'title':'Marks'})}

                        ),

            dcc.Dropdown(id='submission_picker',
            options=[
                {'label': 'Your Submissions Per Assignment', 'value': 'YS'},
                {'label': 'Average Class Submissions Per Assignment', 'value': 'CS'}
            ],
            value="YS"
        ),

            dcc.Graph(id="plotfromdata-2",
                       figure = {'data':[trace1,trace2,trace3],
                       'layout':go.Layout(title='NUMBER OF SUBMISSIONS PER ASSIGNMENT', xaxis={'title':'Assignments'},yaxis={'title':'No of Submissions'})}


            )], style={'margin':'120px'})

#Callbacks to update Dashboard

#Callback to update output div for student name
@app.callback(Output(component_id="my_newname" , component_property="children"),
                    [Input(component_id="my_name", component_property="value")])
def update_name_output(input_value):
    return "Welcome: {}".format(input_value)


if __name__ == '__main__':
    app.run_server()
