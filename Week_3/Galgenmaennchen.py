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
    return letter

def woerterQuelle():
    woerter =["subtrahieren", "sagen", "silikon", "kerzen", "antennen", "elastisch", "fallschirm","posieren", "steckdose", "kinderfrau", "torpedieren"]
    temp=random.randint(0,len(woerter))
    char = list(woerter[temp])
    return char
           
def main():
    eingabeBuchstaben()
    woerterQuelle()
    
if __name__ == "__main__":
    main()