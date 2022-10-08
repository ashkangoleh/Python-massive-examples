import redis


r = redis.Redis("arz.local")
                # , username="default", password="ashkan")

# r.flushdb()  # not recommended in production

products = [{
    "color": "green",
    "price": 49.99,
    "style": "fitted",
    "quantity": 5,
    "nPurchased": 0
}, {
    "color": "black",
    "price": 59.99,
    "style": "office shirt",
    "quantity": 5,
    "nPurchased": 0
}, {
    "color": "Maroon",
    "price": 69.99,
    "style": "office fitted",
    "quantity": 5,
    "nPurchased": 0
}, {
    "color": "pink",
    "price": 79.99,
    "style": "over fitted",
    "quantity": 5,
    "nPurchased": 0
},
]


id = 1
#pipeline
pipe= r.pipeline()

for p in products:
    key = f"shirt:colored:{id}"
    for field, value in p.items():
        r.hset(key, field, value)
    id += 1

# get_all = r.hgetall("shirt:colored:1")
# print("==>> get_all: ", dict(get_all))

# for p in products:
#     for field, value in p.items():
#         key = f"shirt:colored:{p['color']}"
#         r.hset(key, field, value)
#     id += 1


pipe.execute()