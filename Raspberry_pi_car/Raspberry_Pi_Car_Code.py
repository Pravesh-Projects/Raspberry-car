import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(23,gpio.OUT)
gpio.setup(24,gpio.OUT)
gpio.output(24,True)
gpio.output(23,True)
time.sleep(0.8)
gpio.output(24,True)
gpio.output(23,False)
time.sleep(0.2)
gpio.output(24,True)
gpio.output(23,True)
time.sleep(0.3)
gpio.output(24,True)
gpio.output(23,False)
time.sleep(0.855)
gpio.output(24,True)
gpio.output(23,True)
time.sleep(1)
gpio.output(24,False)
gpio.output(23,False)
time.sleep(0.5)




