import hashlib

class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        text = str(self.index) + self.data + self.prev_hash
        return hashlib.sha256(text.encode()).hexdigest()

chain = []

block = Block(0, "Genesis", "0")
chain.append(block)

block = Block(1, "Transaction 1", chain[-1].hash)
chain.append(block)

block = Block(2, "Transaction 2", chain[-1].hash)
chain.append(block)

for block in chain:
    print(f"Блок {block.index}:")
    print(f"hash={block.hash}")
    print(f"prev={block.prev_hash}")
    print()