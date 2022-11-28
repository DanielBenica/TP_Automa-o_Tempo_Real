from socket import *
host = gethostname()
port = 51511
cli = socket(AF_INET, SOCK_STREAM)
cli.connect((host, port))
while 1:
    msg = input("Digite o id e a referência: ")
    cli.send(msg.encode())