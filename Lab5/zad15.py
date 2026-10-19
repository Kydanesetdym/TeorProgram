def forecast_qubits(generations):
    growth = []

    for i in range(1, len(generations)):
        ratio = generations[i] / generations[i - 1]
        growth.append(ratio)

    average = sum(growth) / len(growth)
    forecast = round(generations[-1] * average)

    print("Поколения кубитов:", generations)
    print("Коэффициенты роста:",
          [round(x, 2) for x in growth])
    print(f"Средний темп роста: x{average:.2f}")
    print(f"Прогноз следующего поколения: ~{forecast} кубитов")

generations = [127, 433, 1121]
forecast_qubits(generations)