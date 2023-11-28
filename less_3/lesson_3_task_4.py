import turtle

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_emoji():
    turtle.speed(2)

    # голова
    draw_circle("yellow", 0, 0, 100)

    # глаза
    draw_circle("black", -35, 50, 15)
    draw_circle("black", 35, 50, 15)

    # рот
    turtle.penup()
    turtle.goto(-25, -30)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(25, 180)

    # язык
    turtle.penup()
    turtle.goto(-10, -53)
    turtle.pendown()
    turtle.right(180)
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(10, 180)
    turtle.end_fill()

    turtle.hideturtle()

# Вызываем функцию для отрисовки эмодзи
draw_emoji()


# Необходимо, чтобы окно не закрывалось само, а только по клику
draw_emoji.screen.exitonclick()
draw_emoji.screen.mainloop()
