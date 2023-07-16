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

#-----Image Detection-----#
st.subheader("Vegetable Recognition")
#st.write("Upload your photo and obtain your veggie category!")

model = keras.models.load_model('C:/Users/manya/Documents/Ironhack/Course/Final-project/models/model_def.keras')
train_generator = Image_Data_Generator_train('C:/Users/manya/Documents/Ironhack/Course/Final-project/images_15/train',(224,224), 32)
uploaded_file = st.file_uploader('Upload your photo and obtain your veggie category!',type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image_ = Image.open(uploaded_file)
    st.image(image_, caption="Uploaded photo")

    vegetable = predict_label(uploaded_file)
    st.markdown (f"The photo that you have upload is a **{vegetable}**")

    



#-----Location input------# 

st.subheader("Urban Garden Location in Spain ")
st.markdown ("Simply enter the address of your desired plant location in Spain, whether it's your backyard, a community garden, or a public park. GreenAdvisor will generate the most precise relevant planting recommendation based on the climate zone of your location. ")
address = st.text_input('Enter an address 👇', )
if address:

    #Hardiness Zone
    coordenadas = geocode(address)
    hsz_ = list(get_hsz(coordenadas[0],coordenadas[1]))[0]
    st.markdown (f"Your desired location is in the climate zone **{hsz_}**")




## Mardown
    ## Take a picture!
    #camera code

## Import model
#model = keras.models.load_model('../models/model_def.keras')

# Upload a photo
#uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])


