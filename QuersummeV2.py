def aufteilen_quersumme(zahl):
    summand =[]

    for h in range(0, len(zahl)):
        summand.append(zahl[h])
    
    return summand

def querprodukt_berechnen(zahl):
     querprodukt = 1
     for h in range(0, len(zahl)):
         querprodukt *=(int(zahl[h]))

     print(f"Bei der Zahl {zahl} kommt ein Querprodukt der Menge {querprodukt}")

def boese_sieben(help):
    zahl = int(help)
    zahl = zahl + 1
    set1 = True

    if zahl % 7 != 0:
        set1 = False

    temp = aufteilen_quersumme(help)
    for i in temp:
        if i == 7:
            set1 = False

    if set1:
        print("Die nächste Zahl muss ausgelassen werden, da sie durch 7 teilbar ist oder eine 7 enthält!")
    else:
        print("Die nächste Zahl ist in Ordnung!")

def main():
    zahl = input("Gib mir eine Zahl: ")
    # ergebnis = querprodukt_berechnen(zahl)
    boese_sieben(zahl)

if __name__ == "__main__":
    main()