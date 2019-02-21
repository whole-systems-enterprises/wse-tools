
#
# useful libraries
#
from keras import layers
from keras.models import Sequential
from keras import regularizers
from keras.models import Model

import uuid

#
# build a generic Keras LSTM classifier with equal number of cells in each LSTM layer
#
def build_generic_LSTM_classifier(number_of_layers, number_of_cells_per_layer, l2_regularization_constant = 0.001, dropout_rate = 0.2 ):
    model = Sequential()
    for i in range(0, number_of_layers - 1):
        model.add(layers.LSTM(number_of_cells_per_layer, kernel_regularizer=regularizers.l2(l2_regularization_constant), return_sequences = True))
        model.add(layers.Dropout(dropout_rate))
    model.add(layers.LSTM(cell_number, kernel_regularizer=regularizers.l2(l2_regularization_constant)))
    model.add(layers.Dropout(dropout_rate))
    model.add(layers.Dense(1, activation='sigmoid'))

    properties = {
        'model ID' : str(uuid.uuid4()),
        'construction' : {
            'number_of_layers' : number_of_layers,
            'number_of_cells_per_layer' : number_of_cells_per_layer,
            'l2_regularization_constant' :  l2_regularization_constant,
            'dropout_rate' : dropout_rate,
            },
        }

    return model, properties

#
# compile the generic Keras LSTM classifier given above
#
def compile_generic_LSTM_classifier(model, properties, optimizer='rmsprop', loss='binary_crossentropy', metrics = ['acc']):
    model.compile(
        optimizer = optimizer,
        loss = loss,
        metrics = metrics,
        )

    properties['compilation'] = {
        'optimizer' : optimizer,
        'loss' : loss,
        'metrics' : metrics,
        }

    return properties

#
# fit the generic Keras LSTM classifer given above
#
def fit_generic_LSTM_classifier(model, properties, train_x, train_y, val_x, val_y, epochs=20, batch_size=32):
    history = model.fit(
        train_x,
        train_y,
        validation_data = (val_x, val_y),
        epochs = epochs,
        batch_size = batch_size,
        )

    properties['fit'] = {
        'epochs' : epochs,
        'batch_size' : batch_size,
        }

    return history, properties


#
# create LSTM model framework
#
# This function is heavily modified from that found in https://github.com/natel9178/CS230-news-bias/blob/master/train.py
#
def create_LSTM_for_word_embedded(number_of_layers, number_of_cells_per_layer, embedding_layer, maximum_sequence_length, l2_regularization_constant = 0.001, dropout_rate = 0.2):

    sequence_input = layers.Input(shape=(maximum_sequence_length,), dtype='int32')
    embedded_sequences = embedding_layer(sequence_input)

    X = embedded_sequences
    for i in range(number_of_layers - 1):
        X = layers.LSTM(number_of_cells_per_layer, kernel_regularizer=regularizers.l2(l2_regularization_constant), return_sequences=True)(X)
        X = layers.Dropout(dropout_rate)(X)
    X = layers.LSTM(number_of_cells_per_layer, kernel_regularizer=regularizers.l2(l2_regularization_constant), return_sequences=False)(X)
    X = layers.Dropout(dropout_rate)(X)
    X = layers.Dense(1)(X)
    preds = layers.Activation('sigmoid')(X)

    properties = {
        'model ID' : str(uuid.uuid4()),
        'construction' : {
            'number_of_layers' : number_of_layers,
            'number_of_cells_per_layer' : number_of_cells_per_layer,
            'l2_regularization_constant' :  l2_regularization_constant,
            'dropout_rate' : dropout_rate,
            },
        }
    
    return Model(sequence_input, preds), properties
