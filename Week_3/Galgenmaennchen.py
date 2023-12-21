import random
def eingabeBuchstaben():
    letter =0
    while letter<97 or letter>122:
        temp =False
        while(temp==False):
            try:
                temp=True
                letter = ord(input("Gebe einen Buchstaben ein: "))
            except:
                print("Das war kein einzelner Buchstabe!")
                temp = False 
        if(letter<=97 and letter>=122):
            print("Das Eingegebene war kein Buchstabe!")
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
        count+=1
        letter = eingabeBuchstaben()
        x=0
        for i in wort:
            if letter == wort[x]:
                wortlen[x] = letter
                inwort = True
            x+=1
        if inwort:
            print("Buchstabe vorhanden!")
        else:
            print("Buchstabe nicht vorhanden!")
        print(wortlen)
    print("Glückwunsch! Wort erraten nach ",count," Versuchen")
            
def testFertig(wortlen):
    return "_" in wortlen

def leerWort(wort):
    wortlen =[]
    for i in wort:
        wortlen.append("_")
    return wortlen
        
def main():
    woerterLoesen()
    
if __name__ == "__main__":
    main()