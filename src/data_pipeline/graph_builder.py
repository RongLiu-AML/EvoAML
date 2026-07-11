import networkx as nx
import pandas as pd
from collections import defaultdict

class HeterogeneousGraphBuilder:
    """
    Constructs heterogeneous graphs from cross-industry transaction data.
    Uses NetworkX for graph operations.
    """
    def __init__(self):
        self.graph = nx.DiGraph()
        self.node_attributes = {}
        
    def build_from_transactions(self, transactions):
        """
        Build graph from transaction records.
        
        Args:
            transactions: List of dicts with keys: sender, receiver, amount, sector, timestamp
        """
        if isinstance(transactions, str):
            # If CSV path is provided, load it
            df = pd.read_csv(transactions)
            transactions = df.to_dict('records')
            
        # Track sectors for entities
        sector_map = defaultdict(set)
        
        for tx in transactions:
            sender = str(tx.get('sender', tx.get('from', 'UNKNOWN')))
            receiver = str(tx.get('receiver', tx.get('to', 'UNKNOWN')))
            amount = float(tx.get('amount', 0))
            sector = tx.get('sector', 'General')
            timestamp = tx.get('timestamp', None)
            
            # Add nodes
            self.graph.add_node(sender, type='Entity', sector=sector)
            self.graph.add_node(receiver, type='Entity', sector=sector)
            sector_map[sender].add(sector)
            sector_map[receiver].add(sector)
            
            # Add edge with attributes
            if self.graph.has_edge(sender, receiver):
                self.graph[sender][receiver]['weight'] += amount
                self.graph[sender][receiver]['tx_count'] += 1
            else:
                self.graph.add_edge(sender, receiver, weight=amount, tx_count=1, timestamp=timestamp)
        
        # Update sector attributes
        nx.set_node_attributes(self.graph, dict(sector_map), 'sectors')
        
        return self.graph
    
    def get_statistics(self):
        """Return graph statistics."""
        return {
            "nodes": self.graph.number_of_nodes(),
            "edges": self.graph.number_of_edges(),
            "density": nx.density(self.graph),
            "is_directed": self.graph.is_directed()
        }
    
    def get_high_value_edges(self, threshold=10000):
        """Extract high-value transaction edges."""
        high_value = []
        for u, v, data in self.graph.edges(data=True):
            if data.get('weight', 0) > threshold:
                high_value.append({
                    'from': u, 'to': v, 
                    'amount': data.get('weight', 0),
                    'tx_count': data.get('tx_count', 1)
                })
        return sorted(high_value, key=lambda x: x['amount'], reverse=True)
