import asyncio
from concurrent.futures.process import ProcessPoolExecutor
from datetime import datetime
from fastapi import FastAPI, Query
from math import sqrt, cos

app = FastAPI()


async def run_in_process(fn, *args):
    loop = asyncio.get_event_loop()
    # wait and return result
    return await loop.run_in_executor(app.state.executor, fn, *args)


def add(x, y):
    start = datetime.now()
    data = {}
    for i,j in enumerate(range(x*y)):
        data[i] = cos(sqrt((j*11345362356256578)/26))
    print(datetime.now() - start)
    return data
    


@app.get("/")
async def handler(param: list[int] | None=Query(default=None)):
    start = datetime.now()
    res = await run_in_process(add, param[0], param[1])
    print(datetime.now() - start)
    return {"result": res}


@app.on_event("startup")
async def on_startup():
    app.state.executor = ProcessPoolExecutor()


@app.on_event("shutdown")
async def on_shutdown():
    app.state.executor.shutdown()
