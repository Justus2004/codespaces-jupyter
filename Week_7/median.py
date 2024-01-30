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

liste = [5, 2, 1, 3, 4]
print("Median:", berechne_median(liste))
