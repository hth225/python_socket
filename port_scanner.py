from socket import *
def scan(target_host,target_port):
    soc = socket(AF_INET,SOCK_STREAM)
    soc.connect(target_host,target_port)
    soc.send(target_port+'successfully connected')
    result = soc.recv(100)
    print('port'+target_port+''+target_host+'')