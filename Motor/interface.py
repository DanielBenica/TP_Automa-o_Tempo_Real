import threading
import time

class Interface(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.ref_rpm = 0
        self.onList =""

    def run(self):
        #receive input and convert to int list
        self.onList = input("Enter the motors you want to turn on: ")
        self.onList = [int(x) for x in self.onList.split()]
        self.ref_rpm = float(input("Digite a referencia em RPM: "))
        print(f"Turning on motors {self.onList}!!!")

    def verifyList(self):
        #Verify if the list has sequencial numbers
        for i in self.onList:
            if(i+1  in self.onList or i-1 in self.onList):
                return False
            else:
                return True