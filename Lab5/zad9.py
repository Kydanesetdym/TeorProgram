def confirmation_time(k, n):
    return k / n

k = 1000

for n in [10, 100, 1000]:
    time = confirmation_time(k, n)
    print(
        f"n={n:4} транзакций -> "
        f"время подтверждения = {time:.2f} усл.ед."
    )