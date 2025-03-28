import matplotlib.pyplot as plt
import seaborn as sns

class ProcessVisualizer:
    def plot_usage(self, df):
        """Plot CPU and memory usage"""
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=df, x='timestamp', y='cpu_percent', label='CPU')
        sns.lineplot(data=df, x='timestamp', y='memory_percent', label='Memory')
        plt.title('System Resource Usage')
        plt.ylabel('Usage (%)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()