from django.apps import AppConfig
import html
import pathlib
import os
import pickle
from django.conf import settings
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

class WebappConfig(AppConfig):
    path = os.path.join(settings.MODELS, 'models.p')
 
    # load models into separate variables
    # these will be accessible via this class
    with open(path, 'rb') as pickled:
    	data = pickle.load(pickled)
    logreg = data['logreg']
    linreg = data['linreg']
    vectorizer = data['vectorizer']
