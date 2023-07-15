import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title = "DAT(A)RT", page_icon = ":sunglasses:")

st.header("Introduction")
st.markdown(
    """
    <style>
        .center {
            text-align: left;
            font-size: 1.0rem;
        }
        .italic {
            text-align: center;
            font-size: 1.0rem;
            font-style: italic;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <p class='center'>Art has been a popular form of expression throughout history, capable of evoking emotions, stimulating thought and awakening emotional responses in those who appreciate it. Several studies have proved that art and creativity are attributes that have played a significant role in the evolution and natural selection of human beings.However, understanding how and why paintings evoke emotions is still a challenge.</p>
    <p class='italic'> <span style='color: red;'> What are the emotions most commonly triggered by art? Why are some paintings more evocative than others? Why do we like certain paintings and not others?</p>
    <p class='center'>In this context, emerges the Dat(A)rt project, which aims to explore the interaction between art and the viewer using technology as an ally. The main focus has been the application of image style transfer techniques, allowing to merge a classic artwork with a selfie and thus establishing a dialogue between both forms of expression.</span></p>
    <p class='center'>In addition, an interactive tool has been developed to offer users the possibility to explore and discover artworks according to the emotions they experience. This tool revolutionizes the way we connect with artistic movements and artists by visually organizing a large database of artworks in terms of emotional parameters that describe their emotional content.</p>
    <p class='center'>In conclusion, through the use of image style transfer techniques and the creation of an interactive tool, this project seeks to explore how paintings can influence our emotions and how these emotions can be transmitted and transformed in different contexts. This work offers new perspectives on the relationship between art, emotions and human experience, thus opening new possibilities for the enjoyment and appreciation of art in the digital world.</p>
    """,
    unsafe_allow_html=True
)







tab1, tab2, tab3, tab4 = st.tabs(['WikiArt Emotions Dataset', 
                                  'Workflow',
                                  'Repository organization',
                                  'Next steps'])
with tab1:

    st.markdown('The data handled in this project is based on the ["WikiArt Emotions"](http://saifmohammad.com/WebPages/wikiartemotions.html) dataset. This dataset was compiled from WikiArt and annotated by crowdworkers for the research [paper](http://saifmohammad.com/WebDocs/lrec2018-paper-art-emotion.pdf) entitled *"WikiArt Emotions: An An Annotated Dataset of Emotions Evoked by Art"*, by Dr. Saif M. Mohammad and Dr. Svetlana Kiritchenko. As a result, 4,019 images were obtained representing 22 categories of four major styles: Renaissance, Post-Renaissance, Modern and Contemporary.')

    def main():
        html_donut= """<div class='tableauPlaceholder' id='viz1686147825076' style='position: relative'><noscript><a href='#'><img alt='DONUT ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ar&#47;Art22sentiments&#47;DONUT&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Art22sentiments&#47;DONUT' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ar&#47;Art22sentiments&#47;DONUT&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1686147825076');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='750px';vizElement.style.maxWidth='800px';vizElement.style.width='100%';vizElement.style.height='777px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='750px';vizElement.style.maxWidth='800px';vizElement.style.width='100%';vizElement.style.height='777px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_donut,width=800, height=700)
    if __name__ =="__main__":
        main()

    st.write('Each artwork in the dataset was annotated by ten crowdworkers, who were presented with a set of 20 emotion words classified as "Positive Emotions", "Negative Emotions" and "Mix/Neutral". The crowdworkers were asked to make annotations based on:')
    st.markdown('''
    - **Scenario I**: presenting only the image of the work (without title)
    - **Scenario II**: presenting only the title of the artwork (no image)
    - **Scenario III**: presenting both the title and the image of the artwork
    ''')

    st.write('In addition, each individual was asked to rate:')
    st.markdown('''
    - The artwork on a scale of -3 (strongly dislike) to 3 (strongly like)
    - Whether the image shows the face/body of a person/animal
    - Whether it is a painting or a different thing (e.g., a sculpture)
    ''')


with tab2:
    current_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_path, "../images/workflow/workflow_white-06.png")
    st.image(image_path, caption="Methodology of work")


with tab3:
    st.write('Aqui va un listado sobre la organización del repo')
with tab4:
    st.write('aqui va la explicacion de como el usuario interactua con la plataforma')