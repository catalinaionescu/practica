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
    comp = input()
    lista.append((nr_comp, comp))
nr_lot = 0
for i in lista:
    com = i[1].split()
    nr_c = com.count('C')
    nr_r = com.count('R')
    nr_t = com.count('T')
    if nr_c >= nr_t and nr_r > 0 and nr_t != 0:
        nr_lot += 1
print(nr_lot, maxi)
