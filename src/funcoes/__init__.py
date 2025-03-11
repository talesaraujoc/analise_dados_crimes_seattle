import pandas as pd

def colunas_lower(df):
    return df.rename(columns=str.lower)


def transformando_colunas_em_datetime(data_frame_target, coluna_target):
    return pd.to_datetime(data_frame_target[coluna_target])
