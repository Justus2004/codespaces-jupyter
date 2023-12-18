def zahlAufteilen(zahl):
    ziffern =[]

    for h in range(len(zahl)):
        ziffern.append(int(zahl[h]))
    return ziffern

def berechneQuersumme(zahl):
    ziffern  = zahlAufteilen(zahl)
    temp =0
    for i in range(len(ziffern)):
        temp += ziffern[i]
    return temp
    
def berechneQuerprodukt(zahl):
     ziffern  = zahlAufteilen(zahl)
     temp =1
     for i in range(len(ziffern)):
        temp *= ziffern[i]

     print(f"Bei der Zahl {zahl} kommt ein Querprodukt der Menge {temp}")

def boese_sieben(help):
    zahl = int(help)
    zahl = zahl + 1
    set1 = True

    if zahl % 7 != 0:
        set1 = False

    temp = zahlAufteilen(help)
    for i in temp:
        if i == 7:
            set1 = False

    if set1:
        print("Die nächste Zahl muss ausgelassen werden, da sie durch 7 teilbar ist oder eine 7 enthält!")
    else:
        print("Die nächste Zahl ist in Ordnung!")
        
def ziffernWurzel(zahl):
    temp = berechneQuersumme(zahl)
    while (temp / 1)>9:
        help = str(temp)
        temp=berechneQuersumme(help)
    return temp

def main():
    zahl = input("Gib mir eine Zahl: ")
    #berechneQuersumme(zahl)
    #berechneQuerprodukt(zahl)
    #boese_sieben(zahl)
    print(ziffernWurzel(zahl))

if __name__ == "__main__":
    main()