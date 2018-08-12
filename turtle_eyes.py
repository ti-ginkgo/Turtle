import sys
import os
import logging
import argparse
import time
from turtle import *
from datetime import datetime

points = {'c': (0, 0), 'tl': (-660, 350), 'bl': (-660, -400), 'tr': (660, 350), 'br': (660, -400)}

def main(args):
    turtle = Turtle()
    screen = Screen()
    screen.setup(width=1440, height=855, startx=None, starty=None)
    turtle.hideturtle()
    turtle.penup()

    if args.debug:
        turtle.speed(1)
        print(screen.window_height())
        print(screen.window_width())
        # time.sleep(3)

    turtle.goto(points['c'])
    turtle.pendown()
    turtle.color('red', 'red')
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(0, 0)


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--debug', type=bool, default=False)
    parser.add_argument('--logging', type=bool, default=False)

    return parser.parse_args(argv)


if __name__ == "__main__":
    print("start time:", datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    main(parse_arguments(sys.argv[1:]))

    print("end time:", datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
