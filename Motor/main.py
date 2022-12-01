import numpy as np
import matplotlib.pyplot as plt
import threading
import time
from motor import Motor
from pid import PID
from Constant import *

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



'''PID Parameters'''
Kp = 10
Ki = 16
Kd = 2


if __name__ == '__main__':
    time = []  # time
    speed_rpm = []  # reference speed
    errors = [0]  # keep track of errors
    dt = 0.001  # sampling rate
    #Master list containing all motors
    motorPool = []
    for i in range(MAX_MOTORS):
        motorPool.append(Motor(i))

    motor = Motor(1)  # initialize the motor
    pid = PID(Kp, Ki, Kd, dt)  # initial the PID Controller

    for t in np.arange(dt, 10, dt):
        time.append(t)
        ref_rpm = input_function(t)
        speed_rpm.append(ref_rpm)

        error_now = ref_rpm - motor.outputs[-1]  # calculating the error
        errors.append(error_now)

        integral, derivative, proportional = pid.calculate(errors)
        v = integral + derivative + proportional
        motor.update(v)
        print(f"My speed is {motor.Wm} time: {t}")

    motor.plotSpeed(time,speed_rpm)
    # plt.plot(time, speed_rpm, label="Reference",
    #          color='blue')
    # plt.plot(time, motor.get_outputs(), label="Output", color='red')
    # plt.xlabel('Time(s)')
    # plt.ylabel('Velocidade (rpm)')
    # plt.legend()
    # plt.grid()
    # plt.show()