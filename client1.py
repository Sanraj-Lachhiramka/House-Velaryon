import socket,cv2,pickle,struct
# create socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip='10.16.160.110'
port=9999
client_socket.connect((host_ip,port))#a tuple
data=b""
payload_size=struct.calcsize("Q")

print("HOST IP:",host_ip)
port=8000
socket_address=(host_ip,port)

vid=cv2.VideoCapture(0)
    
while True:
    img,frame=vid.read()
    a=pickle.dumps(frame)
    message=struct.pack("Q",len(a))+a
    client_socket.sendall(message)
    cv2.imshow('Transmitting video',frame)
    key=cv2.waitKey(1) & 0xFF
    if key==ord('q'):
        client_socket.close()