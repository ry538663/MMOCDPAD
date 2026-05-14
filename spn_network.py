import numpy as np

class SPN:
    """
    Substitution-Permutation Network implementation.
    Simplified for 16-bit blocks for prototype clarity.
    """
    def __init__(self):
        # S-Box (4-bit)
        self.s_box = [0xE, 0x4, 0xD, 0x1, 0x2, 0xF, 0xB, 0x8, 0x3, 0xA, 0x6, 0xC, 0x5, 0x9, 0x0, 0x7]
        self.inv_s_box = [self.s_box.index(x) for x in range(16)]
        
        # P-Box (16-bit permutation)
        self.p_box = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]
        self.inv_p_box = [self.p_box.index(x) for x in range(16)]

    def substitute(self, block):
        """Applies S-Box substitution to each 4-bit nibble of the 16-bit block."""
        result = 0
        for i in range(4):
            nibble = (block >> (i * 4)) & 0xF
            result |= (self.s_box[nibble] << (i * 4))
        return result

    def inverse_substitute(self, block):
        result = 0
        for i in range(4):
            nibble = (block >> (i * 4)) & 0xF
            result |= (self.inv_s_box[nibble] << (i * 4))
        return result

    def permute(self, block):
        """Applies P-Box permutation to the bits of the 16-bit block."""
        result = 0
        for i in range(16):
            bit = (block >> i) & 1
            result |= (bit << self.p_box[i])
        return result

    def inverse_permute(self, block):
        result = 0
        for i in range(16):
            bit = (block >> i) & 1
            result |= (bit << self.inv_p_box[i])
        return result

    def encrypt(self, block, key):
        """Single round SPN encryption for demonstration."""
        # Key XOR
        state = block ^ (key & 0xFFFF)
        # Substitution
        state = self.substitute(state)
        # Permutation
        state = self.permute(state)
        return state

if __name__ == "__main__":
    spn = SPN()
    test_block = 0xABCD
    test_key = 0x1234
    encrypted = spn.encrypt(test_block, test_key)
    print(f"Original: {hex(test_block)}, Encrypted: {hex(encrypted)}")
