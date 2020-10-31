import keyboard
import serial
import time

# time.sleep(3)
# keyboard.press_and_release('left arrow')

arduino = serial.Serial('COM4', 115200, timeout=.1)
arduino2 = arduino.inWaiting()

while 1:
        data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
        data1=data.decode()

        if data1==str('Button1'):
            # print('doing action1')
            keyboard.press_and_release('right arrow')
            keyboard.press_and_release('right arrow')

        if data1==str('Button2'):
            # print('doing action2')
            keyboard.press_and_release('n')

        if data1==str('Button3'):
            # print('doing action2')
            keyboard.press_and_release('left arrow')
