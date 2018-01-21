import tensorflow
import keras
import os
import numpy as np
import sys
import pickle
from sklearn.model_selection import train_test_split
from keras.layers import Dense, Embedding, LSTM, Dropout
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

BASE_DIR = ''
GLOVE_DIR = os.path.join(BASE_DIR, 'data/glove')
MAX_SEQUENCE_LENGTH = 2000
MAX_NUM_WORDS = 200000
EMBEDDING_DIM = 50

embeddings_index = {}
f = open(os.path.join(GLOVE_DIR, 'glove.6B.50d.txt'))
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

data = pd.read_csv("data/qa2.csv").sample(20000)

text = []
for index, row in data.iterrows():
    context = str(row['Context'])
    question = str(row['Question'])
    answer = str(row['Answer'])
    text.append(context)
    text.append(question)
    text.append(answer)


# finally, vectorize the text samples into a 2D integer tensor
tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
tokenizer.fit_on_texts(text)

# save the tokenizer
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

tokenizer = pickle.load( open( "tokenizer.pickle", "rb" ) )

word_index = tokenizer.word_index

def cleanString(string, wordIndex):
    splitString = string.split(' ')
    resultwords  = [word for word in splitString if word.lower() in wordIndex]
    result = ' '.join(resultwords)
    return result

data_concat = []
words = list(word_index.keys())
for index, row in data.iterrows():
    context = cleanString(str(row['Context']), words)
    question = cleanString(str(row['Question']), words)
    answer = cleanString(str(row['Answer']), words)
    
    data_concat.append(context + " " + question + " " + answer)

data_int_seq = pad_sequences(tokenizer.texts_to_sequences(data_concat), maxlen=MAX_SEQUENCE_LENGTH)

labels = to_categorical(np.asarray(data['Label']))

print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)

# split the data into train and test test
X_train, X_test, y_train, y_test = train_test_split(data_int_seq, labels, test_size = 0.3)

# number of words which is equal to either the size of the vocabulary or the maximum number of words
num_words = min(MAX_NUM_WORDS, len(word_index))

embedding_matrix = np.zeros((num_words, EMBEDDING_DIM))


for word, i in word_index.items():
    i = i -1
    if i >= MAX_NUM_WORDS:
        continue
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        # words not found in embedding index will be all-zeros.
        embedding_matrix[i] = embedding_vector



# load pre-trained word embeddings into an Embedding layer
# note that we set trainable = False so as to keep the embeddings fixed
embedding_layer = Embedding(input_dim = num_words,
                            output_dim = EMBEDDING_DIM,
                            weights = [embedding_matrix],
                            input_length = X_train.shape[1], #MAX_SEQUENCE_LENGTH,
                            trainable=False, 
                            mask_zero = True)


model = Sequential()
model.add(embedding_layer)
model.add(LSTM(50))
model.add(Dense(2,activation='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])
print(model.summary())


model.fit(X_train, y_train, epochs = 4, batch_size = 128)

scores = model.evaluate(X_test, y_test)
print("Accuracy: %.2f%%" % (scores[1]*100))

model.save('trainedModel2.h5')

new_data = ["Jhon is going to the pub Whre is jhon? going to the pub" ]

new_data_int_seq = pad_sequences(tokenizer.texts_to_sequences(new_data), maxlen=MAX_SEQUENCE_LENGTH)

prediction = model.predict(new_data_int_seq)[0]

if prediction[1] > prediction[0]: 
    print("Correct") 
else:
    print("Incorrect")



