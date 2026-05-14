import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pandas as pd
from stable_baselines3 import DQN
import os

class ZTSNetworkEnv(gym.Env):
    """
    Custom Environment for Zero Trust Security Network Anomaly Detection.
    States: [Trust Score, Packet Size, Protocol, Frequency]
    Actions: 0 = Normal (Allow), 1 = Anomaly (Deny)
    """
    def __init__(self, data_path='features.csv'):
        super(ZTSNetworkEnv, self).__init__()
        self.df = pd.read_csv(data_path)
        self.current_step = 0
        
        # State: Trust Score (0-1), Normalized Packet Size (0-1), Protocol (scaled), Inter-arrival (scaled)
        self.observation_space = spaces.Box(low=0, high=1, shape=(4,), dtype=np.float32)
        self.action_space = spaces.Discrete(2)

    def _get_obs(self):
        row = self.df.iloc[self.current_step]
        # Simplified trust score for training simulation (ideally from profiler)
        # Here we use the actual label but add some noise to simulate "state"
        base_trust = 1.0 - row['label'] 
        trust_score = np.clip(base_trust + np.random.normal(0, 0.1), 0, 1)
        
        norm_packet_size = np.clip(row['packet_size'] / 1500, 0, 1)
        norm_proto = np.clip(row['protocol'] / 17, 0, 1)
        norm_iat = np.clip(row['inter_arrival_time'] * 10, 0, 1)
        
        return np.array([trust_score, norm_packet_size, norm_proto, norm_iat], dtype=np.float32)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.current_step = np.random.randint(0, len(self.df) - 1)
        return self._get_obs(), {}

    def step(self, action):
        target = self.df.iloc[self.current_step]['label']
        
        # Reward function
        if action == target:
            reward = 1.0 # Correct classification
        else:
            reward = -1.0 # Misclassification
            
        self.current_step = (self.current_step + 1) % len(self.df)
        terminated = False
        truncated = False
        
        # End after 100 steps to keep episodes manageable
        if self.current_step % 100 == 0:
            terminated = True
            
        return self._get_obs(), reward, terminated, truncated, {}

def train_drl_agent(model_path='models/drl_anomaly_agent'):
    env = ZTSNetworkEnv()
    model = DQN("MlpPolicy", env, verbose=1, learning_rate=1e-3, buffer_size=10000)
    model.learn(total_timesteps=10000)
    model.save(model_path)
    print(f"DRL Agent saved to {model_path}")

if __name__ == "__main__":
    if not os.path.exists('models'):
        os.makedirs('models')
    train_drl_agent()
