import socket
import re
import os

host = '192.168.1.50' #PC's ip
port = 8080 #Default port number for the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(1)

while True:
    csock, caddr = sock.accept()
    print "Connection from : " + `caddr`
    req = csock.recv(1024)
    print req

    match = re.match('GET /lock\?y=true\sHTTP/1',req)
    if match:
        csock.sendall("HTTP/1.0 200 OK\r\n")
        os.system("xflock4")
    else:
        print "Returning 404"
        csock.sendall("HTTP/1.0 404 Not Found\r\n")
    csock.close()
