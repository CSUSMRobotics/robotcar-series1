import rospy
from std_msgs.msg import String
from gpiozero import Motor
import pygame


motor00 = Motor(5, 6) #front left wheel
motor01 = Motor(16, 12) #front right wheel
motor10 = Motor(20,21) #back left wheel
motor11 = Motor(19,26) #back right wheel

if __name__ == '__main__':
    motor00.forward()
