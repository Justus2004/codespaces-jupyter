import random
import turtle
import GLGMTurtel
import tkinter as tk
from tkinter import simpledialog

def eingabeBuchstaben():
    letter = 0
    while letter < 97 or letter > 122:
        temp = False
        text1 = "Ein Buchstabe:"
        text2 = "Das war kein einzelner Buchstabe!"
        text3 = "Das Eingegebene war kein Buchstabe!"
        textvar = text1
        while temp == False:
            try:
                temp = True
                letter = ord(input("Eingabe: "))
                textvar = text1
            except:
                textvar = text2
                temp = False
        if letter <= 97 and letter >= 122:
            textvar = text3
    letter = chr(letter)
    return letter

def woerterQuelle():
    woerter = ["Hallo"]
    # woerter = ["subtrahieren", "sagen", "silikon", "kerzen", "antennen", "elastisch", "fallschirm","posieren", "steckdose", "kinderfrau", "torpedieren"]
    temp = random.randint(0, len(woerter) - 1)
    char = list(woerter[temp])
    return char

def woerterLoesen(turtle1, turtle2, turtle3):
    count = 0
    inwort = False
    wort = woerterQuelle()
    wortlen = leerWort(wort)
    while testFertig(wortlen):

        letter = eingabeBuchstaben()
        x = 0
        for i in wort:
            if letter == wort[x]:
                wortlen[x] = letter
                inwort = True
            x += 1
        if inwort:
            turtle3.write("Buchstabe vorhanden", align="center", font=("Arial", 8, "normal"))
        else:
            count += 1
            draw(count, turtle1)
            turtle2.write("Buchstabe nicht vorhanden!", align="center", font=("Arial", 8, "normal"))
        print(wortlen)
    turtle3.write("Glückwunsch! Wort erraten!", align="center", font=("Arial", 8, "normal"))

def testFertig(wortlen):
    return "_" in wortlen

def leerWort(wort):
    wortlen = []
    for i in wort:
        wortlen.append("_")
    return wortlen

def draw(count, turtle1):
    match count:
        case 1:
            GLGMTurtel.draw_galgen_fuss(turtle1)
        case 2:
            GLGMTurtel.draw_galgen_stange(turtle1)
        case 3:
            GLGMTurtel.draw_galgen_quer(turtle1)
        case 4:
            GLGMTurtel.draw_galgen_mast(turtle1)
        case 5:
            GLGMTurtel.draw_galgen_seil(turtle1)
        case 6:
            GLGMTurtel.draw_head(turtle1)
        case 7:
            GLGMTurtel.draw_body(turtle1)
        case 8:
            GLGMTurtel.draw_left_arm(turtle1)
        case 9:
            GLGMTurtel.draw_right_arm(turtle1)
        case 10:
            GLGMTurtel.draw_left_leg(turtle1)
        case 11:
            GLGMTurtel.draw_right_leg(turtle1)
            
def ausgabe(turtle2,turtle3):
    turtle2.penup()
    turtle2.left(90)
    turtle2.forward(250)
    turtle2.right(90)
    turtle2.forward(50)
    
    turtle3.penup()
    turtle3.left(90)
    turtle3.forward(250)
    turtle3.right(90)
    turtle3.forward(200)
    

def main():
    screen = turtle.Screen()
    turtle1 = turtle.Turtle()
    turtle2 = turtle.Turtle()
    turtle3 = turtle.Turtle()
    ausgabe(turtle2,turtle3)
    woerterLoesen(turtle1, turtle2, turtle3)

if __name__ == "__main__":
    main()
