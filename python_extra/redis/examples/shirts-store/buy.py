import time
import redis
import logging

r = redis.Redis("arz.local", username="default", password="ashkan")


logging.basicConfig()


class OutOfStockError(Exception):
    """Raised when shirts out of stock"""


def scan_keys(pattern, pos: int = 0) -> list:
    shirts = []
    while 1:
        pos, value = r.scan(cursor=pos, match=pattern)
        shirts.extend(value)
        if pos == 0:
            break

    return shirts


def buy_items(r: redis.Redis, itemId) -> None:
    pipe = r.pipeline()
    try:
        while 1:
            pipe.watch(itemId)
            nleft: bytes = r.hget(itemId, "quantity")
            if nleft > b'0':
                pipe.multi()
                time.sleep(1)
                pipe.hincrby(itemId, "quantity", -1)
                pipe.hincrby(itemId, "nPurchased", 1)
                pipe.execute()
                break
            else:
                pipe.unwatch()
                logging.error(OutOfStockError(
                    f"Sorry {itemId.decode('utf-8')} is out of stock"
                ))
                break
    except redis.WatchError:
        logging.warning("Error in watch, retrying")
    return None


shirts = scan_keys("shirt:colored:*")
print("==>> shirts: ", shirts)

# for i in shirts:
#     buy_items(r, i)

