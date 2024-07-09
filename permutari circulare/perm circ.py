"""
Într-o permutare circulară, toate cifrele secvenţei date, exceptând-
o pe ultima, sunt mutate cu o poziţie spre dreapta, ultima cifră devenind prima.

De exemplu, dacă n=107, scrierea sa în baza 2 este 1101011. Prin permutări circulare succesive
putem obţine, în ordine, secvenţele:
1110101
1111010
0111101
1011110
0101111
...
Fiecare astfel de secvenţă reprezintă transcrierea în bază 2 a unui număr natural m care are o
anumită valoare în baza 10. Lui George jocul nu i s-ar mai părea așa interesant dacă n-ar reuși să
scrie un program care să determine în locul lui numărul natural m. Ajutaţi-l!
Cerinţă
Să se afle cel mai mare număr natural m, scris în baza 10, a cărui scriere în baza 2 se poate obține
prin una sau mai multe permutări circulare ale scrierii în baza 2 a numărului n.
Date de intrare
Se va citi de la tastatură (fluxul standard de intrare, stdin) pe o singură linie, numărul natural nenul
n, în baza 10, care respectă cerinţa din enunţ (primul bit din stânga al reprezentării sale în bază 2
să fie 1).
Date de ieşire
Programul va afişa la consolă (stream-ul standard de ieşire, stdout), pe o singură linie, numărul
natural m, cu semnificaţia cerută în enunţ.
"""

# ultimul devine primul
n = int(input())
bin = []
while n > 0:
    m = int(n % 2)
    bin.append(m)
    n = int(n / 2)
bin = bin[::-1]
maxi = 0
for i in range(len(bin)):
    m = bin[len(bin) - 1]  # iau ultimul element din lista
    bin.insert(0, m)  # il pun pe primul loc
    bin.pop()  # scot ultimul element
    new = 0
    for j in range(len(bin)):
        new += bin[j] * pow(2, j)
    if new > maxi:
        maxi = new

print(maxi)
