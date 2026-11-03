
import gymnasium as gym
import numpy as np
import random
import tensorflow as tf
from collections import deque
from tensorflow.keras import layers

env = gym.make("FrozenLake-v1", is_slippery=False)

Q = tf.keras.Sequential([
    layers.Input(shape=(16,)),
    layers.Dense(24, activation="relu"),
    layers.Dense(4, activation="linear")
])

Q.compile(optimizer="adam", loss="mse")
memory = deque(maxlen=2000)

epsilon, gamma = 1.0, 0.95

for episode in range(500):
    state, _ = env.reset()
    done = False

    while not done:
        s = np.eye(16)[state].reshape(1, 16)

        if random.random() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q.predict(s, verbose=0)[0])

        ns, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated

        memory.append((state, action, reward, ns, done))
        state = ns

        if len(memory) >= 32:
            batch = random.sample(memory, 32)

            for st, a, r, nxt, end in batch:
                x = np.eye(16)[st].reshape(1, 16)
                y = Q.predict(x, verbose=0)
                target = r

                if not end:
                    nx = np.eye(16)[nxt].reshape(1, 16)
                    target += gamma * np.max(Q.predict(nx, verbose=0)[0])

                y[0][a] = target
                Q.fit(x, y, epochs=1, verbose=0)

    epsilon = max(0.05, epsilon * 0.99)

env.close()
print("Training Completed!")
