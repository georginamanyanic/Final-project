import json
from geojson import  Polygon, Feature
import os
import geopandas as gpd
from shapely.geometry import Point
import time
import requests
import glob

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