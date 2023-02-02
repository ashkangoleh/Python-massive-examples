#pip3 install schedule
import schedule
import time


def job():
    print("Job invoked, task is running.....")
    
    
schedule.every(1).seconds.do(job)


while 1:
    schedule.run_pending()
    time.sleep(1)
