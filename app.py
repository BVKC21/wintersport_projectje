import os
import plotly.express as px
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime
import numpy as np
from PIL import Image
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

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


df= pd.read_csv("https://raw.githubusercontent.com/BVKC21/wintersport_projectje/master/data/df.csv",index_col=None,dtype={'Geslacht': 'category', 'Erg veel namen':  'category','Ik wil materiaal huren':  'category'})
fig1 = px.histogram(df, x="Ik wil materiaal huren", color='Geslacht', title='To rent or not to rent',)
fig1.update_layout(title_x=0.5)
fig2 = px.violin(df, y="Geboortedatum",box=True, points="all",title='Leeftijdsverdeling')
fig2.update_layout(title_x=0.5)


text = create_text('2022-03-22')

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,title='Wintersport 2022')

server = app.server
    
app.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.Div('Hi Fijne wintersportvrienden!', className="app-header--title")
        ]
    ),
    html.Div(className="app-base",
        children=html.Div([
            html.H5('Gaan we nou al op wintersport?',className="app-text--title" ),
            html.Div(text,className="app-text--title")
        ])
    ),
    html.Div(children=[
        dcc.Graph(
            id="graph1", 
            style={'display': 'inline-block'},
            figure=fig1
            ),
        dcc.Graph(
            id="graph2", 
            style={'display': 'inline-block'},
            figure=fig2
            )
    ])
    
])

if __name__ == '__main__':
    app.run_server(debug=True)
