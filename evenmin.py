from datetime import datetime
import time
import random
evens=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60]

for i in range(5):
    this_minute=datetime.today().minute
    if this_minute in evens:
        print("We are experiencing an even minute")
    else:
        print("An odd one bro")
    waiting_time=random.randint(1,60)
    time.sleep(waiting_time)
