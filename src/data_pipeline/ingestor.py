import json
from src.data_pipeline.anonymizer import DataAnonymizer

class MultiSourceIngestor:
    def __init__(self):
        self.anonymizer = DataAnonymizer()

    def ingest_json_logs(self, file_path):
        """Load and normalize cross-industry transaction logs."""
        # Mock ingestion
        mock_data = [
            {"raw_account": "ACCT-9921", "amount": 50000, "sector": "Energy"},
            {"raw_account": "ACCT-1102", "amount": 75000, "sector": "Logistics"}
        ]
        
        normalized = []
        for record in mock_data:
            normalized.append({
                "secure_id": self.anonymizer.hash_account_id(record["raw_account"]),
                "amount": record["amount"],
                "sector": record["sector"]
            })
        return normalized
