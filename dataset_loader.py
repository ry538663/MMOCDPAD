import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

class DatasetLoader:
    """
    Handles ingestion and preprocessing of real IoT datasets
    like X-IIoTID and CIC IoT 2022.
    """
    def __init__(self):
        self.scaler = StandardScaler()
        self.encoder = LabelEncoder()

    def process_csv(self, file_path):
        df = pd.read_csv(file_path)
        
        # 1. Handle Missing Values
        df = df.fillna(method='ffill').fillna(0)
        
        # 2. Dynamic Feature Selection (common IoT features)
        # In a real scenario, we'd map column names for specific datasets
        iot_features = [
            'Packet Length', 'Protocol', 'Source Port', 'Destination Port',
            'IAT', 'TTL', 'Flags', 'Flow Duration'
        ]
        
        # Mapping for simulation if columns don't match exactly
        available_features = [col for col in df.columns if col in iot_features]
        if not available_features:
            # Fallback to numeric columns
            available_features = df.select_dtypes(include=[np.number]).columns.tolist()
            
        X = df[available_features]
        
        # 3. Normalization
        X_scaled = self.scaler.fit_transform(X)
        
        # 4. Label Encoding (assuming 'class' or 'label' column exists)
        y = None
        if 'label' in df.columns:
            y = self.encoder.fit_transform(df['label'])
        elif 'class' in df.columns:
            y = self.encoder.fit_transform(df['class'])
        else:
            # Unsupervised/No label found
            y = np.zeros(len(df))
            
        return X_scaled, y, available_features

    def get_stats(self, df):
        return {
            'records': len(df),
            'anomalies': int(df['label'].sum()) if 'label' in df.columns else 'N/A',
            'features': len(df.columns)
        }

if __name__ == "__main__":
    # Test with generated features.csv
    loader = DatasetLoader()
    try:
        X, y, feats = loader.process_csv('features.csv')
        print(f"Processed {len(X)} records with features: {feats}")
    except Exception as e:
        print(f"Error: {e}")
