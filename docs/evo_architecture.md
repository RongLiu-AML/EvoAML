# EvoAML Technical Architecture

## System Data Flow
1. **Data Ingestion:** Transaction logs, KYC data, and cross-sector supply chain records are ingested into a heterogeneous graph structure.
2. **Graph-Driven Monitor:** `graph_tracker.py` executes sub-graph isomorphism and anomaly detection to flag suspicious structural clusters.
3. **Temporal Analyzer:** `temporal_pattern.py` evaluates the flagged entities over time to assess if their behavior matches known evolutionary paths of money laundering.
4. **Compliance Adapter:** `bsa_sar_generator.py` extracts the critical nodes and temporal anomalies, formatting them into a standard FinCEN SAR template.
