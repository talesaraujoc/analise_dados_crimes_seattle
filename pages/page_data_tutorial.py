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
register_page(__name__, name="SOBRE OS DADOS", path='/page_data_tutorial')



# DataFrame =================

########## Pré-layout ================

# Layout    =================
layout = html.Div([
    dbc.Container([
        html.Div([
            html.H1("📁 Sobre o Dataset de Crimes", className="main-title"),
            html.Hr()
        ], className="header"),

        html.Div([
            html.H5("📌 Fonte dos Dados", style={"fontWeight": "bold"}),
            html.P([
                "Os dados utilizados neste painel são fornecidos publicamente pelo ",
                html.A("Seattle Open Data Portal", href="https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5", target="_blank"),
                ", com registros oficiais do Seattle Police Department (SPD)."
            ]),

            html.H5("📊 Volume de Dados", style={"fontWeight": "bold", "marginTop": "15px"}),
            html.P(
                "Após o processo de limpeza e padronização, o conjunto de dados consolidado contém um total de **1.398.740 registros de ocorrências criminais**. "
                "Esses registros representam eventos únicos reportados e processados pelo SPD ao longo dos anos."
            ),
            html.P(
                "Para algumas análises específicas, como aquelas que comparam com o crescimento populacional ou tendências recentes, foi adotado um recorte entre os anos de **2017 a 2024**, "
                "totalizando **365.939 registros**. Esse período garante consistência demográfica e dados mais confiáveis, com menor interferência de mudanças estruturais nos sistemas de registro."
            ),

            html.H5("🧾 O que representa cada registro?", style={"fontWeight": "bold", "marginTop": "15px"}),
            html.P(
                "Cada linha da base de dados representa uma ocorrência criminal oficialmente registrada — ou seja, um boletim de ocorrência validado pela polícia. "
                "Esses registros podem ser criados por denúncias, flagrantes ou investigações, e incluem desde pequenos furtos até crimes violentos. "
                "A base inclui informações como data do evento, tipo e subtipo do crime, localização aproximada, classificação legal e códigos internos do SPD."
            ),
            html.P(
                "É importante entender que esse dataset não captura apenas a denúncia da vítima, mas sim o evento que foi oficialmente reconhecido e cadastrado como ocorrência criminal "
                "pelo departamento de polícia, após análise e verificação mínima. Isso confere um grau maior de confiabilidade e padronização ao histórico."
            ),

            html.H5("🗺️ Dados Geográficos", style={"fontWeight": "bold", "marginTop": "15px"}),
            html.P(
                "Para visualização geográfica, foram utilizados arquivos no formato GeoJSON contendo a malha oficial dos bairros de patrulhamento da cidade, como os níveis "
                "*precinct* e *beat*. Esses arquivos foram sobrepostos ao mapa da cidade com auxílio da biblioteca `plotly.express`, permitindo a criação de mapas interativos com dados agregados por região."
            ),
            html.P(
                "Todos os mapas apresentados neste painel são apenas representações aproximadas, já que o SPD aplica um processo de 'spatial blur' por segurança, "
                "deslocando as coordenadas geográficas para o quarteirão mais próximo."
            ),

            html.H5("🔧 Tratamento e Pré-processamento", style={"fontWeight": "bold", "marginTop": "15px"}),
            html.P(
                "Antes das análises, os dados passaram por etapas de verificação de consistência, remoção de registros duplicados, padronização de datas, "
                "normalização de categorias e segmentação em faixas horárias. O tratamento foi feito com ferramentas como Python, Pandas e Plotly."
            ),

            html.H5("🔗 Acesso Público", style={"fontWeight": "bold", "marginTop": "15px"}),
            html.P([
                "Você pode acessar o dataset original diretamente no ",
                html.A("Seattle Open Data Portal", href="https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5", target="_blank"),
                "."
            ])
        ], style={
            "padding": "20px",
            "backgroundColor": "#f9f9f9",
            "borderRadius": "10px",
            "marginTop": "20px"
        })
    ])
], className="main-container")


# Callbacks =================
