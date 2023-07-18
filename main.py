import streamlit as st
import sys
sys.path.append('C:/Users/manya/Documents/Ironhack/Course/Final-project/src')
import json
#from geojson import  Polygon, Feature
import os
import geopandas as gpd
from shapely.geometry import Point
import time
import requests
import sql
import tensorflow as tf
from PIL import Image 
import seaborn as sns 
import keras.models
from keras.preprocessing import image
from CNN_model import Image_Data_Generator_train
import numpy as np
import calendar
import pandas as pd

#------Functions needed--------#
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

def predict_label (test_image_path):
     # 1. Load and preprocess the image
    test_img = image.load_img(test_image_path, target_size=(224, 224))
    test_img_arr = image.img_to_array(test_img)/255.0
    test_img_input = test_img_arr.reshape((1, test_img_arr.shape[0], test_img_arr.shape[1], test_img_arr.shape[2]))

    # 2. Make Predictions
    class_map = dict([(v, k) for k, v in train_generator.class_indices.items()])
    predicted_label = np.argmax(model.predict(test_img_input))
    predicted_vegetable = class_map[predicted_label]

    return predicted_vegetable

def obtain_values (df):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    values = ['S', 'T', 'P']
    values_description = {'S': 'Plant undercover seed trays',
                           'T': 'Transplant seedlings',
                           'P': 'Plant seeds'}
    dict_ = {}

    for value in values:
        months_value = [month for month in months if df[month].str.contains(value).any()]
        if months_value:
            dict_[values_description[value]] = months_value

    return dict_

#-----Image Detection-----#
st.subheader("Vegetable Recognition" ":camera_with_flash:")
st.markdown('''
            <style>
                .body {
                background-color: #ffffff; /* Establece el color de fondo en blanco */
                }
                .center {
                text-align: justify; 
            ''',  unsafe_allow_html=True)
#st.write("Upload your photo and obtain your veggie category!")

model = keras.models.load_model('C:/Users/manya/Documents/Ironhack/Course/Final-project/models/model_def.keras')
train_generator = Image_Data_Generator_train('C:/Users/manya/Documents/Ironhack/Course/Final-project/images_15/train',(224,224), 32)

##Camera
#img_file_buffer = st.camera_input("Take a picture of a veggie and GreenAdvisor will recognize what it is!")
#if img_file_buffer is not None:
    #To save tmeperoray the iamge
    #image_ = Image.open(img_file_buffer)
    #image_ = image_.resize((224,224))
    #st.image(image_, caption="Uploaded photo")



st.markdown('Upload your photo and GreenAdvisor will recognize what veggie it is!')
uploaded_file = st.file_uploader('Upload photo',type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    #To save tmeperoray the iamge
    image_ = Image.open(uploaded_file)
    image_ = image_.resize((224,224))
    st.image(image_, caption="Uploaded photo")
    
    #Predictions
    vegetable = predict_label(uploaded_file)
    st.markdown (f"The photo that you have upload is a **{vegetable}**")

##-----NO photo-------#
characteristics = pd.read_csv('C:/Users/manya/Documents/Ironhack/Course/Final-project/data/characteristics_cleaned.csv')


#-----Location input------# 

st.subheader("Urban Garden Location in Spain" ":round_pushpin:" )
st.markdown ("<p class='center'>Simply enter the address of your desired plant location in Spain, whether it's your backyard, a community garden, or a public park. GreenAdvisor will generate the most precise relevant planting recommendation based on the climate zone of your location.</p>", unsafe_allow_html=True)
address = st.text_input('Enter an address 👇', )
if address:

    #Hardiness Zone
    coordenadas = geocode(address)
    hsz_ = list(get_hsz(coordenadas[0],coordenadas[1]))[0]
    st.markdown (f"Your desired location is in the climate zone **{hsz_}**")
    



#-----Planting Guide-----#
st.subheader("Planting Guide" ":thumbsup:")
if address and hsz_:
    st.markdown(f"""<p class='center'> Based on the recognition of the vegetable and the climate zones, GreenAdvisor will provide you the ultimate planting guide with general characteristics to take care of the plant and when and how to sow it. </p>""",  unsafe_allow_html=True)

#Import the data frames from sql
    characteristics = sql.get_charactersitics(vegetable)
    seasonality = sql.get_seasonality (vegetable, hsz_)
    st.markdown (f"##### {vegetable} recommendation in climate zone {hsz_}")
    
    #Sowing row
    st.markdown (f"🌱 Sowing recommendation:{characteristics['sowing'][0]}", unsafe_allow_html=True)
    #Temperature 
    st.markdown (f"🌡️ {characteristics['temperature'][0]}", unsafe_allow_html=True)
    #Harvest
    st.markdown (f"☀️ {characteristics['harvest'][0]}", unsafe_allow_html=True)
    #Compatbility
    st.markdown (f"✅ It is compatible with {characteristics['compatibility'][0]}", unsafe_allow_html=True)
    #Avoid
    st.markdown (f"❌ Avoid {characteristics['avoid'][0]}", unsafe_allow_html=True)
    # Spacing
    st.markdown (f"📏 Distance between plants {characteristics['spacing'][0]}", unsafe_allow_html=True)

    # When to sow? 
    #seasonality = seasonality.replace(np.nan,'X', regex = True, inplace= True)
    st.markdown("📆 Sowing time: ")
    def color_cells(val):
        if val == 'S':
            color = '#A68464'  # Color para 'S'
        elif val == 'T':
            color = '#A4AC86'  # Color para 'T'
        elif val == 'P':
            color = '#B6AD90'  # Color para 'P'
        else:
            color = 'white'  # Color para celdas vacías
        return f'background-color: {color}'
    
    styled_cal = seasonality.style.applymap(color_cells)
    st.dataframe(styled_cal)
    
    st.markdown(
        """
        <style>
        .S {
            background-color: #A68464;
        }
        .T {background-color: #A4AC86;
        
        }
        .P {background-color: #B6AD90;
        
        }
        </style>
        """
        , unsafe_allow_html=True
    )
    st.markdown("""Sowing Practices*:""")
    st.markdown(
    '<span class="S">Sowing undercover seed trays (S)</span>',
    unsafe_allow_html=True
    )
    st.markdown(
    '<span class="T"> Transplanting seedlings (T)</span>',
    unsafe_allow_html=True
    )
    st.markdown(
    '<span class="P"> Planting seeds (P)</span>',
    unsafe_allow_html=True
    )
    st.write('*See more information in the about page')

    ## Add button for downloading data 
    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv_1 = convert_df(characteristics)

    st.download_button(
        label="Download general characteristics as CSV",
        data=csv_1,
        file_name='characteristics.csv',
        mime='text/csv',
    )

    csv_2 = convert_df (seasonality)
    st.download_button(
        label="Download time to sowing as CSV",
        data=csv_2,
        file_name='seasonality.csv',
        mime='text/csv',
    )




## Mardown
    ## Take a picture!
    #camera code

## Import model
#model = keras.models.load_model('../models/model_def.keras')

# Upload a photo
#uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])


