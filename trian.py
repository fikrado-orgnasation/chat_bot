import random
import json
import pickle
import numpy as np

import nltk
from nltk.sten import WordNetLemmatizer

from tensorflow.keras.models  import Sequential
from tensorflow.keras.layers Dense, Activation, Dropout
from tensorflow.optimizers import SGD

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

words = []
classess = []
documents = []
ignore_latters = ['!', '?', '.', ',']

for intent in intents['intentss']:
    for pattern in intent['patterns']:
        word-list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((woed_list, intent['tag']))
        if intent['tag'] not in classes:
            classess.append(intent['tag'])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_latters]
words = sorted(set(words))

classess = sorted(set(classess))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(words, open('classes.pkl', 'wb'))

training = []
output_empty = [0] * len(classess)

from document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)   
    output_row[classess.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:, 0])
train_y = list(training[:, 1])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]), ), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation= 'relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentorpy', optimizer=sgd, metrics=[,accuracy])

model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbotmodel.h5', hist)
print("finnaly you did it ")
