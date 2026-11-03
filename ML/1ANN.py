import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense

data = pd.DataFrame({
    'X1': [1,2,3,4,5,6,7,8],
    'X2': [2,3,4,5,6,7,8,9],
    'Y':  [3,5,7,9,11,13,15,17]
})

print(data)

X = data[['X1','X2']].values
Y = data['Y'].values

model = Sequential([
    Dense(5, input_shape=(2,), activation='sigmoid'),
    Dense(1, activation='linear')
])

model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

model.fit(X, Y, epochs=100, batch_size=2, verbose=0)

pred = model.predict(X, verbose=0).flatten()

error = np.abs(Y - pred)

print("\nActual  Predicted  Error")
for a, p, e in zip(Y, pred, error):
    print(a, round(p,4), round(e,4))

print("\nMean Absolute Error:", round(np.mean(error),4))

w = model.get_weights()

print("\nHidden Weights:\n", w[0])
print("\nHidden Bias:\n", w[1])
print("\nOutput Weights:\n", w[2])
print("\nOutput Bias:\n", w[3])
