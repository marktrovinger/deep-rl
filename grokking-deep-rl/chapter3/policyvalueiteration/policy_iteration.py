import gym
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def policy_iteration(P, gamma=0.99):
    pass

def value_iteration(P, gamma=0.99, theta=1e10):
    pass

def main():
    env = gym.make('FrozenLake-v0')
    P = env.unwrapped.P

if __name__=='__main__':
    main()
