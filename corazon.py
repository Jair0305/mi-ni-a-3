import turtle
import time

turtle.bgcolor('#B15E6C')
turtle2 = turtle.Turtle()
turtle2.speed(10)
turtle2.color("#CF8BA9")
turtle2.pensize(8)

turtle2.penup()
turtle2.goto(-300, -200)
turtle2.pendown()

message = "Felices 2 años, Te amo"
for letter in message:
    turtle2.write(letter, font=("Times New Roman", 30, "normal"))
    time.sleep(0.2)
    turtle2.penup()
    if(letter != "i" or letter != "l" or letter != "m"):
        turtle2.forward(10)
    else:
        turtle2.forward(20)
    turtle2.forward(20)
    turtle2.pendown()

turtle1 = turtle.Turtle()
turtle1.speed(2)
turtle1.color("#B3B3F1")
turtle1.pensize(5)

turtle1.penup()
turtle1.goto(0, 0)
turtle1.pendown()
turtle1.begin_fill()
turtle1.fillcolor("#B3B3F1")
turtle1.left(140)
turtle1.forward(224)
for _ in range(200):
    turtle1.right(1)
    turtle1.forward(2)
turtle1.left(120)
for _ in range(200):
    turtle1.right(1)
    turtle1.forward(2)
turtle1.forward(224)
turtle1.color('#CEC2FF')
turtle1.end_fill()

turtle1.penup()
turtle1.goto(-60, 150)
turtle1.pendown()
turtle1.color('#B15E6C')
turtle1.write("J    B", font=("Times New Roman", 50, "normal"))

# Ocultar las tortugas y mostrar la ventana
turtle1.hideturtle()
turtle2.hideturtle()
turtle.done()