import threading
import time
from Motor import *
from Constant import *

sem = threading.Semaphore(3)

if __name__ == "__main__":
    #Master list containing all motors
    motorPool = []

    for i in range(MAX_MOTORS):
        motorPool.append(Motor(i))

    for i in motorPool:
        i.start()


    time.sleep(10)
    print("###############################################################################")
    offList[0] = 1
    offList[2] = 1
    for i in motorPool:
        i.join()


    print("Fim")