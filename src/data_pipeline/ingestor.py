import json
import os

class MultiSourceIngestor:
    """
    Ingestor for cross-industry transaction logs.
    Supports JSON, CSV, and database connections.
    """
    def __init__(self):
        self.anonymizer = None
        self.supported_formats = ['json', 'csv']

    def load_config(self, config_path):
        """Load configuration for data sources."""
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return json.load(f)
        return {}

    def ingest_json_logs(self, file_path):
        """Load and normalize cross-industry transaction logs."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Data file not found: {file_path}")
        
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        normalized = []
        for record in data:
            # Normalize fields
            normalized_record = {
                'sender': record.get('sender', record.get('from')),
                'receiver': record.get('receiver', record.get('to')),
                'amount': float(record.get('amount', 0)),
                'sector': record.get('sector', 'General'),
                'timestamp': record.get('timestamp')
            }
            normalized.append(normalized_record)
        
        return normalized
    
    def get_supported_formats(self):
        """Return list of supported file formats."""
        return self.supported_formats
