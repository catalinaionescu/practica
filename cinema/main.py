# 1 linie ora la care ajung la cinema
# n nr oferte disp
# next linii <ora> <pret> <nume film>
# pot aparea si oferte de dinainte sa ajung
# filme cu pret separat
# niciun film nu incepe la ora la care aj
# cel mai ieftin film


def conv_min_to_int(timp):
    hours, minut = map(int, timp.split(":"))
    tot_time = hours*60 + minut
    return tot_time


me_time = input()
n = int(input())
lista = []
for i in range(n):
    lista.append(input().split())
mini_ora = 1440
mini_pret = 100
for i in range(len(lista)):
    dif_tp = conv_min_to_int(lista[i][0]) - conv_min_to_int(me_time)
    if dif_tp > 0:
        if dif_tp < mini_ora:
            mini_ora = dif_tp
            nume = lista[i][2]
            pret = lista[i][1]
        elif dif_tp == mini_ora:
            if lista[i][1] < pret:
                pret = lista[i][1]
                nume = lista[i][2]
print(nume)