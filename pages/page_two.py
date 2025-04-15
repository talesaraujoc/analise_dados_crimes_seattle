from dash import dash, html, dcc, Output, Input, State, dash_table, callback, register_page
import dash_bootstrap_components as dbc

from pathlib import Path
import json
import pandas as pd
import plotly as plt
from datetime import date
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import dash_ag_grid as dag

from globals import *


# Dash
register_page(__name__, name="2", path='/page_two')



# DataFrame =================
dff_eda_map = dff_eda[~dff_eda['latitude'].isna()]
dff_eda_map = dff_eda_map[dff_eda_map['latitude']!=0]

crimes_por_beat = dff_eda_map.groupby('beat').size().reset_index(name='count')
crimes_por_beat = crimes_por_beat[crimes_por_beat['beat']!="-"]
crimes_por_beat = crimes_por_beat[crimes_por_beat['beat']!=99]
crimes_por_beat = crimes_por_beat.rename({'count':'Total Crimes'},axis=1)

crimes_por_precinct = dff_eda_map.groupby('precinct').size().reset_index(name='count')
crimes_por_precinct = crimes_por_precinct[crimes_por_precinct['precinct']!="-"]
crimes_por_precinct = crimes_por_precinct[crimes_por_precinct['precinct']!="OOJ"]
crimes_por_precinct = crimes_por_precinct.rename({'count':'Total Crimes'},axis=1)


geojson_path = Path.cwd() / 'data'/ 'beats.geojson'
with open(geojson_path, 'r', encoding='utf-8') as f:
    beat_geojson = json.load(f)

geojson_path = Path.cwd() / 'data'/ 'precinct.geojson'
with open(geojson_path, 'r', encoding='utf-8') as f:
    precinct_geojson = json.load(f)

########## Pré-layout ================
fig_mapa = px.choropleth_mapbox(
    crimes_por_precinct,
    geojson=precinct_geojson,
    locations='precinct',
    color='Total Crimes',
    featureidkey='properties.name',  # ajuste conforme o nome da propriedade
    mapbox_style="carto-positron",
    center={"lat": 47.6062, "lon": -122.3321},
    zoom=9.75,
    color_continuous_scale="YlOrRd",
    opacity=0.6
)

fig_mapa.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig_mapa_beat = px.choropleth_mapbox(
    crimes_por_beat,
    geojson=beat_geojson,
    locations='beat',               # coluna do DataFrame
    color='Total Crimes',                  # valor numérico
    featureidkey='properties.name', # deve bater com o GeoJSON
    mapbox_style="carto-positron",
    center={"lat": 47.6062, "lon": -122.3321},
    zoom=9.75,
    opacity=0.6,
    color_continuous_scale="YlOrRd"
)

fig_mapa_beat.update_layout(
    margin={"r":0,"t":0,"l":0,"b":0}
)



# Layout    =================
layout = html.Div([
    html.Div([
        html.H1(
            "Existem áreas específicas de Seattle onde a concentração de crimes é consistentemente maior?",
            className="main-title"
        )
    ], className="header"),

    html.Div([
        # Linha com os dois mapas lado a lado
        dbc.Row([
            dbc.Col([
                html.H6("Mapa por *Precinct* (Distrito Policial)", style={"fontWeight": "bold", "marginBottom": "10px"}),
                dcc.Graph(figure=fig_mapa)
            ], width=6, style={
                "padding": "20px",
                "backgroundColor": "#f9f9f9",
                "borderRadius": "10px"
            }),

            dbc.Col([
                html.H6("Mapa por *Beat* (Unidade de Patrulha)", style={"fontWeight": "bold", "marginBottom": "10px"}),
                dcc.Graph(figure=fig_mapa_beat)
            ], width=6, style={
                "padding": "20px",
                "backgroundColor": "#f9f9f9",
                "borderRadius": "10px"
            })
        ]),

        # Alerta sobre precisão geográfica
        dbc.Row([
            dbc.Col([
                dbc.Alert(
                    "🔎 Aviso: As coordenadas geográficas dos crimes foram propositalmente aproximadas para o quarteirão mais próximo (one hundred block) pelo Seattle Police Department. "
                    "Portanto, os pontos e regiões representados nos mapas devem ser interpretados como estimativas geográficas aproximadas.",
                    color="warning",
                    dismissable=True,
                    style={"marginTop": "20px"}
                )
            ], width=12)
        ]),

        # Insights analíticos sobre as áreas
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H5("📍 Principais Áreas de Concentração de Crimes", style={"fontWeight": "bold", "marginBottom": "15px"}),

                    html.P(
                        "A análise geoespacial dos dados revela que as regiões Norte (*North*) e Oeste (*West*) concentram o maior número de ocorrências criminais em Seattle. "
                        "Essas áreas podem ser consideradas zonas de maior risco, exigindo atenção redobrada no planejamento de ações de segurança pública, como alocação de efetivo, patrulhamento intensivo e monitoramento preventivo."
                    ),

                    html.P(
                        "Em contrapartida, a região Sudoeste (*Southwest*) se destacou por apresentar o menor número de registros de crimes no período analisado, configurando-se como a área com menor índice de criminalidade. "
                        "Essa informação pode contribuir para a avaliação de boas práticas de prevenção já implementadas na região."
                    ),

                    html.P(
                        "Entre as subdivisões de patrulhamento conhecidas como *beats*, a área K3, localizada também na região Oeste, foi a que apresentou a maior concentração de delitos. "
                        "Além de K3, os beats R2, Q3, U3 e U1 completam a lista das cinco áreas com maior número de ocorrências, representando zonas críticas que demandam ações específicas de segurança e presença policial reforçada."
                    )
                ], style={
                    "padding": "20px",
                    "backgroundColor": "#f9f9f9",
                    "borderRadius": "10px"
                })
            ], width=12)
        ])
    ])
], className="main-container")






# Callbacks =================
