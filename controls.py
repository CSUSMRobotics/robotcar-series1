import time
import pygame
from pygame.locals import *

#functions for motor movement
def mForward(but):
    pressed = True
    while pressed:
        print("ZZZZZZZZZZZZZZZZ")
        for event in pygame.event.get():
            if event.type == JOYBUTTONUP:
                pressed = False
        #active.forward()

def mBackwards(but):
    pressed = True
    while pressed:
        print("HHHHHHHHHHHH")
        for event in pygame.event.get():
            if event.type == JOYBUTTONUP:
                pressed = False
        #active.forward()



if __name__ == '__main__':
    pygame.init()
    pygame.joystick.init()
    joysticks = pygame.joystick.Joystick(0)
    print(joysticks)
        
    #axes = joysticks.get_numaxes(x)

    done = False
    while not done:
        for event in pygame.event.get():
            #print(pygame.event)
            if event.type == JOYBUTTONDOWN:
                if event.button == 0:
                    #print(joysticks.get_button(0))
                    print("0?!")
                    mForward(0)
                if event.button == 1:
                    print(1)
                    mBackwards(1)
                if event.button == 2:
                    print(2)
                if event.button == 3:
                    print(3)
                if event.button == 4:
                    print(4)
                if event.button == 5:
                    print(5)
                if event.button == 6:
                    print(6)
                if event.button == 7:
                    print(7)
                if event.button == 8:
                    print(8)
                if event.button == 9:
                    print(9)
                if event.button == 10:
                    print(10)
                if event.button == 11:
                    print(11)
                if event.button == 12:
                    print(12)
                if event.button == 13:
                    print(13)
                if event.button == 14:
                    print(14)
                    mForward(14)
                if event.button == 15:
                    print(15)
                    done = True
                if event.button == 16:
                    print(16)
            elif event.type == JOYBUTTONUP:
                    if event.button == 0:
                        #print(joysticks.get_button(0))
                        print("0?!")
                    #mForward(0)
                    if event.button == 1:
                        print("!1")
                    if event.button == 2:
                        print("!2")
                    if event.button == 3:
                        print("!3")
                    if event.button == 4:
                        print("!4")
                    if event.button == 5:
                        print("!5")
                    if event.button == 6:
                        print("!6")
                    if event.button == 7:
                        print("!7")
                    if event.button == 8:
                        print("!8")
                    if event.button == 9:
                        print("!9")
                    if event.button == 10:
                        print("!10")
                    if event.button == 11:
                        print("!11")
                    if event.button == 12:
                        print("!12")
                    if event.button == 13:
                        print("!13")
                    if event.button == 14:
                        print("!14")
                        mForward(14)
                    if event.button == 15:
                        print("!15")
                        done = True
                    if event.button == 16:
                        print(16)
            elif event.type == JOYAXISMOTION:
                if event.axis == 0:
                    joy = joysticks.get_axis(0)
                    if joy >= 0.20:
                        print("BB")
                    elif joy <= -0.20:
                        print("YY")
                if event.axis == 1:
                    joy = joysticks.get_axis(1)
                    if joy >= 0.20:
                        print("AA")
                    elif joy <= -0.20:
                        print("ZZ")
                if event.axis == 2:
                    joy = joysticks.get_axis(2)
                    if joy >= 0.20:
                        print("CC")
                    elif joy <= -0.20:
                        print("XX")
                if event.axis == 3:
                    joy = joysticks.get_axis(3)
                    if joy >= 0.20:
                        print("DD")
                    elif joy <= -0.20:
                        print("WW")
                if event.axis == 4:
                    joy = joysticks.get_axis(4)
                    if joy >= 0.90:
                        print("clicked")
                if event.axis == 5:
                    joy = joysticks.get_axis(5)
                    if joy >= 0.60:
                        print("clicked")
            
                
'''
    for i in range(axes):
        axis = joystick.get_axis(i)
        print("Axis" + {i} + "value: " + {axis:6.3})
        

        buttons = joystick.get_numbuttons()
        print("Number of buttons:" + {buttons})
        for i in range(buttons):
            button = joystick.get_button(i)
            print("Button" + {i:2} + "value:" + {button})
                

            hats = joystick.get_numhats()
            print("Number of hats:" + {hats})

            # Hat position. All or nothing for direction, not a float like
            # get_axis(). Position is a tuple of int values (x, y).
            for i in range(hats):
                hat = joystick.get_hat(i)
                print("Hat" + {i} + "value:" + {str(hat)})
'''


    