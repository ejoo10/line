from display import *

def draw_line(x0, y0, x1, y1, screen, color):
    if abs(x1 - x0) > abs(y1 - y0):
        if x1 > x0:
            draw_linex(x0, y0, x1, y1, screen, color)
        else:
            draw_linex(x1, y1, x0, y0, screen, color)
    else:
        if y1 > y0:
            draw_liney(x0, y0, x1, y1, screen, color)
        else:
            draw_liney(x1, y1, x0, y0, screen, color)

def draw_linex(x0, y0, x1, y1, screen, color):
    A = abs(y1 - y0)
    a = y1 - y0
    k = 1 if A == a else -1
    B = x1 - x0
    Z = 2 * B - A
    y = y0
    for x in range(x0, x1):
        plot(screen, color, x, y)
        if Z > 0:
            y += k
            Z -= 2 * B
        Z += 2 * A

def draw_liney(x0, y0, x1, y1, screen, color):
    B = y1 - y0
    A = abs(x1 - x0)
    a = x1 - x0
    k = 1 if A == a else -1
    Z = 2 * B - A
    x = x0
    for y in range(y0, y1):
        plot(screen, color, x, y)
        if Z > 0:
            x += k
            Z -= 2 * B
        Z += 2 * A
