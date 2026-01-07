from fastapi import Body, FastAPI
import math
import helper as hp
import initial_data as dt
app = FastAPI()

# Endpoint to get all pools
@app.get("/pools")
async def get_pools():
    return dt.POOLS

# Endpoint to get all quantiles
@app.get("/quantiles")
async def get_pools_percents():
    return dt.QUANTILES

# Endpoint to insert a new pool
@app.post("/pools/insert_pool")
async def create_book(new_pool=Body()):
    for pool in dt.POOLS:
        if pool["poolId"] == new_pool["poolId"]:
            return {"error": "This pool with this ID already exists."}
    dt.POOLS.append(new_pool)
    return {"message": "Appended."}

# Endpoint to insert a new quantile
@app.post("/quantiles/insert_quantile")
async def create_book(new_quantile=Body()):
    for quantile in dt.QUANTILES:
        if quantile["poolId"] == new_quantile["poolId"]:
            return {"error": "This quantile already exists."}
    dt.QUANTILES.append(new_quantile)
    # Calculate and return the quantile for the newly added quantile
    quantile = hp.get_quantile_by_pool_id(dt.POOLS, new_quantile)
    return {"quantile": quantile}

