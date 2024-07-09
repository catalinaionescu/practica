"""
Deci, vă interesează în
principal ca filmul pe care o să îl vizionați să înceapă cât mai repede din momentul în care ajungeți
la casa de bilete, iar, în cazul în care sunt mai multe filme care încep la ora dorită, să îl alegeți pe cel
cu prețul biletului cel mai mic.
Cerință
Dându-se ora la care ajungeți la cinematograf, scrieți un program care să selecteze din lista de filme
pe cel care respectă cel mai bine dorințele voastre.
Date de intrare
Se vor citi de la tastatură (fluxul stdin) de pe prima linie ora la care ajungeți la cinema, în format
hh:mm, iar de pe a doua linie un număr întreg n reprezentând numărul de oferte disponibile în
programul cinematografului. De pe următoarele n linii se vor citi datele despre fiecare film din ofertă
în formatul:
<oră> <preț> <nume film>
Datele din format vor fi separate prin câte un spațiu. Ora de începere a fiecărui film va fi tot în
formatul hh:mm, prețul va fi un număr întreg fără semn, iar numele filmului va fi un șir de caractere,
el putând fi format din mai multe cuvinte, dar pentru ușurință, ele vor fi separate prin caracterul
cratimă (‘-’). Fiecare linie se va termina cu un caracter newline (‘\n’).
Date de ieșire
Programul va afișa pe ecran (stream-ul standard de ieșire) un singur șir de caractere, reprezentând
numele filmului ales, în formatul dat în datele de intrare.
"""


# 1 linie ora la care ajung la cinema
# n nr oferte disp
# next linii <ora> <pret> <nume film>
# pot aparea si oferte de dinainte sa ajung
# filme cu pret separat
# niciun film nu incepe la ora la care aj
# cel mai ieftin film

def conv_min_to_int(timp):
    hours, minut = map(int, timp.split(":"))
    tot_time = hours * 60 + minut
    return tot_time


me_time = input()
n = int(input())
lista = []
for i in range(n):
    lista.append(input().split())
ora_minim = 1440
pret_minim = 100
for i in range(len(lista)):
    dif_tp = conv_min_to_int(lista[i][0]) - conv_min_to_int(me_time)
    if dif_tp > 0:
        if dif_tp < ora_minim:
            ora_minim = dif_tp
            nume = lista[i][2]
            pret = lista[i][1]
        elif dif_tp == ora_minim:
            if lista[i][1] < pret:
                pret = lista[i][1]
                nume = lista[i][2]
print(nume)
