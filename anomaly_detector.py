from sklearn.ensemble import IsolationForest
import numpy as np

class ProcessAnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05, random_state=42)
    
    def detect(self, df):
        """Detect anomalous processes"""
        features = df[['cpu_percent', 'memory_percent']].values
        self.model.fit(features)
        anomalies = self.model.predict(features)
        df['anomaly'] = np.where(anomalies == -1, True, False)
        return df