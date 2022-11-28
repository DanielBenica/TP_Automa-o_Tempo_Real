import threading
import time
import sys
from Motor import *
from Constant import *
from Controller import *

#Master list containing all motors
motorPool = []
controllerList =[]
reference=[0]*30

if __name__ == "__main__":
    

    for i in range(MAX_MOTORS):
        motorPool.append(Motor(i))


    for i in motorPool:
        i.start()


    for i in onList:
        if(i == True):
            controllerList.append(i)


    for i in motorPool:
        i.join()
        
    controller = Controller()
    time.sleep(10) 
    controller.start()
    controller.join()


    print("Fim")