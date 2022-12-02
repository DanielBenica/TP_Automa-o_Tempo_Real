import numpy as np
import matplotlib.pyplot as plt
import threading
import time
from motor import Motor
from pid import PID
from Constant import *
from interface import Interface
from logger import Logger

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


if __name__ == '__main__':
    timeSpan = []  # timeSpan
    speed_rpm = []  # reference speed
    errors = [[0]]  # keep track of errors
    dt = 0.001  # sampling rate
    #Master list containing all motors
    motorPool = []

    #Interface thread object
    interfaceThread = Interface()
    sem.acquire()
    interfaceThread.start()
    sem.release()
    interfaceThread.join()
    


    for i in range(MAX_MOTORS):
        motorPool.append(Motor(i))
        #errors.append([0])


    for m in motorPool:
        m.start()


    loggerThread = Logger(motorPool)
    loggerThread.start()
  

    #loggerThread.join()

    for t in np.arange(dt, 15, dt):
        timeSpan.append(t)
        #ref_rpm = input_function(t)

        speed_rpm.append(interfaceThread.ref_rpm)


        #Turns on motors in onlist
        for i in interfaceThread.onList:
            motorPool[i].calculateError(interfaceThread.ref_rpm)
        
        #sleeps if dt is an integer


        # error_now = ref_rpm - motorPool[0].outputs[-1]  # calculating the error
        # errors[0].append(error_now)
        # integral, derivative, proportional = pid.calculate(errors[0])
        # v = integral + derivative + proportional
        # motorPool[0].update(v)
        #print(f"My speed is {motor.Wm} time: {t}")


    motorPool[0].plotSpeed(timeSpan,speed_rpm)


    for m in motorPool:
        print(f"speed is {m.Wm}")
        m.join()

    