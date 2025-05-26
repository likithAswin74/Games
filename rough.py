# import turtle as t
# import random
# timmy = t.Turtle()

# random shapes!!

# def get_angles(num):
#     angle = 360 / num
#     for _ in range(num):
#         timmy.forward(100)
#         timmy.right(angle)
# for i in range(3, 11):
#     get_angles(i)


# colour walk!!

# t.colormode(255)
# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
#
# timmy.speed("fastest")
# direction = [0, 90, 180, 270]
# for i in range(200):
#     timmy.width(10)
#     timmy.forward(20)
#     timmy.setheading(random.choice(direction))
#     timmy.color(random_colour())

# drawing spirograph!!

# t.colormode(255)
# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
# timmy.speed("fastest")
# def fast(size):
#     for i in range(int(360/size)):
#
#         timmy.color(random_colour())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size)
#
# fast(5)
# screen = t.Screen()
# # screen.exitonclick()
# a = int(input())
# b = a // 2
# c = b*2
# if c == a:
#     print("even")
# else:
#     print("odd")
# a, b = input().split("/"), input().split("/")
# if a[0] == b[0] or a[1] == b[1]:
#     print("yes")
# else:
#     print("no")
# a = 'a'
# b = 1
# print(ord(a))
# print(chr(b))
def is_even_or_odd(number):
    if number & 1 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
number = 10
result = is_even_or_odd(number)
print(f"{number} is {result}")



