from socket import *
host = gethostname()
port = 51511
cli = socket(AF_INET, SOCK_STREAM)
cli.connect((host, port))
while 1:
    msg = input("Digite os id separados por espaços: ")
    #Verifies if the message is exit
    if msg == "exit":
        cli.send(msg.encode())
    msg = msg + " /x/ " + input("Digite a referencia: ")
    cli.send(msg.encode())