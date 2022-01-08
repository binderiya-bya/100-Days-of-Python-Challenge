import turtle as t
import random

# import colorgram as col
#
# rgb_colors = []
# colors = col.extract('Damien-Hirst-Veil-Paintings-Kew-ca-2020.jpg', 100)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     combo = (r, b, g)
#     rgb_colors.append(combo)

color_list = [(235, 234, 235), (187, 105, 166), (132, 187, 173), (59, 139, 103), (135, 159, 177), (66, 104, 126), (169, 63, 149), (149, 54, 84), (81, 131, 152), (26, 127, 52), (204, 219, 212), (147, 76, 64), (216, 212, 206), (208, 213, 218), (77, 159, 150), (15, 89, 39), (181, 163, 152), (205, 152, 198), (124, 45, 35), (130, 29, 37), (194, 76, 86), (77, 19, 30), (167, 192, 204), (185, 98, 86), (75, 34, 24), (160, 211, 204), (95, 173, 119), (35, 56, 85), (205, 192, 183), (182, 208, 188), (27, 36, 62), (80, 26, 80), (211, 178, 182), (29, 89, 79)]

tim = t.Turtle()
t.colormode(255)


def start_position():
    tim.hideturtle()
    tim.penup()
    tim.goto(-230, -230)
    tim.pendown()

def draw_spots():
    for i in range(10):
        color = random.choice(color_list)
        tim.dot(20, color)
        tim.penup()
        tim.forward(50)


def next_row():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading(0)


def almost_damien():
    tim.speed("fastest")
    start_position()
    draw_spots()
    n = 0
    while n < 9:
        next_row()
        draw_spots()
        n += 1


almost_damien()

screen = t.Screen()
screen.exitonclick()
