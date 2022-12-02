import numpy as np
import matplotlib.pyplot as plt
import threading
import time
from motor import Motor
from pid import PID
from Constant import *
from interface import Interface

#Global variables
'''PID Parameters'''
Kp = 10
Ki = 16
Kd = 2


sem = threading.Semaphore(1)


#step function
def heaviside(t,stepTime,stepVal):
    if t < stepTime:
        return 0
    else:
        return stepVal


# reference input function
def input_function(t):
    #rpm = np.sin(1e-2*t**2 + 1e-3*t + 1)
    rpm = heaviside(t,2,215)
    return rpm

def loggerThreadFunc():
    file1 = open("log.txt", "a")
    while(True):
        for i in range(len(motorPool)):
            file1.write(f"Motor {motorPool[i].id} speed: {motorPool[i].Wm} \n")
        file1.write("\n ################# \n\n")
        time.sleep(2)


if __name__ == '__main__':
    timeSpan = []  # timeSpan
    speed_rpm = []  # reference speed
    errors = [[0]]  # keep track of errors
    dt = 0.001  # sa220mpling rate
    #Master list containing all motors
    motorPool = []

    #Interface thread object
    interfaceThread = Interface()
    interfaceThread.start()
    interfaceThread.join()


    for i in range(MAX_MOTORS):
        motorPool.append(Motor(i))
        #errors.append([0])


    for m in motorPool:
        m.start()


    loggerThread = threading.Thread(target = loggerThreadFunc)
    sem.acquire()
    loggerThread.start()
    sem.release()

    #loggerThread.join()
    #motor = Motor(1)  # initialize the motor
    #pid = PID(Kp, Ki, Kd, dt)  # initial the PID Controller

    for t in np.arange(dt, 15, dt):
        timeSpan.append(t)
        #ref_rpm = input_function(t)

        speed_rpm.append(interfaceThread.ref_rpm)


        #Turns on motors in onlist
        for i in interfaceThread.onList:
            motorPool[i].calculateError(interfaceThread.ref_rpm)
            
        # error_now = ref_rpm - motorPool[0].outputs[-1]  # calculating the error
        # errors[0].append(error_now)
        # integral, derivative, proportional = pid.calculate(errors[0])
        # v = integral + derivative + proportional
        # motorPool[0].update(v)
        #print(f"My speed is {motor.Wm} time: {t}")

    #motorPool[0].plotSpeed(timeSpan,speed_rpm)
    
    for m in motorPool:
        print(f"speed is {m.Wm}")
        m.join()

    