class ProcessRecommender:
    def __init__(self):
        self.knowledge_base = {
            'chrome': ['Reduce number of open tabs', 'Disable unused extensions'],
            'python': ['Optimize loops', 'Use efficient data structures'],
            'default': ['Check for updates', 'Monitor resource usage']
        }
    
    def recommend(self, process_name):
        """Generate optimization recommendations"""
        return self.knowledge_base.get(
            process_name.lower(), 
            self.knowledge_base['default']
        )