import turtle
import math
turtle1=turtle
def hypotenuse(kathete):
    hypo = math.sqrt((kathete*kathete)*2)
    return hypo

def draw_galgen_fuss(turtle1):
    # Startpunkt
    turtle1.penup()
    turtle1.goto(-180, -150)
    turtle1.pendown()
    # Galgenfuss
    turtle1.right(45)
    turtle1.forward(120)
    turtle1.right(180)
    turtle1.forward(120)
    turtle1.left(90)
    turtle1.forward(120)
    turtle1.left(180)
    turtle1.forward(120)
    
def draw_galgen_stange(turtle1):
    turtle1.left(45)
    turtle1.forward(250)
    
def draw_galgen_quer(turtle1):
    turtle1.left(180)
    turtle1.forward(50)
    turtle1.left(135)
    turtle1.forward(hypotenuse(50))
    turtle1.right(45+180)
    turtle1.forward(50)
    turtle1.left(180)
    
def draw_galgen_mast(turtle1):
    turtle1.forward(200)
    turtle1.right(90)
    
def draw_galgen_seil(turtle1):
    turtle1.forward(50)
    turtle1.right(90)

def draw_head(turtle1):
    turtle1.circle(20)
    turtle1.left(90)
    turtle1.penup()
    turtle1.forward(40)
    turtle1.pendown()
    

def draw_body(turtle1):
    turtle1.forward(70)
    turtle1.right(180)
    turtle1.forward(40)

def draw_left_arm(turtle1):
    turtle1.left(45)
    turtle1.forward(35)
    turtle1.right(180)
    turtle1.forward(35)
    turtle1.left(90)

def draw_right_arm(turtle1):
    turtle1.forward(35)
    turtle1.right(180)
    turtle1.forward(35)
    turtle1.left(45)
    turtle1.forward(40)

def draw_left_leg(turtle1):
    turtle1.left(45)
    turtle1.forward(35)
    turtle1.right(180)
    turtle1.forward(35)
    turtle1.left(90)

def draw_right_leg(turtle1):
    turtle1.forward(35)
    turtle1.right(180)
    turtle1.forward(35)
    turtle1.left(45)
