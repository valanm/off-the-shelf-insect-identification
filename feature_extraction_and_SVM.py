
import matplotlib.pyplot as plt

import os
import numpy as np

from sklearn.svm import SVC, LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedKFold

from keras.models import Sequential, Model
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import GlobalAveragePooling2D, GlobalMaxPooling2D
from keras.applications.vgg16 import VGG16



def save_all_features(nb_samples, source="images", dest="features", input_size = (416, 416), batch_size=6):
    
    """
    This function extracts features after every MaxPool layer in VGG16.
        Input:
            - nb_samples - total number of images you have 
            - source     - directory whit images as shown below:
                           - images:
                                -class 0:
                                    - im 0
                                    - im 1
                                    - im 2...
                                -class 1:
                                    - im 0
                                    - im 1...,
            - dest       - save features to this directory
            - input_size - image size in pixels
            - batch_size - number of images per epoch (larger input_size requires smaller batches)
        
        Output: 
            saves to "dest" directory:
                - X - features
                - Y - labels
                - filenames 
    """
    
    # check if the directory exists, and if not make it
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    # define image height and width
    (img_height, img_width) = input_size
    
    # build the VGG16 network and extract features after every MaxPool layer
    model = VGG16(weights='imagenet', include_top=False)
    
    c1 = model.layers[-16].output 
    c1 = GlobalAveragePooling2D()(c1)       

    c2 = model.layers[-13].output
    c2 = GlobalAveragePooling2D()(c2)       

    c3 = model.layers[-9].output
    c3 = GlobalAveragePooling2D()(c3)       

    c4 = model.layers[-5].output
    c4 = GlobalAveragePooling2D()(c4)       

    c5 = model.layers[-1].output
    c5 = GlobalAveragePooling2D()(c5)       

    model = Model(inputs=model.input, outputs=(c1,c2,c3,c4,c5))
    
    # define image generator without augmentation
    datagen = ImageDataGenerator(rescale=1./255.)    
    generator = datagen.flow_from_directory(
            source,
            target_size=(img_height, img_width),
            batch_size=batch_size,
            class_mode="sparse",
            shuffle=False)
    
    # generate and save features, labels and respective filenames
    steps = nb_samples/batch_size+1
    X = model.predict_generator(generator,steps)
    Y = np.concatenate([generator.next()[1] for i in range(0, generator.samples, batch_size)])
    names = generator.filenames

    for n, i in enumerate(X):
        with open(dest+"X-"+str(img_height)+"-c"+str(n+1)+"-AVG.npy", 'w') as f:
                np.save(f, i)
    if not os.path.exists(dest+"Y.npy"):
        with open(dest+"Y.npy"  , 'w') as f:
            np.save(f, Y)
    if not os.path.exists(dest+"filenames.npy"):
        with open(dest+"filenames.npy"  , 'w') as f:
            np.save(f, names)



def kfoldSVM_on_features(X, Y):
    # define 10-fold cross validation test harness
    kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=555)
    cvscores, splits = [],[]
    for train, test in kfold.split(X, Y):
        clf = LinearSVC(C=1.0, loss='squared_hinge', penalty='l2',multi_class='ovr')
        clf.fit(X[train], Y[train])
        y_pred = clf.predict(X[test])
        acc = accuracy_score(Y[test],y_pred)*100
        cvscores.append(acc)
        splits.append((Y[test], y_pred))
    print("Accuracy score averaged across 10 kfolds %.2f%% (+/- %.2f%%)" % (np.mean(cvscores), np.std(cvscores)))
   



def evaluate(dest="features", size=416, strategy = "-AVG"):
    #
    size = str(size)
    l1 = np.load(dest+"X-"+size+"-c1"+strategy+".npy")
    l2 = np.load(dest+"X-"+size+"-c2"+strategy+".npy")
    l3 = np.load(dest+"X-"+size+"-c3"+strategy+".npy")
    l4 = np.load(dest+"X-"+size+"-c4"+strategy+".npy")
    l5 = np.load(dest+"X-"+size+"-c5"+strategy+".npy")
    a_all = np.concatenate([l1,l2,l3,l4,l5], 1)
    
    X =[l1, l2, l3, l4, l5, a_all]
    
    Y = np.load(dest +"Y.npy")
    
    for n, x in enumerate(X):
        print
        if n==5:
        	print "fused features across all conv blocks"
        else:
	        print "conv block", n+1 
        print "without normalization"
        kfoldSVM_on_features(x, Y)
        print "with square root normalization"
        x = np.sqrt(np.abs(x)) * np.sign(x)
        kfoldSVM_on_features(x, Y)



input_size = (416,416)
nb_samples = 240 
save_all_features(nb_samples, source="./images/", dest="./features/", input_size=input_size)




print 
print
print "evaluating dataset with input size", input_size, "and GlobalAveragePooling2D"

evaluate(dest="./features/", size=input_size[0])

