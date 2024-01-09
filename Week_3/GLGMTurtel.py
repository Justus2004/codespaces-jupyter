import turtle
import math

def hypotenuse(kathete):
    hypo = math.sqrt((kathete*kathete)*2)
    return hypo

def draw_galgen_fuss():
    # Startpunkt
    turtle.penup()
    turtle.goto(-180, -150)
    turtle.pendown()
    # Galgenfuss
    turtle.right(45)
    turtle.forward(120)
    turtle.right(180)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(180)
    turtle.forward(120)
    
def draw_galgen_stange():
    turtle.left(45)
    turtle.forward(250)
    
def draw_galgen_quer():
    turtle.left(180)
    turtle.forward(50)
    turtle.left(135)
    turtle.forward(hypotenuse(50))
    turtle.right(45+180)
    turtle.forward(50)
    turtle.left(180)
    
def draw_galgen_mast():
    turtle.forward(200)
    turtle.right(90)
    
def draw_galgen_seil():
    turtle.forward(50)
    turtle.right(90)

def draw_head():
    turtle.circle(20)
    turtle.left(90)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
    

def draw_body():
    turtle.forward(70)
    turtle.right(180)
    turtle.forward(40)

def draw_left_arm():
    turtle.left(45)
    turtle.forward(35)
    turtle.right(180)
    turtle.forward(35)
    turtle.left(90)

def draw_right_arm():
    turtle.forward(35)
    turtle.right(180)
    turtle.forward(35)
    turtle.left(45)
    turtle.forward(40)

def draw_left_leg():
    turtle.left(45)
    turtle.forward(35)
    turtle.right(180)
    turtle.forward(35)
    turtle.left(90)

def draw_right_leg():
    turtle.forward(35)
    turtle.right(180)
    turtle.forward(35)
    turtle.left(45)
