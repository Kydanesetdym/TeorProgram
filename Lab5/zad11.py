def analyze_requests(log):
    stats = {}

    for subgraph, count in log:
        stats[subgraph] = stats.get(subgraph, 0) + count

    for subgraph, count in stats.items():
        print(f"{subgraph}: {count:,} запросов")

    busiest = max(stats, key=stats.get)
    total = sum(stats.values())

    print(f"Самый нагруженный: {busiest}")
    print(f"Всего запросов: {total:,}")

log = [
    ("uniswap", 10000),
    ("aave", 5000),
    ("compound", 2500),
    ("uniswap", 2500),
    ("aave", 3500),
    ("compound", 2000)
]

analyze_requests(log)