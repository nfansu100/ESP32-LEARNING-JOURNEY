import machine
import network
import socket
import time

#Creating the leds
greenLed = machine.Pin(2, machine.Pin.OUT, value=0)
blueLed = machine.Pin(22, machine.Pin.OUT, value=0)
yellowLed = machine.Pin(23, machine.Pin.OUT, value=0)
buzzer = machine.PWM(machine.Pin(15, machine.Pin.OUT))
buzzer.duty(0)

#Wifi Credentials
SSID = 'Wifi_Perso_2.4G'
PASSWORD = 'DCEF80DE08D5'

#Creating the Connection
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.scan()
if not sta.isconnected():
    sta.connect(SSID, PASSWORD)
    time.sleep(1)

while not sta.isconnected():
    print("Waiting to be connected on the WIFI")
    time.sleep(1)

print("AAh finally connected to the wifi")
print("ESP32 IP Address is : ", sta.ifconfig()[0])

def webPage():
    greenState = "ON" if greenLed.value() else "OFF"
    blueState = "ON" if blueLed.value() else "OFF"
    yellowState = "ON" if yellowLed.value() else "OFF"
    buzzerState = "ON" if buzzer.duty() else "OFF"
    
    html = """
       <!DOCTYPE html>
       <html lang="en">
       <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ESP32 WEB SERVER CONTROL</title>
        <style>
            body{background-color: hsl(0, 2%, 49%);font-family: sans-serif ;font-weight: bold;}
            h1{color: rgb(0, 255, 255) ;text-align: center;text-shadow: 2px 2px 5px red;}
            h1::first-letter{color: rgb(231, 163, 163) ;font-size: 2.5rem;}
            form{width: 70% ;margin: auto ;text-align: center;border: none ;padding: 15px ;border-radius: 15px ;background-color: hsla(0, 1%, 35%, 0.904);}
            form:hover{background-color: hsla(0, 1%, 70%, 0.904);box-shadow: 2px 2px 5px red;}
            form h2{color: rgb(0, 149, 255) ;font-weight: bold;font-style: italic ;}
            button{display: block ;margin: auto ;margin-bottom: 20px;font-size: 1.5rem;border: none ;
                  border-radius: 15px;padding: 10px 15px ;background-color: hsl(0, 2%, 75%); cursor: pointer ;}
            button:hover{background-color: hsl(0, 2%, 30%); color: white ;}
            button:active{background-color: hsl(0, 2%, 50%); }
            #descriptionContainer{border: none; margin: auto ; width: 70%; margin-top: 30px; padding: 15px; text-align: center;
                              background-color: white; border-radius: 15px; font-family:'Courier New';}
            #descriptionContainer:hover{box-shadow: 0px 0px 7px red;}
            #descriptionContainer .state{ color: red; font-weight: bold; font-size: 1.5rem;}
        </style>
        </head>
        <body>

        <h1>WELCOME TO MY ESP32 WEB SERVER MINI PROJECT</h1>

        <form id="myForm" name="myForm">
            <h2>CONTROLLING HARDWARE VIA INTERNET</h2>
            <button name="led" value="greenOn" type="submit">GREEN LED ON</button>
            <button name="led" value="greenOff" type="submit">GREEN LED OFF</button>
            <button name="led" value="blueOn" type="submit">BLUE LED ON</button>
            <button name="led" value="blueOff" type="submit">BLUE LED OFF</button>
            <button name="led" value="yellowOn" type="submit">YELLOW LED ON</button>
            <button name="led" value="yellowOff" type="submit">YELLOW LED OFF</button>
            <button name="buzzer" value="buzzerOn" type="submit">TURN ON BUZZER</button>
            <button name="buzzer" value="buzzerOff" type="submit">TURN OFF BUZZER</button>
        </form>
        <div id="descriptionContainer">
            <h3>Green Led is <span class="state">""" + greenState + """</span></h3>
            <h3>Blue Led is <span class="state">""" + blueState + """ </span></h3>
            <h3>Yellow Led is <span class="state">""" + yellowState + """ </span></h3>
            <h3>The buzzer is  <span class="state">""" + buzzerState + """ </span></h3>
        </div>
    </body>
    </html> """
    return html

# set up socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

#Waiting for the Client
while True:
    conn, addr = s.accept()
    print("Client is from address: ", addr)
    request = conn.recv(1024).decode("utf-8")
    print("Request is : ", request)
    
    if "/?led=greenOn" in request:
        greenLed.on()
    if "/?led=greenOff" in request:
        greenLed.off()
    if "/?led=blueOn" in request:
        blueLed.on()
    if "/?led=blueOff" in request:
        blueLed.off()
    if "/?led=yellowOn" in request:
        yellowLed.on()
    if "/?led=yellowOff" in request:
        yellowLed.off()
    if "/?buzzer=buzzerOn" in request:
        buzzer.duty(512)
    if "/?buzzer=buzzerOff" in request:
        buzzer.duty(0)  
    
    response = webPage()
    conn.sendall(response)
    conn.close()

#**********END OF PROGRAM************************
    