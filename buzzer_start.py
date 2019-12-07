from gpiozero import Buzzer, OutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
from math import pi, sin


factory = PiGPIOFactory(host='pi912.local')
buzzer = Buzzer(4, active_high=False, pin_factory=factory)

buzzer.value=0;
sleep(2)
# buzzer.on()
# sleep(2)
# buzzer.off()
#
# print(buzzer.pin)
# print(buzzer.is_active)
# # buzzer.off()
# print(buzzer.is_active)

step = 0.1

while True:
    x = 0
    if x >= pi :
        x = 0
    buzzer.value = x
    sleep(1)
    x = x + step
    print(buzzer.value)
    print(buzzer.pin)
    print(buzzer.is_active)
