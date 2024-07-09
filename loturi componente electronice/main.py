"""
Loturile care vă sunt utile sunt doar loturile care au un
număr de condensatoare mai mare sau egal cu numărul de tranzistoare, numărul de rezistoare mai
mare sau egal cu numărul de condensatoare, și au cel puțin un condensator, un tranzistor și un rezistor.
În plus, vă interesează și lotul cu cele mai multe componente, pentru că din ele o să le mai completați
pe cele lipsă.
Cerință
Scrieți un program care primește la intrare loturile de componente și afișează câte dintre aceste loturi
vă sunt utile și câte componente are lotul cel mai mare. Un lot se consideră util dacă respectă condițiile
impuse mai sus. Aceste condiții trebuie îndeplinite simultan.
Date de intrare
Se va citi de la tastatură (fluxul stdin) pe o singură linie un număr întreg n reprezentând numărul de
loturi. Apoi, se vor citi cele n loturi după cum urmează: se citește pe o linie numărul de componente
din lotul respectiv, k, iar pe următoarea linie k litere reprezentând tipurile de componente ale lotului,
separate prin spatii (R reprezentând un rezistor, C reprezentând un condensator și T reprezentând un
tranzistor).
Date de ieșire
Programul va afișa pe ecran (stream-ul standard de iesire) două numere întregi, reprezentând numărul
de loturi utile dintre cele citite cât și numărul de componente ale lotului cel mai mare, valori separate
printr-un spațiu.
"""


# cit nr de loturi
# lot bun nr cond >= nr tranz
# cel put un c, t,r
# ma intereseaza lotul cu cele mai m compo
# out nr lot utile + nr comp lot cel mai mare
n = int(input())
lista = []
maxi = 0
for i in range(n):
    nr_comp = int(input())
    if nr_comp > maxi:
        maxi = nr_comp
    comp_list = input()
    lista.append((nr_comp, comp_list))
nr_lot = 0
for i in lista:
    componente = i[1].split()
    nr_c = componente.count('C')
    nr_r = componente.count('R')
    nr_t = componente.count('T')
    if nr_c >= nr_t and nr_r > 0 and nr_t != 0:
        nr_lot += 1
print(nr_lot, maxi)
