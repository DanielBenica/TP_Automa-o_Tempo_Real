import threading
import time
from Constant import *

class Interface(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.ref_rpm = 0
        self.onList = ""

    def run(self):
        while(True):
        #receive input and convert to int list
            self.onList = input("Enter the motors you want to turn on: ")
            self.onList = [int(x) for x in self.onList.split()]
            if(self.verifyList()):
                break
        self.ref_rpm = float(input("Digite a referencia em RPM: "))
        print(f"Turning on motors {self.onList}!!!")


    def verifyList(self):
        #verify all numbers are less than MAX_MOTORS
        for i in self.onList:
            if(i > MAX_MOTORS-1):
                print("Invalid motor ID, try again")
                return False

        #verify if the list is less than 12
        if(len(self.onList) > 12):
            print("Too many motors, try again")
            return False

        #Verify if the list has sequencial numbers
        for i in self.onList:
            if(i+1  in self.onList or i-1 in self.onList):
                print("Invalid list, try again")
                return False

        return True