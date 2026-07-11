import streamlit as st
import sys
import os
import random
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.core_engine.graph_tracker import GraphTracker
from src.core_engine.temporal_pattern import TemporalAnalyzer
from src.compliance_adapter.bsa_sar_generator import BSASARGenerator
from src.data_pipeline.graph_builder import HeterogeneousGraphBuilder

st.set_page_config(page_title="EvoAML Dashboard", layout="wide")

st.title("EvoAML Dashboard")
st.markdown("### Regulatory-Grade Anti-Money Laundering Detection System")

# Sidebar
st.sidebar.header("Configuration")
detection_mode = st.sidebar.selectbox("Detection Mode", ["Standard", "Enhanced"])
min_amount = st.sidebar.slider("Minimum Transaction Amount ($)", 1000, 50000, 10000)

def generate_demo_data(n=50):
    """Generate synthetic transaction data for demo."""
    sectors = ['Energy', 'Logistics', 'Manufacturing', 'Finance', 'Retail']
    entities = [f"Entity_{i:03d}" for i in range(1, 21)]
    
    transactions = []
    for i in range(n):
        sender = random.choice(entities)
        receiver = random.choice([e for e in entities if e != sender])
        transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': random.randint(1000, 100000),
            'sector': random.choice(sectors),
            'timestamp': f"2024-01-{random.randint(1, 28):02d}"
        })
    return transactions

if st.button("Run Full Analysis", type="primary"):
    with st.spinner("Generating transaction data..."):
        # Step 1: Generate data
        transactions = generate_demo_data(50)
        
        # Step 2: Build graph
        builder = HeterogeneousGraphBuilder()
        graph = builder.build_from_transactions(transactions)
        stats = builder.get_statistics()
        
        # Step 3: Graph analysis
        tracker = GraphTracker()
        tracker.ingest_transaction_graph(transactions)
        anomalies = tracker.detect_anomalous_subgraphs(min_amount=min_amount)
        
        # Step 4: Temporal analysis
        analyzer = TemporalAnalyzer(window_size=10)
        temporal_results = []
        for anomaly in anomalies[:3]:
            history = np.random.lognormal(10, 1, 30).tolist()
            history[-5:] = [h * 2.0 for h in history[-5:]]
            result = analyzer.analyze_behavior_evolution(anomaly['entity_id'], history)
            temporal_results.append(result)
        
        # Step 5: Generate SAR
        generator = BSASARGenerator()
        risk_score = temporal_results[0]['temporal_confidence'] if temporal_results else 0.5
        report = generator.generate_sar_narrative(anomalies[:3], temporal_results[0] if temporal_results else {}, risk_score)
    
    # Display results
    st.success("Analysis Complete!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Nodes", stats['nodes'])
        st.metric("Total Edges", stats['edges'])
    with col2:
        st.metric("High Risk Entities", len(anomalies))
        st.metric("Detection Mode", detection_mode)
    
    st.subheader("Top Suspicious Entities")
    st.dataframe(anomalies[:5] if anomalies else [], use_container_width=True)
    
    st.subheader("Generated SAR Report")
    st.text_area("SAR Narrative", report, height=300)
    
    st.caption("EvoAML v1.0 | BSA/AMLA 2020 Compliant")

else:
    st.info("Click 'Run Full Analysis' to start the detection pipeline.")
