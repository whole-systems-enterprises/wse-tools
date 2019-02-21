#
# load useful libraries
#
import numpy as np
from keras.layers import Embedding

#
# index GloVe embeddings
#
# This function is (very) slightly modified from that found in https://github.com/natel9178/CS230-news-bias/blob/master/train.py
#
def index_glove_embeddings(filename):
    embeddings_index = {}
    with open(filename) as f:
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            embeddings_index[word] = coefs
    return embeddings_index

#
# Create embedding layer
#
# This function is (very) slightly modified from that found in https://github.com/natel9178/CS230-news-bias/blob/master/train.py
#
def create_embedding_layer_GloVe(word_index, embeddings_index, EMBEDDING_DIM=100):
    num_words = len(word_index) + 1

    embedding_matrix = np.zeros((num_words, EMBEDDING_DIM))

    for word, i in word_index.items():
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector

    return Embedding(
        num_words,
        EMBEDDING_DIM,
        weights=[embedding_matrix],
        trainable=False
        )
