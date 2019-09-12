#Import python libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd

#Initialise dash application
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
             html.Div("Vula Dashboard"),
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

)])

if __name__ == '__main__':
    app.run_server()
