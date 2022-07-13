import socket
port = 1234
address = "127.0.0.1"
BUF_SIZE = 1024

#create a socket object name 'server'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((address,port))
server.listen(5)
print("Listening..")
while True:
    con,addr = server.accept()
    print("Connection Address is:" ,addr)
    data = con.recv(BUF_SIZE)
    print(data.decode("utf-8")
    con.send(data) 
