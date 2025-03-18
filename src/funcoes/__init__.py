import pandas as pd

def colunas_lower(df):
    return df.rename(columns=str.lower)


def transformando_colunas_em_datetime(data_frame_target, coluna_target):
    return pd.to_datetime(data_frame_target[coluna_target])



def df_filtrado_taxa_cem_mil(df_crimes, df_populacao, categoria_filtro, valor_filtro):
    """
    Calcula a taxa de crimes por 100 mil habitantes, agrupada por ano.

    Parâmetros:
        df_crimes (pd.DataFrame): DataFrame contendo os dados de crimes, com colunas 'year', 'offense id' e a categoria de filtro.
        df_populacao (pd.DataFrame): DataFrame contendo a população por ano, com colunas 'year' e 'population'.
        categoria_filtro (str): Nome da coluna em df_crimes usada para filtrar os dados (exemplo: 'state' ou 'city').
        valor_filtro (str): Valor específico da categoria_filtro para aplicar o filtro (exemplo: nome de um estado ou cidade).

    Retorna:
        pd.DataFrame: DataFrame contendo o ano, o número de crimes registrados, a população correspondente e a taxa de crimes por 100 mil habitantes.
    """
    df_target = pd.merge((df_crimes[df_crimes[categoria_filtro]==valor_filtro].groupby('year').agg({'offense id':'count'}).sort_index().reset_index()), (df_populacao), how='left', on='year')
    df_target['taxa'] = round(((df_target['offense id'] / df_target['population']) * 100000), 2)

    return df_target