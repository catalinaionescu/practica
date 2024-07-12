"""Un studiu de marketing cerut de o galerie de artă mai excentrică a arătat că, în mod surprinzător,
clienţii analizează o perioadă mai mare de timp exponatele care au preţuri ce pot fi exprimate ca un
palindrom şi de obicei le preferă, chiar şi în cazul în care un alt obiect similar are un preţ ceva mai
scăzut. Pe de altă parte, din anumite motive (doar de ei ştiute) artiştii, care creează aceste produse,
vor ca numerele care definesc preţul unui obiect de artă sa fie atent elaborate şi să conţină doar
anumite cifree considerate de ei ca fiind foarte importante. Sub aceste constrângeri, proprietarii
galeriei de artă vor să maximizeze câştigurile şi să afişeze cele mai mari preţuri posibile în
condiţiile menţionate.
Astfel, se cere să se realizeze un program care interpretează o secvenţă de cifree nenule oferite la
intrare, în vederea obţinerii unor reprezentări zecimale (numere în bază 10). Plecând de la cifrele
oferite sunt posibile mai multe reprezentări zecimale. Dintre numerele zecimale astfel obţinute se va
alege cel mai mare număr care are proprietatea de palindrom (vedeţi explicaţiile de mai jos).
Date de intrare
La intrarea programului, pe prima linie se prezintă un număr natural n, iar pe a doua linie n cifree,
separate prin câte un spaţiu. Cu aceste cifree se pot construi numere în baza 10.
Fiecare dintre cele două linii de intrare se încheie cu caracterul newline (\n), obţinut prin apăsarea
tastei Enter.
Date de ieşire
Să se determine numărul cel mai mare de tip palindrom (în situaţia în care se pot forma mai
multe palindromuri) ce se poate forma cu toate cifrele conţinute pe a doua linie. Programul va afişa
la consolă (pe stream-ul stdout) numărul astfel determinat urmat de caracterul newline (\n) (tasta
Enter).
Dacă nu se poate forma niciun palindrom, la ieşire se va afişa cifra 0 (zero); dacă se poate forma un
singur palindrom, acesta, evident, se va afişa la ieşire ca atare.
Restricţii şi precizări
1. Numărul n este un număr natural, în gama 2 < n < 20.
2. Cifrele citite pe cea de-a doua linie sunt în gama [1; 9]."""


# palindrom max cu toate cifrele print 0 daca nu gasesc :(

def sortare(cifre):  # functie de sortare a aparitiilor cifrelor in ordine descrescatoare
    for i in range(len(cifre) - 1):
        for j in range(i+1, len(cifre)):
            if cifre[i][1] < cifre[j][1]:
                cifre[i], cifre[j] = cifre[j], cifre[i]
            elif cifre[i][1] == cifre[j][1]:
                if cifre[i][0] < cifre[j][0]:
                    cifre[i], cifre[j] = cifre[j], cifre[i]
    return cifre


n = int(input())
cifre = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]
lista = list(map(int, input().split()))
for i in lista:
    cifre[i-1][1] += 1
cifre = sortare(cifre)
counter1 = 0  # un palindrom poate avea maxim o cifra care poate sa apara doar odata, daca sunt mai multe cifre atunci nu are rost sa mai continui
criteriu = 1
palindrom = ""
cifra_jum = ""
for i in range(len(cifre)):
    if cifre[i][1] % 2 == 1:  # daca gasesc o cifra care apare de un nr impar de ori cresc counter ca sa vad cate cifre s-ar duce la mijloc
        counter1 += 1
        if counter1 > 1:  # daca e mai mare ca 1 e clar ca nu e palindrom
            criteriu = 0
            break
        elif criteriu == 1:  # daca criteriu e 1 atunci pot sa retin cifra de mijloc
            cifra_jum = str(cifre[i][0])
    for j in range(int(cifre[i][1]/2)):  # construiesc palindromul doar pe jumate la print ii adaug si inversul
        palindrom += str(cifre[i][0])

if criteriu == 1:
    print(palindrom + cifra_jum + palindrom[::-1])
else:
    print(0)
