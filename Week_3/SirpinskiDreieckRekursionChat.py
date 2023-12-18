import turtle

def draw_sierpinski_triangle(order, size, turtle_obj):
    if order == 0:
        for _ in range(3):
            turtle_obj.forward(size)
            turtle_obj.left(120)
    else:
        size /= 2
        draw_sierpinski_triangle(order - 1, size, turtle_obj)
        turtle_obj.forward(size)
        draw_sierpinski_triangle(order - 1, size, turtle_obj)
        turtle_obj.backward(size)
        turtle_obj.left(60)
        turtle_obj.forward(size)
        turtle_obj.right(60)
        draw_sierpinski_triangle(order - 1, size, turtle_obj)
        turtle_obj.left(60)
        turtle_obj.backward(size)
        turtle_obj.right(60)

def main():
    order = int(input("Gib die Rekursionsstufe ein: "))
    size = 400
    turtle_obj = turtle.Turtle()
    turtle_obj.speed(200000)
    turtle_obj.penup()
    turtle_obj.goto(-size/2, -size/2*(3**0.5)/2)
    turtle_obj.pendown()

    draw_sierpinski_triangle(order, size, turtle_obj)

    turtle.done()

if __name__ == "__main__":
    main()
