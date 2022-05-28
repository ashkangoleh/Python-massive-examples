import time
from threading import Thread, Condition


class StingySpendy:
    money = 100
    cv = Condition()

    def stingy(self):
        for i in range(20):
            self.cv.acquire()
            self.money += 10
            self.cv.notify()
            self.cv.release()
        print("Stingy Done")

    def spendy(self):
        for i in range(10):
            self.cv.acquire()
            while self.money < 20:
                self.cv.wait()
            self.money -= 20
            if self.money < 0:
                print(f"Money in bank: {self.money}")
            self.cv.release()
        print("Spendy Done")


st = time.time()
ss = StingySpendy()
Thread(target=ss.stingy, args=()).start()
Thread(target=ss.spendy, args=()).start()
en = time.time()
time.sleep(5)
print(f"time taken: {en - st:0.02f}")
print(f"Money in the end: {ss.money}")
