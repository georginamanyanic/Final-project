import pandas as pd 
import re 
import numpy as np
import json
import os 

def cleaning_names (df, column):
    for i in range(len(df[column])):
        df[column][i] = df[column][i].replace('%2B', ' ').replace('%20(Globe)','').replace('%29', '').replace('~','/').replace('%28', '').rstrip()
    return df



def column_cleaner (df):

    #Sowing column:
    df['sowing'] = df['sowing'].apply(lambda i: re.sub(r'\.\s+','. ',i))
    df['sowing'] = df['sowing'].apply(lambda i: i.replace('(Show °F/in) \n','').rstrip())
    df['temperature'] = df['sowing'].apply(lambda x: re.findall(r'\d+°C\s+and\s+\d+°C', x)[0]) #Creo una columna nueva
    df['sowing'] = df['sowing'].apply(lambda x: re.sub(r'\s+Best\s+planted\s+at\s+soil\s+temperatures\s+between\s+\d+°C\s+and\s+\d+°C\.', '', x))

    df['spacing'] = df['spacing'].apply(lambda i: re.sub(r'\s+',' ',i).split(':')[1])

    df['harvest'] = df['harvest'].apply(lambda i: re.sub(r'\s+',' ',i))

    df['compatibility'] = df['compatibility'].apply(lambda i: i.split(':')[1] if type(i)==str else np.nan )

    df['avoid'] = df['avoid'].apply(lambda i: i.split(':')[1] if type(i)==str else np.nan )

    df.drop(columns='Unnamed: 0', inplace = True)

    return df 



def filter_and_aggregate(df, column, dict_):
    # Convertir las keys a integer
    dict_int = {int(k): v for k, v in dict_.items()}
    
    # Filtrar las filas que contengas los  mismos valores de la columna "zone" que las claves del diccionario
    df_filtered = df[df[column].isin(dict_int.keys())].copy()

    
    # Agregar una nueva columna al DataFrame con los valores correspondientes del diccionario
    df_filtered['hardiness_zone'] = df_filtered[column].map(dict_int)
    
    return df_filtered



def invert_coordinates(geojson):

    """Esta función se utiliza para invertir las coordenadas de los archivos .geojson que se encuentran en la carpeta geojson dado que estan
    al revés. La función toma como valor el archivo .geojson iterar sobre las keys hasta encontrar las coordenadas e invertirlas devolviendo otra vez
    un archivo invertido"""
    
    # Convertir el geojson
    data = json.loads(geojson)
    
    # Iterar sobre las features
    for feature in data['features']:
        # Encontrar las coordenadas geométricas
        coordinates = feature['geometry']['coordinates']
        
        # Iterar sobre los polígonos
        for polygon in coordinates:
            # Iterar sobre los rings de cada polígono
            for ring in polygon:
                # Invertir las coordenadas
                for i in range(len(ring)):
                    ring[i] = [ring[i][1], ring[i][0]]
    
    # Convertir los datos modificados a geojson otra vez
    inverted_geojson = json.dumps(data)
    return inverted_geojson

