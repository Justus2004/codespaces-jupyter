def aufteilen_quersumme(zahl):
    summand =0

    for h in range(0, len(zahl)):
        summand +=(int(zahl[h]))
    
    return summand

def main():
    zahl = input("Gib mir eine Zahl: ")
    ergebnis = aufteilen_quersumme(zahl)
    print(ergebnis)

if __name__ == "__main__":
    main()