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
    colors = {
        'red': 'app-red--title',
        'orange': 'app-orange--title',
        'green':'app-green--title'
    }
    #vertrekdatum needs to be in YYYY-MM-DD format
    my_date = datetime.strptime(vertrekdatum, "%Y-%m-%d")
    today = datetime.now()
    delta= my_date-today
    a= "JAAAAAAAA, Let's GO"
    b= 'Bijna, nog '+ str(delta.days)+ ' dagen :)'
    c= 'Nee, nog '+ str(delta.days)+ ' dagen :('
    if delta.days < 10:
        return (b,colors['orange'])
    elif delta.days <1:
        return (a,colors['green'])
    else:
        return (c,colors['red'])

# inladen dataframes
getallen= pd.read_csv("https://raw.githubusercontent.com/BVKC21/wintersport_projectje/master/data/getallen.csv",
index_col=None,
dtype={'Skitag': 'float64',
'artiest': 'float64',
'avondeten': 'float64',
'dal_piste_team': 'float64',
'extra_namen': 'int64',
'films': 'float64',
'flugel': 'float64',

'geslacht': 'int64',
'kat_hond': 'float64',
'kneipe': 'float64',
'leeftijd': 'float64',
'lezen': 'float64',
'materiaal_huur': 'object',
'muziek': 'float64',
'pre_ski_feestje': 'float64',
'skistijl': 'float64',
'stad': 'object',
'tosti': 'float64'},
parse_dates=['tijdstempel','geboortedatum']
)
getallen.drop('Unnamed: 0',axis=1, inplace=True)

waarden= pd.read_csv("https://raw.githubusercontent.com/BVKC21/wintersport_projectje/master/data/waarden.csv",
index_col=None,
dtype={'Skitag': 'float64',
'artiest': 'category',
'avondeten': 'float64',
'dal_piste_team': 'category',
'extra_namen': 'category',
'films': 'category',
'flugel': 'float64',
'geslacht': 'category',
'kat_hond': 'category',
'kneipe': 'float64',
'leeftijd': 'float64',
'lezen': 'float64',
'materiaal_huur': 'category',
'muziek': 'category',
'pre_ski_feestje': 'float64',
'skistijl': 'float64',
'stad': 'category',
'tosti': 'category'},
parse_dates=['tijdstempel','geboortedatum']
)
waarden.drop('Unnamed: 0', axis=1, inplace=True)

#Creeren grafieken 
huren = px.histogram(waarden, x="materiaal_huur", color='geslacht', title='Lekker huren',labels=dict(x="Type verhuur", y="Aantal personen", color="Geslacht"))
huren.update_layout(title_x=0.5)

violin = px.violin(getallen, y="geboortedatum",box=True, points="all",title='Uit met alle leeftijden',labels=dict(y="Geboortedatum"))
violin.update_layout(title_x=0.5)

sunburst = px.sunburst(waarden.dropna(), path=['stad','kat_hond', 'dal_piste_team','tosti'], 
color= 'stad', 
title= 'Hoe kom ik erachter wat iemand bij zijn tosti wil?'
)
sunburst.update_layout(title_x=0.5)

artiest = px.histogram(waarden.dropna(), x="artiest",
color="geslacht",
title= 'Wat is onze favoriete artiest',
labels=dict(x='Artiest', y='Fans!', color= 'Geslacht'))
artiest.update_layout(title_x=0.5)


hond_kat = px.histogram(waarden.dropna(), x="kat_hond",
color="geslacht",
title='Honden of katten mensen, wat zijn we?',
labels=dict(x='Voorkeursbeestje', y='Aantal personen', color= 'Geslacht')
)
hond_kat.update_layout(title_x=0.5)

