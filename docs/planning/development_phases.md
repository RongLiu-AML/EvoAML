# EvoAML Phased Development Plan

This document outlines the detailed 6-phase strategic roadmap for developing the EvoAML RegTech Framework. Each phase is designed to incrementally bridge the gap between advanced AML typologies (graph & temporal modeling) and FinCEN (BSA/AMLA 2020) compliance standards.

## Phase 1: Foundation & Compliance Architecture (Completed)
**Objective:** Establish the repository structure, define the regulatory mapping, and scaffold the core modules.
*   **Tasks:**
    *   Initialize Git repository with branch protection and CI/CD stubs.
    *   Draft the `AMLA 2020 Compliance Mapping` document (`bsa_amla_2020_mapping.md`).
    *   Design the high-level system architecture (`evo_architecture.md`).
    *   Implement empty class interfaces for `GraphTracker`, `TemporalAnalyzer`, and `BSASARGenerator`.
*   **Deliverable:** A fully structured, RegTech-oriented repository skeleton ready for algorithm integration.

## Phase 2: Heterogeneous Data Ingestion & Preprocessing
**Objective:** Build the data pipelines capable of handling cross-industry transaction logs (e.g., supply chain, energy mobility).
*   **Tasks:**
    *   Develop `src/data_pipeline/ingestor.py` to parse multi-source financial CSV/JSON logs.
    *   Create `src/data_pipeline/graph_builder.py` to convert flat transactions into heterogeneous graph structures (Nodes: Entities, Accounts; Edges: Transactions, Supply-Chain Links).
    *   Implement data anonymization to align with data privacy regulations.
*   **Deliverable:** A robust data ingestion module that outputs standardized graph tensors.

## Phase 3: Graph-Driven Tracking Integration (GNN Module)
**Objective:** Implement the core algorithm from the author's primary research paper on cross-industry monitoring.
*   **Tasks:**
    *   Integrate Graph Neural Network (GNN) embeddings within `src/core_engine/graph_tracker.py`.
    *   Implement subgraph anomaly detection algorithms to identify obfuscated money laundering rings (layering and integration).
    *   Write unit tests simulating complex supply-chain money laundering typologies.
*   **Deliverable:** A functional GNN detection engine capable of scoring risk based on graph topology.

## Phase 4: Temporal Behavior Evolution Analysis
**Objective:** Implement the core algorithm from the author's primary research paper on temporal dynamics.
*   **Tasks:**
    *   Integrate Dynamic Self-Attention mechanisms in `src/core_engine/temporal_pattern.py`.
    *   Develop logic to track how a flagged entity's transaction velocity and volume mutate over time.
    *   Fuse the temporal scores with the graph risk scores to reduce false positives.
*   **Deliverable:** A temporal analysis module that detects evolving AML typologies.

## Phase 5: BSA/AMLA 2020 Compliance Engine & SAR Generation
**Objective:** Translate the complex AI metrics into actionable, FinCEN-compliant regulatory reports.
*   **Tasks:**
    *   Flesh out `src/compliance_adapter/bsa_sar_generator.py` to map GNN and Temporal outputs to specific BSA reporting fields.
    *   Implement natural language generation (NLG) templates for the SAR Narrative section.
    *   Ensure outputs are structured in an auditable JSON/XML format compatible with government e-filing systems.
*   **Deliverable:** An automated reporting engine that makes AI outputs understandable for compliance officers and regulators.

## Phase 6: System Simulation, UI, and Deployment Readiness
**Objective:** Create end-to-end demonstrations proving the real-world viability of EvoAML for financial institutions.
*   **Tasks:**
    *   Develop interactive Jupyter Notebooks in `examples/` demonstrating the full lifecycle from data ingestion to SAR generation.
    *   Create a lightweight Streamlit dashboard (`app.py`) for compliance officers to visualize anomalous subgraphs and temporal trends.
    *   Finalize API documentation, write deployment guides (Docker setup), and release version 1.0.
*   **Deliverable:** A production-ready demonstration suite with a visualization dashboard.
