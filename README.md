# Final-project 

## Índice 


## Descripción del proyecto


## Base de Datos 

## Workflow

## Machine Learning Model 

## Resultados

## Organización del proyecto 
Notebooks: 
-  **Scrapping**: extracción de los datos de la página web [Gardenate](https://www.gardenate.com/) mediante BeautifulSoup y obtención de dos Data frames importados a dos archivos .csv 
-  **Cleaning**: Transformación y limpieza de los dos Data Frames. 
-  **Location**: Encontrar en que zona climática se ubica una dirección usando los geojson y graficarlo mediante Folium. 
-  **Import_mysql**: importación de los dos archivos csv a MySQL para obtener la información en base a la zona climática de la ubicación y la verdura reconocida por el modelo de ML.
-  **CNN**: Convolutional Neural Network Model 
  

Data: 
- **characteristics (file)**: csv file extraído de Gardenate que contiene la información relativa a las características de la planta.
- **characteristics_cleaned (file)**: csv file limpio. 
- **seasonality (file)**: csv file extraido de Gardenate que contiene los meses en los que se debe sembrar la planta según la zona climática que sigue el sistema de clasificación de [Hardiness Zone](https://en.wikipedia.org/wiki/Hardiness_zone). 
- **seasonality_cleaned (file)**: csv file limpio.

Images: 
- La carpeta images contiene las imagenes usadas para el modelo de reconocimiento de verduras divididas en tres subcarpetas para el entrenamiento, validación y testeo del modelo. El dataset está formado por un total de 11440 imágenes de 11 clases de verduras distintas.

## Próximos pasos 

