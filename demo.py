import logging
from datetime import datetime
from turtle import *

def main():
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()


if __name__ == '__main__':
    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    main()
    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
