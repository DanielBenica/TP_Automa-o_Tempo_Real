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
        
        self.Ra = 1		    #armature_resistance
        self.La = 0.35		#armature_inductance
        self.Ia = 2		    #armature_current
        self.Km = 0		    # torque_nt
        self.Tl = 0		    # load_torque
        self.Jm = 0.02		#inertia
        self.B = 0.3		# viscous_friction
        self.Kb = 0.02		#eletric_constant
        self.Wm = 0				#Speed
        self.Kt = 0.1
        self.Tm = 0.1
        self.Control = False
        self.dt = 0.001         #Sampling time

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
            


