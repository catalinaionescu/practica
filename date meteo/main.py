"""Meteorologii notează pe parcursul a N zile
consecutive temperaturile maxime zilnice şi sunt interesaţi să determine cea mai lungă perioadă de
timp în care temperaturile înregistrate în zile consecutive au alternat ca semn, precum și statistica
valorilor pozitive vs. negative de pe parcursul celor N zile.
Cerinţă
Scrieţi un program care, pe baza temperaturilor înregistrate pe parcursul a N zile consecutive,
determină o secvenţă de zile având lungime maximă, pentru care temperaturile înregistrate au alternat
ca semn. Dacă există mai multe astfel de secvenţe, meteorologii sunt interesaţi de cea mai recentă.
Dacă nu există măcar două zile consecutive cu temperaturi alternante ca semn, ei vor înregistra
rezultatul 0, neavând date suficiente pentru calcule suplimentare. În plus, meteorologii sunt interesați
și de procentul valorilor pozitive și negative înregistrate pe parcursul celor N zile.
Date de intrare
De la intrare (fluxul stdin) de pe prima linie se citește numărul natural N, reprezentând numărul total
de zile pentru care se efectuează studiul. Pe cea de-a doua linie se prezintă N numere întregi separate
prin spaţii, al i-lea număr de pe linie reprezentând temperatura maximă înregistrată în ziua i a studiului
(1 ≤ i ≤ N).
Date de ieşire
La ieşire (fluxul stdout) pe prima linie se afişează numărul natural NrMax, reprezentând numărul
maxim de zile consecutive pentru care temperaturile au alternat ca semn. Pe cea de a doua linie vor fi
scrise NrMax valori întregi, separate prin spaţii, reprezentând temperaturile (alternante ca semn)
înregistrate în cele NrMax zile. Dacă există mai multe secvenţe cu acelaşi NrMax, va fi afişată cea
mai recentă dintre acestea. Pe ultima linie se afișează procentele, calculate cu două zecimale exacte
prin rotunjire, aferente valorilor negative și pozitive de temperatură identificate pe parcursul celor N
zile, în felul următor:
+:AB.CD% -:EF.GH%
Aceste procente se calculează ca raport între numărul valorilor pozitive sau negative și totalul
valorilor înregistrate. Afişarea se face cu două zecimale exacte prin rotunjire. Nu se va face
completarea cu 0 dacă partea întreagă a procentului calculat conține o singură cifră.
În cazul în care nu există măcar două zile consecutive cu temperaturi alternante ca semn, la ieşire se
va afişa o singură linie, pe care va fi scrisă valoarea 0. Nici o altă afişare nu va mai fi făcută în acest
caz. Toate valorile afișate sunt urmate de caracterul linie nouă (‘\n’) obținut prin apăsarea tastei Enter."""


# N zile consecutive
# det secv de lung max pt care temp au alternat ca semn
# daca sunt mai multe secvente o iau pe cea mai recenta
# daca nu ex macar 2 zile consec print 0
# proc val poz si neg
# NrMax nr max de zile consec prima linie
# nex linie val in interval
# ult linie proc cu 2 zec exacte

def semn_nr(nr):
    if nr < 0:
        return False  # negativ
    else:
        return True  # pozitiv


N = int(input())
temp = list(map(int, input().split()))
nr_poz = nr_neg = 0
for i in temp:
    if semn_nr(i):
        nr_poz += 1
    else:
        nr_neg += 1
contor = 1
i = 0
secv_max = 0
while i < len(temp) - 1:
    j = i
    while semn_nr(temp[j]) != semn_nr(temp[j + 1]):
        contor += 1
        if j == len(temp) - 2:  # daca j ajunge la penultimul element nu trebuie sa treaca de el, da eroare
            break
        else:
            j += 1
    if contor >= secv_max:
        secv_max = contor
        secv = temp[i:j + 1]
        contor = 0
    if j < len(temp) - 1:
        i = j
    i += 1
proc_p = float(nr_poz / len(temp) * 100)
proc_n = float(nr_neg / len(temp) * 100)
print(f'{len(secv)}\n{" ".join(map(str, secv))}')
print(f'+:{proc_p:.2f}% -:{proc_n:.2f}%')
