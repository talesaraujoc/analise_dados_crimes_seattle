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
register_page(__name__, name="1.1", path='/page_one_a')



# DataFrame =================
dff_por_cem_mil = pd.merge((dff.groupby('year').agg({'offense id':'count'}).reset_index()), (df_population), how='left', on='year')
dff_por_cem_mil = dff_por_cem_mil[dff_por_cem_mil['year']>=2008]
dff_por_cem_mil['taxa'] = round(((dff_por_cem_mil['offense id'] / dff_por_cem_mil['population']) * 100000), 2)


########## Pré-layout ================
## gráfico linha crescimento populacional
fig_curva_populacao = px.line(
    df_population, 
    x='year', 
    y='population', 
    title="Ocorrências de Crimes ao Longo do Tempo",
    line_shape="spline",
    markers=True
)
fig_curva_populacao.update_traces(line=dict(color="#003DA5", width=2))
fig_curva_populacao.update_layout(
    plot_bgcolor="white",
    title_font=dict(size=20),
    xaxis=dict(title="Ano", gridcolor="#e0e0e0"),
    yaxis=dict(title="Número de Ocorrências", gridcolor="#e0e0e0"),
    font=dict(family="Arial", size=14)
)

## gráfico linha comportamento crimes (geral)
fig_curva_crimes_geral = px.line(
    dff_por_cem_mil, 
    x='year', 
    y='taxa', 
    title="Ocorrências de Crimes ao Longo do Tempo (Taxa | Crimes/100mil habitantes)",
    line_shape="spline",
    markers=True
)
fig_curva_crimes_geral.update_traces(line=dict(color="#003DA5", width=2))
fig_curva_crimes_geral.update_layout(
    plot_bgcolor="white",
    title_font=dict(size=20),
    xaxis=dict(title="Ano", gridcolor="#e0e0e0"),
    yaxis=dict(title="Taxa Número de Ocorrências", gridcolor="#e0e0e0"),
    font=dict(family="Arial", size=14)
)



# Layout    =================
#app.layout = html.Div([
layout = html.Div([
    html.Div([
        html.H1("O número de crimes em Seattle aumenta conforme a população cresce?", className="main-title")
    ], className="header"),

    html.Div([
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure=fig_curva_populacao, style={"width": "100%"})
            ], width=6),

            dbc.Col([
                dcc.Graph(figure=fig_curva_crimes_geral, style={"width": "100%"})
            ], width=6),
        ]),

        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        html.Label("Categoria Principal:", style={"fontWeight": "bold", "marginTop": "6px"}),
                        dcc.RadioItems(
                            id='dcc-one_tipo_feature',
                            options=[
                                {'label': 'NIBRS Group A/B', 'value': 'nibrs group ab'},
                                {'label': 'Categoria de Crime NIBRS', 'value': 'nibrs crime against category'}
                            ],
                            value='nibrs group ab',
                            labelStyle={'display': 'block', 'margin-bottom': '6px'},
                            inputStyle={"margin-right": "8px"}
                        )
                    ], width=6, style={"padding": "20px", "backgroundColor": "#f9f9f9", "borderRadius": "10px"}),
                    dbc.Col([
                        html.Label("Subcategoria:", style={"fontWeight": "bold", "marginTop": "6px"}),
                        dcc.RadioItems(
                            id='dcc-two_suboptions_dcc-one',
                            labelStyle={'display': 'block', 'margin-bottom': '6px'},
                            inputStyle={"margin-right": "8px"}
                        )
                    ], width=6, style={"padding": "20px", "backgroundColor": "#f9f9f9", "borderRadius": "10px"})
                ]),

                dbc.Row(dcc.Graph(id='grafico_3_p_one'))
            ], width=8), # grafico

            dbc.Col([
                    html.H5("📊 Análise dos Gráficos", style={"fontWeight": "bold"}),

                    html.P(
                        "Entre 2008 e 2024, os dados indicam uma tendência geral de queda na taxa de crimes por 100 mil habitantes em Seattle, "
                        "sugerindo avanços em segurança pública quando se observa a criminalidade de forma proporcional à população."
                    ),

                    html.P(
                        "No entanto, os crimes mais graves — classificados como Grupo A pelo sistema NIBRS (como homicídio, roubo e estupro) — "
                        "apresentam oscilações ao longo dos anos, sem uma tendência clara de redução consistente. "
                        "Isso é preocupante, pois mesmo com o crescimento populacional e os avanços sociais, esses delitos mantêm um comportamento instável. "
                        "O sistema NIBRS organiza os crimes em dois grupos: A (infrações mais sérias) e B (infrações de menor gravidade), permitindo uma análise mais segmentada. "
                        "Enquanto os crimes do Grupo B demonstram uma tendência clara de queda desde 2008, os do Grupo A requerem atenção especial em políticas públicas."
                    ),

                    html.P(
                        "Sob a ótica da natureza do crime — contra a pessoa, a propriedade ou a sociedade — os dados também revelam padrões distintos. "
                        "Os crimes contra a propriedade, por exemplo, seguem uma trajetória de queda entre 2014 e 2019, mas sofrem uma forte inflexão entre 2019 e 2022, possivelmente associada ao período da pandemia. "
                        "Após 2022, a tendência de queda se estabiliza, retomando o comportamento anterior."
                    ),
                    html.P(
                        "A taxa de crimes contra a pessoa apresenta um comportamento cíclico entre 2008 e 2024, com períodos alternados de alta e queda. "
                        "Observa-se uma queda entre 2008 e 2013, seguida de uma elevação contínua até 2018. Após um declínio em 2020, a taxa volta a subir até 2022, "
                        "mas apresenta nova queda acentuada em 2024. Esse padrão oscilante demonstra a ausência de uma tendência clara de melhoria contínua, "
                        "reforçando a necessidade de ações específicas e sustentáveis voltadas à proteção do indivíduo."
                        "Esse tipo de crime impacta diretamente a sensação de segurança da população, por atingir o indivíduo de forma direta. "
                        "Por isso, torna-se essencial o investimento em políticas preventivas específicas voltadas à proteção individual, "
                        "uma vez que os dados não indicam melhora consistente nesse segmento."
                    )

            ], width=4, style={"padding": "20px", "backgroundColor": "#f9f9f9", "borderRadius": "10px"})

        ])
    ])


], className="main-container")


