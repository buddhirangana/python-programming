import socket
port = 1236
address = '127.0.0.1'
BUF_SIZE = 15
HEADER_SIZE = 10

# create a socket object name 'con'
con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((address, port))

message = "Hello!This is a longer message than the available buffer size of 15bytes"

con.send(bytes("{msg_length:{hs}d}".format(msg_length=len(message),hs=HEADER_SIZE) + message,"utf-8"));

message = ""    #Clear buffer to receive the data from server
newmsg = True
while True:
    data = con.recv(BUF_SIZE)
    if newmsg:
        msg_length = int(data[:HEADER_SIZE].decode("utf-8"))
        #print(msg_length)
        message+=data[HEADER_SIZE:].decode("utf-8")
        newmsg = False
    else:
        message+=data.decode("utf-8")
        
    #print(len(full_msg))
    if(len(message)>=msg_length):
        #print("full message received")
        print(message)
        break

#If I need to send another message before closing connection, it can be done here.
    
con.close()

