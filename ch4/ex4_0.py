'''
4.3 Exercises
The following is a series of exercises using TurtleWorld. They are meant to be fun, but they
have a point, too. While you are working on them, think about what the point is.
The following sections have solutions to the exercises, so don’t look until you have finished
(or at least tried).
1. Write a function called square that takes a parameter named t, which is a turtle. It
should use the turtle to draw a square.
Write a function call that passes bob as an argument to square, and then run the
program again.
2. Add another parameter, named length, to square. Modify the body so length of the
sides is length, and then modify the function call to provide a second argument. Run
the program again. Test your program with a range of values for length.
3. Make a copy of square and change the name to polygon. Add another parameter
named n and modify the body so it draws an n-sided regular polygon. Hint: The
exterior angles of an n-sided regular polygon are 360/n degrees.
4. Write a function called circle that takes a turtle, t, and radius, r, as parameters and
that draws an approximate circle by calling polygon with an appropriate length and
number of sides. Test your function with a range of values of r.
Hint: figure out the circumference of the circle and make sure that length * n =
circumference.
5. Make a more general version of circle called arc that takes an additional parameter
angle, which determines what fraction of a circle to draw. angle is in units of degrees,
so when angle=360, arc should draw a complete circle.
'''

import turtle
import math

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

# bob = turtle.Turtle()
# square(bob, 100)

def polygon(t, n, length):
    angle = 360 / n
    for j in range(n):
        t.fd(length)
        t.lt(angle)
# alice = turtle.Turtle()
# polygon(alice, 6, 100)

# turtle.mainloop()

def circle(t, r):
    l = 2 * math.pi * r
    n = 50
    length = l / n
    polygon(t, n, length)

def circle_gen(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)

# cathy = turtle.Turtle()
# circle_gen(cathy, 100)

def arc(t, r, angle):
    larc = 2 * math.pi *r * angle / 360
    n = int(larc / 3) + 10
    step_num = larc / n
    step_ang = angle / n

    for k in range(n):
        t.fd(step_num)
        t.lt(step_ang)

david = turtle.Turtle()
arc(david, 100, 540)

turtle.mainloop()