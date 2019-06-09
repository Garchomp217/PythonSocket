import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 4567))
s.listen(5)

while True:
    clientsocket, addres = s.accept()
    print(f"Connection from {addres} has been established!")
    clientsocket.send(bytes("welcome to the server!", "utf-8"))
