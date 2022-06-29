import asyncio
from concurrent.futures.process import ProcessPoolExecutor
from datetime import datetime
from typing import List
from fastapi import FastAPI, Query, Depends
from math import sqrt, cos


app = FastAPI()


async def run_in_process(fn, *args):
    loop = asyncio.get_event_loop()
    # wait and return result
    return await loop.run_in_executor(app.state.executor, fn, *args)


async def add(x):
    start = datetime.now()
    data = []
    for j in range(x*x):
        # yield cos(sqrt((j*11345362356256578)/26))
        data.append(cos(sqrt((j*11345362356256578)/26)))
    print(datetime.now() - start)
    return data


def get_something_different(p_i: int=Query(alias="id")):
    print('p_i: ', p_i)
    id = p_i * 10
    return id


def get_something_different2(q: int = Depends(get_something_different,use_cache=False), q1: int=1):
    print('q: ', q)
    if q > 100:
        return q*q1
    else:
        return q+q1

@app.get("/{param}")
async def handler1(param: int):
    try:
        print('param: ', param)
        start = datetime.now()
        res = await run_in_process(add, param)
        print(datetime.now() - start)
        return {"result": res}
    except Exception as e:
        raise e

@app.get("/tt/{p_i}/{q1}")
async def handler2(i: int = Depends(get_something_different2)):
    print('i: ', i)
    
    return {"result": i}


@app.on_event("startup")
async def on_startup():
    app.state.executor = ProcessPoolExecutor()


@app.on_event("shutdown")
async def on_shutdown():
    app.state.executor.shutdown()
