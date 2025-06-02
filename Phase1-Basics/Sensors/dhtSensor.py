import dht
import machine
import time

sensor = dht.DHT11(machine.Pin(23))  # Use the correct GPIO pin
time.sleep(2)  # WAIT before reading!
sensor.measure()
print(sensor.temperature())
print(sensor.humidity())