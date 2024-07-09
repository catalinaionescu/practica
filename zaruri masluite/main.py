"""
Costică a ales un zar și s-a apucat să îl testeze
aruncând cu el și notând de câte ori a picat fiecare față. Încearcă apoi să-și dea seama dacă zarul e
măsluit sau nu, considerând că diferența dintre numărul maxim de apariții a unei fețe și numărul
minim de apariții (a oricăror alte fețe) nu trebuie să depășească 10% din numărul total de aruncări.
Cerinţă
Dându-se un număr N de aruncări cu zarul și apoi N numere naturale în intervalul [1:6] reprezentând
numerele obținute la aruncări, să se determine dacă zarul e măsluit conform condiției de mai sus.
Date de intrare
De la intrare (fluxul stdin) de pe prima linie se citește numărul natural N, reprezentând numărul de
aruncări cu zarul. Pe următoarele N linii se află câte un număr natural în intervalul [1:6] reprezentând
numerele obținute la aruncări.
Date de ieşire
La ieşire (fluxul stdout) se va afișa un singur număr, 0 sau 1, 0 dacă zarul e normal, și 1 dacă este
măsluit.
"""

# dif nr max de ap unei fete si nr min de ap < 10% din nr tot de aruncari

n = int(input())
dictio = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for i in range(n):
    x = int(input())
    dictio[x] += 1
if max(dictio.values()) - min(dictio.values()) > n/10:
    print(1)
else:
    print(0)
