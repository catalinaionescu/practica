"""
Fotbalul se joacă pe goluri, astfel că o
echipă este declarată câştigătoare dacă înscrie mai multe goluri decât cealaltă. Dacă ambele echipe
înscriu la fel de multe goluri, meciul este declarat remiză. Este cunoscut faptul că o victorie se
punctează cu 3 puncte, o remiză cu un punct, iar în cazul unei înfrângeri echipa în cauză nu
primeşte niciun punct. La finalul campionatului, echipele sunt ordonate în funcţie de numărul de
puncte acumulate, cea cu cele mai multe puncte câştigând trofeul.
Cerinţă
Stabiliţi clasamentul final al campionatului de fotbal pe baza rezultatelor directe între echipele
participante.
Date de intrare
Se vor citi de la tastatură (fluxul stdin) următoarele date:
 o valoare întreagă k reprezentând numărul de echipe participante, urmată de caracterul
newline (tasta Enter);
 o valoare întreagă n reprezentând numărul de meciuri disputate în campionat, urmată de
caracterul newline (tasta Enter);
 n linii reprezentând rezultatele celor n meciuri disputate, în următorul format:
<Nume echipa 1> <Numar goluri echipa 1> – <Numar goluri echipa 2> <Nume echipa 2>
Entităţile componente ale liniilor reprezentând rezultate sunt separate printr-un spaţiu, ca în
exemplul dat în final. Fiecare dintre cele n linii reprezentând rezultate este urmată de caracterul
newline (tasta Enter).
Date de ieşire
Programul va afişa pe ecran (stream-ul standard de ieşire), lista de k echipe participante, sortată în
ordinea numărului de puncte. Fiecare dintre cele k linii va avea formatul de mai jos (între entităţile
componente fiind câte un spaţiu, ca în exemplul dat în final):
<Nume echipa> <Numar puncte> <Numar goluri inscrise> < Numar goluri primite>

"""


# k nr echipe participante
# n nr meciuri
# pe n linii: <nume echipa 1> <nume echipa 2> - <nr goluri echi 1> <nr gol ech 2>
# out: <nume> <nr pct> <nr goluri inscrise> <nr goluri primite>

k = int(input())
n = int(input())
fotbal = {}  # fotbal['ro'] = [scor, gol inscris, gol prim]
for i in range(n):
    txt = list(input().split())
    del txt[2]  # sterg linia
    if txt[0] not in fotbal.keys():
        fotbal[txt[0]] = [0, 0, 0]  # creez valori daca nu gasesc tara in dict
        fotbal[txt[3]] = [0, 0, 0]
    fotbal[txt[0]][1] += int(txt[1])  # adun goluri date pt prima tara
    fotbal[txt[0]][2] += int(txt[2])  # adun goluri primte pt prima tara
    fotbal[txt[3]][1] += int(txt[2])    # goluri date pt a doua tara
    fotbal[txt[3]][2] += int(txt[1])  # goluri prim pt a doua tara
    if txt[1] == txt[2]:
        fotbal[txt[0]][0] += 1  # scor cand e = primesc amandoua tarile 1 pct
        fotbal[txt[3]][0] += 1
    elif txt[1] > txt[2]:
        fotbal[txt[0]][0] += 3
    else:
        fotbal[txt[3]][0] += 3

for key, value in fotbal.items():
    print(key, value[0], value[1], value[2])
