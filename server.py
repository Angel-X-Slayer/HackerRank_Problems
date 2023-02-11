import socket
s=socket.socket()
print("[Server] created...")
s.bind(('localhost',9999))
s.listen()
print(f"waiting for connection from the client :")
c,addr=s.accept()
print("connection established ")
print()
while True:
    name=c.recv(1024).decode()
    if name=="exit":
        print("connection ended")
        break
    print("client :",name)
    k=input("server :")
    
    c.send(bytes(k,'utf-8'))
    if k=="exit":
        print("connection ended")
        break
    
    # c.send(bytes(k,'utf-8'))
c.close()

        
