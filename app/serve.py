#
"""
serve.py -
"""
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import pickle


def model_api(text, question, answer):
    path_to_model = 'static/trainedModel1.h5'
    model = load_model(path_to_model)
    query = [str(text) + ' ' + str(question) + ' ' + str(answer)]
    path_to_pickle = 'static/tokenizer.pickle'
    p = open(path_to_pickle, 'rb')
    tokenizer = pickle.load(p)
    print(tokenizer)
    query_sequences_int = pad_sequences(
        tokenizer.texts_to_sequences(query), maxlen=2000)
    result = model.predict(query_sequences_int)[0]
    print(result)
    return result[0] < result[1]


if __name__ == '__main__':
    print(model_api('John is going home.', 'Where is John going?', 'Home'))

    #response = model_api(request)
