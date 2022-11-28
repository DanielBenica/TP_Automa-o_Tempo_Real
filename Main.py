import threading
import time
import sys
from Motor import *
from Constant import *
from Controller import *


def loggerThreadFunc():
    file1 = open("log.txt", "w")
    while(True):
        for i in range(len(motorPool)):
            file1.write(f"Motor {motorPool[i].id} speed: {motorPool[i].Wm} \n")
    

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

    time.sleep(4)
    loggerThread = threading.Thread(target = loggerThreadFunc)
    loggerThread.start()
    loggerThread.join()

    # controller = Controller()
    # time.sleep(10) 
    # controller.start()
    # controller.join()
    
    for i in motorPool:
        i.join()
        


    print("Fim")

