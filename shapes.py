import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("yellow")

    slo = turtle.Turtle()
    slo.shape("turtle")
    slo.color("magenta")
    slo.speed(1.5)

    slo.forward(100)
    slo.right(90)
    slo.forward(100)
    slo.right(90)
    slo.forward(100)
    slo.right(90)
    slo.forward(100)
    slo.right(90)

    fast = turtle.Turtle()
    fast.shape("arrow");
    fast.color("green")
    fast.speed(3)

    fast.circle(100)

    window.exitonclick()

draw_square()


    
