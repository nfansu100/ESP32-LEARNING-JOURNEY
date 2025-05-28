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
        
    #blinking led n times
    def blinkingLed(self, number_of_times, on_delay, off_delay):
        for i in range(number_of_times):
            self.led.on()
            time.sleep(on_delay)
            self.led.off()
            time.sleep(off_delay)
        print("End of blinking ✌")

myLed = LED(2)

        
