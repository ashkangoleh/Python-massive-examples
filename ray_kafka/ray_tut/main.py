import time
import ray
import cv2
import numpy as np

ray.init(address='192.168.26.60:6385')

@ray.remote
def test(img):
    orb = cv2.AKAZE_create()
    kp = orb.detect(img,None)
    kp , des = orb.compute(img,kp)
    return des

if __name__ == "__main__":
    start_time = time.time()
    img = cv2.imread("/home/ashkan/Pictures/code_rate.png")
    futures = [test.remote(img) for i in range(10000)]
    ray.get(futures)

    print(time.time() - start_time)