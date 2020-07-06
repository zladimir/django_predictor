from django.apps import AppConfig
import html
import pathlib
import os
import pickle

class WebappConfig(AppConfig):
    name = 'fastbert'
    path = 'fastbert/model/models.p'
 
    # load models into separate variables
    # these will be accessible via this class
    with open(path, 'rb') as pickled:
    	data = pickle.load(pickled)
    logreg = data['logreg']
    linreg = data['linreg']
    vectorizer = data['vectorizer']
