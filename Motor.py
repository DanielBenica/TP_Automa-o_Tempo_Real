import threading
import time

onList = [0]*30
sem = threading.Semaphore(5)
lock = threading.Lock()



#########################################################
class Motor(threading.Thread):
    def __init__(self,id):
        #Motor variables
        threading.Thread.__init__(self)
        self.id = id
        
        self.Ra = 1		        #armature_resistance
        self.La = 0.5		    #armature_inductance	    
        self.Jm = 0.01		    #inertia
        self.B = 0.3		    # viscous_friction
        self.Kb = 0.01		    #eletric_constant
        self.Wm = 0			    #Speed
        self.Kt = 0.01
        self.dt = 0.001         #Sampling time
        self.Control = False    #Flag for control
        self.outputs = [0, 0]

##########################################################
    def update(self, v):
        output_now = (v + (self.L * self.B * self.outputs[-1] / self.dt / self.Kt) + (self.L * self.J * (2 * self.outputs[-1] - 
        self.outputs[-2]) / self.Kt / (self.dt ** 2)) + 
        (self.R * self.J * self.outputs[-1] / self.Kt)) / ((self.L * self.B / self.dt / self.Kt) + 
            (self.L * self.J / self.Kt / (self.dt**2))+(self.R * (self.B + self.J) / self.Kt) - self.Kb)
        self.outputs.append(output_now)

    def get_outputs(self):
        return self.outputs[2:]


##########################################################

    def turnOn(self):
        
        onList[self.id] = 1
        initTime = time.time()
        while(True):

            if (self.Wm<self.WmMax):
                self.Wm = self.Wm + 12
            print(f"Hello from motor: {self.id} my speed is : {self.Wm}") 
            time.sleep(2)
            if(self.Control):
                self.setWm()
                break

              
        onList[self.id] = 0 
        self.Control = False
        print(f"Realising sem :{self.id}")
        sem.release()     
        time.sleep(5)   
        


##########################################################

    def setControl(self):
        self.Control = True

########################################################

    def setWm(self):
            
        initTime = time.time()


        while(time.time() < initTime + 30): 
            if (self.Wm>self.WmMax/2):
                self.Wm = self.Wm - 8
            print(f"Hello from motor: {self.id} my speed is : {self.Wm}") 



##########################################################
    def run(self):
        try:
            while (True):
                after = self.id + 1
                before = self.id - 1

                
                if (after > 29):
                    after = 29
                if(before<0):
                    before = 0
                sem.acquire()
                if(not onList[after] and not onList[before]):
                    self.turnOn()
                else:
                    sem.release()

        except:
            print(f"Error in thread:{self.id} \n after: {after} \n before:{before} ")
            


