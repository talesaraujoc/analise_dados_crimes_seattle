from dash import dash, html, dcc, Output, Input, State, dash_table, callback, register_page
import dash_bootstrap_components as dbc
#from dash_bootstrap_templates import load_figure_template

import pandas as pd
import plotly as plt
from datetime import date
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import dash_ag_grid as dag

from globals import *


# Servidor
#load_figure_template("minty")

#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY, "https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css"])
#server = app.server

register_page(__name__, name="MENU", path='/')



# DataFrame =================



########## Pré-layout ================



# Layout    =================
#app.layout = html.Div([
layout = html.Div([
    html.Div([
        html.H1("Análise de Crimes em Seattle", className="main-title"),
        html.P("Um dashboard interativo baseado em dados do Seattle Police Department", className="subtitle"),
    ], className="header"),

    html.Div([
        html.Div([
            html.H2("Sobre o Projeto 📍"),
            html.P("Este projeto realiza uma análise dos dados de criminalidade da cidade de Seattle fornecidos pelo Departamento de Polícia (SPD). Identificamos padrões, tendências sazonais e locais com maior incidência para apoiar estratégias de segurança."),

            html.H3("Objetivos"),
            html.Ul([
                html.Li("Analisar dados por tipo, localização e tempo."),
                html.Li("Detectar padrões e variações sazonais."),
                html.Li("Mapear áreas críticas para apoiar a tomada de decisão."),
            ]),

            html.H3("Tecnologias"),
            html.Ul([
                html.Li("Python"),
                html.Li("Pandas"),
                html.Li("Matplotlib"),
                html.Li("Folium"),
                html.Li("Scikit-learn"),
            ]),

            html.H3("Fonte de Dados"),
            html.P([
                "Dados públicos do portal ",
                html.A("Seattle Open Data Portal", href="https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5/about_data", target="_blank")
            ]),

            html.Hr(),
            html.P("Relatório elaborado por Tales Araújo Carvalho — ", style={"marginTop": "30px"}),
            html.A("GitHub: talesaraujoc", href="https://github.com/talesaraujoc/analise_dados_crimes_seattle", target="_blank"),
        ], className="column"),

        html.Div([
            html.H2("About the Project 🌐"),
            html.P("This project analyzes crime data from Seattle's Police Department (SPD). We explore trends, patterns and high-crime areas to support public security planning."),

            html.H3("Main Goals"),
            html.Ul([
                html.Li("Analyze crime by type, time and location."),
                html.Li("Identify trends and seasonal patterns."),
                html.Li("Visualize critical areas for strategic policing."),
            ]),

            html.H3("Technologies"),
            html.Ul([
                html.Li("Python"),
                html.Li("Pandas"),
                html.Li("Matplotlib"),
                html.Li("Folium"),
                html.Li("Scikit-learn"),
            ]),

            html.H3("Data Source"),
            html.P([
                "Public data from the ",
                html.A("Seattle Open Data Portal", href="https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5/about_data", target="_blank")
            ])
        ], className="column")

    ], className="content-wrapper")

], className="main-container")








# Callbacks =================



# Servidor  =================
#if __name__ == '__main__':
#    app.run_server(debug=False)