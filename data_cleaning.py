import numpy as np
import pandas as pd


def limpiar_columna_country(df):
    
    df_clean = df.copy()

    df_clean['country'] = df_clean['country'].fillna('Unknown')
    
    df_clean['country'] = df_clean['country'].str.split(',').str[0]

    return df_clean
    # """
    # TODO:
    # - Analizar la columna country
    # - Rellenar los valores nulos con el valor knowing 'Unknown'
    # - En los casos donde haya varios paises separados por coma, quedarse solo con el primero
    # - No modificar el DataFrame original
    # - Devolver un nuevo DataFrame con la columna country limpia
    # """
    # pass


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
        

    # """
    # TODO:
    # - Recibir una fila del DataFrame
    # - Analizar la columna duration
    # - Extraer el valor numerico de la duracion
    # - Para peliculas, interpretar el valor como minutos
    # - Para series, interpretar el valor como numero de temporadas
    # - Devolver un entero o NaN si no es posible obtener el valor
    # """
pass


def limpiar_duracion(df):

    df_clean = df.copy()

    df_clean['duration_num'] = df_clean.apply(extraer_duracion_numerica, axis = 1)

    return df_clean

    # """
    # TODO:
    # - Crear una nueva columna llamada duration_num
    # - Usar una funcion que procese fila a fila la columna duration
    # - No modificar el DataFrame original
    # - Devolver un nuevo DataFrame con la duracion numerica
    # """
    pass


def preparar_dataset(df):

    df_clean = df.copy()

    df_clean = limpiar_columna_country(df_clean)
    df_clean = limpiar_duracion(df_clean)

    return df_clean

    # """
    # TODO:
    # - Aplicar todas las funciones de limpieza necesarias sobre el dataset
    # - Garantizar que el DataFrame resultante es una copia del original
    # - Devolver el DataFrame final preparado para el analisis
    # """
    # pass
