# Using the Servo

import machine
import pyb
from time import sleep_ms

#----------------------------------------------------------

def change_servo_angle(angle, time_ms):
    led_pin(1)
    servo.angle(angle, time_ms)
    sleep_ms(100)
    led_pin(0)

#----------------------------------------------------------

adc_pin = machine.Pin('Y4')
led_pin = machine.Pin('Y12')
led_pin(0)

servo = pyb.Servo(1)
adc = pyb.ADC(adc_pin)

#----------------------------------------------------------

servo_range = 180
slider_range = 256 # Sider: adc

zero_point = -90

previous_angle = round(adc.read() * (servo_range/slider_range) + zero_point)

while True:
    new_angle = round(adc.read() * (servo_range/slider_range) + zero_point)
    
    if new_angle != previous_angle:
        change_servo_angle(new_angle, 500)
        previous_angle = new_angle
        
        sleep_ms(500)
    
    else:
        pass