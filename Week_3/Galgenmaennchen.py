import random
import GLGMTurtel
import turtle
import tkinter as tk
from tkinter import simpledialog


def eingabeBuchstaben():
    letter =0
    while letter<97 or letter>122:
        temp =False
        text1 = "Ein Buchstabe:"
        text2 = "Das war kein einzelner Buchstabe!"
        text3 = "Das Eingegebene war kein Buchstabe!"
        textvar = text1
        while(temp==False):
            try:
                temp=True
                letter = ord(simpledialog.askstring("Ei Feld", textvar))
                textvar = text1
            except:
                textvar = text2
                temp = False 
        if(letter<=97 and letter>=122):
            textvar = text3
    letter =chr(letter)
    return letter

def woerterQuelle():
    woerter =["subtrahieren", "sagen", "silikon", "kerzen", "antennen", "elastisch", "fallschirm","posieren", "steckdose", "kinderfrau", "torpedieren"]
    temp=random.randint(0,len(woerter)-1)
    char = list(woerter[temp])
    return char

def woerterLoesen():
    count =0
    inwort = False
    wort = woerterQuelle()
    wortlen = leerWort(wort)
    while testFertig(wortlen):
        
        letter = eingabeBuchstaben()
        x=0
        for i in wort:
            if letter == wort[x]:
                wortlen[x] = letter
                inwort = True
            x+=1
        if inwort:
            turtle.write(arg="Buchstabe vorhanden")
        else:
            count+=1
            draw(count)
            turtle.write(arg="Buchstabe nicht vorhanden!")
        print(wortlen)
    turtle.write(arg="Glückwunsch! Wort erraten!")
            
def testFertig(wortlen):
    return "_" in wortlen

def leerWort(wort):
    wortlen =[]
    for i in wort:
        wortlen.append("_")
    return wortlen

def draw(count):
    match count :
        case 1:
            GLGMTurtel.draw_galgen_fuss()
        case 2:
            GLGMTurtel.draw_galgen_stange()
        case 3:
            GLGMTurtel.draw_galgen_quer()
        case 4:
            GLGMTurtel.draw_galgen_mast()
        case 5:
            GLGMTurtel.draw_galgen_seil()
        case 6:
            GLGMTurtel.draw_head()
        case 7:
            GLGMTurtel.draw_body()
        case 8:
            GLGMTurtel.draw_left_arm()
        case 9:
            GLGMTurtel.draw_right_arm()
        case 10:
            GLGMTurtel.draw_left_leg()
        case 11:
            GLGMTurtel.draw_right_leg()
        
def show_input_dialog():
    result = simpledialog.askstring("Eingabe", "Geben Sie etwas ein:")
    print("Eingabe:", result)

def main():
    root = tk.Tk()
    root.geometry("300x200")
    button = tk.Button(root, text="Eingabefenster anzeigen",command=show_input_dialog)
    button.pack(pady=20)
    woerterLoesen()
    root.mainloop()
    
if __name__ == "__main__":
    main()