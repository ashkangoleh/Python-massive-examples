import redis


r = redis.Redis("arz.local", username="default", password="ashkan")


r.flushdb()

i = 1

pipe = r.pipeline()

while i <= 140:
    name = f"check:{i}"
    data = f"hello:{i}"
    pipe.set(name, data)
    i += 1
pipe.execute()