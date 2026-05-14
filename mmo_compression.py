from spn_network import SPN
import hashlib

class MMOCompression:
    """
    Matyas-Meyer-Oseas Compression Module.
    Constructs a hash function using a block cipher (SPN).
    Formula: H_i = E_{H_{i-1}}(m_i) XOR m_i
    """
    def __init__(self):
        self.spn = SPN()
        self.iv = 0x5555 # Initial Value (H_0)

    def generate_hash(self, data):
        """
        Generates an MMO hash for the given data (string or bytes).
        Breaks data into 16-bit blocks and applies the MMO construction.
        """
        if isinstance(data, str):
            data = data.encode()
        
        # Simple padding to ensure data is multiple of 2 bytes
        if len(data) % 2 != 0:
            data += b'\x00'
            
        h_prev = self.iv
        
        # Process in 16-bit chunks
        for i in range(0, len(data), 2):
            m_i = int.from_bytes(data[i:i+2], byteorder='big')
            # H_i = E_{H_{i-1}}(m_i) ^ m_i
            h_i = self.spn.encrypt(m_i, h_prev) ^ m_i
            h_prev = h_i
            
        return hex(h_prev)

    def encrypt_block(self, device_id, payload):
        """Simulates the encryption of a device data block."""
        data_to_hash = f"{device_id}{payload}"
        return self.generate_hash(data_to_hash)

    def verify_integrity(self, original_hash, current_data):
        """Verifies if the current data matches the original hash."""
        current_hash = self.generate_hash(current_data)
        return original_hash == current_hash

if __name__ == "__main__":
    mmo = MMOCompression()
    h = mmo.encrypt_block("DEV001", "temp:25,hum:60")
    print(f"Generated Hash: {h}")
    is_valid = mmo.verify_integrity(h, "DEV001" + "temp:25,hum:60")
    print(f"Integrity Valid: {is_valid}")
    is_valid_bad = mmo.verify_integrity(h, "DEV001" + "temp:26,hum:60")
    print(f"Integrity Valid (Tampered): {is_valid_bad}")
