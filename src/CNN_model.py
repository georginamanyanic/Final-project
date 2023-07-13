from PIL import Image 
import os 
import imghdr
import random
import shutil
import matplotlib.pyplot as plt
from keras.preprocessing import image
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import keras
from keras.callbacks import EarlyStopping
import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns


#TRANSFORMATION, REDISTRIBUTION AND RELOCATION OF THE EXTENDED IMAGE DATASET

def convert_png_to_jpg(folder_path):

    """This function is used to convert the PNG images from a folder to JPG images and drop
    the PNG images from the folder. The function takes one argument that is the folder
    path where the files are and doesn't return anything"""


    # Obtain the file list from the folder
    files = os.listdir(folder_path)

    for file in files:
        if file.endswith('.png'):
            # Create the complete path to the PNG file
            file_path = os.path.join(folder_path, file)

            # Open the PNG file and convert it to JPG 
            image = Image.open(file_path)
            image = image.convert('RGB')

            # Create the name of the output file in JPG format
            filename = os.path.splitext(file)[0]
            output_path = os.path.join(folder_path, f"{filename}.jpg")

            # Save the image in JPG
            image.save(output_path, 'JPEG')

            # Drop the original file in PNG
            os.remove(file_path)

    print('Complete conversion and PNG files eliminated.')


def resize_images(original_folder): 

    """This function is used to resize the files to 224x224 pixels in order to be uniform
    among them. This function takes as argument the original folder where the files are
    located. """
    
    #Loop through each file in the original folder
    for filename in os.listdir(original_folder): 
        # Get the file path
        file_path = f'{original_folder}/{filename}'
        try: 
            #Open the image file 
            image = Image.open(file_path)
            #Resize the image file to 224x224 pixels using antialias
            image = image.resize((224, 224), Image.ANTIALIAS)
            #Save the resized image
            image.save(file_path)
            #print(f"Rescaled {filename} successfully.")
        except Exception as e:
                #If an error occurs during the resizing, print a message 
                print(f"Error rescaling {filename}: {e}")


def split_train_test_val (original_folder, name_vegetable):
    """This function is used to split randomly the files from the original folder in the proportion of 
    70% for training set, 20% for test set and 20% for validation set and distributed to the 
    destination file. This function takes as arguments the orginal folder path where the files are located 
    name of the vegetable, """
    
    #Paths to train, test and validation folders
    train_dir = f'../images/train/{name_vegetable}'
    test_dir = f'../images/test/{name_vegetable}'
    val_dir = f'../images/validation/{name_vegetable}'

    #Original files list
    file_list = os.listdir(original_folder)

    # Obtain the quantity of files regarding the proportion desired
    num_train = int(len(file_list) * 0.7)
    num_test = int(len(file_list) * 0.15)
    num_validation = int(len(file_list) * 0.15)

    # Randomly shuffle the files list
    random.shuffle(file_list)

    #Distributes the files from original folder to the three diferent directories based on the file's position on the list
    for i, filename in enumerate(file_list):
        src_path = f'{original_folder}/{filename}' #SRC_pat is the source path from the file
        if i < num_train:
            dst_path = f'{train_dir}/{filename}'
        elif i < num_train + num_test:
            dst_path = f'{test_dir}/{filename}'
        else:
            dst_path = f'{val_dir}/{filename}'

        #Create the dst_path (destination path)
        os.makedirs(os.path.dirname(dst_path), exist_ok=True) 
        #Ciot the file fromt the src_path to the dst_path
        shutil.copy(src_path, dst_path) 

    print('Ended redistribution')



#CNN MODEL FUNCTIONS

def plot_images(image_categories, train_path):

    """This function is used to plot a photo of each category from the image data set. It takes two arguments: 
    - image categories: a list of the categories in the path (os.makedir())
    - train_path: folder train"""
    
    # Create plot
    plt.figure(figsize=(12, 12))

    #Enumerate adds a counter(label) on the list of vegetables categories
    for label, category in enumerate(image_categories): 

        # Load images for the ith category
        image_path = train_path + '/' + category 
        #List of all image files from a category
        images_in_folder = os.listdir(image_path)
        #Only plot the first one of each category
        first_image_of_folder = images_in_folder[0]
        first_image_path = image_path + '/' + first_image_of_folder
        img = image.load_img(first_image_path)
        #Convert the image to an array
        img_arr = image.img_to_array(img)/255.0 
        
        
        # Create a subplot and add the images for each category
        plt.subplot(4, 4, label+1)
        plt.imshow(img_arr)
        plt.title(category)
        plt.axis('off')
        
    plt.show()


def ImageDataGenerator (train_path, validation_path, test_path, target_size, batch_size): 

    """This function is used to create an image data flow generator that serves to provide 
    batches of image data during the training, validation and test phases of the model. The generator
    realizes the loading and pre-processing of the data and it returns batches of images along with 
    their labels. The function takes the following arguments: 
    - train_path, validation_path and test_path: paths to each set of images
    - target_size: tuple that is the width and height in pixel of the images
    - batch size: int, number of samples (images) propagated through the network """
    train_gen = ImageDataGenerator(rescale = 1.0/255.0) # Normalise the data
    train_image_generator = train_gen.flow_from_directory(
                                            train_path,
                                            target_size=target_size,
                                            batch_size=batch_size,
                                            class_mode='categorical')

