import pandas as pd


def cargar_dataset(ruta_csv):
    try:
        df = pd.read_csv(ruta_csv)
        print('\n Archivo CSV cargado correctamente')
        return df
    except FileNotFoundError:
        print('\n El archivo no se encuentra en la ruta', ruta_csv)
        return None
    except Exception as e:
        print('\n Hay un error al cargar el archivo: ', e)
        return None
    
    # """
    # TODO:
    # - Cargar el archivo CSV indicado por la ruta recibida como parametro
    # - Comprobar que el archivo se ha cargado correctamente
    # - Devolver el DataFrame resultante
    # """


def exploracion_inicial(df):
    print('\nPrimeras filas del Dataset: \n')
    print(df.head())

    print("\n--- DIMENSIONES DEL DATASET ---")
    print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")

    print("\n--- TIPOS DE DATOS EN LAS COLUMNAS ---")
    print(df.type)

    print("\n--- NÚMERO DE VALORES NULOS POR COLUMNA ---")
    print(df.isnull().sum())


    # """
    # TODO:
    # - Mostrar las primeras filas del dataset para entender su estructura
    # - Mostrar el numero de filas y columnas
    # - Mostrar los tipos de datos de cada columna
    # - Mostrar el numero de valores nulos por columna
    # - Usar esta informacion para detectar posibles problemas de calidad de datos
    # """

