# What I found on github about similar robot projects

1. [bka](https://github.com/BKaiwalya/Autonomous-Tennis-Ball-Picking-Robot)

Project sponsored by Schaeffler Technologies AG & Co. KG
Development of an autonomous robot for picking tennis balls off a lawn tennis field.

Detection of tennis balls through Computer Vision and Machine Learning (Haar Cascading, CNN).

Traversal of the robot towards the co-ordinate of ball by closed loop locomotion through gyroscope & rotary encoders.

The microcontroller used is ARM Cortex M4 (STM32 Nucleo-64 F446RE): $15

Wireless data transmission to the robot via communication protocols Zigbee and Bluetooth v2.0.

Sensors: Camera, gyroscope, proximity, rotary encoders.

Software development in C: 12.7%, Python 3: 87.3%

2. [fetch-it](https://github.com/nalindas9/fetch-it)

Operating System - Ubuntu 18.04

Programming language - C++ 11/14

Open Source Libraries - OpenCV (Apache License)

Build System - CMake

ROS Version - Melodic

Simulation Environment - Gazebo

Code Coverage - Coveralls

Automated Unit Testing - Travic CI

Version Control - Git & Github

3. [dasa](https://github.com/EricDinging/DASA)

We will design and build a small device that will consist of a container for storage and a rotor at the front that will spin balls into the container when detected. The device will maneuver a defined range (borders marked by mini walls) and automatically detect tennis balls using a Raspberry Pixy camera, IR sensor, and two wheel drive, and by running OpenCV libraries on a Raspberry Pi. Once storage has reached maximum capacity, it will return to a defined destination where someone can retrieve the balls. A Nucleo controller and motors will be used to enable movement.

4. [tenezbot](https://github.com/Pruthvi-Sanghavi/TenezBot)
**software only**

We propose to design "TenezBot" a tennis ball collecting robot, by incorporating high-quality software engineering practices for Acme Robotics. "TenezBot" package is a complete software package which will be integrated in their new line of products. Tennis is played widely throughout the world. Mastering this game requires a good amount of time. But with that comes the demanding task of collecting hundreds of tennis balls scattered across the court, which becomes really frustrating after a tiring practice session. Thus we are aiming to develop “TenezBot” a robot which can detect ball, its position in the environment, reach out to the ball and collect it in a sac using a custom made collector attached with the TurtleBot base platform. The robot would use vision camera for vision and depth measurement. Path planning algorithms are used to reach out to the balls so that the task performance is optimum.

language: C++: 95.8%, Cmake: 4.2%

5. [tenitsu](https://github.com/skyzh/tenitsu)

A robot automatically finds and fetches tennis balls on the ground. Use OpenCV on Android for computer vision. Final project for SJTU ME116 "IntroME".

6. [IFRoS](https://github.com/IFRoS-ELTE/ball_picking_project)
**big robot**

To create inputs for GMapping (2D SLAM), the robot's odometry gets calculated using Direct Lidar Inertial Odometry, which uses LiDAR and IMU data. There is unwanted drift in z-direction of the odometry because of unknown reasons, so it needs to be set to a static value to be usable. Since GMapping is a 2D SLAM algorithm, the LiDAR point cloud gets downsampled to a 2D laser scan. Based on the created 2D map, the mobile base can either autonomously explore the area using frontier exploration or approach a 3D world coordinate given to it by the ball detection module. For controlling the robot, move_base receives navGoals and sends twist messages to the scout_base, which is responsible for communicating with the physical robot through CAN.

language: Shell

7. [sameday85](https://github.com/sameday85/tennis)

language: C++

Hardware (total cost around $480)

Raspberry Pi 3 B+

Pi Camera with long cable

A robot car with structure frame

A heavy duty DC motor()

Three motor controllers (L298N)

Two ultra sound sensors

Three leds (R,G and B)

An active buzzer

Two buttons

Wires

Breadboard

Resistorsp c z

Misc (Power Banks etc)
