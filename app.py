import streamlit as st
from src.core_engine.graph_tracker import GraphTracker
from src.core_engine.temporal_pattern import TemporalAnalyzer
from src.compliance_adapter.bsa_sar_generator import BSASARGenerator
import pandas as pd

st.title("EvoAML Dashboard")
st.markdown("### Regulatory-Grade AML Detection System")

# 1. Data Input
st.sidebar.header("Configuration")
model_mode = st.sidebar.selectbox("Detection Mode", ["Standard", "Enhanced"])

if st.button("Run Full Analysis"):
    tracker = GraphTracker()
    analyzer = TemporalAnalyzer()
    generator = BSASARGenerator()
    
    st.info("Running Graph & Temporal Analysis...")
    
    # Simulate detection
    anomalies = tracker.detect_anomalous_subgraphs()
    shifts = analyzer.analyze_behavior_evolution("Entity_001", [], graph_risk_score=0.85)
    report = generator.generate_sar_narrative(anomalies, shifts, shifts.get("combined_fused_risk", 0.0))
    
    st.success("Analysis Complete")
    st.text_area("Generated SAR Report", report, height=300)
