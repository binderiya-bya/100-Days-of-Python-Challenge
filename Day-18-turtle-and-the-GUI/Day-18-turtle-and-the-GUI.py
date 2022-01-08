import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color('red')
# timmy_the_turtle.forward(100)

# Challenge 1: draw a square
# for i in range(4):
#     tim.forward(100)
#     tim.left(90)

# Challenge 2: draw a dashed line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Challenge 3: Draw shapes up to 11 sides

# colors = ['red', 'blue', 'green', 'yellow', 'orange', 'teal', 'gray', 'pink', 'purple', 'navy']


# def draw_shape(corner):
#     color = random.choice(colors)
#     tim.color(color)
#     for i in range(corner):
#         angle = 360/corner
#         tim.forward(100)
#         tim.right(angle)
#
#
# for num_sides in range(3, 11):
#     draw_shape(corner=num_sides)

# Challenge 4: draw a random walk using a random color from rbg spectrum

# directions = [0, 90, 180, 270]
#
#
# def random_color():
#     r = random.randint(0, 255)
#     b = random.randint(0, 255)
#     g = random.randint(0, 255)
#     return r, b, g
#
#
# def random_walk():
#     direction = random.choice(directions)
#     tim.color(random_color())
#     tim.speed('fastest')
#     tim.forward(10)
#     tim.setheading(direction)
#
#
# for i in range(1000):
#     random_walk()


# Challenge 5: Draw a Spirograph

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return r, b, g


def draw_spirograph(size_of_gap):
    for i in range(round(360 / size_of_gap)):
        tim.color(random_color())
        tim.speed("fastest")
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()
