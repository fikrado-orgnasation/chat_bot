import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.eras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('word.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbotmodel.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.limmatize(word) for word in sentence_words]
    return sentence_word

def bag_of_words(sentence):
    sentence_word = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)            

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = mode.predict(np.array([bow]))[0]
    ERROR THRESHOLD = 0.25
    result = [[i, r] for i, r in enumerate(res) if r > ERROR THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0], 'probabil': str(r[1])]})
    return return_list
