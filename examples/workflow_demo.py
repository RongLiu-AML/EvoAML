#!/usr/bin/env python3
"""
EvoAML End-to-End Workflow Demo

This script demonstrates the complete EvoAML pipeline:
1. Ingest transaction data
2. Build transaction graph
3. Run graph-based anomaly detection
4. Run temporal behavior analysis
5. Generate SAR report
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_pipeline.graph_builder import HeterogeneousGraphBuilder
from src.data_pipeline.anonymizer import DataAnonymizer
from src.core_engine.graph_tracker import GraphTracker
from src.core_engine.temporal_pattern import TemporalAnalyzer
from src.compliance_adapter.bsa_sar_generator import BSASARGenerator

def generate_synthetic_data(n_transactions=100):
    """Generate synthetic transaction data for demo."""
    import random
    import datetime
    
    sectors = ['Energy', 'Logistics', 'Manufacturing', 'Finance', 'Retail']
    entities = [f"Entity_{i:03d}" for i in range(1, 21)]
    
    transactions = []
    base_date = datetime.datetime(2024, 1, 1)
    
    for i in range(n_transactions):
        sender = random.choice(entities)
        receiver = random.choice([e for e in entities if e != sender])
        
        transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': random.randint(1000, 100000),
            'sector': random.choice(sectors),
            'timestamp': (base_date + datetime.timedelta(days=random.randint(0, 180))).isoformat()
        })
    
    return transactions

def main():
    print("=" * 60)
    print("EvoAML Workflow Demo")
    print("=" * 60)
    
    # Step 1: Generate synthetic data
    print("\n[1/5] Generating synthetic transaction data...")
    transactions = generate_synthetic_data(100)
    print(f"      Generated {len(transactions)} transactions")
    
    # Step 2: Build Graph
    print("\n[2/5] Building transaction graph...")
    builder = HeterogeneousGraphBuilder()
    graph = builder.build_from_transactions(transactions)
    stats = builder.get_statistics()
    print(f"      Graph built: {stats['nodes']} nodes, {stats['edges']} edges")
    
    # Step 3: Graph-based Anomaly Detection
    print("\n[3/5] Running graph-based anomaly detection...")
    tracker = GraphTracker()
    tracker.ingest_transaction_graph(transactions)
    anomalies = tracker.detect_anomalous_subgraphs(min_amount=20000)
    print(f"      Detected {len(anomalies)} high-risk entities")
    
    # Step 4: Temporal Analysis
    print("\n[4/5] Running temporal behavior analysis...")
    analyzer = TemporalAnalyzer(window_size=10, zscore_threshold=2.0)
    
    # Simulate historical data for each anomaly
    temporal_results = []
    for anomaly in anomalies[:3]:  # Analyze top 3
        import numpy as np
        # Generate realistic historical pattern with occasional spikes
        history = np.random.lognormal(10, 1, 50).tolist()
        history[-5:] = [h * 2.5 for h in history[-5:]]  # Add spike
        
        result = analyzer.analyze_behavior_evolution(anomaly['entity_id'], history)
        temporal_results.append(result)
        print(f"      - {result['entity_id']}: {result['mutation_type']} (confidence: {result['temporal_confidence']})")
    
    # Step 5: Generate SAR Report
    print("\n[5/5] Generating SAR report...")
    generator = BSASARGenerator()
    report = generator.generate_sar_narrative(
        anomalies[:3], 
        temporal_results[0] if temporal_results else {},
        0.85
    )
    
    print("\n" + "=" * 60)
    print("GENERATED SAR REPORT")
    print("=" * 60)
    print(report)
    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    
    return report

if __name__ == "__main__":
    main()
