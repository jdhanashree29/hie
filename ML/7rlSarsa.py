#Slippery_True:


import numpy as np
import gymnasium as gym
import time


env = gym.make("FrozenLake-v1", is_slippery=True)

Q = np.zeros((16, 4))

alpha = 0.1
gamma = 0.99
epsilon = 1.0
min_epsilon = 0.01
epsilon_decay = 0.9995

episodes = 20000

for episode in range(episodes):

    state, _ = env.reset()

    for step in range(100):

        if np.random.random() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state])

        next_state, reward, terminated, truncated, _ = env.step(action)

        if terminated or truncated:
            target = reward
        else:
            target = reward + gamma * np.max(Q[next_state])

        Q[state, action] += alpha * (
            target - Q[state, action]
        )

        state = next_state

        if terminated or truncated:
            break

    # Reduce exploration gradually
    epsilon = max(min_epsilon, epsilon * epsilon_decay)

env.close()

print("Training Completed")
print("\nQ-Table:")
print(np.round(Q, 3))


env = gym.make(
    "FrozenLake-v1",
    is_slippery=True,
    render_mode="human"
)

success = 0
test_episodes = 10

for episode in range(test_episodes):

    state, _ = env.reset()
    reward = 0

    print("\nTest Run:", episode + 1)

    for step in range(100):

        action = np.argmax(Q[state])

        state, reward, terminated, truncated, _ = env.step(action)

        time.sleep(0.2)

        if terminated or truncated:
            break

    if reward == 1:
        print("Reached the Goal!")
        success += 1
    else:
        print("Did not reach the Goal.")

print("\nSuccessful Runs:", success, "/", test_episodes)

env.close()







#Slippery_False:


import numpy as np
import gymnasium as gym
import time

env = gym.make("FrozenLake-v1", is_slippery=False)

Q = np.zeros((16, 4))

alpha = 0.1
gamma = 0.95
epsilon = 1.0

for episode in range(1000):
    state, _ = env.reset()

    for step in range(100):

        if np.random.random() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state])

        next_state, reward, terminated, truncated, _ = env.step(action)

        if terminated or truncated:
            target = reward
        else:
            target = reward + gamma * np.max(Q[next_state])

        Q[state, action] += alpha * (
            target - Q[state, action]
        )

        state = next_state

        if terminated or truncated:
            break

    epsilon = max(0.01, epsilon * 0.995)

env.close()

print("Training Completed")
print("Q-Table:")
print(np.round(Q, 2))

env = gym.make(
    "FrozenLake-v1",
    is_slippery=False,
    render_mode="human"
)

for episode in range(5):
    state, _ = env.reset()
    reward = 0

    for step in range(100):
        action = np.argmax(Q[state])

        state, reward, terminated, truncated, _ = env.step(action)

        time.sleep(0.1)

        if terminated or truncated:
            break

    print("Episode:", episode + 1)

    if reward == 1:
        print("Reached the Goal!")
    else:
        print("Failed to reach the Goal.")

env.close()

