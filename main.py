from data_collector import ProcessDataCollector
from data_preprocessor import ProcessDataPreprocessor
from anomaly_detector import ProcessAnomalyDetector
from performance_analyzer import PerformanceAnalyzer
from visualizer import ProcessVisualizer
from recommender import ProcessRecommender

class PerformanceMonitor:
    def __init__(self):
        self.collector = ProcessDataCollector()
        self.preprocessor = ProcessDataPreprocessor()
        self.detector = ProcessAnomalyDetector()
        self.analyzer = PerformanceAnalyzer()
        self.visualizer = ProcessVisualizer()
        self.recommender = ProcessRecommender()
    
    def run(self, duration=10):
        """Run the performance monitoring pipeline"""
        print(f"Monitoring system for {duration} seconds...")
        
        # Data collection
        df = self.collector.collect(duration)
        
        # Data processing
        df = self.preprocessor.preprocess(df)
        
        # Anomaly detection
        df = self.detector.detect(df)
        
        # Performance analysis
        results = self.analyzer.analyze(df)
        
        # Visualization
        self.visualizer.plot_usage(df)
        
        # Recommendations
        for _, process in results['top_cpu'].iterrows():
            print(f"\nRecommendations for {process['name']}:")
            for rec in self.recommender.recommend(process['name']):
                print(f"- {rec}")

if __name__ == "__main__":
    monitor = PerformanceMonitor()
    monitor.run(duration=15)