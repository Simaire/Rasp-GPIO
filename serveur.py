import socket
import RPi.GPIO as GPIO
import time

global data

#Def gpio
GPIO.setmode(GPIO.BCM)
buzer = 22
GPIO.setwarnings(False)
GPIO.setup(buzer, GPIO.OUT)

#Def network
data = ""
host, port = ('', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Serveur start")


def connection():
    global data
    
    data = ""
    
    socket.listen()
    conn, address = socket.accept()
    print("Connection effectuer")
    
    data = conn.recv(1024)
    data = data.decode("utf8")

def acct():
    print("ok")
    GPIO.output(buzer, True);
    time.sleep(2)
    GPIO.output(buzer, False);
    time.sleep(2)



while True:
    connection()
    
    if data == "led":
        acct()
        
    if data == "ledcl":
        acct()
        acct()
        acct()
        acct()



conn.close()
socket.close()