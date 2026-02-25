import numpy as np
import pandas as pd


def limpiar_columna_country(df):
    
    df_clean = df.copy()

    df_clean['country'] = df_clean['country'].fillna('Unknown')
    
    df_clean['country'] = df_clean['country'].str.split(',').str[0]

    return df_clean


def extraer_duracion_numerica(row):

    duracion = row['duration']

    if pd.isna(duracion):
        return np.nan
    try:
        numero = int(str(duracion).split(' ')[0])

        if type == 'Movie':
            return numero
        if type == 'TV Show':
            return numero
        else:
            return numero
    except (ValueError, IndexError):
        return np.nan
        

pass


def limpiar_duracion(df):

    df_clean = df.copy()

    df_clean['duration_num'] = df_clean.apply(extraer_duracion_numerica, axis = 1)

    return df_clean

    pass


def preparar_dataset(df):

    df_clean = df.copy()

    df_clean = limpiar_columna_country(df_clean)
    df_clean = limpiar_duracion(df_clean)

    return df_clean
    
