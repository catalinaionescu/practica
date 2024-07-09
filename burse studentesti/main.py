"""Doamna secretară trebuie să stabilească numărul de studenți ce vor lua bursă de merit în anul
universitar următor și să identifice studentul care va lua bursa de performanță (există o singură bursă
de performanță). Are la dispoziție lista tuturor studenților și notele obținute de aceștia la diversele
discipline. Bursa de performanță se acordă studentului integralist cu media cea mai mare. Bursele de
merit se acordă în ordinea descrescătoare a mediilor, în limita numărului maxim de burse, tuturor
studenților integraliști care au media generală peste 8.00.
Cerinţă
Stabiliți ce student va lua bursă de performanță și câți studenți vor lua bursă de merit în anul
universitar următor.
Date de intrare
Se vor citi de la tastatură (fluxul stdin) următoarele date:
• Trei numere întregi pozitive m, n, p separate prin spaţiu, reprezentând
o m – numărul de studenţi,
o n – numărul de discipline,
o p – numărul de burse de merit disponibile;
• 2*m linii de pe care se citesc, în ordine, în formatul:
o <NS>, un şir de caractere reprezentând numele studentului;
o <N1> <N2> ... <Nn>, n numere întregi din intervalul 1 – 10 separate prin spaţiu
reprezentând notele obţinute de respectivul student la cele m discipline;
Toate liniile conţinând date de intrare sunt finalizate cu caracterul newline (tasta Enter).
Date de ieşire
Programul va afișa pe ecran (stream-ul standard de ieșire):
• Pe prima linie: numărul de studenți ce vor lua bursă de merit
• Pe a doua linie: numele studentului care va lua bursă de performanță și media media lui (număr
fracționar cu 2 zecimale) separate prin spațiu.
"""
# burse med descr stud integr cu med > 8
# m nr stud
# n nr discipline
# p nr de burse
# 2*m linii <NS> nume stud next linie: notele <Nn>

linie_inp = input()
m, n, p = map(int, linie_inp.split())
catalog = {}
for i in range(m):
    name = input()
    note = input().split()
    note = list(map(int, note))
    catalog[name] = note
maxim = 8
contor = 0
for key, value in catalog.items():
    criteriu = 1
    med = 0
    for i in value:
        if i < 5:
            criteriu = 0
            break
        med += float(i/n)
    if criteriu == 1 and med > 8:
        contor += 1
        if med > maxim:
            maxim = med
            name = key

if contor > p:
    print(p)
else:
    print(contor - 1)
print(f"{name} {maxim:.2f}")
