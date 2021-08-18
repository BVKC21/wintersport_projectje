import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from datetime import date
from datetime import datetime
import numpy as np
from PIL import Image
import requests
from whitenoise import WhiteNoise

import os

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value')
])

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)

"""
url = "achtergrond.png"
#"https://github.com/BVKC21/wintersport_projectje/blob/master/achtergrond.png" 
#load background 
img = Image.open(url)
#Image.open(requests.get(url, stream=True).raw)

#create text depending on datetime
def create_text(vertrekdatum):
#vertrekdatum needs to be in YYYY-MM-DD format
    my_date = datetime.strptime(vertrekdatum, "%Y-%m-%d")
    today = datetime.now()
    delta= my_date-today
    a= "JAAAAAAAA, Let's GO"
    b= 'Bijna, nog '+ str(delta.days)+ ' dagen :)'
    c= 'Nee, nog '+ str(delta.days)+ ' dagen :('
    if delta.days < 10:
        return (b)
    elif delta.days <1:
        return (a)
    else:
        return (c)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root="static/")

#create figure element

import plotly.graph_objects as go
text = create_text('2022-03-16')
# Create figure
fig = go.Figure()

# Constants
img_width = 1600
img_height = 900
scale_factor = 0.5

# Add invisible scatter trace.
# This trace is added to help the autoresize logic work.
fig.add_trace(
    go.Scatter(
        x=[0, img_width * scale_factor],
        y=[0, img_height * scale_factor],
        mode="markers",
        marker_opacity=0
    )
)

# Configure axes
fig.update_xaxes(
    visible=False,
    range=[0, img_width * scale_factor]
)

fig.update_yaxes(
    visible=False,
    range=[0, img_height * scale_factor],
    # the scaleanchor attribute ensures that the aspect ratio stays constant
    scaleanchor="x"
)

# Add image
fig.add_layout_image(
    dict(
        x=0,
        sizex=img_width * scale_factor,
        y=img_height * scale_factor,
        sizey=img_height * scale_factor,
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        sizing="stretch",
        source=img)
)
fig.add_annotation(x=img_width * scale_factor/2, y=img_height * scale_factor/1.2,
            text="Gaan we nou al op wintersport?",
            showarrow=False,
            yshift=10,
            font_size=40,
            font_color='black')

fig.add_annotation(x=img_width * scale_factor/2, y=img_height * scale_factor/1.5,
            text=text,
            showarrow=False,
            yshift=10,
            font_size=30,
            font_color='black')
# Configure other layout
fig.update_layout(
    width=img_width * scale_factor,
    height=img_height * scale_factor,
    margin={"l": 0, "r": 0, "t": 0, "b": 0},
)

app.layout = html.Div(children=[
    html.H1(children='Hey fijne wintersport liefhebber!'),

    html.Div(children='''
        Hier vind je de belangrijkste informatie van dit moment.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)"""