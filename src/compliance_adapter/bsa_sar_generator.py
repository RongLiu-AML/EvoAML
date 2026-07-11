import json
from datetime import datetime

class BSASARGenerator:
    def __init__(self):
        self.template_version = "FinCEN_SAR_v1.2"

    def generate_sar_narrative(self, graph_anomalies, temporal_shifts, fused_risk_score):
        """
        Translates AI detection metrics into a human-readable SAR narrative 
        compliant with Bank Secrecy Act standards.
        """
        if not graph_anomalies:
            return "No anomalies detected."

        primary_anomaly = graph_anomalies[0]
        mutation = temporal_shifts.get("mutation_type", "Unknown")
        risk = fused_risk_score

        narrative = f"SUSPICIOUS ACTIVITY REPORT\n"
        narrative += f"Date: {datetime.now().strftime('%Y-%m-%d')}\n"
        narrative += f"Subject: {primary_anomaly.get('entity_id', 'N/A')}\n"
        narrative += f"Sector: {primary_anomaly.get('sector', 'Financial Services')}\n\n"
        
        narrative += f"DETECTION SUMMARY:\n"
        narrative += f"The EvoAML system detected anomalous activity with a risk score of {risk}.\n"
        
        narrative += f"GRAPH ANALYSIS (Phase 3):\n"
        narrative += f"Typology: {primary_anomaly.get('typology', 'Complex Structuring')}\n"
        narrative += f"Risk Score: {primary_anomaly.get('risk_score', 0.0)}\n\n"
        
        narrative += f"TEMPORAL ANALYSIS (Phase 4):\n"
        narrative += f"Behavioral Evolution: {mutation}\n"
        narrative += f"Confidence: {temporal_shifts.get('temporal_confidence', 0.0)}\n\n"
        
        narrative += f"CONCLUSION:\nBased on the cross-validation of spatial topology and temporal evolution, "
        narrative += f"this entity exhibits high-risk characteristics consistent with money laundering typologies. "
        narrative += f"Recommended for filing Suspicious Activity Report."
        
        return narrative

    def export_json_report(self, graph_anomalies, temporal_shifts, fused_risk_score):
        """Exports structured JSON for e-filing."""
        return {
            "report_type": "SAR",
            "generator": "EvoAML",
            "risk_score": fused_risk_score,
            "anomalies": graph_anomalies,
            "temporal_analysis": temporal_shifts
        }
