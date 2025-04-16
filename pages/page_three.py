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
register_page(__name__, name="3", path='/page_three')



# DataFrame =================
dff_count_month = dff_eda['month'].value_counts().to_frame().reset_index().rename({'month':'Mês', 'count':'Total Crimes'}, axis=1)
dff_count_month = dff_count_month.sort_values(by='Mês')

dff_periodo_dia = dff_eda.groupby('periodo').agg({'offense id':'count'}).reset_index()
dff_periodo_dia = dff_periodo_dia.rename({'periodo':'Período do dia'}, axis=1)

########## Pré-layout ================
## gráfico distribuição mensal
fig_crimes_mensais = px.bar(
    dff_count_month,
    x='Mês',
    y='Total Crimes',
    text='Total Crimes',
    title="Distribuição de Crimes por Mês"
)
fig_crimes_mensais.update_traces(
    marker_color="#003DA5",
    textposition='inside'
)
fig_crimes_mensais.update_layout(
    plot_bgcolor="white",
    title_font=dict(size=18),
    xaxis=dict(title="", gridcolor="#e0e0e0"),
    yaxis=dict(title="Total por mês", gridcolor="#e0e0e0"),
    font=dict(family="Arial", size=12),
    margin=dict(l=180)  # espaço extra p/ rótulos longos
)

## gráfico período do dia
fig_periodo_dia = px.bar(
    dff_periodo_dia,
    x='Período do dia',
    y='offense id',
    text='offense id',
    title="Distribuição de Crimes por Período do Dia"
)
fig_periodo_dia.update_traces(
    marker_color="#003DA5",
    textposition='inside'
)
fig_periodo_dia.update_layout(
    plot_bgcolor="white",
    title_font=dict(size=18),
    xaxis=dict(title="", gridcolor="#e0e0e0"),
    yaxis=dict(title="Total por período", gridcolor="#e0e0e0"),
    font=dict(family="Arial", size=12),
    margin=dict(l=180)  # espaço extra p/ rótulos longos
)



# Layout    =================
layout = html.Div([
    html.Div([
        dbc.Row([
            # Coluna da esquerda (Crimes por mês)
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            html.H4("Sazonalidade por Mês", className="main-title")
                        ], className="header", style={"marginBottom": "10px"}),

                        dcc.Graph(figure=fig_crimes_mensais),

                        html.Div([
                            html.H5("📆 Sazonalidade na Ocorrência de Crimes", style={"fontWeight": "bold", "marginBottom": "15px"}),

                            html.P(
                                "A análise da distribuição mensal dos crimes entre 2017 e 2024 revela uma variação relativamente sutil ao longo do ano. "
                                "Embora alguns meses apresentem um volume ligeiramente maior de ocorrências — como maio, julho e agosto —, essa diferença não caracteriza uma tendência sazonal forte."
                            ),
                            html.P(
                                "A discrepância entre o mês com maior número de registros (maio, com cerca de 32 mil ocorrências) e o mês com menor incidência (fevereiro, com aproximadamente 27 mil) "
                                "é inferior a 2 pontos percentuais em termos proporcionais. Essa pequena variação sugere uma distribuição dos crimes relativamente homogênea ao longo dos meses."
                            ),
                            html.P(
                                "Portanto, embora existam flutuações mensais, os dados não indicam uma concentração sazonal acentuada de criminalidade. Isso sugere que, do ponto de vista temporal, "
                                "as estratégias de prevenção e policiamento devem ser aplicadas de forma contínua e consistente durante todo o ano."
                            )
                        ], style={
                            "padding": "20px",
                            "backgroundColor": "#f9f9f9",
                            "borderRadius": "10px"
                        })
                    ])
                ])
            ], width=6, style={"padding": "20px"}),

            # Coluna da direita (Crimes por período do dia)
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            html.H4("Sazonalidade por Período do Dia", className="main-title")
                        ], className="header", style={"marginBottom": "10px"}),

                        dcc.Graph(figure=fig_periodo_dia),

                        html.Div([
                            html.H5("🕒 Distribuição por Período do Dia", style={"fontWeight": "bold", "marginBottom": "15px"}),

                            html.P(
                                "Para tornar a análise temporal mais objetiva e comparável, o dia foi segmentado em quatro intervalos estratégicos: "
                                "*Madrugada (0h–6h)*, *Manhã (6h–12h)*, *Tarde (12h–18h)* e *Noite (18h–24h)*. Essa divisão simplifica a leitura dos padrões de ocorrência "
                                "e permite entender melhor a dinâmica criminal ao longo das diferentes fases do dia — respeitando os ritmos sociais e operacionais da cidade."
                            ),
                            html.P(
                                "A análise revela que a grande maioria dos crimes ocorre entre 12h e 24h, ou seja, durante a tarde e a noite. Juntas, essas faixas representam mais de 60% das ocorrências. "
                                "Esse padrão pode estar associado a maior circulação de pessoas, atividades comerciais, sociais e maior exposição ao risco nesses horários."
                            ),
                            html.P(
                                "Por outro lado, os períodos da madrugada e da manhã concentram a menor quantidade de registros. Isso pode refletir tanto uma menor atividade urbana nesses horários, "
                                "quanto uma possível subnotificação — especialmente na madrugada. "
                                "Essas informações são relevantes para o planejamento tático e estratégico da segurança pública, indicando que a alocação de recursos e ações preventivas deve priorizar o período entre o meio-dia e a meia-noite."
                            )
                        ], style={
                            "padding": "20px",
                            "backgroundColor": "#f9f9f9",
                            "borderRadius": "10px"
                        })
                    ])
                ])
            ], width=6, style={"padding": "20px"})
        ])
    ])
], className="main-container")







# Callbacks =================
