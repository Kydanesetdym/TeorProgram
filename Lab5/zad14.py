def factorize(n):
    factors = []
    d = 2

    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d

        d += 1

    if n > 1:
        factors.append(n)

    return factors

for number in [15, 21, 91]:
    factors = factorize(number)
    print(f"{number} = {' x '.join(map(str, factors))}")