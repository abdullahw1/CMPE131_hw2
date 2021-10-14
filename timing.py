import time

def calculate_time(method):
    def timer():
        #store start time
        start = time.time()
        time.sleep(2)
        # store end time
        end = time.time()
        print("total", end - start)
       
    return timer
