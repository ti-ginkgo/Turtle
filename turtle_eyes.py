import sys
import os
import argparse
import time
from turtle import *
from logging import getLogger, StreamHandler, FileHandler, DEBUG
from datetime import datetime

points = {'c': (0, 0), 'tl': (-660, 350), 'bl': (-660, -400), 'tr': (660, 350), 'br': (660, -400)}
keys = ['c', 'tl', 'bl', 'tr', 'br']

def move(turtle, key):
    turtle.clear()
    turtle.penup()
    turtle.goto(points[key])
    turtle.pendown()
    turtle.color('white', 'red')
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    time.sleep(1)


def main(args):
    turtle = Turtle()
    screen = Screen()
    screen.setup(width=1440, height=855, startx=None, starty=None)
    turtle.hideturtle()
    turtle.pendown()
    turtle.write('Start', font=('Arial', 20, 'normal'))
    turtle.penup()

    if args.debug:
        time.sleep(1)
        turtle.speed(1)
        print(screen.window_height())
        print(screen.window_width())

    if args.logging:
        logger = getLogger(__name__)
        handler = FileHandler(datetime.now().strftime('%Y.%m.%d')+'.log')
        handler.setLevel(DEBUG)
        logger.setLevel(DEBUG)
        logger.addHandler(handler)
        logger.propagate = False

    for key in keys:
        if args.logging:
            logger.debug(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        move(turtle, key)
        time.sleep(3)


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--debug', type=bool, default=False)
    parser.add_argument('--logging', type=bool, default=False)

    return parser.parse_args(argv)


if __name__ == '__main__':
    print('start time:', datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    main(parse_arguments(sys.argv[1:]))
    print('end time:', datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
