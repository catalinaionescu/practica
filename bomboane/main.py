"""
Andrei cumpără bomboane într-o anumită zi dacă el are destui bani de la tatăl său şi acest lucru duce la
creşterea fericirii lui cu un anumit număr de puncte egal cu aroma bomboanei. Obligatoriu, dacă are destui bani, el va
cumpăra bomboana. El păstrează toţi banii rămaşi după ce a cumpărat bomboanele pentru a-şi putea cumpăra mai multe
următoarea zi. Dacă el nu are destui bani să îşi cumpere bomboane într-o anumită zi, asta nu înseamnă că este necesar
ca punctele lui de fericire să scadă (evident că nici mai fericit nu îl vor face). Punctele de fericire vor scădea doar dacă
el nu a cumpărat, în oricare din zilele trecute, cel puţin o bomboană cu o aromă mai bună decât cea din ziua curentă, pe
care nu şi-o permite.
Cerinţă
Dându-se un număr n pozitiv, reprezentând numărul de zile în care băiatul primeşte bani de la tatăl său, apoi n numere
pozitive, reprezentând suma de bani pe care o primeşte băiatul într-o anumită zi, apoi n perechi de numere pozitive, care
reprezintă costul şi aroma bomboanelor din magazin într-o anumită zi, să se calculeze numărul de puncte de fericire al
lui Andrei. Numărul de puncte de fericire va creşte sau va scădea cu numărul pozitiv prin care este reprezentată aroma,
conform spuselor din enunţ. Presupunem că la început Andrei avea 0 lei şi 0 puncte de fericire.
Date de intrare
Pe prima linie se află numărul întreg pozitiv n, reprezentând numărul de zile în care băiatul primeşte bani de la tatăl său,
urmat de caracterul newline. Pe următoarea linie se află n valori întregi pozitive, separate prin whitespace, reprezentând
suma de bani pe care o primeşte băiatul într-o anumită zi, urmate de caracterul newline. Pe următoarele n linii se află
perechi de numere întregi de forma "cost_bomboana aroma_bomboana", care reprezintă costul şi aroma
bomboanelor din magazin în fiecare zi.
Date de ieşire
Se va afişa, pe o singură linie, un singur număr întreg, reprezentând numărul de puncte de fericire pe care le are Andrei
la finalul celor n zile. Linia se va termina obligatoriu cu un caracter newline ("\n").
"""

# crestere fericire  = pct aroma bombo
# mereu cumpara daca are bani si ce i ramane ramane pt next day
# nu are bani intr o zi nu ii scade neaparat fericirea
# ii scad punctele doar daca in orice zi de dinainte de azi nu si a luat cel put o bomboana mai buna decat cea de azi pe care nu si o permite
# n nr de zile in care primeste bani
# n sume de bani pe care le primeste zilnic pe o linie
# n perechi cost aroma bombo pe n linii

n = int(input())
bani = list(map(int, input().split()))
bombo = []
suma = 0
fericire = 0
for i in range(n):
    bombo.append(list(map(int, input().split())))

for i in range(n):
    suma += bani[i]
    if suma - bombo[i][0] >= 0:
        suma -= bombo[i][0]
        fericire += bombo[i][1]
    else:
        criteriu = 0  # presupun ca nu e nicio aroma mai buna
        for j in range(i-1):
            if bombo[i][1] < bombo[j][1]:
                criteriu = 1  # gasesc o aroma mai buna si dau break la loop
                break
        if criteriu == 0:
            fericire -= bombo[i][1]
print(fericire, '\n')
