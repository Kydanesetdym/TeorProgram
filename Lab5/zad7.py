def is_threat(p):
    return p > 0.5

shares = [0.3, 0.51, 0.49, 0.6]

for p in shares:
    if is_threat(p):
        status = "УГРОЗА (атака 51%)"
    else:
        status = "безопасно"

    print(f"Доля мощности {p:.0%}: {status}")