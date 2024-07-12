import sys
"""Scrieți un program care să ajute la detectarea trișorilor. În cazul în care se detectează că o carte apare
de prea multe ori, programul va afișa cartea și va opri jocul.
Date de intrare
Se vor citi de la tastatură (fluxul stdin) următoarele date:
• Pe prima linie se află numărul n, reprezentând numărul maxim de mâini ce vor fi jucate;
• Pe următoarele n linii se află cartea jucată, în formatul:
<număr_carte> <semn_carte>
Date de ieşire
În cazul în care nimeni nu încearcă să trișeze se va afișa textul JOC OK. În cazul în care cineva a
încercat sa trișeze, se va afișa cartea problemă în același format ca la intrare: numărul cărții urmat de
semn, separate prin spațiu. """

"""de facut: inlocuit input cu trimisul datelor din fisiere
fis sa fie argum la momentul rularii adica main.py joc1.txt 
de uit la mod sys.args sys.argv
"""
# n = int(input())
nume_fisier = sys.argv[1]
print(sys.argv[0], nume_fisier)
with open(nume_fisier, 'r') as file:
    lines = file.readlines()

n = int(lines[0].strip())  # strip da remove la white space la inc si sf
m = {}
ok = 0

for i in range(1, n + 1):
    key = lines[i].strip()
    if key not in m:
        m[key] = 0
    m[key] += 1
    if m[key] > 1 and ok == 0:  # Change 2 to 1 for detecting immediate repeat
        sus = key
        ok = 1
        break

if ok == 1:
    print(sus)
else:
    print("JOC OK")

# for i in range(n):
#     key = input()
#     if key not in m:
#         m[key] = 0
#     m[key] += 1
#     if m[key] > 2 and ok == 0:
#         sus = key
#         ok = 1
#         break
#
# if ok == 1:
#     #print(f'\n{sus}')
#     print('\n', sus, sep='')
# else:
#     print("JOC OK")
