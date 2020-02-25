import turtle

def get_turtle_state(turtle):
    """ Return turtle's current heading and position. """
    return turtle.heading(), turtle.position()


def restore_turtle_state(turtle, state):
    """ Set the turtle's heading and position to the given values. """
    turtle.setheading(state[0])
    turtle.setposition(state[1][0], state[1][1])


def draw_l_system(some_turtle, instructions, angle, distance):
    """Draw with some_turtle, interpreting each letter in the instructions passed in."""
    state_stack = []
    for task in instructions:
        if task == 'F':
            some_turtle.forward(distance)
        elif task == 'B':
            some_turtle.backward(distance)
        elif task == '[':
            state = get_turtle_state(some_turtle)
            state_stack.append(state)
        elif task == ']':
            state = state_stack.pop()
            restore_turtle_state(some_turtle, state)
        elif task == '+':
            some_turtle.right(angle)
        elif task == '-':
            some_turtle.left(angle)


def turtule_initialize():
    # setup for drawing
    window = turtle.Screen()
    jill = turtle.Turtle()
    jill.speed(0)
    turtle.mode("logo")
    #jill.hideturtle()

    # using screen.tracer() speeds up your drawing (by skipping some frames when drawing)
    # window.tracer(5)
    turtle.tracer(0)

    # move turtle to left side of screen
    jill.up()
    jill.back(300)
    jill.down()
    return jill
