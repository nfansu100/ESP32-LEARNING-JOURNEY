from machine import *
import time
from ultrasonic import *

def creating_ultra_sensor(trigger_pin, echo_pin):
    sensor = UltrasonicSensor(trigger_pin, echo_pin)
    return sensor
    
# def creating_buzzer(pin_number):
#     pin = Pin(pin_number, Pin.OUT)
#     buzzer = PWM(pin)
#     buzzer.duty(0)

yellowLed = Pin(5, Pin.OUT, value = 0)
redLed = Pin(18, Pin.OUT, value = 0)
greenLed = Pin(17, Pin.OUT, value = 0)
buzzer = PWM(Pin(19, Pin.OUT))
buzzer.duty(0)
ultraSensor = creating_ultra_sensor(23, 22)

while True:
    distance = ultraSensor.distance_cm()
    if distance is not None and (distance <= 10):
        yellowLed.on()
        redLed.off()
        greenLed.off()
        buzzer.duty(200)
    elif distance is not None and (distance > 10 and distance <= 28):
        yellowLed.off()
        redLed.on()
        greenLed.off()
        buzzer.duty(0)
    else:
        yellowLed.off()
        redLed.off()
        greenLed.on()
        buzzer.duty(0)
    print("The distance is " + str(distance) + " cm")
    time.sleep(0.7)
        
