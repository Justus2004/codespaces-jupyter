zahl = int(input("Zahl eingeben!\n"))
temp = False
ints = []
for i in range(2, zahl):
    if zahl % i == 0 and zahl != 2:
        temp = True
        ints.append(i)
if temp:
    print(f"{zahl} ist keine Primzahl")
    for i in ints:
        print(i)
else:
    print(f"{zahl} ist eine Primzahl")