# Callbacks =================
@callback(
    Output('dcc-two_suboptions_dcc-one', 'options'),
    Input('dcc-one_tipo_feature', 'value')
)
def update_dcc_two_suboptions_pone(feature_p_one):
    if feature_p_one == 'nibrs group ab':
        lista_options = dff_eda['nibrs group ab'].unique()
    else:
        lista_options = dff_eda['nibrs crime against category'].unique()
    
    return lista_options

@callback(
    Output('dcc-two_suboptions_dcc-one', 'value'),
    Input('dcc-two_suboptions_dcc-one', 'options')
)
def update_value_dcc_two_pone(options):
    value_update = options[0]
    return value_update


@callback(
    Output('grafico_3_p_one', 'figure'),
    Input('dcc-one_tipo_feature', 'value'),
    Input('dcc-two_suboptions_dcc-one', 'value')
)
def update_grafico_3_pag_one(feature_mae, sub_feature):
    df_graf_tres_p_one = dff[dff[feature_mae]==sub_feature]
    df_graf_tres_p_one = df_graf_tres_p_one[(df_graf_tres_p_one['year']>=2008) & (df_graf_tres_p_one['year']<2025)]
    df_graf_tres_p_one = pd.merge((df_graf_tres_p_one.groupby('year').agg({'offense id':'count'}).reset_index()), (df_population), how='left', on='year')
    df_graf_tres_p_one['taxa'] = round(((df_graf_tres_p_one['offense id'] / df_graf_tres_p_one['population']) * 100000), 2)
    px.line(df_graf_tres_p_one, x='year', y='taxa')

    fig_grafico_tres_p_one = px.line(
    df_graf_tres_p_one, 
    x='year', 
    y='taxa', 
    title=f"Taxa de Crimes ao Longo do Tempo | {feature_mae}",
    line_shape="spline",
    markers=True
    )
    fig_grafico_tres_p_one.update_traces(line=dict(color="#003DA5", width=2))
    fig_grafico_tres_p_one.update_layout(
    plot_bgcolor="white",
    title_font=dict(size=20),
    xaxis=dict(title="Ano", gridcolor="#e0e0e0"),
    yaxis=dict(title="Taxa Número de Ocorrências", gridcolor="#e0e0e0"),
    font=dict(family="Arial", size=14)
    )

    return fig_grafico_tres_p_one