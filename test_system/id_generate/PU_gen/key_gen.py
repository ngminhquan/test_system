import rsa

# Generate a 2048-bit RSA key pair
(pubkey, privkey) = rsa.newkeys(512)

# Print the public key in PEM format
print(pubkey.save_pkcs1().decode('utf-8'), '\n\n\n')

# Print the private key in PEM format
print(privkey.save_pkcs1().decode('utf-8'))