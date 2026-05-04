from src.core_engine.graph_tracker import GraphTracker
from src.core_engine.temporal_pattern import TemporalAnalyzer
from src.compliance_adapter.bsa_sar_generator import BSASARGenerator

print("--- EvoAML System Initialized ---")
tracker = GraphTracker()
analyzer = TemporalAnalyzer()
generator = BSASARGenerator()

print("1. Scanning cross-industry transaction graphs...")
anomalies = tracker.detect_anomalous_subgraphs()

print("2. Analyzing temporal evolution of flagged entities...")
shifts = analyzer.analyze_behavior_evolution(anomalies[0]['entity_id'], [])

print("3. Generating FinCEN compliant SAR...")
sar_report = generator.generate_sar_narrative(anomalies, shifts)

print("\n--- FINAL REPORT ---")
print(sar_report)
