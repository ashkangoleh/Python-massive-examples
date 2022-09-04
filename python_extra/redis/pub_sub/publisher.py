import redis


class Publisher:
    def __init__(self,host:str='arz.local',port:int = 6379,db=0):
        self.queue = redis.StrictRedis(host=host,port=port,db=db)
        
        
    def pub(self,name,value):
        self.queue.publish(name,value)
        
        
channel = "test"
message ="test2"
Publisher().pub(channel, message)