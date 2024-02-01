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

liste = [5, 6, 3, 10, 10]
print("Median:", berechne_median(liste))