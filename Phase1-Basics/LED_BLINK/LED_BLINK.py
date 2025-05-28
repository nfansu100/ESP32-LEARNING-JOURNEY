import machine
import time

class LED_CONTROLLER:
    
    #Constructor method
    def __init__(self, pin_number, active_state = True):
        self.led = machine.Pin(pin_number, machine.Pin.OUT)
        self.active = active_state
        
    #method for switching on led 
    def led_on(self):
        self.led.value(1)
    
    #method to turn off led
    def led_off(self):
        self.led.value(0)
    
    #method to toggle led state
    def led_toggle(self):
        self.led.value(not self.led.value())
        
    def value(self):
        return self.led.value()
        
    #blinking led n times
    def blinkingLed(self, number_of_times, on_delay, off_delay):
        for i in range(number_of_times):
            self.led.on()
            time.sleep(on_delay)
            self.led.off()
            time.sleep(off_delay)
        print("End of blinking ✌")
        
    def Blink(self, on_delay, off_delay):
        while True:
            self.led.value(1)
            time.sleep(on_delay)
            self.led.value(0)
            time.sleep(off_delay)
        
        
# am using 4, 2, 15


def traffic_light(redPin, bluePin, yellowPin):
    #instantiating led objects
    redLight = LED_CONTROLLER(redPin)
    blueLight = LED_CONTROLLER(bluePin)
    yellowLight = LED_CONTROLLER(yellowPin)
    
    while True:
        redLight.led_on()
        time.sleep(1)
        redLight.led_off()
        
        blueLight.led_on()
        time.sleep(1)
        blueLight.led_off()
        
        yellowLight.led_on()
        time.sleep(1)
        yellowLight.led_off()
        

#traffic_light(redPin=2, bluePin=15, yellowPin=4)


        
        
    
    


        
