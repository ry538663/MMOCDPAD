from feature_extraction import simulate_dataset
from device_profiler import DeviceProfiler
from drl_anomaly_detector import train_drl_agent
import os

def main():
    print("=== Starting MMOCDPAD-DRL Training Pipeline ===")
    
    # 1. Data Simulation
    if not os.path.exists('features.csv'):
        print("Step 1: Generating features.csv...")
        simulate_dataset()
    else:
        print("Step 1: features.csv already exists.")
        
    # 2. Device Profiling (Random Forest)
    print("\nStep 2: Training Device Profiler (Random Forest)...")
    profiler = DeviceProfiler()
    profiler.train()
    
    # 3. DRL Agent Training (DQN)
    print("\nStep 3: Training DRL Anomaly Detector (DQN)...")
    train_drl_agent()
    
    print("\n=== Training Pipeline Completed Successfully ===")

if __name__ == "__main__":
    main()
