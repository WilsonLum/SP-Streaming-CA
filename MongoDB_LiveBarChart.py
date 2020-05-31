import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import random

import pymongo
from pymongo import MongoClient
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='CA2 Streaming Assignment', id='first'),
    dcc.Interval(id='timer', interval=30*1000),
    html.Div(id='dummy'),
    dcc.Graph(
            id='example-graph',
        )
])

@app.callback(output=Output('example-graph', 'figure'),
              inputs=[Input('timer', 'n_intervals')])

def update_graph(n_clicks):

    client = MongoClient()
    db = client.bakeinc
    mycollections = db.user

    X = []
    Y = []

    df = pd.DataFrame(list(mycollections.find()))
    x = df['num_transactions']
    y = df['time_window']

    X = x[-20:].values
    Y = y[-20:].values

    return {
                'data': [
                    {'x': Y,
                     'y': X,
                     'type': 'bar', 'name': 'SF'},
                   
                ],
                'layout': {
                    'title': 'Bakeinc Transactions Data Visualization'
                }
            }


if __name__ == '__main__':
    app.run_server(debug=True)