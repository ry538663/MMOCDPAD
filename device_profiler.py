import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

class DeviceProfiler:
    def __init__(self, model_path='models/device_profiler.pkl'):
        self.model_path = model_path
        self.model = None
        
        if not os.path.exists('models'):
            os.makedirs('models')

    def train(self, csv_path='features.csv'):
        df = pd.read_csv(csv_path)
        # Features mentioned in paper
        features = ['tcp_flag', 'udp_flag', 'packet_size', 'ttl', 'inter_arrival_time', 'protocol', 'avg_et', 'max_et', 'min_et']
        X = df[features]
        y = df['label']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        
        accuracy = self.model.score(X_test, y_test)
        print(f"Profiler Training Accuracy: {accuracy:.4f}")
        
        joblib.dump(self.model, self.model_path)
        print(f"Model saved to {self.model_path}")

    def get_trust_score(self, feature_vector):
        """
        Returns a trust score between 0 and 1.
        Higher score means higher trust (more likely to be normal).
        """
        if self.model is None:
            if os.path.exists(self.model_path):
                self.model = joblib.load(self.model_path)
            else:
                raise Exception("Model not trained yet.")
        
        # Predict probability for class 0 (Normal)
        probs = self.model.predict_proba([feature_vector])[0]
        # Assuming label 0 is normal and 1 is anomaly
        # Trust score = Probability of class 0
        return probs[0]

if __name__ == "__main__":
    profiler = DeviceProfiler()
    profiler.train()
    # Test
    test_feat = [0, 1, 1200, 64, 0.05, 17, 1620000500, 1620000550, 1620000450]
    score = profiler.get_trust_score(test_feat)
    print(f"Test Trust Score: {score}")
