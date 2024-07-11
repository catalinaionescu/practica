"""
Pentru compresia unui şir binar se foloseşte tehnica White Block Skipping adaptat - ignorarea blocurilor (grupelor)
uniforme (compuse numai din biţi de 0 sau numai din biţi de 1). Şirul este împărţit în blocuri (grupe) de câte n biţi,
codate independent. Există două codări posibile: codarea în care se ignoră blocurile compuse numai din biţi 0, şi codarea
în care se ignoră blocurile compuse numai din biţi 1. In final, se alege codarea care asigură raportul maxim de compresie.
In cazul în care cele două variante de compresie ajung la acelaşi raport de compresie, se utilizează varianta în care se
ignoră blocurile compuse numai din biţi 0.
Pentru codarea în care se ignoră blocurile compuse numai din biţi 0, şirul comprimat începe cu un bit 0, la care se adaugă
codurile corespunzătoare blocurilor de biţi din şirul iniţial, codate după regula următoare: dacă toţi biţii blocului sunt
nuli, blocul este înlocuit de un bit unic de zero; dacă cel puţin un bit din bloc este nenul, atunci biţii blocului se copiază
şi în faţa lor este adăugat un bit de 1 (ca prefix).
Pentru codarea în care se ignoră blocurile compuse numai din biţi 1, şirul comprimat începe cu un bit 1, la care se adaugă
codurile corespunzătoare blocurilor de biţi din şirul iniţial, codate după regula următoare: dacă toţi biţii sunt 1, blocul
este înlocuit de un bit unic de 1; dacă cel puţin un bit din bloc este nul, atunci biţii blocului se copiazăşi în faţa lor este
adăugat un bit de 0 (ca prefix).
Cerință
Dându-se un număr N pozitiv reprezentand numărul de elemente din şir, apoi numărul n pozitiv reprezentând numărul
de elemente din fiecare bloc ce va fi codat, apoi cele N elemente ale şirului, să se genereze şirul comprimat (codat) şi să
se calculeze raportul de compresie (raportul dintre numărul de biţi din şirul iniţial - N - şi numărul de biţi din şirul
comprimat). Dacă şirul de intrare nu poate fi împărţit exact în grupe de n biţi, ultimii biţi rămaşi se codează ca şi când
ar face parte dintr-un grup neuniform (dar fără a adăuga biţi de completare).
Date de intrare
Pe prima linie se află numărul întreg pozitiv N, reprezentând numărul de elemente din şir, urmat de caracterul newline,
apoi numărul întreg pozitiv n, reprezentând numărul de elemente din fiecare grupă, urmat de caracterul newline. Pe
următoarele N linii se află elementele şirului (numere de 0 sau 1), câte unul pe linie, urmat de caracterul newline.
Date de ieșire
Se va afișa pe prima linia valoarea raportului de compresie, cu două zecimale, cu rotunjire, apoi şirul comprimat, câte
un număr (0 sau 1) pe fiecare linie.
"""


# ignor 00 sau 11, aleg cod cu rap max de compresie
# daca e ac rap aleg cod in care ignor bitii de 0
# cod care ignora bloc comp numai din 0: sir incepe cu 0 si dupa se adauga: daca toti sunt 0 se inloc bloc cu 0, daca ex un 1 in bloc at adaug un 1 in fata
# pt cod cu 1: sir inc cu 1 si dupa se adauga asa: toti bitii 1 inloc cu 1, daca nu se adauga 0 in fata
# N nr elem sir
# n nr de elem din fiec bloc care va fi cod
# N elem ale sir
# rap de compr = nr de biti sir init / nr biti sir compr 2 zec cu rotun
# daca nu pot imp sir in grupe de n, at ult biti se cod ca si cand ar fi grup neunfi dar nu adaug biti de comp

def split_string(string, n):  # impart bitii in grupe si ii pun in lista
    lista = []
    for i in range(0, len(string), n):
        lista.append(string[i:i + n])
    return lista


def check_tip_bloc(bloc):  # verific ce biti am in bloc
    if bloc.count('0') == len(bloc):
        return 'zero'
    elif bloc.count('1') == len(bloc):
        return 'unu'
    else:
        return 'mixt'


def regula_0(lista):
    new_string = '0'
    for i in range(len(lista)):
        if check_tip_bloc(lista[i]) == 'zero':
            new_string += '0'
        else:
            new_string += '1' + lista[i]
    return new_string


def regula_1(lista):
    new_string = '1'
    for i in range(len(lista)):
        if check_tip_bloc(lista[i]) == 'unu':
            new_string += '1'
        else:
            new_string += '0' + lista[i]
    return new_string


N = int(input())
n = int(input())
sir_init = ''
for i in range(N):
    sir_init += input()
lista_biti = split_string(sir_init, n)
string0 = regula_0(lista_biti)
string1 = regula_1(lista_biti)
rap0 = float(len(sir_init)/len(string0))
rap1 = float(len(sir_init)/len(string1))
if rap0 >= rap1:
    print(f"{(len(sir_init)/len(string0)):.2f}")
    for i in string0:
        print(f'{i}')
else:
    print(f"{(len(sir_init) / len(string1)):.2f}")
    for i in string1:
        print(f'{i}')
