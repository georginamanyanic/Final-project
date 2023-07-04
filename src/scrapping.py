import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from dotenv import load_dotenv
import time
import os
load_dotenv()

from bs4 import BeautifulSoup
import re as re
import time
import pandas as pd
import os
import numpy as np
import requests

def plant_names (url): 
    """Esta función sirve para obtener el nombre de todas las plantas usando la librería beautiful soup. La función toma como argumento un url
    donde aparecen todos los nombres de las plantas y devuelve una lista de nombre."""
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")

    plants_list = soup.find_all('div',{'class':'plant col-sm-12'})
    names_plants = [i.getText().split('(')[0].strip().replace(' ','%2B').replace('/','~') for i in plants_list] #Cambio formato replace para adecuarlo al formato que tiene el url

    for i in range(len(names_plants)):
        if names_plants[i] == 'Artichokes':
            names_plants[i] = 'Artichokes%20(Globe)'
        elif names_plants[i] == 'Strawberries':
            names_plants[i] = 'Strawberries%2B%28from%2Bseeds%29'

    return names_plants

names_plants = plant_names('http://www.gardenate.com/plants/')


def zones (url):
    """Esta función sirve para obtener todas las zonas climáticas registradas en la página web y guardarlos en un diccionario donde la key es el value (numero
     de zona climática) y el value es el nombre de la zona climática. La función toma como argumento un link y devuelve un diccionario. """

    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")

    filter = soup.find("select", class_="form-control zone-selector")
    
    # Diccionario vació para guardar las zonas climáticas
    climate_zones = {}

    # Extraer la opción elementos y completar el diccionario
    for option in filter.find_all("option"):
        zone_number = option["value"]
        zone_name = option.text.strip()
        climate_zones[zone_number] = zone_name

    return climate_zones



def filter_dict_climate (dict_, substring): 

    """Esta función sirve para crear un nuevo diccionario a partir de otro en base a aquellos values que contengan una substring, lo uso para obtener solamente
    los links que sean de las zonas climáticas de USA."""
    new_dict = {}

    for key, value in dict_.items(): 
        if substring in value:
            new_dict[key] = value
    return new_dict


def get_urls_plants (list_):
    """Esta función sirve para crear los link de todas las plantas a partir de la lista de nombre de plantas. Toma como argumento una lista y devuelve
    otra lista de links"""
    list_url = []
    for i in list_:
        list_url.append(f'https://www.gardenate.com/plant/{i}')
    return list_url


def get_urls_complete (list_, dict_): 
    """Esta función sirve para crear los links de todas las plantas según zona climática. Toma como argumento la lista de nombre de plantas y el diccionario
    de zonas climáticas y devuelve una lista de links"""
    list_url = []
    for i in list_:
        for j in dict_.keys():
            list_url.append(f'https://www.gardenate.com/plant/{i}?zone={j}')
    return list_url


def characterisitics(list_):

    """Esta función se utiliza para extraer de una lista de links y crear un dataframe de características de las plantas, por lo que la función 
    toma como valor una lista de urls y devuelve un data frame"""

    plants = []

    for i in list_: #url_plants
        html = requests.get(i)
        soup = BeautifulSoup(html.content, "html.parser")
        
        
        # Find the position of the last / 
        last_slash_index = i.rfind("/")

        # Extract the desired part of the url
        name = i[last_slash_index + 1 :]
  
         
        # Extract sowing if available
        sowing_element = soup.find("li", {'class': 'sowing'})
        sowing = sowing_element.getText() if sowing_element else np.nan
        
        # Extract spacing if available
        spacing_element = soup.find("li", {'class': 'spacing'})
        spacing = spacing_element.getText() if spacing_element else np.nan
        
        # Extract harvest if available
        harvest_element = soup.find("li", {'class': 'harvest'})
        harvest = harvest_element.getText() if harvest_element else np.nan

        companion_element = soup.find("li", {'class': 'companion'})
        companion = companion_element.getText() if companion_element else np.nan

        avoid_element = soup.find("li", {'class': 'avoid'})
        avoid = avoid_element.getText() if avoid_element else np.nan



        image_link_element = soup.find("div", {"class":"image"})
        image_link = ('www.gardenate.com' + image_link_element.find("a").get('href') if image_link_element is not None else np.nan)

        dict_ = {'name':name ,'sowing':sowing, 'spacing':spacing, 'harvest':harvest, 'compatibility':companion,'avoid':avoid, 'image_link': image_link}

        plants.append(dict_)

        df = pd.DataFrame(plants)
        
    return df 


def drop_url_list (list_, string):
    """Función para quitar un link de la lista de links"""
    list_.remove(string)
    return list_



def check_links(list_):

    """Función para chequar si todos los urls de la lista funcionan. Toma como valor la lista y printea solamente los links que no
    funcionen."""
    for link in list_:
        try:
            response = requests.get(link)
            if response.status_code != 200:
                print(f"Link {link} is not working. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while checking link {link}: {str(e)}")



def months_to_plant (url): 
    
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")

    table = soup.find('table')
    rows = table.find_all('tr')

    name = re.search(r'/([^/?]+)\?', url).group(1)
    zone = re.search(r'zone=(\d+)', url).group(1)

    data = []
    headers = [header.text.strip() for header in rows[0].find_all('th')]

    for row in rows[1:]:
        if row is None:
            cells = np.nan
        else:
            cells = [cell.text.strip() for cell in row.find_all('td')]
        data.append(cells)


    df_plant = pd.DataFrame(data, columns = headers)
    df_plant ['name'] = name 
    df_plant ['zone'] = zone

    return df_plant 


def concat_multiple_tables(list_):
    
    dfs = []

    for i in list_:
        df = months_to_plant(i)
        if df is not None: 
            dfs.append(df)
    combined_df = pd.concat(dfs, ignore_index = True)

    return combined_df





