import networkx as nx
from src.data_pipeline.graph_builder import HeterogeneousGraphBuilder

class GraphTracker:
    """
    Tracks money flows using graph analysis algorithms.
    Identifies suspicious patterns in transaction networks.
    """
    def __init__(self, model_path=None):
        self.model_path = model_path
        self.graph_builder = HeterogeneousGraphBuilder()
        self.graph = None
        
    def ingest_transaction_graph(self, transactions):
        """Load and process transaction graph."""
        self.graph = self.graph_builder.build_from_transactions(transactions)
        print(f"Loaded graph with {self.graph.number_of_nodes()} nodes and {self.graph.number_of_edges()} edges.")
        return self.graph
    
    def detect_anomalous_subgraphs(self, min_amount=5000):
        """
        Detect anomalous subgraphs based on structural analysis.
        
        Returns:
            List of suspicious entities with risk scores
        """
        if not self.graph:
            return []
            
        anomalies = []
        
        # 1. High Degree Nodes (potential hub for layering)
        degree_cent = nx.degree_centrality(self.graph)
        
        # 2. High Volume Edges
        high_value = self.graph_builder.get_high_value_edges(min_amount)
        
        # 3. PageRank for influence
        try:
            pagerank = nx.pagerank(self.graph, weight='weight')
        except:
            pagerank = {}
        
        # Score each entity
        for node in self.graph.nodes():
            score = 0.0
            factors = []
            
            # Degree factor
            if degree_cent.get(node, 0) > 0.1:
                score += 0.3
                factors.append("High Centrality")
                
            # Influence factor
            if pagerank.get(node, 0) > 0.01:
                score += 0.3
                factors.append("High Influence")
                
            # Check incoming/outgoing volume
            in_vol = sum(self.graph.predecessors(node))
            out_vol = sum(self.graph.successors(node))
            if in_vol > 5 or out_vol > 5:
                score += 0.2
                factors.append("High Transaction Volume")
                
            if score > 0.3:
                anomalies.append({
                    "entity_id": node,
                    "risk_score": min(score, 0.99),
                    "factors": factors,
                    "typology": "Network Centrality Pattern"
                })
        
        return sorted(anomalies, key=lambda x: x['risk_score'], reverse=True)
    
    def get_statistics(self):
        """Return graph statistics."""
        if not self.graph:
            return {}
        return self.graph_builder.get_statistics()
