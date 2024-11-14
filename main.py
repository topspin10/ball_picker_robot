#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
motor_7 = Motor(Ports.PORT7, False)
motor_12 = Motor(Ports.PORT12, True)
frontleft = Bumper(Ports.PORT3)
frontright = Bumper(Ports.PORT4)
rightfront = Bumper(Ports.PORT9)
rightback = Bumper(Ports.PORT10)



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

sides = []

def one_of_my_finest_creations_3():
    brain.screen.clear_row(1)
    brain.screen.set_cursor(brain.screen.row(), 1)
    brain.screen.print("Phase 3: TURN DA CORNER")
    motor_7.spin_for(REVERSE, 1, TURNS)
    motor_12.spin_for(REVERSE, 1, TURNS)
    motor_12.spin_for(FORWARD, 1, TURNS)

def one_of_my_finest_creations_2():
    global sides
    brain.screen.clear_row(1)
    brain.screen.set_cursor(brain.screen.row(), 1)
    brain.screen.print("Phase 2: FOLLOW DA FENCE")
    # rename number and myvariable, give functional names
    # it looks like the 2 variables can be merged into 1
    sides.append = ('motor_7.position(TURNS) * 19.5')
    # AND works because machine will turn automatically.
    while not (frontleft.pressing() and frontright.pressing()):
        motor_7.spin(FORWARD)
        motor_12.spin(FORWARD)

def one_of_my_finest_creations_1():
    brain.screen.clear_row(1)
    brain.screen.set_cursor(brain.screen.row(), 1)
    brain.screen.print("Phase 1: FIND DA FENCE")
    while not rightfront.pressing():
        motor_7.set_velocity(50, PERCENT)
        motor_12.set_velocity(40, PERCENT)
        motor_7.spin(FORWARD)
        motor_12.spin(FORWARD)
        if frontright.pressing():
            motor_7.spin_for(REVERSE, 1, TURNS)
            motor_12.spin_for(REVERSE, 1, TURNS)
            motor_12.spin(FORWARD)
            wait(0.2, SECONDS)
        

def when_started1():
    global sides
    # switch to python
    # open a github account and make sure to be able to login anywhere (accessible 2 factor authentication)
    # see if you can implement each phase as custom blocks
    for repeat_count in range(4):
        one_of_my_finest_creations_1()
        one_of_my_finest_creations_2()
        one_of_my_finest_creations_3()
        brain.screen.clear_row(1)
    brain.screen.set_cursor(brain.screen.row(), 1)
    brain.screen.print(sides)
    brain.screen.print("cm ")

when_started1()
