from pathlib import Path
import pandas as pd
from src import funcoes

########## configurações iniciais
#parcial_path_absolute = Path.home() / 'OneDrive' / 'Documentos' / 'GitHub'
#parcial_path_relative = Path('analise_dados_crimes_seattle')
#full_path = parcial_path_absolute / parcial_path_relative
full_path = Path.cwd()

absolute_path_data_raw = full_path / 'data' / 'raw'
absolute_path_data_processed = full_path / 'data' / 'processed'

path_data = absolute_path_data_processed / 'SPD_Crime_data_cleaned.csv'

path_data_split_one = absolute_path_data_processed / 'split_SPD_Crime_data_cleaned_1.csv'
path_data_split_two = absolute_path_data_processed / 'split_SPD_Crime_data_cleaned_2.csv'
path_data_split_three = absolute_path_data_processed / 'split_SPD_Crime_data_cleaned_3.csv'

path_data_population = absolute_path_data_raw / 'population.xlsx'





########## leituras
df_population = pd.read_excel(path_data_population)

dff_split_one = pd.read_csv(path_data_split_one, parse_dates=['report datetime', 'offense date'])
dff_split_two = pd.read_csv(path_data_split_two, parse_dates=['report datetime', 'offense date'])
dff_split_three = pd.read_csv(path_data_split_three, parse_dates=['report datetime', 'offense date'])

dff = pd.concat([dff_split_one, dff_split_two, dff_split_three])





########## transform
# 'report datetime'
dff['report datetime'] = funcoes.transformando_colunas_em_datetime(dff, 'report datetime')

# 'offense date
dff['offense date'] = funcoes.transformando_colunas_em_datetime(dff, 'offense date')

dff['hour'] = dff['offense date'].apply(lambda x: x.hour)
dff['minute'] = dff['offense date'].apply(lambda x: x.minute)
dff['day_of_week'] = dff['offense date'].apply(lambda x: x.day_of_week)
dff['month'] = dff['offense date'].apply(lambda x: x.month)
dff['year'] = dff['offense date'].apply(lambda x: x.year)

# Definindo a função para categorizar os períodos do dia
def categorizar_periodo(hora):
    if 0 <= hora < 6:
        return 'Madrugada (0-6h)'
    elif 6 <= hora < 12:
        return 'Manhã (6-12h)'
    elif 12 <= hora < 18:
        return 'Tarde (12-18h)'
    else:
        return 'Noite (18-24h)'


# Aplicando a função à coluna 'hour'
dff['periodo'] = dff['hour'].apply(categorizar_periodo)

dff['day_type'] = dff['day_of_week'].apply(lambda x: 'weekend' if x >= 4 else 'business day')

dff_eda = dff.copy()

# filtrando ano
dff_eda = dff_eda[(dff_eda['year']>=2017) & (dff_eda['year']<2025)]

#limpando outliers
dff_eda = dff_eda[dff_eda['offense sub category']!='ALL OTHER']
dff_eda = dff_eda[(dff_eda['hour']!=0) & (dff_eda['minute']!=0)]