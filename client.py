import socket

host, port = ('192.168.1.40', 5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((host, port))

    data = "led"
    data = data.encode("utf8")
    socket.sendall(data)

except ConnectionRefusedError:
    print("Connection imposible")

except:
    print("error")
finally:
    socket.close()
