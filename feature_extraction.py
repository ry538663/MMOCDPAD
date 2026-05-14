import pandas as pd
import numpy as np
import os

def simulate_dataset(n_samples=2000):
    """
    Simulates a dataset similar to X-IIoTID and CIC IoT 2022
    based on the features specified in the research paper.
    """
    np.random.seed(42)
    
    data = {
        'device_id': np.random.randint(1000, 1010, n_samples),
        'tcp_flag': np.random.randint(0, 2, n_samples),
        'udp_flag': np.random.randint(0, 2, n_samples),
        'http_flag': np.random.randint(0, 2, n_samples),
        'https_flag': np.random.randint(0, 2, n_samples),
        'packet_size': np.random.normal(500, 200, n_samples).clip(40, 1500),
        'ttl': np.random.choice([64, 128, 255], n_samples),
        'inter_arrival_time': np.random.exponential(0.1, n_samples),
        'protocol': np.random.choice([6, 17, 1], n_samples), # TCP, UDP, ICMP
        'src_port': np.random.randint(1024, 65535, n_samples),
        'dst_port': np.random.choice([80, 443, 22, 1883, 502], n_samples),
        'epoch_timestamp': np.linspace(1620000000, 1620000000 + 3600, n_samples),
    }
    
    df = pd.DataFrame(data)
    
    # Derived Features
    df['avg_et'] = df['epoch_timestamp'].rolling(window=10).mean().fillna(df['epoch_timestamp'])
    df['max_et'] = df['epoch_timestamp'].rolling(window=10).max().fillna(df['epoch_timestamp'])
    df['min_et'] = df['epoch_timestamp'].rolling(window=10).min().fillna(df['epoch_timestamp'])
    
    # Add Anomaly Label (for training initial profiler)
    # Anomaly conditions: unusual port, high packet size, or specific protocols
    df['label'] = 0
    df.loc[(df['dst_port'] == 502) & (df['packet_size'] > 1000), 'label'] = 1 # Modbus anomaly
    df.loc[(df['packet_size'] > 1400) & (df['protocol'] == 17), 'label'] = 1 # UDP Flood
    df.loc[np.random.choice(df.index, size=int(n_samples*0.05)), 'label'] = 1 # Random anomalies
    
    output_path = 'features.csv'
    df.to_csv(output_path, index=False)
    print(f"Dataset simulated and saved to {output_path}")
    return df

if __name__ == "__main__":
    simulate_dataset()
