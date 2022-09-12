#pip install redis

import redis


r = redis.Redis("arz.local",username="default",password="ashkan")

r.set("name", "Alamat")

name_bytes = r.get("name")
print("==>> name_bytes: ", name_bytes)
name = name_bytes.decode("utf-8")
print("==>> name: ", name)