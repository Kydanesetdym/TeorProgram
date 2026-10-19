import hashlib

def sha256_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()

text = "blockchain"
result = sha256_hash(text)

print(f"SHA-256('{text}') =")
print(result)