def contenido_por_tipo(df):

   return df['type'].value_counts()

    # """
    # TODO:
    # - Analizar la columna que indica el tipo de contenido
    # - Calcular cuantos titulos hay de cada tipo (por ejemplo Movie y TV Show)
    # - Devolver el resultado en una estructura adecuada para su posterior analisis o visualizacion
    # """
    # pass


def contenido_por_anio(df):

    return df['release_year'].value_counts().sort_index()

    # """
    # TODO:
    # - Analizar la columna de anio de lanzamiento
    # - Calcular cuantos titulos se publicaron en cada anio
    # - Ordenar el resultado de forma cronologica
    # - Devolver el resultado
    # """
    # pass


def top_paises(df, n=5):

    return df['country'].value_counts().head(n)

    # """
    # TODO:
    # - Analizar la columna de pais
    # - Calcular que paises tienen mayor numero de titulos
    # - Devolver unicamente los n paises con mas contenido
    # """
    # pass


def top_generos(df, n=5):

    generos = df['listed_in'].dropna().str.split(', ')

    generos_exploded = generos.explode()

    return generos_exploded.value_counts().head(n)

    # """
    # TODO:
    # - Analizar la columna de generos, teniendo en cuenta que puede haber varios generos por titulo
    # - Separar correctamente los distintos generos
    # - Calcular cuantos titulos hay por genero
    # - Devolver unicamente los n generos mas frecuentes
    # """
    # pass


def contenido_por_rating(df):

    return df['rating'].fillna('Unknown').value_counts()

    # """
    # TODO:
    # - Analizar la columna de rating
    # - Calcular cuantos titulos hay por cada rating
    # - Tener en cuenta valores faltantes o inconsistentes
    # - Devolver el resultado
    # """
    # pass

