import math

POOLS = [
    { "poolId": 10001, "poolValues": [1, 7, 2, 6] },
    { "poolId": 10002, "poolValues": [1, 5, 3, 6] }
]
QUANTILES = [
    { "poolId": 10001, "poolPercents": 99.5},
    { "poolId": 10002, "poolPercents": 95.0}
]

def get_quantile(pool_values: list, pool_percents: float):
    sorted_pool_values = sorted(pool_values)
    n = len(sorted_pool_values)
    print(f'n: {n}')
    p = pool_percents/100
    print(f'p: {p}')
    h = (n - 1) * p
    print(f'h: {h}')
    lower = math.floor(h)  # 3
    print(f'lower: {lower}')
    upper = math.ceil(h)
    print(f'upper: {upper}')
    fraction = h - lower
    print(f'fraction: {fraction}')
    quantile = sorted_pool_values[lower] + fraction * (sorted_pool_values[upper] - sorted_pool_values[lower])
    print(f'quantile: {quantile}')
    return quantile

def get_quantile_by_pool_id(quantile: dict[str, object]):
    for pool in POOLS:
        if pool["poolId"] == quantile['poolId']:
            return { "quantile": get_quantile(pool["poolValues"], quantile['poolPercents']) }
    return None

def main():
    for quantile in QUANTILES:
        result = get_quantile_by_pool_id(quantile)
        print(f'Quantile for poolId {quantile["poolId"]} at percent {quantile["poolPercents"]} is: {result}')


if __name__ == "__main__":
    main()

