import pigpio
import time

# Set the GPIO pin for PWM
gpio_pin = 18

# Set the PWM frequency (25 kHz)
pwm_frequency = 25000

# Set the PWM duty cycle (75%)
pwm_duty_cycle = 750000  # 75% of the range (0-1000000)

# Initialize the pigpio library
pi = pigpio.pi()

if not pi.connected:
    print("Unable to connect to pigpio daemon. Exiting.")
    exit()

try:
    # Set the PWM frequency and duty cycle using hardware_PWM
    pi.hardware_PWM(gpio_pin, pwm_frequency, pwm_duty_cycle)

    # Run the PWM for a certain duration (e.g., 10 seconds)
    time.sleep(10)

finally:
    # Stop PWM and cleanup
    pi.hardware_PWM(gpio_pin, 0, 0)  # Set duty cycle to 0 to stop PWM
    pi.stop()
