L = [8, 24, 48, 2, 16]
compteur = 0
l = len(L)
compteur = L[0]
L[0] = L[l-1]
L[l-1] = compteur
print (L)

for num in L:
    if num % 3 == 0:
        compteur += 1

print("Le nombre de multiples de 3 dans la liste est :", compteur)
