import random
import turtle
import GLGMTurtel
import time

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
    woerter = ["subtrahieren", "sagen", "silikon", "kerzen", "antennen", "elastisch", "fallschirm","posieren", "steckdose", "kinderfrau", "torpedieren"]
    temp = random.randint(0, len(woerter) - 1)
    char = list(woerter[temp])
    return char

def woerterLoesen(turtle1, turtle2, turtle3,turtle4):
    count = 0
    wort = woerterQuelle()
    wortlen = leerWort(wort)
    while testFertig(wortlen):
        if count >11:
            break
        
        inwort = False
        letter = eingabeBuchstaben()
        x = 0
        for i in wort:
            
            if letter == wort[x]:
                wortlen[x] = letter
                inwort = True
                
            x += 1
            
        if inwort==True:
            turtle3.write("Buchstabe vorhanden", align="center", font=("Arial", 8, "normal"))
            turtle2.clear()
            
        elif inwort==False:
            count += 1
            draw(count, turtle1)
            turtle2.write("Buchstabe nicht vorhanden!", align="center", font=("Arial", 8, "normal"))
            turtle3.clear()

        turtle4.clear()
        turtle4.write(wortlen)
    turtle2.clear()
    turtle3.clear()
    if testFertig(wortlen):
        turtle3.write("Du hast zu viele Versuche gebraucht!", align="center", font=("Arial", 8, "normal"))
    else:
        turtle3.write("Glückwunsch! Wort erraten!", align="center", font=("Arial", 8, "normal"))
        
    time.sleep(20)

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
            
def ausgabe(turtle2,turtle3,turtle4):
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
    
    turtle4.penup()
    turtle4.left(90)
    turtle4.forward(250)
    turtle4.left(90)
    turtle4.forward(200)
    
def main():
    turtle1 = turtle.Turtle()
    turtle2 = turtle.Turtle()
    turtle3 = turtle.Turtle()
    turtle4 = turtle.Turtle()
    ausgabe(turtle2,turtle3,turtle4)
    woerterLoesen(turtle1, turtle2, turtle3,turtle4)

if __name__ == "__main__":
    main()
