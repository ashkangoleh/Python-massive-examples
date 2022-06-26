#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 08:58:24 2022

@author: ashkan
"""

from typing import Optional, Callable, Awaitable
import asyncio
from functools import wraps



def repeat_every(*, seconds: float, wait_first: bool = False)-> Callable:
    def decorator(function: Callable[[], Optional[Awaitable[None]]]):
        is_coroutine = asyncio.iscoroutinefunction(function)

        @wraps(function)
        async def wrapped():
            async def loop():
                if wait_first:
                    await asyncio.sleep(seconds)
                while True:
                    try:
                        if is_coroutine:
                            await function()
                        else:
                            await asyncio.run_in_threadpool(function)
                    except Exception as e:
                        raise e
                    await asyncio.sleep(seconds)

            asyncio.create_task(loop())

        return wrapped
    print("Repeat every working well.")
    return decorator


@repeat_every(seconds=2)
async def main():
    print(2*2)

try:
    loop = asyncio.get_running_loop()
except RuntimeError: 
    loop = None
    
if loop and loop.is_running():
    print('Async event loop already running.')
    tsk = loop.create_task(main())
    tsk.add_done_callback(
        lambda t: print(f'Task done with result= {t.result()}'))
else:
    print('Starting new event loop')
    asyncio.run(main())