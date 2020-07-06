from django.apps import AppConfig
import html
import pathlib
import os
import pickle
from django.conf import settings


class WebappConfig(AppConfig):
    path = os.path.join(settings.MODELS, 'models.p')
 
    # load models into separate variables
    # these will be accessible via this class
    with open(path, 'rb') as pickled:
    	data = pickle.load(pickled)
    logreg = data['logreg']
    linreg = data['linreg']
    vectorizer = data['vectorizer']
