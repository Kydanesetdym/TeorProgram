import random

def create_tangle(n):
    random.seed(42)
    tangle = {}

    for i in range(n):
        if i < 2:
            tangle[i] = []
        else:
            tangle[i] = random.sample(range(i), 2)

    return tangle

tangle = create_tangle(6)

for tx, references in tangle.items():
    if references:
        print(f"Транзакция {tx} подтверждает: {references}")
    else:
        print(f"Транзакция {tx} подтверждает: — (начальная)")