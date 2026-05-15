import random

class TemporalAnalyzer:
    def __init__(self, sequence_length=30):
        self.attention_weights = None
        self.sequence_length = sequence_length

    def _compute_dynamic_attention(self, transaction_sequence):
        """Simulates Dynamic Self-Attention over a sequence of financial behaviors."""
        # Mocking attention scores where a sudden spike indicates anomaly
        scores = [random.uniform(0.01, 0.05) for _ in range(len(transaction_sequence))]
        spike_index = random.randint(0, len(scores)-1)
        scores[spike_index] = random.uniform(0.15, 0.40) # Attention peak
        self.attention_weights = scores
        return max(scores)

    def analyze_behavior_evolution(self, entity_id, historical_data=None, graph_risk_score=0.0):
        """
        Evaluates pattern shifts over time and fuses with graph-based risk.
        historical_data: List of daily transaction volumes/velocities.
        """
        if not historical_data:
            # Fallback mock data if history is missing
            historical_data = [random.uniform(100, 10000) for _ in range(self.sequence_length)]
        
        attention_peak = self._compute_dynamic_attention(historical_data)
        
        # Evolution mutation detection logic
        mutation_type = "Stable"
        confidence = 0.5
        evolution_detected = False
        
        if attention_peak > 0.15:
            evolution_detected = True
            mutation_type = "Velocity Acceleration & Temporal Structuring"
            confidence = min(0.60 + attention_peak, 0.98)
        
        # Cross-validation: Fuse temporal sequence risk with GNN topological risk
        combined_risk = (graph_risk_score * 0.6) + (confidence * 0.4)

        return {
            "entity_id": entity_id,
            "evolution_detected": evolution_detected,
            "mutation_type": mutation_type,
            "temporal_confidence": round(confidence, 3),
            "combined_fused_risk": round(combined_risk, 3),
            "actionable": combined_risk > 0.8
        }
