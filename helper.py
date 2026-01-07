import math 

def get_quantile_by_pool_id(pools: list, quantile: dict[str, object]):
    for pool in pools:
        if pool["poolId"] == quantile['poolId']:
            return get_quantile(pool["poolValues"], quantile['poolPercents'])
    return None

# Calculate the quantile for given pool values and percent
def get_quantile(pool_values: list, pool_percents: float):
    sorted_pool_values = sorted(pool_values)
    n = len(sorted_pool_values)
    p = pool_percents/100
    h = (n - 1) * p
    lower = math.floor(h)
    upper = math.ceil(h)
    fraction = h - lower
    quantile = sorted_pool_values[lower] + fraction * (sorted_pool_values[upper] - sorted_pool_values[lower])
    return round(quantile, 2)