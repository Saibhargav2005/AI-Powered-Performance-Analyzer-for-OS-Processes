import psutil
import pandas as pd
from datetime import datetime
import time

class ProcessDataCollector:
    def __init__(self):
        self.columns = ['timestamp', 'pid', 'name', 'cpu_percent', 'memory_percent', 'status']
    
    def collect(self, duration=5):
        """Collect process data for specified duration (seconds)"""
        data = []
        for _ in range(duration):
            timestamp = datetime.now()
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'status']):
                try:
                    data.append([timestamp] + list(proc.info.values()))
                except psutil.NoSuchProcess:
                    continue
            time.sleep(1)
        return pd.DataFrame(data, columns=self.columns)