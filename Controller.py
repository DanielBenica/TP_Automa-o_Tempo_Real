import threading
import time
from Main import motorPool
from Main import controllerList

sem = threading.Semaphore(5)
lock = threading.Lock()



#########################################################
class Controller(threading.Thread):
    def __init__(self):
        #Motor variables
        threading.Thread.__init__(self)
       


##########################################################
    def run(self):
        try:
            while (True):
                for motor in controllerList:
                    motorPool[motor].setControl()
                print("Hello from controller !!!")
                time.sleep(2)  
        except:
            print(f"Error in thread controller \n  ")




