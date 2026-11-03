#FROZEN LAKE

import numpy as np
import gymnasium as gym
import time

env = gym.make("FrozenLake-v1", is_slippery=False)

Q = np.zeros((16, 4))

lr = 0.8
gamma = 0.95
epsilon = 1.0

for episode in range(3000):

    state, info = env.reset()

    for step in range(100):

        if np.random.random() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state])

        next_state, reward, done, truncated, info = env.step(action)

        if done or truncated:
            target = reward
        else:
            target = reward + gamma * np.max(Q[next_state])

        Q[state, action] += lr * (target - Q[state, action])

        state = next_state

        if done or truncated:
            break

    epsilon = max(0.01, epsilon - 0.001)

env.close()

print("Training Completed")
print("\nQ-Table:")
print(Q)

# ================= PLAY =================

env = gym.make(
    "FrozenLake-v1",
    is_slippery=False,
    render_mode="human"
)

state, info = env.reset()

print("\nAgent Playing...")

while True:

    action = np.argmax(Q[state])

    next_state, reward, done, truncated, info = env.step(action)

    print("State:", state, "Action:", action, "Reward:", reward)

    state = next_state

    time.sleep(1)

    if done or truncated:
        break
    
print("\nGame Finished")
print("Final Reward:", reward)

env.close()




# TAXI

import numpy as np
import gymnasium as gym
import time

env = gym.make("Taxi-v4")

Q = np.zeros((env.observation_space.n, env.action_space.n))

lr = 0.7
gamma = 0.99
epsilon = 1.0

for episode in range(3000):

    state, _ = env.reset()

    for step in range(100):

        if np.random.rand() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state])

        next_state, reward, done, truncated, _ = env.step(action)

        target = reward
        if not done:
            target += gamma * np.max(Q[next_state])

        Q[state, action] += lr * (target - Q[state, action])

        state = next_state

        if done or truncated:
            break

    epsilon = max(0.01, epsilon - 0.003)

env.close()

print("Training Completed")
print("\nQ-Table:")
print(Q)

# ================= PLAY TAXI =================

env = gym.make("Taxi-v4", render_mode="human")

state, _ = env.reset()

print("\nTaxi Agent Playing...")

while True:

    action = np.argmax(Q[state])

    next_state, reward, done, truncated, _ = env.step(action)

    print("State:", state, "Action:", action, "Reward:", reward)

    state = next_state

    time.sleep(0.5)

    if done or truncated:
        break

print("\nGame Finished")
print("Final Reward:", reward)

env.close()
