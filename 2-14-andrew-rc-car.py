from bluedot import BlueDot
from signal import pause
import time
import pigpio

dot = BlueDot()
orders = []
# Set the GPIO pin for PWM
gpio_pin = 18

# Set the PWM frequency (25 kHz)
pwm_frequency = 60

# Initialize the pigpio library
pi = pigpio.pi()

if not pi.connected:
    print("Unable to connect to pigpio daemon. Exiting.")
    exit()

def figure(pos):
    orders.append(pos)
def move(pos):
    if pos.top:
        # Set the PWM frequency and duty cycle using hardware_PWM
        pi.hardware_PWM(gpio_pin, pwm_frequency, 9*10000)
    elif pos.bottom:
        # Set the PWM frequency and duty cycle using hardware_PWM
        pi.hardware_PWM(gpio_pin, pwm_frequency, 9*10000)
    elif pos.left:
        # Set the PWM frequency and duty cycle using hardware_PWM
        pi.hardware_PWM(gpio_pin, pwm_frequency, int(5.88*10000))
    elif pos.right:
        # Set the PWM frequency and duty cycle using hardware_PWM
        pi.hardware_PWM(gpio_pin, pwm_frequency, int(11.76*10000))

# def stop():
    

dot.when_pressed = move
# dot.when_released = stop
dot.when_moved = figure
list_length = len(orders)-1

while True:
    if len(orders)>0:
        move(orders[-1])
        orders = []
    time.sleep(0.3)

# pause()
