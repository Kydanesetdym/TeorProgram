import hashlib

def mine(data, difficulty):
    nonce = 0
    prefix = "0" * difficulty

    while True:
        text = data + str(nonce)
        h = hashlib.sha256(text.encode()).hexdigest()

        if h.startswith(prefix):
            return nonce, h

        nonce += 1

nonce, h = mine("block1", 4)

print("difficulty=4")
print(f"nonce={nonce}")
print(f"hash={h}")