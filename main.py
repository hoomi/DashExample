from dash import Dash, html, dcc, callback, Output, Input

import plotly.express as px
import pandas as pd
import os
import datetime
import pandas as pd


dash = Dash(__name__)
app=dash.server

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
dash.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])


@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')



if __name__ == '__main__':
    dash.run_server(host="127.0.0.1", port=int(os.environ.get("PORT", 8080)))