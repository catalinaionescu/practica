"""
Date de intrare
Secvenţa de intrare este formată din linii terminate de caracterul newline (\n), generat prin apăsarea
tastei Enter. Fiecare linie este formată din 3 şiruri de caractere separate de spaţiu. Structura fiecărei
linii este ilustrată generic în cele ce urmează:
String1 String2 String3
unde String1, String2 şi String3 sunt şiruri de caractere a căror structură va fi descrisă în continuare.
Logica internă
Programul va verifica dacă, luate împreună, cele 3 şiruri de caractere din fiecare linie reprezintă un
număr de înmatriculare valid, folosind următoarele reguli:
 Valorile valide pentru String1 sunt: AB, AR, AG, B, BC, BH, BN, BT, BV, BR, BZ, CS,
CL, CJ, CT, CV, DB, DJ, GL, GR, GJ, HR, HD, IL, IS, IF, MM, MH, MS, NT, OT, PH,
SM, SJ, SB, SV, TR, TM, TL, VS, VL, VN (atenţie: doar litere mari!)
 String2 e format din 2 sau 3 caractere numerice (numărul de caractere numerice nu este
condiţionat de valoarea String1)
 String3 e format din exact 3 caractere litere mari
Date de ieşire
Programul trebuie să afişeze la ieşire, în consolă (pe stream-ul stdout), exclusiv liniile de intrare
care reprezintă un număr de înmatriculare valid conform regulilor de mai sus. Liniile ce conţin
numere valide nu vor fi modificate în niciun fel, iar ordinea lor va fi păstrată. Fiecare dintre liniile
afişate va fi terminată de caracterul newline (\n).
"""
import sys


def check_str2(str2):
    for i in range(len(str2)):
        if '0' <= str2[i] <= '9':
            continue
        else:
            return 0
    return 1


txt = sys.stdin.read()
linii = txt.splitlines()
judete = "AB, AR, AG, B, BC, BH, BN, BT, BV, BR, BZ, CS, CL, CJ, CT, CV, DB, DJ, GL, GR, GJ, HR, HD, IL, IS, IF, MM, MH, MS, NT, OT, PH, SM, SJ, SB, SV, TR, TM, TL, VS, VL, VN"
judete = judete.split(", ")

for i in range(len(linii)):
    linie_curenta = linii[i].split()
    String1 = linie_curenta[0]
    String2 = linie_curenta[1]
    String3 = linie_curenta[2]
    criteriu = 1
    if String1 in judete and check_str2(String2) and 2 <= len(String2) <= 3:
        for j in String3:
            if j.isupper() == 0:
                criteriu = 0
                break
    else:
        criteriu = 0
    if criteriu == 1:
        print(String1, String2, String3)
