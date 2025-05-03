from buildhat import Motor
from bluedot import BlueDot
import time

dot = BlueDot()
orders = []
motor_A = Motor('A')
motor_B = Motor('B')


def direction(pos):
    orders.append(pos)


def move(pos):
    if pos.top:
        motor_B.run_to_position(0)
        motor_A.start(-100)
    elif pos.bottom:
        motor_B.run_to_position(0)
        motor_A.start(100)
    elif pos.left:
        motor_B.run_to_position(-15)
        motor_A.start(-100)
    elif pos.right:
        motor_B.run_to_position(15)
        motor_A.start(100)


def stop():
    motor_A.stop()


dot.when_pressed = move
dot.when_released = stop
dot.when_moved = direction
list_length = len(orders)-1
while True:
    if len(orders) > 0:
        move(orders[-1])
        orders = []
    time.sleep(0.3)
