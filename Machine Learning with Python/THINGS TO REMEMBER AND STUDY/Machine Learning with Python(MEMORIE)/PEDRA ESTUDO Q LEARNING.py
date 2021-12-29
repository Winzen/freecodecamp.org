import gym
import numpy as np
#import time

"""
ESTUDO DE COMO POSSO ENCAIXAR Q LEARNING NO PROBLEMA
"""
"""
[[0.17872579 0.13937885 0.1389728  0.1387616 ]
 [0.10466532 0.12437199 0.1027685  0.15702541]
 [0.15299244 0.12187305 0.12238193 0.12224583]
 [0.09255613 0.06697467 0.05841905 0.11186339]
 [0.20260086 0.15621415 0.14396867 0.13655239]
 [0.         0.         0.         0.        ]
 [0.04879585 0.05040327 0.14657333 0.02418918]
 [0.         0.         0.         0.        ]
 [0.14722061 0.19652307 0.19621939 0.26091348]
 [0.18480374 0.4008428  0.28347166 0.1764042 ]
 [0.42982534 0.15825489 0.13072048 0.09239276]
 [0.         0.         0.         0.        ]
 [0.         0.         0.         0.        ]
 [0.12566141 0.24381753 0.59626888 0.37940819]
 [0.34439117 0.7568718  0.38502158 0.33715503]
 [0.         0.         0.         0.        ]]
"""

env = gym.make('FrozenLake-v0')
STATES = env.observation_space.n
ACTIONS = env.action_space.n

Q = np.zeros((STATES, ACTIONS))

EPISODES = 100 # how many times to run the enviornment from the beginning
MAX_STEPS = 100  # max number of steps allowed for each run of enviornment

LEARNING_RATE = 1.0  # learning rate
GAMMA = 0.96

RENDER = True # if you want to see training set to true

epsilon = 0.9

rewards = []
for episode in range(EPISODES):

  state = env.reset()
  for _ in range(MAX_STEPS):
    
    if RENDER:
      env.render()

    if np.random.uniform(0, 1) < epsilon:
      action = env.action_space.sample()  
    else:
      action = np.argmax(Q[state, :])
      print(action)

    next_state, reward, done, _ = env.step(action)
    print(next_state, reward, done)

    Q[state, action] = Q[state, action] + LEARNING_RATE * (reward + GAMMA * np.max(Q[next_state, :]) - Q[state, action])
    print(state, action)
    #print(Q)

    state = next_state

    if done: 
      rewards.append(reward)
      epsilon -= 0.001
      break  # reached goal
#print(rewards)
print(Q)
print(f"Average reward: {sum(rewards)/len(rewards)}:")
# and now we can see our Q values!
