import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

    
    '''window = turtle.Screen()
    window.bgcolor("violet")

    brad = turtle.Turtle()

    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    
    brad.forward(100)
    brad.right(90)

    brad.forward(100)
    brad.right(90)

    brad.forward(100)
    brad.right(90)

    brad.forward(100)
    brad.right(90)


    brad2 = turtle.Turtle()
    brad2.shape("arrow")
    brad2.color("blue")
    brad2.circle(100)'''


def draw_art():
    window = turtle.Screen()
    window.bgcolor("violet")
    #Create the turtle brad - Draw square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    for i in range(1,73):
         draw_square(brad)
         brad.right(5)

    #Create the turtle brad2 - Draw a circle

    '''brad2 = turtle.Turtle()
    brad2.shape("arrow")
    brad2.color("blue")
    brad2.circle(100)'''
    

    window.exitonclick()


draw_art()
