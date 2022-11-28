from socket import *


def readMessage(msg):
    splitMsg = msg.split("/x/")
    motorId = list(map(int, splitMsg[0].split()))
    voltage = splitMsg[1]
    print(f"Id do motor: {motorId} tensão de referencia: {voltage}")


host = gethostname()
port = 51511

print(f'HOST: {host} , PORT {port}')
serv = socket(AF_INET, SOCK_STREAM)
serv.bind((host, port))
serv.listen(5)
while 1:
    con, adr = serv.accept()
    while 1:
        msg = con.recv(1024)
        msg = msg.decode()
        #print(msg)
        readMessage(msg)

