class PerformanceAnalyzer:
    def analyze(self, df):
        """Analyze system performance"""
        analysis = {}
        
        # Resource intensive processes
        analysis['top_cpu'] = df.nlargest(5, 'cpu_percent')[['pid', 'name', 'cpu_percent']]
        analysis['top_memory'] = df.nlargest(5, 'memory_percent')[['pid', 'name', 'memory_percent']]
        
        # System health
        analysis['cpu_usage'] = df['cpu_percent'].mean()
        analysis['memory_usage'] = df['memory_percent'].mean()
        
        return analysis