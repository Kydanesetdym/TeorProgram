def calculate_reads(writes):
    minimum = writes * 100
    maximum = writes * 10000

    return minimum, maximum


writes = 500
minimum, maximum = calculate_reads(writes)

print(f"Записей в секунду: {writes}")
print(f"Минимум чтений/с: {minimum:,}")
print(f"Максимум чтений/с: {maximum:,}")