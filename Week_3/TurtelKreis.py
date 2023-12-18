import turtle

def kreisMalen():
    ws = turtle.Turtle()
    ws.speed(10)
    ws.color("cyan")
    for j in range(1,100):
        for i in range(1,6):
            ws.left(144)
            ws.forward(200)
        ws.left(5)
    turtle.done
    
def main():
    kreisMalen()
    
if __name__ == "__main__":
    main()
