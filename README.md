# off-the-shelf-insect-identification
Main contribution of this repo is thorough evaluation of off-the-shelf approach for image classification based on a feature extraction with a single feed forward pass trough pretrained VGG16.

To run on your own dataset:
1. 
```console
git clone https://github.com/valanm/off-the-shelf-insect-identification.git
```
2. download and install [anaconda](https://www.anaconda.com/distribution/)
3. 
```console
cd /path/to/destination/off-the-shelf-insect-identification
```
4. 
```console
conda create -n myprojectname python=2.7 anaconda
```
5. 
```console
conda activate myprojectname
```
6. 
```console
pip install requirements.txt
```
7. place your images in directory named **images** so it has the following structure
      - images:
            - class 0:
                  - im 0
                  - im 1
                  - im 2...
            - class 1:
                  - im 0
                  - im 1...,
8. run a stand alone script **feature_extraction_and_SVM.py**. The script extracts features from all the images and performes SVM classification with 10fold cross validation
```console
python feature_extraction_and_SVM.py
```
9. 
```console
conda deactivate
```

```python
s = "Python syntax highlighting"
print s
```
