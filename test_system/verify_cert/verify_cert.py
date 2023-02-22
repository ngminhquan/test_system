
import struct
import sha256

class verify_cert(object):
    def __init__(self, nonce) -> None:
        self._nonce: bytes = nonce

    #RSA decrypt, using PU & PK
    def _rsa_decrypt(self, block: bytes) -> bytes:
        pass

    #verify received msg
    def verify(self, ciphertext: bytes) -> bytes:          #verify the received msg
        self._ciphertext: bytes = ciphertext
        self._len_cp: int = len(ciphertext)
        '''
        _hash = self._ciphertext[-256:]

        text = self._ciphertext[:-256]
        text = self.rsa_decrypt(text)

        new_hash = sha256(text)

        if _hash != new_hash:
            raise ValueError('hash after generate is not equal to initial hash')
        else:
            return text'''



    def pt_gen(self, msg: bytes) -> bytes:
        # Formatting control information and nonce
        self.q:int = 15 - len(self._nonce)  # length of Q, the encoded message length


        flags: int = (64 * (self._assoc_len > 0) + 8 * ((self._mac_len - 2) // 2) +      \
                 (self.q - 1))
        b_0:bytes = struct.pack("B", flags) + self._nonce + long_to_bytes(len(msg), self.q)

       
        b = b_0 + msg
        return b