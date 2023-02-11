import socket
cl=socket.socket()
cl.connect(('localhost',9999))
print("client connected with the server ")
print("start the convo.........")
print()
while True:
    p=input("client :")
    cl.send(bytes(p,'utf-8'))
    if p=="exit":
        print("connection ended")
        break
    # cl.send(bytes(p,'utf-8'))
    name=cl.recv(1024).decode()
    if name=="exit":
        print("connection ended")
        break
    print("server :",name)
cl.close()


