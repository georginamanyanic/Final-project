# VeggieAdvisor

## Table of Contents
- [VeggieAdvisor](#veggieadvisor)
  - [Table of Contents](#table-of-contents)
  - [Project Description](#project-description)
  - [Database](#database)
  - [Workflow](#workflow)
  - [Convolutional Neural Network](#convolutional-neural-network)
  - [My model and results](#my-model-and-results)
  - [Demonstration](#demonstration)
  - [Project Organization](#project-organization)
  - [Next steps](#next-steps)


## Project Description
Urban gardens play a vital role in the transformation and sustainability of cities by contributing to mitigate the impact of climate change in urban areas by decreasing the urban heat island effect or capturing carbon dioxide, fostering social interaction among neighbours and bring educational opportunities for children and young adults to learn practical skills and understand the importance of sustainable food systems.

VeggieAdvisor emerges as a tool to empower citizens to become urban gardeners by recognizing the precise vegetable category of a photo and providing them a planting guide of it relative to the climate zone of their location.

## Database
The database used for this project is divided into two parts: 
1. The image dataset corresponds to the [**Vegetable Image Dataset**](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset) created for the research paper "DCNN-Based Vegetable Image Classification Using Transfer Learning: A Comparative Study" by M. Israk Ahmed, Shahriyar Mahmud Mamun and Asif Uz Zaman Asif. The dataset contains 21000 images of 15 different kinds of vegetables, which are Bean, Bitter Gourd, Bottle Gourd, Brinjal, Broccoli, Cabbage, Capsixum, Carrot, Cauliflower, Cucumber, Potato, Pumpkin, Radish and Tomato. The dataset of images is splitted from 70% for training, 15% for validation, and 15% for testing purposes. This dataset is used for the **classification and recognition** of vegetables by applying a Convolutional Neural Networks (CNN) model.
   
2. The data for the creation of the planting guide was extracted from the webpage [Gardenate](https://www.gardenate.com/) through BeautifulSoup. It is divided in two DataFrames: 
     -  Dataframe of the general characteristics(characteristics) of the plants where you can find information on how to plant, the spacing between plants, temperature range, growing time and compatibility or incompatibility with other plants. 
     -  Dataframe of the months (seasonality) in which the plants should be planted according to the climatic zone determined by the [Hardiness Zone](https://en.wikipedia.org/wiki/Hardiness_zone) (HSZ) and the way in which they should be planted, i.e. plant under cover in seed trays, transplant seedlings or plant seeds.
  
    In total we have information on 95 categories of plants that include herbs and vegetables. However, for this project we will only use the information from the vegetables we have in the image dataset.

## Workflow
![Image](graphs/workflow.jpg)

## Convolutional Neural Network

Convolutional Neural Network (CNN) is a class of artifical neural network that is widely used for image classification and recognition. 

![CNNschema](https://www.researchgate.net/publication/336805909/figure/fig1/AS:817888827023360@1572011300751/Schematic-diagram-of-a-basic-convolutional-neural-network-CNN-architecture-26.ppm)

First, the model receives an **image input** that is interpreted as 3D matrix where the height and width are the spatial dimensions of the image, while the third dimension represents de color channels for RGB images. Secondly, CNN applies **convolutional layers** that slides a filter over the image to extract specific features of the images, which can be edges, textures or shapes. Then, a **pooling layer** is used to decrease the spatial size and focus on the relevant features, which helps to make the model more efficient and less sensitive to image changes. After that, the pooled features are **flattened** into a one-dimension vector that are passed to **fully connected layers**, which analyzes the features and make predictions based on them. Finally, the model produces an **output** that represents the predicted class of the input image. 

## My model and results 
Although my model shows good performance on the testing dataset, as observed in the confusion matrix, the accuracy decreases and the loss increases, indicating the presence of overfitting.

![ConfusionMatrix]('graphs/confusion_amtrix.png')

The overfitting phenomenon occurs when a model becomes too well-adapted to the training data, leading to difficulties in generalizing to new and unseen data. This is reflected in a decrease in accuracy and an increase in loss when evaluating the model with new data.

There are several reasons why overfitting may occur in a model. Some common causes include insufficient training data, excessive complexity in the model architecture, or a lack of regularization.

To address this issue, it is important to consider some strategies. One option is to gather more training data if possible, as this can provide a broader and more diverse range of cases. Another approach is to simplify the model architecture by reducing the number of layers or neurons, which can help prevent the model from overfitting.

Additionally, regularization techniques can be employed to prevent overfitting. This includes methods such as L1 or L2 regularization, dropout, or early stopping, which introduce constraints or penalties to the model during training, discouraging it from fitting the training data too closely.

By implementing these strategies, it is possible to mitigate overfitting and improve the model's generalization capabilities on unseen data.

## Demonstration
![Demonstration](streamlit_video_def.gif)


## Project Organization 
Notebooks: 
-  **Scrapping**: extraction of the data from de webpage [Gardenate](https://www.gardenate.com/) through BeautifulSoup and obtaining two Dataframes imported to csv 
-  **Cleaning**:Cleaning and transformation of 2 Dataframes. 
-  **Location**: Find in which climatic zone an address is located using the geojson files and graph it using Folium.
-  **Import_mysql**: import of the two csv files to MySQL to obtain the information based on the climatic zone of the location and the vegetable recognized by the ML model.
-  **CNN**: Convolutional Neural Network Model 
  

Data: 
- **characteristics (file)**: csv file extracted from Gardenate that contains the information related to the characteristics of the plant.
- **characteristics_cleaned (file)**: csv cleaned. 
- **seasonality (file)**: csv file extracted from Gardenate that contains the months in which the plant should be sown according to the climatic zone that follows the classification system of [Hardiness Zone](https://en.wikipedia.org/wiki/Hardiness_zone) (HSZ) .
- **seasonality_cleaned (file)**: csv cleaned.

Images_15: 
- Vegetable Image Dataset for classification and recognition with a total of 15 categories of vegetables.

Images_extended: 
- Vegetable Iamge Dataset of new categories for a future implentation of the model

Geojson: 
- To extrapolate the HSZ climate zones from the US to Spain, I have used the geojson files from the [PlantMaps](https://www.plantmaps.com/interactive-spain-plant-hardiness-zone-map-celsius.php) website. where each file in the old_geojson folder is an HSZ containing the areas of Spain that have those weather conditions. The final file used is tableau.geojson where all the files in the old folder have been compiled into a single geojson.

Pages: 
- About.py page with streamlit for the demostration

Main.py: 
- Functions and streamlit code for the realtization of the demonstration

src:
- modularized and encapsulate code


## Next steps 
- Enlarge the image dataset with more vegetable categories
- Extend the extrapolation of the location to more European countries
- Improve the model in order to avoid overfitting
- Add a calendar of when the vegetables can be collected
