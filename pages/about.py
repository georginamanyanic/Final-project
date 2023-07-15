import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components
from PIL import Image
import codecs
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

image = Image.open('c:/Users/manya/Documents/Ironhack/Course/Final-project/images_15/urban_garden_1.jpg')
st.image(image, caption = 'Barcelona urban garden', use_column_width=True)


st.markdown("""
            <p class='center'> GreenAdvisor is a tool that empowers citizens to embark on their journey as urban gardeners by providing them with valuable information on how and when to plant their desired crops. Whether if you're a beginner or an experienced gardener, GreenAdvisor equips you with the necessary knowledge to make well-grounded decisions about your garden.</span></p>
            <p class='center'>The functionality of GreenAdvisor is simple yet powerful. Users can simply capture a photo of a vegetable using the tool, and thanks to its advanced neural network models, GreenAdvisor accurately detects the vegetable type. Moreover, users can then input their location and GreenAdvisor leverages this information to provide detailed plant-specific insights. The information offered by the tool includes optimal sowing times and methods based on the climate zone of the location, temperature and spacing requirements, harvesting guidlines and even compatibility or incompatibility with other plants. It becomes your personalized gardening advisor, offering tailored recommendations specific to your urban environment.</p>
            <p class= 'center'> Find below more specific information on the classification of climate zones and the different sowing practices:</p>
            """, unsafe_allow_html = True
)

tab1, tab2= st.tabs(['Climate Zones - Hardiness Zones Classification System', 
                                  'Sowing practices'])

with tab1: 
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
    st.markdown ("""
                <p class='center'> For the climate zones, GreenAdvisor lies on the Hardiness Zones that consists on a classification system that divides regions based on ther average annual minimum temperatures. The system was developed by the United States Deparment of Agriculture (USDA) in order to help the gardeners and horticulturests in determining which plant species are most likely to thrive in specific areas. Each zone is identified by a numerical and alphetical designation that represents the average minimum degrees (see the below table).</p>  
                """,unsafe_allow_html=True)
                 
    image = Image.open('c:/Users/manya/Documents/Ironhack/Course/Final-project/images_15/hsz1.jpg')
    st.image(image, caption = 'Hardiness Zones table')
    st.markdown("""<p class='center'>Currently, the tool is limited to the Spanish territory, although it is planned to expand to all European countries and the United States. The following map represents all the hardiness zones of Spain: </p>
                """,unsafe_allow_html=True)
    
    def main():
        html_donut= """<div class='tableauPlaceholder' id='viz1689460253149' style='position: relative'><noscript><a href='#'><img alt='GreenAdvisor ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Gr&#47;GreenAdvisor&#47;Historia1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='GreenAdvisor&#47;Historia1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Gr&#47;GreenAdvisor&#47;Historia1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1689460253149');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1016px';vizElement.style.height='991px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_donut,width=800, height=700)
    if __name__ =="__main__":
        main()
        
 
    



#show_pages(
    #[
        #Page("main.py", "GreenSense Tool", "🌱"),
        #Page("pages/about.py", "About", "💁‍♀️"),
    #]
#)



