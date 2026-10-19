def quantum_states(n):
    return 2 ** n

for n in [1, 2, 8, 127]:
    states = quantum_states(n)

    print(
        f"{n:3} кубит(ов): "
        f"{states:,} состояний одновременно | "
        f"классика: {n} состояний"
    )