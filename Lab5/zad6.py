import hashlib

def sha256_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def merkle_root(transactions):
    hashes = [sha256_hash(tx) for tx in transactions]

    while len(hashes) > 1:
        if len(hashes) % 2 != 0:
            hashes.append(hashes[-1])

        new_hashes = []

        for i in range(0, len(hashes), 2):
            combined = hashes[i] + hashes[i + 1]
            new_hashes.append(sha256_hash(combined))

        hashes = new_hashes

    return hashes[0]

transactions = ["tx1", "tx2", "tx3", "tx4"]

root = merkle_root(transactions)
print("Merkle root:", root)