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
register_page(__name__, name="1.3", path='/page_one_c')



# DataFrame =================
df_analitico_crimes_mais_comuns = dff_eda['offense sub category'].value_counts(normalize=True).head(10).to_frame().reset_index()
df_analitico_crimes_mais_comuns = df_analitico_crimes_mais_comuns.rename({'proportion':'percentual'}, axis=1)
df_analitico_crimes_mais_comuns['percentual'] = df_analitico_crimes_mais_comuns['percentual'].apply(lambda x: round((x*100), 2))
df_analitico_crimes_mais_comuns['percentual_str'] = df_analitico_crimes_mais_comuns['percentual'].apply(lambda x: str(x)+'%')

df_analitico_agrupado_ano = dff_eda.groupby(['year','offense sub category']).agg({'offense sub category':'count'}).rename({'offense sub category':'cat'},axis=1).reset_index()
lista_tipos_crimes = df_analitico_agrupado_ano['offense sub category'].unique()

########## Pré-layout ================
## gráfico tipos crimes (propriedade, pessoa ou sociedade)
fig_dez_crimes_mais_comuns = px.bar(
    df_analitico_crimes_mais_comuns,
    x='percentual',
    y='offense sub category',
    orientation='h',
    text='percentual_str',
    title="10 Crimes Mais Frequentes"
)
fig_dez_crimes_mais_comuns.update_traces(
    marker_color="#003DA5",
    textposition='inside'
)
fig_dez_crimes_mais_comuns.update_layout(
    plot_bgcolor="white",
    title_font=dict(size=18),
    xaxis=dict(title="Percentual de Ocorrências", gridcolor="#e0e0e0"),
    yaxis=dict(title="", gridcolor="#e0e0e0"),
    font=dict(family="Arial", size=12),
    margin=dict(l=180)  # espaço extra p/ rótulos longos
)



# Layout    =================
layout = html.Div([
    dbc.Row([
        # Parte Esquerda – Crimes em Destaque
        dbc.Col([
            html.Div([
                html.H1("Quais os tipos de crimes em destaque?", className="main-title"),
                
                dcc.Graph(figure=fig_dez_crimes_mais_comuns),

                html.Div([
                    html.H5("🔎 Principais Crimes Registrados", style={"fontWeight": "bold", "marginBottom": "15px"}),

                    html.P(
                        "O crime mais recorrente em Seattle entre 2017 e 2024 foi o furto simples (*Larceny-Theft*), responsável por quase um terço das ocorrências. "
                        "Esse tipo de infração geralmente ocorre sem uso de força ou violência direta contra a vítima, como furtos em lojas, residências ou veículos destrancados. "
                        "Esse dado reforça a predominância de crimes contra a propriedade no conjunto total de registros."
                    ),

                    html.P(
                        "Em seguida, as infrações classificadas como *Assault Offenses* representam 13% dos casos. "
                        "Esses crimes envolvem ataques físicos diretos a outra pessoa, como empurrões, socos ou agressões sem uso de arma. "
                        "Embora menos frequentes que os furtos, impactam diretamente a integridade das vítimas e exigem respostas rápidas por parte das forças de segurança."
                    ),

                    html.P(
                        "*Burglary* (arrombamento/invasão de imóveis) responde por aproximadamente 11% dos registros. "
                        "Inclui invasões a residências e estabelecimentos comerciais com o objetivo de cometer furto ou outros crimes. "
                        "É também um indicativo da fragilidade em estruturas físicas e da importância de proteção patrimonial urbana."
                    ),

                    html.P(
                        "Por fim, os chamados *Property Offenses* — que englobam destruição, dano e roubo de bens materiais — também representam cerca de 11% do total. "
                        "A presença de três categorias relacionadas à propriedade entre os quatro crimes mais frequentes demonstra a urgência de medidas preventivas "
                        "voltadas à proteção de bens, infraestrutura urbana e espaços vulneráveis."
                    )
                ], style={
                    "padding": "20px",
                    "backgroundColor": "#f9f9f9",
                    "borderRadius": "10px"
                })
            ])
        ], width=6),

        # Parte Direita – Tendência Temporal
        dbc.Col([
            html.Div([
                html.H1("Tendência de crimes ao longo do tempo", className="main-title"),

                dcc.Dropdown(
                    id='dpd_page_three',
                    options=lista_tipos_crimes,
                    value='AGGRAVATED ASSAULT',
                    style={"marginBottom": "20px"}
                ),

                dcc.Graph(id='figura_linha_temporal'),

                html.Div([
                    html.H5("📈 Tendências Recentes e Observações Críticas", style={"fontWeight": "bold", "marginBottom": "15px"}),

                    html.P(
                        "Os dados entre 2017 e 2024 revelam um crescimento contínuo e acentuado em diversas categorias de crimes violentos, "
                        "incluindo *Aggravated Assault* (agressões graves), *Homicídios*, *Rape* (estupro) e *Kidnapping/Abduction* (sequestros e abduções). "
                        "Esses delitos indicam uma intensificação da violência interpessoal, exigindo estratégias específicas de prevenção, resposta rápida e proteção às vítimas."
                    ),

                    html.P(
                        "Crimes contra a propriedade, como *Burglary* (arrombamentos), *Arson* (incêndios criminosos) e *Motor Vehicle Theft* (roubos de veículos), "
                        "também apresentaram aumento consistente ao longo do período analisado. Esses dados reforçam a importância de políticas públicas voltadas à segurança patrimonial, "
                        "como vigilância urbana, infraestrutura de iluminação e conscientização comunitária."
                    ),

                    html.P(
                        "O ano de 2020 se destacou como um ponto fora da curva, com aumento de até 200% em crimes de *Extorsão* e *Fraude* em relação ao ano anterior. "
                        "Esse comportamento atípico sugere forte influência das condições impostas pela pandemia de COVID-19, como crise econômica, desemprego e maior exposição a crimes digitais."
                    ),

                    html.P(
                        "De forma geral, os dados apontam uma tendência preocupante de intensificação da criminalidade, tanto em crimes violentos quanto patrimoniais. "
                        "Esse cenário reforça a necessidade de ações integradas que levem em conta os fatores sociais e econômicos envolvidos, além da natureza específica de cada tipo de crime."
                    )
                ], style={
                    "padding": "20px",
                    "backgroundColor": "#f9f9f9",
                    "borderRadius": "10px"
                })
            ])
        ], width=6)
    ])
], className="main-container")




# Callbacks =================
@callback(
    Output('figura_linha_temporal', 'figure'),
    Input('dpd_page_three', 'value')
)
def update_grafico(feature_crime):

    df_grap_p3 = df_analitico_agrupado_ano[df_analitico_agrupado_ano['offense sub category']==feature_crime]

    ## gráfico linha evolucao crimes por ano
    fig_curva_agrupado_anos = px.line(
        df_grap_p3, 
        x='year', 
        y='cat',
        title="Tendência ao longo do tempo",
        line_shape="spline",
        markers=True
    )
    #fig_curva_agrupado_anos.update_traces(line=dict(color="#003DA5", width=2))
    fig_curva_agrupado_anos.update_layout(
        plot_bgcolor="white",
        title_font=dict(size=20),
        #xaxis=dict(title="Ano", gridcolor="#e0e0e0"),
        xaxis=dict(title="", gridcolor="#e0e0e0"),
        yaxis=dict(title="Número de Ocorrências", gridcolor="#e0e0e0"),
        font=dict(family="Arial", size=14)
    )

    return fig_curva_agrupado_anos