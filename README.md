## off-the-shelf-insect-identification
Main contribution of this repo is thorough evaluation of off-the-shelf approach for image classification based on a feature extraction with a single feed forward pass trough pretrained VGG16 ([Paper](https://academic.oup.com/sysbio/article/68/6/876/5368535) ).

### Dependencies (included in requirements.txt):
* python 2.7
* tensorflow (1.4.0)
* keras (2.1.1)
* plotly (2.2.2)

### Run instructions:
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

## Citation
If you find this useful, please cite our [paper](https://academic.oup.com/sysbio/article/68/6/876/5368535) with the following information:
```
@article{10.1093/sysbio/syz014,
    author = {Valan, Miroslav and Makonyi, Karoly and Maki, Atsuto and Vondráček, Dominik and Ronquist, Fredrik},
    title = "{Automated Taxonomic Identification of Insects with Expert-Level Accuracy Using Effective Feature Transfer from Convolutional Networks}",
    journal = {Systematic Biology},
    volume = {68},
    number = {6},
    pages = {876-895},
    year = {2019},
    month = {03},
    issn = {1063-5157},
    doi = {10.1093/sysbio/syz014},
    url = {https://doi.org/10.1093/sysbio/syz014},
    eprint = {http://oup.prod.sis.lan/sysbio/article-pdf/68/6/876/30252059/syz014.pdf},
}
```


