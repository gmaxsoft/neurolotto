# libraries
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers

#intro
print("Neural Network Lottery prediction for lotto.pl")

# loading data from a file
def load_data():
    data = np.genfromtxt('dataset/data_lotto.txt', delimiter=',', dtype=int)
    data[data == -1] = 0
    train_data = data[:int(0.8*len(data))]
    val_data = data[int(0.8*len(data)):]
    max_value = np.max(data)
    return train_data, val_data, max_value

# Create the model
def create_model(num_features, max_value):
    model = keras.Sequential()
    model.add(layers.Embedding(input_dim=max_value+1, output_dim=64))
    model.add(layers.LSTM(256))
    model.add(layers.Dense(num_features, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# train the model
def train_model(model, train_data, val_data):
    history = model.fit(train_data, train_data, validation_data=(val_data, val_data), epochs=500)

# predict numbers
def predict_numbers(model, val_data, num_features):
    predictions = model.predict(val_data)
    indices = np.argsort(predictions, axis=1)[:, -num_features:]
    predicted_numbers = np.take_along_axis(val_data, indices, axis=1)
    return predicted_numbers

# print the predicted numbers
def print_predicted_numbers(predicted_numbers):
   print("Prawdopodobne numery to: ")
   print(', '.join(map(str, predicted_numbers[0])))

# main function
def run():
   train_data, val_data, max_value = load_data()
   num_features = train_data.shape[1]
   model = create_model(num_features, max_value)
   train_model(model, train_data, val_data)
   predicted_numbers = predict_numbers(model, val_data, num_features)
   print_predicted_numbers(predicted_numbers)

#run program
run()