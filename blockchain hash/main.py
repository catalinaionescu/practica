"""
Algoritmul funcționează în modul
următor: asupra unui număr natural se face următoarea transformare: dacă numărul are cel puțin două
cifre, se iau pe rând din număr câte două cifre vecine și se scade cea mai mică din cea mai mare. Cu
cifrele astfel obținute se formează un nou număr. De exemplu, pentru numărul 5734, din cifrele 5 și
7 se obține 2, din 7 și 3 se obține 4 iar din 3 și 4 se obține 1. Formăm deci un nou număr 241, căruia
i se poate aplica aceeași transformare, obținându-se 23. Din 23, prin același procedeu, obținem 1.
Dacă numărul este format dintr-o singură cifră, transformarea îl lasă nemodificat. Hash-ul se
calculează realizând succesiv transformarea asupra numărului original și apoi asupra rezultatului
obținut, de k ori, și sumând toate rezultatele parțiale și rezultatul final (excluzând valoarea de start).
Cerință
Se dau două numere naturale N şi k și apoi încă N numere naturale. Se cere să se determine valoarea
maximă a hash-ului care se va obține aplicând algoritmul de hash celor N numere folosind k pentru
numărul de iterații de transformare, conform descrierii de mai sus.
Date de intrare
La intrarea programului se prezintă pe prima linie două numere naturale N și k, separate prin spațiu.
Pe a doua linie se află cele N numere, separate tot prin spații. Liniile de intrare se încheie cu caracterul
newline (\n), obținut prin apăsarea tastei Enter.
Date de ieșire
Programul va afișa la consolă (pe stream-ul stdout) un singur număr, reprezentând valoarea maximă
dintre toate hash-urile obținute conform procedeului descris anterior.

"""

# nr are cel put 2 cifre, luam vecinele si le scadem pana se face un nr de o cifras
# N nr nat
# k nr de operatii pe care le putem face si dupa le adunam


def modifcare_nr(nr):
    nr_nou = ''
    for i in range(len(nr)-1):
        nr_nou += str(abs(int(nr[i]) - int(nr[i+1])))  # fac modul de diferenta celor doi vecini din numar
    return nr_nou


N, k = map(int, input().split())
nr = []
suma_max = 0

for i in range(N):
    nr.append(input())

for i in range(len(nr)):
    suma = 0
    j = k
    nr_mod = nr[i]
    if len(nr[i]) == 1:  # nr daca e de o cifra il adun direct
        suma += int(nr[i])
    else:
        while j:
            nr_mod = modifcare_nr(nr_mod)  # trebuie sa fac doar pentru k pasi
            suma += int(nr_mod)
            j -= 1
    if suma_max < suma:
        suma_max = suma
print(suma_max)
