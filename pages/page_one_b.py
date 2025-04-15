from dash import dash, html, dcc, Output, Input, State, dash_table, callback, register_page
import dash_bootstrap_components as dbc

import pandas as pd
import plotly as plt
from datetime import date
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import dash_ag_grid as dag

from globals import *


# Dash
register_page(__name__, name="1.2", path='/page_one_b')



# DataFrame =================
df_analitico_tipo_crime = dff_eda['nibrs crime against category'].value_counts().to_frame().reset_index()

coluna_percentual = dff_eda['nibrs crime against category'].value_counts(normalize=True).to_frame().reset_index()['proportion']
df_analitico_tipo_crime['percentual'] = round((coluna_percentual*100), 2)
df_analitico_tipo_crime = df_analitico_tipo_crime.rename({'count':'total'}, axis=1)

########## Pré-layout ================
## gráfico tipos crimes (propriedade, pessoa ou sociedade)
fig_tipo_crime_analitico = px.bar(
    df_analitico_tipo_crime, 
    x='nibrs crime against category', 
    y='total',
    text='total',
    title="Ocorrências por Tipo de Crimes"
)

fig_tipo_crime_analitico.update_traces(marker_color="#003DA5")

fig_tipo_crime_analitico.update_layout(
    plot_bgcolor="white",
    title_font=dict(size=20),
    xaxis=dict(title="", gridcolor="#e0e0e0"),
    yaxis=dict(title="Número de Ocorrências", gridcolor="#e0e0e0"),
    font=dict(family="Arial", size=14)
)




# Layout    =================
#app.layout = html.Div([
layout = html.Div([
    html.Div([
        html.H1("Certas categorias de crime (propriedade, pessoa e sociedade) são mais frequentes?", className="main-title")
    ], className="header"),

    html.Div([
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure=fig_tipo_crime_analitico, style={"height": "100%"})
            ], width=6, style={
                "padding": "20px",
                "backgroundColor": "#f9f9f9",
                "borderRadius": "10px"
            }),

            dbc.Col([
                html.H5("🔎 Análise por Categoria de Crime", style={"fontWeight": "bold", "marginBottom": "15px"}),

                html.P(
                    "Esta análise se baseia no recorte entre 2017 e 2024, período no qual a população de Seattle se manteve relativamente estável, "
                    "permitindo comparações mais justas e evitando distorções por crescimento demográfico. Embora a análise temporal anterior revele oscilações relevantes "
                    "nas taxas de criminalidade, a segmentação por categoria oferece uma nova perspectiva sobre onde esses crimes estão concentrados."
                ),

                html.P(
                    "A maioria dos crimes nesse período está concentrada na categoria de crimes contra a propriedade, que representa 65,8% das ocorrências. "
                    "Esse grupo inclui delitos como furtos, roubos, arrombamentos e vandalismo — muitos dos quais acompanharam os padrões de queda observados até 2019, "
                    "mas também sofreram reversões durante o período pandêmico. Dada sua predominância, essa categoria deve ser prioridade em ações preventivas, como reforço de policiamento ostensivo, "
                    "melhorias na iluminação pública, instalação de sistemas de monitoramento e programas de conscientização sobre segurança patrimonial."
                ),

                html.P(
                    "Crimes contra a pessoa, embora em menor volume (21,6%), possuem impacto direto na sensação de segurança da população. "
                    "Esse tipo de crime — que inclui agressões, homicídios e estupros — apresentou comportamento cíclico ao longo dos anos, com oscilações significativas que exigem atenção contínua. "
                    "Dada sua gravidade, é fundamental direcionar recursos para patrulhamento preventivo, políticas públicas de combate à violência doméstica e estratégias de acolhimento às vítimas."
                ),

                html.P(
                    "Por fim, os crimes contra a sociedade representam 12,6% dos registros e abrangem condutas como tráfico de drogas, porte ilegal de armas, "
                    "prostituição e crimes ambientais. Embora numericamente menores, esses crimes afetam a ordem pública e o bem-estar coletivo, demandando respostas estruturais, "
                    "como políticas de controle social, educação comunitária e, quando necessário, revisão legislativa local."
                )
            ], width=6, style={
                "padding": "20px",
                "backgroundColor": "#f9f9f9",
                "borderRadius": "10px"
            })
        ])
    ])
], className="main-container")



# Callbacks =================
