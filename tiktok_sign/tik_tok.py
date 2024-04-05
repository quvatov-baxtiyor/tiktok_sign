#making tiktok logo

# from turtle import *
#
# width(20)
# bgcolor('black')
# colors = ['#db0f3c','#50ebe7','white']
# pos = [(0,0),(-5,13),(-5,5)]
#
# for (x,y), col in zip(pos,colors):
#     up()
#     goto(x,y)
#     down()
#     color(col)
#     # left(50)
#     right(180)
#     circle(50,270)
#     forward(120)
#     left(180)
#     circle(50,90)
#
# done()




#making circle
# import turtle
# window = turtle.Screen()
# t = turtle.Turtle()
# t.shape('turtle')
# t.color('blue')
# t.circle(100)
# window.mainloop()



#making circle and filling it with black color
# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# t.color('red')
# t.fillcolor('black')
# t.pensize(3)
# t.begin_fill()
# t.circle(100)
# t.end_fill()
# t.screen.exitonclick()
# t.screen.mainloop()



#making graphic design
# from turtle import *
# from random import randint
# speed(0)
# bgcolor('black')
# x = 1
# while x <= 400:
#     r = randint(0,255)
#     g = randint(0,255)
#     b = randint(0,255)
#     colormode(255)
#     pencolor(r,g,b)
#     fd(50 + x)
#     rt(90.91)
#     x += 1
# exitonclick()



#using 7 colours to make design
# from turtle import *
# speed(0)
# bgcolor('black')
# pensize(3)
# for x in range(15):
#     for colours in ['red','magenta','blue','cyan','green','yellow','white']:
#         color(colours)
#         left(12)
#         for j in range(4):
#             forward(200)
#             left(90)
# exitonclick()



#making design using kvadrat
# import turtle
# window = turtle.Screen()
# t = turtle.Turtle()
# t.color('yellow')
# window.bgcolor('blue')
# t.pensize(3)
# t.speed(10)
# def kvadr():
#     for i in range(4):
#         t.forward(80)
#         t.left(90)
# for j in range(12):
#     kvadr()
#     t.left(30)
# t.screen.mainloop()