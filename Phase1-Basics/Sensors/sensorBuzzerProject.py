import machine
from ultrasonic import *
import time

trigger = machine.Pin(22, machine.Pin.OUT)
echo = machine.Pin(15, machine.Pin.IN)
led = machine.Pin(23, machine.Pin.OUT, value = 0)

mySensor = UltrasonicSensor(trigger, echo)
p2 = machine.Pin(2, machine.Pin.OUT, value = 0)

buzzer = machine.PWM(p2)
buzzer.duty(0)


while True:
    distance = mySensor.distance_cm()
    print("The distance is: " + str(distance) + " cm.")
    if distance is not None and (distance <= 10):
        led.on()
        buzzer.duty(512)
    else:
        led.off()
        buzzer.duty(0)
    
    time.sleep(0.5)
    


