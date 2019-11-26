# off-the-shelf-insect-identification
Main contribution of this repo is thorough evaluation of off-the-shelf approach for image classification based on a feature extraction with a single feed forward pass trough pretrained VGG16.

To run on your own dataset follow these steps (tested on Ubuntu 16.04):

open your terminal
```console
ctrl + alt + T
```


clone the off-the-shelf project
```console
git clone https://github.com/valanm/off-the-shelf-insect-identification.git
```

download and install [anaconda](https://www.anaconda.com/distribution/)

navigate to the cloned directory 
```console
cd /path/to/destination/off-the-shelf-insect-identification
```

create a new conda environment
```console
conda create -n myprojectname python=2.7 anaconda
```

activate the environment
```console
conda activate myprojectname
```

install the dependencies 
```console
pip install requirements.txt
```

place your images in directory named **images** so it has the following structure
```console
      - images:
            - category 0:
                  - im 0
                  - im 1
                  - im 2...
            - category 1:
                  - im 0
                  - im 1...,
```

run a stand alone script **feature_extraction_and_SVM.py**. The script extracts features from all the images and performes SVM classification with 10fold cross validation
```console
python feature_extraction_and_SVM.py
```

deactivate the environment
```console
conda deactivate
```
