import turtle as t
import random
# import colorgram
# colors = colorgram.extract("spots.jpg", 72)
t.colormode(255)
tum = t.Turtle()
# rgb_colors = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new = (r, g, b)
#     rgb_colors.append(new)
# print(rgb_colors)
colors = [(249, 232, 19), (199, 12, 31), (195, 67, 21), (213, 13, 9), (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59), (35, 33, 154), (240, 246, 251), (14, 205, 222), (18, 27, 60), (244, 42, 159), (71, 8, 51), (55, 24, 11), (228, 165, 9), (61, 200, 232), (16, 153, 16), (226, 19, 118), (98, 75, 9), (244, 44, 17), (66, 241, 159), (223, 140, 207), (248, 11, 9), (10, 97, 61), (5, 38, 33), (65, 221, 153), (238, 156, 218), (83, 75, 211), (79, 228, 237), (250, 8, 16), (244, 165, 157), (176, 179, 228), (26, 243, 180), (10, 80, 111), (11, 50, 246)]
tum.speed("fastest")
tum.penup()
tum.hideturtle()
tum.setheading(215)
tum.forward(350)
tum.setheading(0)

def direction():

    tum.setheading(90)
    tum.forward(50)
    tum.setheading(180)
    tum.forward(600)
    tum.setheading(0)


def colours():
    for i in range(12):
        tum.dot(20, random.choice(colors))
        tum.forward(50)
    direction()

for i in range(10):
    colours()



screen = t.Screen()
screen.screensize(10, 10)
screen.exitonclick()
