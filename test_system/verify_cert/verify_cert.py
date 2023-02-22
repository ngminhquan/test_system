
import struct
import sha256
from sha256 import long_to_bytes, bytes_to_long

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

        _hash = self._ciphertext[-32:]

        text = self._ciphertext[:-32]
        #text = self.rsa_decrypt(text)

        new_hash = sha256.hash_function(text)

        if _hash != new_hash:
            print('INVALID')
        else:
            return text



    def pt_gen(self, msg: bytes) -> bytes:
        # Formatting control information and nonce
        self.q:int = 15 - len(self._nonce)  # length of Q, the encoded message length


        flags: int = self.q - 1
        b_0:bytes = struct.pack("B", flags) + self._nonce + long_to_bytes(len(msg), self.q)

       
        b = b_0 + msg
        return b

ver = verify_cert(b'12345')
a = b"\t12345\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0512345\x9f\x7f\x0f\xfc\x86@[\xa0\x88k\x0f\x17\xd7\xe4\xd8'\x91\xd1\xe2\xb8\xef\x7f7\x1cLN\x03\x01~\x10\x01?"

print(ver.verify(a))