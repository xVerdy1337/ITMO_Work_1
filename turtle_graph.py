from turtle import *
from math import sqrt

scale = 10
tracer(0)

variant = int(input('1 или 2\n'))

if variant == 1:
    for i in range(8):
        forward(10 * scale)
        right(45)
elif variant == 2:
    for i in range(4):
        forward(10 * scale)
        left(90)

    goto(0, 10 * scale)
    goto(10 * scale, 0)
    goto(10 * scale, 10 * scale)
    goto(0, 10 * scale)

    left(45)
    forward(sqrt(2) * 5 * scale)
    right(90)
    forward(sqrt(2) * 5 * scale)

    goto(0, 0)
else:
    print('Такого варианта нет!')

update()
done()
