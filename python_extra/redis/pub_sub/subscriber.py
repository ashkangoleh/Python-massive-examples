import redis
import threading


class Listener(threading.Thread):
    def __init__(self, host: str = "arz.local", port: int = 6379, db: int = 0) -> None:
        threading.Thread.__init__(self)
        self.redis = redis.StrictRedis(host='arz.local', port=6379, db=0)

        self.pubsub = self.redis.pubsub()
        # self.pubsub.subscribe(channels)

    def channel(self, channels: list[str]) -> None:
        self.pubsub.subscribe(channels)

    def work(self, item) -> None:
       
        if isinstance(item['data'], bytes):
            # TODO: implement work method to anything we want
            print("==>> item['data']: ", item['data'].decode('utf-8'))
            print("==>> item['channel']: ", item['channel'].decode('utf-8'))
        else:
            # TODO: implement work method to anything we want
            print("==>> item['data']: ", item['data'])
            print("==>> item['channel']: ", item['channel'].decode('utf-8'))

    def run(self) -> work:
        for item in self.pubsub.listen():
            self.work(item)

    @property
    def start(self) -> None:
        return super().start()


if __name__ == "__main__":
    client = Listener(host='arz.local', port=6379, db=0)
    client.channel(['test'])
    client.start