# 2. Validation Set
    val_gen = ImageDataGenerator(rescale = 1.0/255.0) # Normalise the data
    val_image_generator = train_gen.flow_from_directory(
                                            validation_path,
                                            target_size=target_size,
                                            batch_size=batch_size,
                                            class_mode='categorical')

# 3. Test Set
    test_gen = ImageDataGenerator(rescale = 1.0/255.0) # Normalise the data
    test_image_generator = train_gen.flow_from_directory(
                                            test_path,
                                            target_size=target_size,
                                            batch_size=batch_size,
                                            class_mode='categorical')
    
    return train_image_generator, val_image_generator, test_image_generator


def model_creation ():
    """Fucntion:
    - filters: number of patterns learned by the layer from a input
    - kernel_size: dimensions of the filter for feature extraction
    - strides: number of pixels the kernel moves at each step while scanning the input
    - padding: technique to adjust the size of input data/feature maps before and after de convolutional process
    - activation: activation function that introduces non-linearity to the network
    - input_shape: 3D tensor [height, width, channels], definition of the shape of the input to the first layers
    """
    
    
    #Creation of sequential model object
    model = Sequential()

    #Add layers: 
    model.add(Conv2D(filters=filters, kernel_size=3, strides=1, padding='same', activation='relu', input_shape=[150, 150, 3]))
    model.add(MaxPooling2D(2)) #reduces the spatial dimensions of the input to 2x2
    model.add(Conv2D(filters=64, kernel_size=3, strides=1, padding='same', activation='relu'))
    model.add(MaxPooling2D(2))

    # Flatten the feature map to reshape the previous layer to one dimesional vector
    model.add(Flatten())

    # Add the fully connected layers that are responsible for non-linear mapping between input features and output labels
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.25)) #to prevent over-fitting droping a 0.25 rate 
    model.add(Dense(128, activation='relu')) #layer of 128 neurons and apply a relu function
    model.add(Dense(12, activation='softmax'))

    model.summary()

    return model


def train_model (model, train_image_generator, validation_image_generator):
    """
    - Optimizer: adam optimizer = momentum optimization + RMSProp
    - loss: categorical_crossentropy = measures difference between predicted class probabilities and true class labels
    """

    # Set up EarlyStopping callback, train will stop if there's no improvement in validation loss for 5 epochs
    early_stopping = EarlyStopping(patience=5)

    # Compile the model
    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])

    #Training the model
    history = model.fit(train_image_generator,
                        epochs=100,
                        verbose=1,
                        validation_data=validation_image_generator,
                        steps_per_epoch=len(train_image_generator),
                        validation_steps=len(validation_image_generator),
                        callbacks=[early_stopping])
    
    return history


def plot_trainig_metrics (history):

    """This function is used to plot the training and validation loss and accuracy curves to see the
     performance of the model and determine if there's over-fitting, under-fitting or goodfitting. It takes as 
     an argument the history, which is training history of the model"""
    plt.style.use('ggplot')
    plt.figure(figsize=(10, 5))
    plt.plot(history.history['loss'], c='teal', label='Training Loss')
    plt.plot(history.history['val_loss'], c='teal', linestyle='--', label='Validation Loss')
    plt.plot(history.history['accuracy'], c='orange', label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], c='orange', linestyle='--', label='Validation Accuracy')
    plt.xlabel("Number of Epochs")
    plt.legend(loc='best')
    plt.show()


def generate_predictions(train_image_generator, test_image_path, actual_label):

    class_map = dict([(v, k) for k, v in train_image_generator.class_indices.items()])
    
    # 1. Load and preprocess the image
    test_img = image.load_img(test_image_path, target_size=(150, 150))
    test_img_arr = image.img_to_array(test_img)/255.0
    test_img_input = test_img_arr.reshape((1, test_img_arr.shape[0], test_img_arr.shape[1], test_img_arr.shape[2]))

    # 2. Make Predictions
    #Find the index of the class with the highest probability representinc de predicted label
    predicted_label = np.argmax(model.predict(test_img_input)) 
    predicted_vegetable = class_map[predicted_label] #Retrieve the vegetable name associated with the label
    
    #3. Plotting
    plt.figure(figsize=(4, 4))
    plt.imshow(test_img_arr)
    plt.title("Predicted Label: {}, Actual Label: {}".format(predicted_vegetable, actual_label))
    plt.grid()
    plt.axis('off')
    plt.show()


def confusion_matrix (test_image_generator, predictions):

    y_pred_class = np.argmax(predictions, axis=1)
    y_true_class = test_image_generator.classes


    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        confusion_matrix(y_true_class, y_pred_class),
        annot=True,
        annot_kws={"fontsize": 10},
        fmt=".0f",
        linewidth=0.5,
        square=True)
    plt.show()













