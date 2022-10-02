import cv2,socket,pickle,struct

#socket create
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name=socket.gethostname()
host_ip=socket.gethostbyname(host_name)
print("HOST IP:",host_ip)
port=8000
socket_address=(host_ip,port)

#Socket BIND
server_socket.bind(socket_address)

#Socket listen
server_socket.listen()
print("Listening at:",socket_address)

#socket accept
client_socket,addr=server_socket.accept()
print("Got connection from:",addr)


data=b""
payload_size=struct.calcsize("Q")
while True:
    while len(data)<payload_size:
        packet=client_socket.recv(4*1024)#4K
        if not packet:break
        data+=packet
    packed_msg_size=data[:payload_size]
    data=data[payload_size:]
    msg_size=struct.unpack("Q",packed_msg_size)[0]

    while len(data)<msg_size:
        data+=client_socket.recv(4*1024)
    frame_data=data[:msg_size]
    data=data[msg_size:]
    frame=pickle.loads(frame_data)
    cv2.imshow("Received",frame)
    key=cv2.waitKey(1)&0xFF
    if key==ord('q') :
        break
client_socket.close()
