import machine
import time
from ultrasonic import *

p23 = machine.Pin(23, machine.Pin.OUT)
led = machine.Pin(4, machine.Pin.OUT, value=0)

buzzer = machine.PWM(p23)
buzzer.duty(0)

sensor = UltrasonicSensor(trigger_pin = 22, echo_pin = 2)

while True:
    #measuring the distance of object
    distance = sensor.distance_cm()
    print(distance)
    if distance is not None and  (distance < 10.00):
        buzzer.duty(200)
        led.on()
    else:
        buzzer.duty(0)
        led.off()
        
    time.sleep(1)
    
        