class HeterogeneousGraphBuilder:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def build_from_transactions(self, normalized_transactions):
        """Convert flat transactions into graph topology."""
        for tx in normalized_transactions:
            node_id = tx["secure_id"]
            if node_id not in self.nodes:
                self.nodes[node_id] = {"type": "Entity", "sector": tx["sector"]}
            
            # Mock edge creation logic
            self.edges.append({
                "source": node_id,
                "target": "Clearing_House_A",
                "weight": tx["amount"],
                "relation_type": "FUNDS_TRANSFER"
            })
        
        return {"nodes": self.nodes, "edges": self.edges}
