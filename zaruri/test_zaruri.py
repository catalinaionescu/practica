"""
Cerinţă
Dându-se un număr N de zaruri și valorile de pe fețele vizibile ale zarurilor, calculați suma tuturor
fețelor care nu se văd. Se ignoră ordinea reală a numerelor pe fețele zarurilor, adică cele 6 numere
pot apărea pe zar în orice aranjament.
Date de intrare
De la intrare (fluxul stdin) de pe prima linie se citește numărul natural N, reprezentând numărul de
zaruri suprapuse. Pe cea de-a doua linie se află 5 numere naturale distincte în intervalul [1; 6]
reprezentând cele 5 fețe vizibile pentru zarul de sus, apoi pe următoarele N-1 linii se află 4 numere
de același fel, reprezentând cele 4 fețe vizibile ale zarurilor.
Date de ieşire
La ieşire (fluxul stdout) se va afișa un singur număr întreg pozitiv ce reprezintă suma fețelor invizibile
ale zarurilor.

"""

# zaruri suma fete care nu se vad
# prima linie n zaruri suprapuse
# 2 linie 5 fete viz pentru zar de sus
#  next linii 4 fete vizibile
import pytest


def suma_fete(n, nr):
    if not 1 <= n <= 100:
        raise ValueError('n trebuie sa fie intre 1 si 100')
    sum_tot_zaruri = n * 6 * 7 / 2
    suma_zaruri = 0
    for i in nr:
        for j in i:
            suma_zaruri += j
            if not 1 <= j <= 6:
                raise ValueError('fata are numar invalid')
    suma_fina = sum_tot_zaruri - suma_zaruri
    if suma_fina < 0:
        raise ValueError('suma este mai mica decat 0')
    return suma_fina


def test_suma_fete_1():
    n = 4
    lista = [[1, 3, 2, 5, 6], [6, 4, 1, 5], [1, 4, 3, 5], [6, 5, 4, 3]]
    assert suma_fete(n, lista) == 20


def test_suma_fete_2():
    n = 2
    lista = [[1, 2, 3, 4, 5], [1, 2, 3, 4]]
    assert suma_fete(n, lista) == 17

def test_suma_fete_3():
    n = 101
    lista = [[1, 2, 3, 4, 5], [1, 2, 3, 4]]
    with pytest.raises(ValueError, match='n trebuie sa fie intre 1 si 100') as excinfo:
        suma_fete(n, lista)
    print(excinfo.value)


def test_suma_fete_4():
    n = 2
    lista = [[1, 2, 3, 4, 8], [1, 2, 3, 4]]
    with pytest.raises(ValueError, match='fata are numar invalid') as excinfo:
        suma_fete(n, lista)
    print(excinfo.value)