line_chart = waarden[['tijdstempel', 'leeftijd', 'artiest', 'geslacht']].sort_values('tijdstempel').copy()
line_chart.index = line_chart.tijdstempel
line_chart.drop('tijdstempel',axis=1,inplace=True)
line_chart['cum_avg_mean']= line_chart.leeftijd.expanding().mean().round(2)
line_chart.dropna(inplace=True)
lijn = px.line(line_chart.reset_index(), x="tijdstempel", y="cum_avg_mean",color='geslacht', title='Wanneer is de vragenlijst ingevuld tov de leeftijd')
lijn.update_layout(title_x=0.5)

stad = px.histogram(waarden.dropna(), x="stad").update_xaxes(categoryorder='total descending',title='Waar vier je nou een feestje?')
stad.update_layout(title_x=0.5)
stad.update_xaxes(tickangle=45)

table = go.Figure(data=[go.Table(
    columnorder = [1,2,3],
    columnwidth = [20,60,20],
    header=dict(values=['<b>Wat</b>', '<b>De schaal van 0 tot 5 in woord</b>','<b>Gemiddelde</b>'],
                line_color='steelblue',
                fill_color='steelblue',
                font = dict(color = 'white', size = 13),
                align='left'),
    cells=dict(values=[['Avondeten', 'Flugel', 'Die Kneipe', 'Skistijl', 'Skidag', 'Lezen', 'Pre skifeest'], # 1st column
    ['Kebab - Fine dining', 'Alleen - Dapper in het midden ', 'Dansschoenen aan- Alleen op skischuhe', 'Groen - Zwart ', 'Zon, Zneeuw, Zuipen - Eerste lift', 'Lezen? - Belezen', 'Geen polonaise - Meid ik moet door!!'], # 2nd column 
    waarden.mean().values[:-1]], # 3nd column
    line_color='white',
    fill_color='white',
    align='left',
    font=dict(color='black', size=12)))
])
table.update_layout(width=800, height=355)

sunburst = px.sunburst(waarden.dropna(), path=['stad','kat_hond', 'dal_piste_team','tosti'], color= 'stad', title= 'Hoe kom ik erachter wat iemand bij zijn tosti wil?')
sunburst.update_layout(title_x=0.5)

#tekst voor het uitrekenen maken
text = create_text('2022-03-16')

#creeren app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,title='Wintersport 2022')

server = app.server
    
app.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.Div('Welkom fijne wintersportvrienden!', className="app-header--title")
        ]
    ),
    html.H5('In dit dashboard zal de komende periode nuttige informatie verschijnen.',className="app-text--title" ),       
    html.Br(),

    html.Div(className="app-base",
        children=html.Div([
            html.H5('Gaan we nou al op wintersport?',className="app-text--title" ),
            html.Div(text[0],className=text[1]),
#            html.Img(src='assets/achtergrond.png',className="app-hero-image")
        ])
    ),
    
    html.Br(),
    html.Div(children=[
    dcc.Graph(className= 'four columns',
        id="graph7", 
        style={'display': 'inline-block'},
        figure=sunburst
        ),
    dcc.Graph(className= 'eight columns',
        id="graph6", 
        style={'display': 'inline-block'},
        figure=lijn
        )
    
        ]
    ),

    html.Div(children=[
    dcc.Graph(className= 'four columns',
        id="graph3", 
        style={'display': 'inline-block'},
        figure=artiest
        ),
    dcc.Graph(className='four columns',
        id="graph4", 
        style={'display': 'inline-block'},
        figure=hond_kat
        ),
    dcc.Graph(className='four columns',
        id="graph5", 
        style={'display': 'inline-block'},
        figure=stad
        )
],
    className="row"
    ),    
    html.Div(children=[
        dcc.Graph(className= 'four columns',
            id="graph1", 
            style={'display': 'inline-block'},
            figure=huren
            ),
        dcc.Graph(className='four columns',
            id="table", 
            style={'display': 'inline-block'},
            figure=table
            ),
        dcc.Graph(className='four columns',
            id="graph2", 
            style={'display': 'inline-block'},
            figure=violin
            )
    ],
    className="row"
    ),
    
    html.Br(), 
])

if __name__ == '__main__':
    app.run_server(debug=False)