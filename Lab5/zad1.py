def calculate_tps(networks):
    results = {}

    for name, tps in networks.items():
        results[name] = tps * 3600
        print(f"{name}: {results[name]:,} транзакций/час")

    leader = max(networks, key=networks.get)
    print(f"Лидер: {leader}")


networks = {
    "Ethereum": 30,
    "Binance Smart Chain": 160,
    "Solana": 50000
}

calculate_tps(networks)