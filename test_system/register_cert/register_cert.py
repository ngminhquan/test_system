import struct
import sha256
from sha256 import long_to_bytes, bytes_to_long

class cert(object):
    def __init__(self, nonce) -> None:
        self._nonce: bytes = nonce

    #RSA encrypt & decrypt, using PU & PK
    def _rsa_encrypt(self, block: bytes) -> bytes:
        pass

    #sent message
    def encrypt(self, msg: bytes) -> bytes:     #msg = ID(A) + PU(A)
        self._msg: bytes = msg
        self._msg_len: int = len(msg)

        
        text = self.pt_gen(self._msg)
        print(text)
        #_hash = self.rsa_encrypt(sha256(text))
        cp = text + sha256.hash_function(text)
        return cp
   



    def pt_gen(self, msg: bytes) -> bytes:
        # Formatting control information and nonce
        self.q:int = 15 - len(self._nonce)  # length of Q, the encoded message length


        flags: int = self.q - 1
        b_0:bytes = struct.pack("B", flags) + self._nonce + long_to_bytes(len(msg), self.q)

       
        b = b_0 + msg
        return b


register = cert(b'12345')
print(register.encrypt(b'12345'))