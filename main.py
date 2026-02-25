from data_loader import cargar_dataset, exploracion_inicial
from data_cleaning import preparar_dataset
from analysis import (contenido_por_tipo, contenido_por_rating, contenido_por_anio, top_generos, top_paises)
from visualization import (grafico_contenido_por_anio, grafico_contenido_por_rating, grafico_contenido_por_tipo, grafico_distribucion_duracion, grafico_top_generos, grafico_top_paises)

# BONUS
# from netflix_analyzer import NetflixAnalyzer


def main():

    ruta_csv = 'netflix_titles.csv'
    df = cargar_dataset(ruta_csv)

    if df is None:
        print('No se puede cargar el dataset. Fin del programa')
        return
    
    exploracion_inicial(df)

    df_clean = preparar_dataset(df)

    print("\n--- CONTENIDO POR TIPO ---")
    print(contenido_por_tipo(df_clean))

    print("\n--- CONTENIDO POR AÑO (primeros años) ---")
    print(contenido_por_anio(df_clean).head())

    print("\n--- TOP PAISES ---")
    print(top_paises(df_clean))

    print("\n--- TOP GENEROS ---")
    print(top_generos(df_clean))

    print("\n--- CONTENIDO POR RATING ---")
    print(contenido_por_rating(df_clean))

    grafico_contenido_por_tipo(df_clean)
    grafico_contenido_por_anio(df_clean)
    grafico_top_paises(df_clean)
    grafico_distribucion_duracion(df_clean)
    grafico_contenido_por_rating(df_clean)
    grafico_top_generos(df_clean)

    # """
    # TODO:
    # - Definir la ruta al archivo netflix_titles.csv
    # - Cargar el dataset usando la funcion de carga
    # - Realizar una exploracion inicial del dataset para detectar posibles problemas
    # - Limpiar y preparar los datos antes del analisis
    # - Ejecutar las funciones de analisis definidas en el proyecto
    # - Mostrar por pantalla los resultados principales del analisis
    # - Generar y mostrar las visualizaciones correspondientes
    # - Asegurarse de que el flujo de ejecucion sigue un orden logico
    # """
    # pass


if __name__ == "__main__":

    main()
    # """
    # TODO:
    # - Ejecutar la funcion main
    # - Verificar que todo el flujo del programa se ejecuta correctamente
    # """
    # pass
