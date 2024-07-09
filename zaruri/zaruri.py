"""
Cerinţă
Dându-se un număr N de zaruri și valorile de pe fețele vizibile ale zarurilor, calculați suma tuturor
fețelor care nu se văd. Se ignoră ordinea reală a numerelor pe fețele zarurilor, adică cele 6 numere
pot apărea pe zar în orice aranjament.
Date de intrare
De la intrare (fluxul stdin) de pe prima linie se citește numărul natural N, reprezentând numărul de
zaruri suprapuse. Pe cea de-a doua linie se află 5 numere naturale distincte în intervalul [1; 6]
reprezentând cele 5 fețe vizibile pentru zarul de sus, apoi pe următoarele N-1 linii se află 4 numere
de același fel, reprezentând cele 4 fețe vizibile ale zarurilor.
Date de ieşire
La ieşire (fluxul stdout) se va afișa un singur număr întreg pozitiv ce reprezintă suma fețelor invizibile
ale zarurilor.

"""

# zaruri suma fete care nu se vad
# prima linie n zaruri suprapuse
# 2 linie 5 fete viz pentru zar de sus
#  next linii 4 fete vizibile

n = int(input())
lista = []
sum_tot_zaruri = n * 6 * 7 / 2
sum_fete = 0
for i in range(n):
    lista = input().split()
    lista = map(int, lista)
    sum_fete += sum(lista)
print("%d" % (sum_tot_zaruri - sum_fete))
