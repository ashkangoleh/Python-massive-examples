import logging

logger = logging.getLogger()
logging.basicConfig(format='[%(asctime)s] %(levelname)-8s [%(filename)s:%(lineno)d] --> %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)


try:
    def test(x, y): return x/y
    logger.warning(f"{test(1,1)}")
except ZeroDivisionError:
    logger.error(f"{test(1,0)}")

test(1, 0)
