from dash import Dash, html, dcc, callback, Output, Input
# import plotly.express as px
# import pandas as pd
import os
import datetime

from flask import Flask, render_template

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)
server=app.server

# app.layout = html.Div([
#     html.H1(children='Title of Dash App', style={'textAlign':'center'}),
#     dcc.Dropdown(['test','test2'], 'Canada', id='dropdown-selection'),
#     dcc.Graph(id='graph-content')
# ])

# # @callback(
# #     Output('graph-content', 'figure'),
# #     Input('dropdown-selection', 'value')
# # )
# # def update_graph(value):
# #     dff = df[df.country==value]
# #     return px.line(dff, x='year', y='pop')

# app.layout = html.Div([html.H2('Hello World')])




# server = Flask(__name__)


@server.route("/")
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    dummy_times = [
        datetime.datetime(2018, 1, 1, 10, 0, 0),
        datetime.datetime(2018, 1, 2, 10, 30, 0),
        datetime.datetime(2018, 1, 3, 11, 0, 0),
    ]

    return render_template("index.html", times=dummy_times)


if __name__ == '__main__':
    server.run(host="127.0.0.1", port=int(os.environ.get("PORT", 8080)))