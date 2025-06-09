import machine
import time
import network
import socket

# #Creating Led objects
greenLed = machine.Pin(13, machine.Pin.OUT)
blueLed = machine.Pin(22, machine.Pin.OUT)
yellowLed = machine.Pin(23, machine.Pin.OUT)

#Wifi Credentials
SSID = 'Wifi_Perso_2.4G'
PASSWORD = 'DCEF80DE08D5'

#Connecting to the wifi
sta = network.WLAN(network.STA_IF)
sta.active(True)
if not sta.isconnected():
    sta.connect(SSID, PASSWORD)
    time.sleep(1)

while not sta.isconnected():
    print("Connecting to the WIFI")
    time.sleep(1)

print("Finally Connected to the WIFI")
print("IP Address is : ", sta.ifconfig()[0])

def webPage():
    greenState = "ON" if greenLed.value() else "OFF"
    blueState = "ON" if blueLed.value() else "OFF"
    yellowState = "ON" if yellowLed.value() else "OFF"
    
    html = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Controlling the 3 Leds via webpage</title>
                <meta name="Viewport" content="width=device-width, initial-scale=1.0">
                <style></style>
            </head>
            <body>
                
                <form>
                    <button name="led" value="greenOn" type="submit">GREEN LED ON</button>
                    <button name="led" value="greenOff" type="submit">GREEN LED OFF</button>
                    <button name="led" value="blueOn" type="submit">BLUE LED ON</button>
                    <button name="led" value="blueOff" type="submit">BLUE LED OFF</button>
                    <button name="led" value="yellowOn" type="submit">YELLOW LED ON</button>
                    <button name="led" value="yellowOff" type="submit">YELLOW LED OFF</button>
                </form>
                
                <h1>ESP32 Web Base Control Leds</h1>
                <h3>Green led is """ + greenState + """</h3>
                <h3>Blue led is """ + blueState + """</h3>
                <h3>Yellow led is """ + yellowState + """</h3>
            </body>
        </html> """
    return html

#Socket set up
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr) # 80 = HTTP
s.listen(1)

#Waiting for Client Responses


while True:
    
    conn, addr = s.accept()
    print("Client is from address: ", addr)
    request = conn.recv(1024).decode("utf-8")
    print("REquest: ", request)

    if "/?led=greenOn" in request:
        greenLed.on()
    elif "/?led=greenOff" in request:
        greenLed.off()
    elif "/?led=blueOn" in request:
        blueLed.on()
    elif "/?led=blueOff" in request:
        blueLed.off()
    elif "/?led=yellowOn" in request:
        yellowLed.on()
    elif "/?led=yellowOff" in request:
        yellowLed.off()

    response = webPage()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
