import json
import random

import numpy
import tflearn
import tensorflow


import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()


with open('intents.json') as file:
    data = json.load(file)
    print(data)
