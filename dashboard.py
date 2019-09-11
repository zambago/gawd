#Import python libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

#Initialise dash
app= dash.Dash()

#get data for app
np.random.seed(42)
random_x=np.random.randint(1,101,100)
random_y=np.random.randint(1,101,100)

#Add styling to app
colors = {'background':'#a7cef2', 'text':'#7FDBFF'}

#Use dash html components to diplay html on dash
app.layout = html.Div(children=[
            html.H1("Hello Kedumetse!", style={'textAlign':'center'
                                                }),
            html.Div("Welcome to your personal workspace"),
# Display graph showing assignment completion
            dcc.Graph(id="completion",
                        figure={'data':[{'x':[1,2,3],'y':[4,5,6],'type':'bar','name':'scores'},
                                        {'x':[2,4,5],'y':[6,7,8],'type':'bar','name':'total'},
                        ],
                                'layout':{
#Add colors to the graphs using html core componets
                                    'plot_bgcolor':colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font':{'color':colors['text']},
                                    'title':'My Marks!'
                                } })



])

if __name__ == '__main__':
    app.run_server()
