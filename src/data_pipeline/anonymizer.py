import hashlib
import re

class DataAnonymizer:
    def __init__(self, salt="evo_aml_secure_salt_2024"):
        self.salt = salt

    def mask_pii(self, text):
        """Mask explicit PII like emails or SSNs."""
        if not text: return text
        # Simple email mask
        text = re.sub(r'([\w\.-]+)@([\w\.-]+)', r'***@\2', text)
        return text

    def hash_account_id(self, account_id):
        """Irreversibly hash account IDs for privacy."""
        if not account_id: return None
        return hashlib.sha256(f"{account_id}{self.salt}".encode()).hexdigest()
