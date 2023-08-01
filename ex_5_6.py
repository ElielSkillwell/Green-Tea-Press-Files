import turtle

t = turtle.Turtle()
t.speed(15)

def draw_koch(t, length, n):
    if n < 3:
        t.fd(length)
        return
    angle_1 = 60
    angle_2 = 120
    draw_koch(t, length / 3, n - 1)
    t.lt(angle_1)
    draw_koch(t, length / 3, n - 1)
    t.rt(angle_2)
    draw_koch(t, length / 3, n - 1)
    t.lt(angle_1)
    draw_koch(t, length / 3, n - 1)


def draw_snowflake(t, length, n):
    for i in range(3):
        draw_koch(t, length, n)
        t.rt(120)

# for i in range(100, 500, 50):
#     draw_snowflake(t, 50 + i, 4)

draw_snowflake(t, 250, 5)