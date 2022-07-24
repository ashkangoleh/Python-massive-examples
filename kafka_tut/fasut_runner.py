import asyncio
from faust_consumer import example_sender

async def send_value() -> None:
    print(await example_sender.ask())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_value())