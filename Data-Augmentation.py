import os
lsOfFileNames = []    
#Iterate over folder and append filenames in list declared above. 
for files in os.walk("./granite"):#Make sure to give relative or absolute path to set-a folder
# you can check you current path via os.getcwd()
        for filename in files:
            print(files)
            lsOfFileNames.append(filename)
print(lsOfFileNames)
# Actual filenames start from 2nd index
lsOfFileNames = lsOfFileNames[2]


import io
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator,img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=90,
        width_shift_range=0.2,
        height_shift_range=[0.2, 1.0],
        brightness_range = [0.2, 1.0],
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

for image in os.walk('./granite/' + lsOfFileNames[image]):
    img = load_img()  
    x = img_to_array(img)

    x = x.reshape((1,) + x.shape)  # converting to a Numpy array with shape (1, 3, 150, 150)
    i = 0
    for batch in datagen.flow(x,save_to_dir='./ag/', save_format='jpg'):
        i += 1
        if i > 36:
            break 
