zahl = 20 # Eingabe
x=zahl
for a in range (1,zahl,2):# Schleife für das "Bauen" des Baums
    x = x-1 # Abstand von der Stern sonst "Falsch herum" deswegen muss etwas von der Zahl runterzählen
    for b in range(0,x,1):#schleife für die leerzeichen 
        print(" ",end ="") #leerzeichen damit pyramidenform entsteht und end=""ndamit kein zeilenumbruch
    for c in range (0,a,1): # schleife für die sterne 
        print("*",end ="") # Stern für muster
    print() # zeilenumbruch nach jeder ebene des Baums
for a in range (0,2,1): # Shcleife für Stamm
    for b in range (1,zahl-1,1): # hochzählen für mittigen Abstand des Stammes    
        print(" ",end ="")
    for c in range (0,3,1): # Schleife für Bauen des Stammes
        print("*",end ="")
    print() 
