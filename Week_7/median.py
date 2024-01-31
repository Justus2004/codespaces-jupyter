def berechne_median(liste):
    sortierte_liste = sorted(liste)
    laenge = len(sortierte_liste)

    if laenge == 0:
        return None


    if laenge % 2 == 0:

        index1 = laenge // 2
        index2 = index1 - 1
        median = (sortierte_liste[index1] + sortierte_liste[index2]) / 2
    else:
        index = laenge // 2
        median = sortierte_liste[index]

    return median

def berechne_arithmetisches_mittel(liste):
    if len(liste) == 0:
        return None
    return sum(liste) / len(liste)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def berechne_fibonacci_reihe(n):
    fibonacci_reihe = []
    for i in range(n):
        fibonacci_reihe.append(fibonacci(i))
    return fibonacci_reihe

n = 10
fibonacci_reihe = berechne_fibonacci_reihe(n)
print("Die ersten", n, "Fibonacci-Zahlen sind:", fibonacci_reihe)

liste = [5, 6, 3, 10, 10]
print("Median:", berechne_median(liste))
