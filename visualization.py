import seaborn as sns
import matplotlib.pyplot as plt
from analysis import contenido_por_rating, top_generos, contenido_por_tipo, contenido_por_anio, top_paises
import pandas as pd

def grafico_contenido_por_tipo(df):
    
    datos = contenido_por_tipo(df)

    sns.barplot(x=datos.index, y=datos.values)
    plt.title = ('Numero de titulos por tipo de contenido')
    plt.xlabel = ('Tipo de contenido')
    plt.ylabel = ('Número de titulos')
    plt.show

    pass


def grafico_contenido_por_anio(df):

    datos = contenido_por_anio(df)

    sns.barplot(x=datos.index, y=datos.values)
    plt.title = ('Evolución del contenido por año')
    plt.xlabel = ('Año de lanzamiento')
    plt.ylabel = ('Número de titulos')
    plt.show()


    pass


def grafico_top_paises(df, n=5):

    datos = top_paises(df, n)
    
    sns.barplot(x = datos.values, y= datos.index)
    plt.title = ('Top', n, 'países con más titulos en Netflix')
    plt.xlabel = ('Número de titulos')
    plt.ylabel = ('País')
    plt.show()

    pass


def grafico_distribucion_duracion(df):

    df_filtrado = df.dropna(subset= ['duration_num'])

    sns.histplot(
        data=df_filtrado,
        x= 'duration_num',
        hue = 'type',
        bins = 30,
        multiple='stack'
    )
    plt.title = ('Distribución de la duración por contenido')
    plt.xlabel = ('Duración (minutos / temporadas)')
    plt.ylabel = ('Número de titulos')
    plt.show()

    pass


def grafico_contenido_por_rating(df):
    
    datos = contenido_por_rating(df)

    sns.barplot(x=datos.index, y=datos.values)
    plt.title= ("Número de títulos por rating")
    plt.xlabel= ("Rating")
    plt.ylabel= ("Numero de títulos")
    plt.xticks (rotation=45)
    plt.show()
    

    pass


def grafico_top_generos(df, n=5):

    datos = top_generos(df, n)

    sns.barplot(x=datos.values, y=datos.index)
    plt.title= ('Top', n, 'generos mas frecuentes')
    plt.xlabel= ("Numero de titulos")
    plt.ylabel= ("Genero")
    plt.show()

    pass

