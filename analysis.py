def contenido_por_tipo(df):

   return df['type'].value_counts()


def contenido_por_anio(df):

    return df['release_year'].value_counts().sort_index()


def top_paises(df, n=5):

    return df['country'].value_counts().head(n)


def top_generos(df, n=5):

    generos = df['listed_in'].dropna().str.split(', ')

    generos_exploded = generos.explode()

    return generos_exploded.value_counts().head(n)


def contenido_por_rating(df):

    return df['rating'].fillna('Unknown').value_counts()



