import numpy as np
import pandas as pd
from collections import deque

class TemporalAnalyzer:
    """
    Analyzes temporal patterns in transaction sequences.
    Uses sliding window statistical anomaly detection.
    """
    def __init__(self, window_size=20, zscore_threshold=2.5):
        self.window_size = window_size
        self.zscore_threshold = zscore_threshold
        self.history = {}
        
    def analyze_behavior_evolution(self, entity_id, historical_data):
        """
        Analyze temporal behavior for an entity.
        
        Args:
            entity_id: Unique identifier for the entity
            historical_data: List of transaction volumes or velocities over time
            
        Returns:
            dict with evolution analysis results
        """
        if not historical_data:
            return {"error": "No historical data provided"}
            
        # Convert to numpy array
        if isinstance(historical_data, list):
            data = np.array(historical_data, dtype=float)
        else:
            data = historical_data
            
        # Calculate rolling statistics
        results = self._sliding_window_analysis(data)
        
        return {
            "entity_id": entity_id,
            "evolution_detected": results['anomaly_detected'],
            "mutation_type": results['mutation_type'],
            "temporal_confidence": round(results['confidence'], 3),
            "mean": round(results['mean'], 2),
            "std": round(results['std'], 2),
            "recent_anomaly_count": results['anomaly_count'],
            "actionable": results['anomaly_detected']
        }
    
    def _sliding_window_analysis(self, data):
        """Real sliding window statistical analysis."""
        n = len(data)
        if n < self.window_size:
            return {
                "anomaly_detected": False,
                "mutation_type": "Insufficient Data",
                "confidence": 0.0,
                "mean": np.mean(data) if n > 0 else 0,
                "std": np.std(data) if n > 0 else 0,
                "anomaly_count": 0
            }
        
        # Calculate rolling mean and std
        rolling_mean = []
        rolling_std = []
        anomalies = []
        
        for i in range(n - self.window_size + 1):
            window = data[i:i+self.window_size]
            rolling_mean.append(np.mean(window))
            rolling_std.append(np.std(window))
            
            # Detect anomaly: current point deviates from rolling mean
            current = data[i + self.window_size - 1]
            if rolling_std[-1] > 0:
                zscore = abs(current - rolling_mean[-1]) / rolling_std[-1]
                if zscore > self.zscore_threshold:
                    anomalies.append(zscore)
        
        # Determine mutation type based on pattern
        mean_val = np.mean(data)
        recent_mean = np.mean(data[-10:]) if len(data) >= 10 else mean_val
        
        if recent_mean > mean_val * 1.5:
            mutation_type = "Velocity Acceleration"
            confidence = min(0.7 + (recent_mean / mean_val - 1), 0.95)
        elif recent_mean < mean_val * 0.5:
            mutation_type = "Volume Reduction (Potential Integration)"
            confidence = 0.75
        elif len(anomalies) > 3:
            mutation_type = "High Frequency Structuring"
            confidence = min(0.6 + len(anomalies) * 0.1, 0.9)
        else:
            mutation_type = "Stable"
            confidence = 0.4
            
        return {
            "anomaly_detected": len(anomalies) > 0,
            "mutation_type": mutation_type,
            "confidence": confidence,
            "mean": mean_val,
            "std": np.std(data),
            "anomaly_count": len(anomalies)
        }
    
    def detect_sequence_anomalies(self, sequence):
        """Detect anomalies in a sequence of events."""
        if len(sequence) < 5:
            return []
            
        data = np.array(sequence)
        results = self._sliding_window_analysis(data)
        return results
