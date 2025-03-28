from sklearn.preprocessing import StandardScaler
import numpy as np

class ProcessDataPreprocessor:
    def preprocess(self, df):
        """Clean and normalize process data"""
        # Handle missing values
        df = df.dropna(subset=['cpu_percent', 'memory_percent'])
        
        # Feature engineering
        df['cpu_memory_ratio'] = np.where(
            df['memory_percent'] > 0,
            df['cpu_percent'] / df['memory_percent'],
            0
        )
        
        # Normalization
        scaler = StandardScaler()
        df[['cpu_percent', 'memory_percent']] = scaler.fit_transform(df[['cpu_percent', 'memory_percent']])
        return df