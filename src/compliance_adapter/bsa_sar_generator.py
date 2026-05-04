import json

class BSASARGenerator:
    def __init__(self):
        self.template_version = "FinCEN_SAR_v1.2"

    def generate_sar_narrative(self, graph_anomalies, temporal_shifts):
        """Translates AI detection metrics into BSA-compliant narratives."""
        narrative = f"SUSPICIOUS ACTIVITY REPORT\n"
        narrative += f"The EvoAML system detected anomalous activity regarding {graph_anomalies[0]['entity_id']}.\n"
        narrative += f"Typology identified: {graph_anomalies[0]['typology']} with risk score {graph_anomalies[0]['risk_score']}.\n"
        narrative += f"Temporal analysis indicates {temporal_shifts['mutation_type']} (Confidence: {temporal_shifts['confidence']}).\n"
        return narrative
