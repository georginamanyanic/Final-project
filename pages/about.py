import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components
from PIL import Image
#from st_pages import Page, show_pages, add_page_title

st.set_page_config(page_title = "GreenAdvisor", page_icon = ":seedling:")

st.header("GreenAdvisor" ":seedling:")
st.markdown('''
            <style>
                .body {
                background-color: #ffffff; /* Establece el color de fondo en blanco */
                }
            .center {
            text-align: justify;
            font-size: 1.0rem;
            }
            </style>
            ''',  unsafe_allow_html=True)

st.markdown(
    """
    <p class='center'>Urban gardens play a crutial role in the transformation and sustainability of cities due to their environmental and social benefits. As environmental benefits they contribute to improve the local environment and reduce the impact of climate change by mitigating air pollution, reducing the urban heat island effect and capturing carbon dioxide. On the social side, urban gardens serve as community hubs, bringing people together, fostering social interactions and creating spaces for neighbors to collaborate and share knowledge. Moreover, they bring educational opportunities for children and young adults to learn practical skills and understand the importance of sustainable food systems.</p>
    """,
    unsafe_allow_html=True
)

image = Image.open('"c:/Users/manya/Documents/Ironhack/Course/Final-project/pages/urban_garden_1.jpg')
st.image(image, caption = 'Barcelona urban garden')

st.markdown("""
            <p class='center'> GreenAdvisor is a tool that empowers citizens to embark on their journey as urban gardeners by providing them with valuable information on how and when to plant their desired crops. Whether if you're a beginner or an experienced gardener, GreenAdvisor equips you with the necessary knowledge to make well-grounded decisions about your garden.</span></p>
            <p class='center'>The functionality of GreenAdvisor is simple yet powerful. Users can simply capture a photo of a vegetable using the tool, and thanks to its advanced neural network models, GreenSense accurately detects the vegetable type. Moreover, users can then input their location and GreenAdvisor leverages this information to provide detailed plant-specific insights. The information offered by the tool includes optimal sowing times and methods based on the climate zone of the location, temperature and spacing requirements, harvesting guidlines and even compatibility or incompatibility with other plants. It becomes your personalized gardening advisor, offering tailored recommendations specific to your urban environment.</p>
            <p class= 'center'> Find below more specific information on the classification of climate zones and the different sowing practices:</p>
            """, unsafe_allow_html = True
)

tab1, tab2= st.tabs(['Climate Zones - Hardiness Zones Classification System', 
                                  'Sowing practices'])

#with tab1: 

 
    





#show_pages(
    #[
        #Page("main.py", "GreenSense Tool", "🌱"),
        #Page("pages/about.py", "About", "💁‍♀️"),
    #]
#)



