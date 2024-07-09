"""
Împreună cu echipa de la firmă ați inventat un nou algoritm de generare de numere pseudo-aleatoare.
Pentru a valida că generatorul poate fi folosit în algoritmi criptografici (cryptographically secure)
trebuie să implementați și să rulați o baterie de teste. Unul din aceste teste verifică numărul de apariții
pentru fiecare secvență posibilă de doi biți: 00, 01, 10 și 11 cât și raportul între numărul de biți de 0
și de 1. Pentru ca secvența de biți să fie aleatoare, trebuie ca numărul de apariții pentru fiecare din
cele patru perechi să fie aproximativ egale și în același timp numărul de biți de 0 să fie aproximativ
egal cu cei de 1. Mai precis, trebuie ca raporturile R1 dintre numărul de apariții a perechii care apare
de cele mai multe ori și numărul de apariții a perechii care apare de cele mai puține ori, cât și raportul
R2 între numărul de apariții ale celui mai frecvent bit și numărul de apariții ale celui mai puțin frecvent
bit să fie mai mici sau egale cu 110%.
Cerință
Dându-se un număr n reprezentând numărul de biți generat de RNG și secvența de n biți, să se
calculeze raporturile R1 și R2 și să se decidă dacă generatorul este valid sau nu.
Date de intrare
Pe prima linie se află n, numărul de biți generați. Pe a doua linie se află o secvență continuă de n biți
(valori de 0 sau 1), ne-separați prin spații.
Date de ieșire
Programul va afișa în consolă (pe stream-ul stdout) pe prima linie raporturile R1 și R2 calculate
conform descrierii, valori fracționare cu două zecimale, separate prin spațiu, iar pe a doua linie
valoarea 1 dacă generatorul este valid sau 0 dacă nu este.
"""


# 2 cate 2 biti
# r1 rap nr ap per m m/m put
# r2 rap frec bit/put bit
# amandoua mai mici sau eg cu 110% out e 1

n = int(input())
digits = input()
lista = []
dictio = {'count_00': 0, 'count_01': 0, 'count_10': 0, 'count_11': 0}
for i in digits:
    lista.append(int(i))
if lista.count(0) > lista.count(1):
    try:
        r2 = lista.count(0) / lista.count(1)
    except ZeroDivisionError:
        r2 = float('inf')
else:
    try:
        r2 = lista.count(1) / lista.count(0)
    except ZeroDivisionError:
        r2 = float('inf')  # am scris o exceptie pt ca imi da eroare cand am 1/0

for i in range(0, len(lista) - 1, 2):
    if str(lista[i]) + str(lista[i + 1]) == '00':
        dictio['count_00'] += 1
    elif str(lista[i]) + str(lista[i + 1]) == '01':
        dictio['count_01'] += 1
    elif str(lista[i]) + str(lista[i + 1]) == '10':
        dictio['count_10'] += 1
    else:
        dictio['count_11'] += 1
mini = 5000
for i in dictio.values():  # val dictionarului sunt nr de ap ale grupurilor de biti
    if i < mini and i != 0:
        mini = i
if lista.count(1) != 0 and lista.count(0) != 0:
    try:
        r1 = float(max(dictio.values()) / mini)
    except ZeroDivisionError:
        r1 = float('inf')
else:
    r1 = float('NaN')  # exceptie pentru cand e doar 1 sau 0
print(f"{r1:.2f} {r2:.2f}")
if r1 == 'inf' or 'r2' == 'inf':
    print(0)
elif r1 and r2 <= 1.1:
    print(1)
else:
    print(0)
