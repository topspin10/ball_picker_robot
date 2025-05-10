#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
controller = Controller()
motor_1 = Motor(Ports.PORT1, False)
motor_2 = Motor(Ports.PORT2, False)
motor_3 = Motor(Ports.PORT3, False)
motor_4 = Motor(Ports.PORT4, False)



# generating and setting random seed
def initializeRandomSeed():
    wait(100, MSEC)
    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000
    systemTime = brain.timer.system() * 100
    urandom.seed(int(xaxis + yaxis + zaxis + systemTime)) 
    
# Initialize random seed 
initializeRandomSeed()

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
# 	Author:       VEX
# 	Created:
# 	Description:  VEXcode IQ Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
# GOAL!!! code robot to follow the remote. in: xy. out: movement.
def rad_to_deg(rad):
    return (rad/math.pi)*180

def deg_to_rad(deg):
    return (deg/180)*math.pi

def car_to_pol(x, y):
    d = math.sqrt(x**2+y**2)
    a = math.atan2(x, y)
    return d, rad_to_deg(a)

def spin_motors(d, a, b):
    motor_1.set_velocity(d*math.cos(deg_to_rad(a-45)) + b)
    motor_1.spin(FORWARD)
    motor_2.set_velocity(d*math.cos(deg_to_rad(a-135)) + b)
    motor_2.spin(FORWARD)
    motor_3.set_velocity(d*math.cos(deg_to_rad(a+135)) + b)
    motor_3.spin(FORWARD)
    motor_4.set_velocity(d*math.cos(deg_to_rad(a+45)) + b)
    motor_4.spin(FORWARD)

while True:
    d, a = car_to_pol(controller.axisC.position(), controller.axisD.position())
    a = a - brain_inertial.heading()
    spin_motors(d, a, controller.axisB.position())
