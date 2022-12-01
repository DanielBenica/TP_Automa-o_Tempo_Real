import threading
import time
from Main import motorPool
from Main import controllerList

sem = threading.Semaphore(5)
lock = threading.Lock()



#########################################################
class Controller(threading.Thread):
    def __init__(self, Kp, Ki, Kd, dt):
        #Controller variables
        threading.Thread.__init__(self)
        self.Kp = Kp
        self.Kd = Kd
        self.Ki= Ki
        self.dt = dt
       
    def calculate(self, errors):
        integral_new = self.integral + self.Ki * (errors[-1]) * self.dt
        self.integral = integral_new
        derivative = self.Kd * (errors[-1] - errors[-2])/self.dt
        proportional = self.Kp * errors[-1]
        return integral_new, proportional, derivative

##########################################################
    def run(self):
        try:
            while (True):
                print("Hello from controller !!!")
                for motor in controllerList:
                    motorPool[motor].setControl()
                time.sleep(2)  
        except:
            print(f"Error in thread controller \n  ")




