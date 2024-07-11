"""
Pentru a valida că generatorul poate fi folosit în algoritmi criptografici (cryptographically secure)
trebuie să implementați și să rulați o baterie de teste. Unul din aceste teste verifică numărul de apariții
pentru secvențe de 1 de diferite lungimi. Pentru ca secvența de biți generată să fie aleatoare, trebuie
ca numărul de apariții pentru fiecare lungime de secvență de 1 să aibă o anumită distribuție statistică.
Mai precis, trebuie ca numărul de secvențe de un bit 1 să fie mai mare sau egal decât numărul de
secvențe de doi biți 1 care trebuie să fie mai mare sau egal decât numărul de secvențe de trei biți 1,
șamd.
Cerință
Dându-se un număr n reprezentând numărul de biți generat de RNG și secvența de n biți, să se
calculeze numărul de apariții pentru fiecare lungime de secvență de biți 1 și să se decidă dacă
generatorul este valid sau nu.
Date de intrare
Pe prima linie se află n, numărul de biți generați. Pe a doua linie se află o secvență continuă de n biți
(valori de 0 sau 1), ne-separați prin spații.
Date de ieșire
Programul va afișa în consolă (pe stream-ul stdout) pe prima linie o secvență de numere întregi
pozitive, separate prin spațiu, reprezentând numărul de apariții pentru fiecare lungime de secvență de
biți 1, începând cu numărul de apariții pentru o secvență de un singur bit 1 (delimitat de biți 0) și
terminând cu ultimul număr de apariții nenul. Pe a doua linie se va afișa valoarea 1 dacă generatorul
este valid sau 0 dacă nu este.

"""

# nr secv de 1 bit de 1 >= nr secv de 2 biti de 1 etc
# n nr biti gen RNG
# calc lung secv
# 1 linie nr aparatii pt fiecare lung de secv inc cu ap de 1

n = int(input())
sir = input()
nr_ap = {1: 0}
i = 0
if int(sir[len(sir)-1]) == 1:  # verific daca ultimul element
    nr_ap[1] += 1
while i < len(sir):
    j = i
    contor = 0
    criteriu = 0
    if i < len(sir) - 1:
        if int(sir[i]) == 1 and int(sir[i+1]) == 0:  # cand apare doar unu de 1
            nr_ap[1] += 1
        else:
            contor = 1
            while int(sir[j]) == int(sir[j+1]) == 1:  # verifica succesiunea de 1
                contor += 1
                criteriu = 1
                if j == len(sir) - 2:
                    break
                else:
                    j += 1
    if contor not in nr_ap.keys() and contor > 1:  # le init cu 0 cheile in dict
        nr_ap[contor] = 0
    if contor > 1 and criteriu == 1:
        nr_ap[contor] += 1  # cresc val ap cu 1
    i = j
    i += 1

for i in range(1, max(nr_ap.keys())):  # val care nu s au inregistrat le init cu 0
    if i not in nr_ap.keys():
        nr_ap[i] = 0
criteriu = 1
for i in range(1, max(nr_ap.keys())):  # caut sa vad daca se indeplineste criteriul
    print(nr_ap[i], end=' ')
    if nr_ap[i] < nr_ap[i+1]:
        criteriu = 0
print(nr_ap[max(nr_ap.keys())])  # afisez ultima valoare
print(criteriu)