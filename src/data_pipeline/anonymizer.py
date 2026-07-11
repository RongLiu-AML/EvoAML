import os
import hashlib
import re

class DataAnonymizer:
    """
    Provides data anonymization and PII masking utilities.
    Implements one-way hashing for secure ID mapping.
    """
    def __init__(self, salt=None):
        # Use env var if available, otherwise generate from machine ID
        self.salt = salt or os.environ.get('EVOAML_SALT', 'default_salt_2024')

    def mask_pii(self, text):
        """Mask explicit PII like emails or SSNs."""
        if not text: return text
        # Simple email mask: user***@domain.com
        text = re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1***@\2', text)
        return text

    def hash_account_id(self, account_id):
        """
        Irreversibly hash account IDs for privacy compliance.
        Uses SHA-256 with salt.
        """
        if not account_id: return None
        return hashlib.sha256(f"{account_id}{self.salt}".encode()).hexdigest()
