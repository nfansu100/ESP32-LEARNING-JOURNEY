from machine import *
import time
from lcd_i2c import *
import dht

scl = Pin(23, Pin.OUT, Pin.PULL_UP)
sda = Pin(22, Pin.OUT, Pin.PULL_UP)
i2c = I2C(scl = scl, sda = sda, freq = 400000)
i2c_addr = 0x27
lcd = I2CLcd(i2c, i2c_addr)

def printStatement(row, col, message, clear=False):
    if clear:
        lcd.clear()
    lcd.move_to(col, row)
    lcd.putstr(message)
    
def CreatingDHT(pin_number):
    dht11 = dht.DHT11(pin_number)
    return dht11

dht11 = CreatingDHT(19)
    
while True:
    dht11.measure()
    temperature = dht11.temperature()
    humidity = dht11.humidity()
    m1 = "T = " + str(temperature) + "°C"
    m2 = "Hum = " + str(humidity) + "%"
    printStatement(0, 0, m1, clear=False)
    printStatement(1, 1, m2, clear=False)
    print(m1)
    print(m2)
    time.sleep(0.5)
    
    

    
