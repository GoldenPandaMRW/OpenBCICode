from pyfirmata import Arduino, SERVO
from time import sleep
port = 'COM6'
pin = 10
board = Arduino(port)
board.digital[pin].mode = SERVO

def rotateServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

def triggerServo(is_open: bool):
    if is_open:
        for angle in range(180):
            rotateServo(pin, angle)
    else:
        for angle in range(180, 1, -1):
            rotateServo(pin, angle)
