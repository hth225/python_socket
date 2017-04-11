from socket import *
from select import *
import sys

def socket_handler(ipaddr, port_num):
    size = 1024

    server = socket(AF_INET,SOCK_STREAM)
    server.bind((ipaddr, port_num))
    server.listen()
    print("Server started")
    print("Now waiting requests")
    input_list = [server]

    while True:
        read_socket, write_socket, error_socket = select(input_list, [], [])
        for req in read_socket:
            if req == server:
                client, addr = server.accept()
                print(addr, 'successfully connected', flush=True)
                input_list.insert(req, client)
            else:
                data = req.recv(size)
                if data != None:
                    print(req.getpeername(), 'send', flush=True)
                    req.send(data)
                elif data == None:
                    print(req.getpeername(), 'ended', flush=True)
                    req.close()
                    input_list.remove(req)

    server.close()


if __name__=='__main__':
    ipaddr = '10.156.146.177'
    port_num = 5600

    socket_handler(ipaddr, port_num)