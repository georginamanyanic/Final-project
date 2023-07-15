import os 
from dotenv import load_dotenv 
import pandas as pd
import pymysql
import sqlalchemy as alch

load_dotenv()
password = os.getenv("password")
#password = getpass("Please enter your password: ")

def get_charactersitics (vegetable):

    """This funciton takes a parameter vegetable, connects to a MYSQL database, executes de SQL query to filter 
    the characteristics of the spefici vegetable and return a DataFrame"""
    
    dbName = "plants"
    connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
    engine = alch.create_engine(connectionData)

    query = f"""SELECT name, sowing,spacing, harvest, compatibility, avoid, image_link, temperature FROM characteristics WHERE name = '{vegetable}'"""
                                
    df = pd.read_sql_query(query,engine)

    return df 


def get_seasonality (vegetable, hsz_):
     
    """This funciton takes two parameters (vegetable and hsz), connects to a MYSQL database, executes de SQL query to filter 
    when this vegetable can be sow based on the climateic zone and return a DataFrame"""
        
    dbName = "plants"
    connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
    engine = alch.create_engine(connectionData)

    query = f"""SELECT * FROM seasonality WHERE name = '{vegetable}' AND hardiness_zone = '{hsz_}'"""
                                    
    df = pd.read_sql_query(query,engine)

    return df 
