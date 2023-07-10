import json
from geojson import  Polygon, Feature
import os
import geopandas as gpd
from shapely.geometry import Point
import time
import requests
import glob
import folium

def invert_coordinates(geojson):
    # Parse the GeoJSON data
    data = json.loads(geojson)
    
    # Iterate over the features
    for feature in data['features']:
        # Get the geometry coordinates
        coordinates = feature['geometry']['coordinates']
        
        # Iterate over the polygons
        for polygon in coordinates:
            # Iterate over the rings in each polygon
            for ring in polygon:
                # Invert the coordinates
                for i in range(len(ring)):
                    ring[i] = [ring[i][1], ring[i][0]]
    
    # Convert the modified data back to GeoJSON and return it
    inverted_geojson = json.dumps(data)
    return inverted_geojson

#Funció per transformar un multipolygon a polygon
def multipolygon_to_polygon(feature):
    polygons = []
    properties = feature['properties']
    for coordinates in feature['geometry']['coordinates']:
        polygon = Polygon(coordinates)
        polygon_feature = Feature(geometry=polygon, properties=properties)
        polygons.append(polygon_feature)
    return polygons


def get_hsz (lat,long):
    coordinates = Point(long, lat)
    data = gpd.read_file ('C:/Users/manya/Documents/Ironhack/Course/Final-project/geojson/tableau.geojson')
    result= data[data.intersects(coordinates)]['hzs']

    return result


def geocode (address):
    try:
            res = requests.get(f"https://geocode.xyz/{address}?json=1").json()
            if 'latt' in res and 'longt' in res:
                    coordenadas = [float(res['latt']),float(res['longt'])]
                    return coordenadas
                    
            else:
                print('No se pudo obtener las coordenadas. Error:', res.get('error', ''))
                
            
    except:
            time.sleep(3)
            #geocode(address)

    def estilo_hsz(feature):
        colores_hsz = {
    '4b': '#ff0000',
    '5a': '#00ff00',
    '5b': '#0000ff',
    '6a': '#ffff00',
    '6b': '#00ffff',
    '7a': '#ff00ff',
    '7b': '#800000',
    '8a': '#008000',
    '8b': '#000080',
    '9a': '#808000',
    '9b': '#800080',
    '10a': '#008080',
    '10b': '#ff8000',
    '11a': '#8000ff',
    '11b': '#ff0080',
    '12a': '#0080ff'
}
        hsz = feature['properties']['hzs']
        color = colores_hsz.get(hsz, '#ffffff')  # Color blanco si el tipo de hsz no está definido en la lista
        return {
        'fillColor': color,
        'color': '#000000',
        'weight': 1,
        'fillOpacity': 0.5}