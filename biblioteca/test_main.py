"""
Bibliotecara știe
că are un număr suficient de rafturi încât să pună toate cărțile. Pe fiecare raft încap cărți însumând în
total D pagini. De asemenea, ştie câte cărţi cu un anumit număr de pagini există în bibliotecă. Dat
fiind acestea şi urmărind să ocupe cât mai puţine rafturi, bibliotecara şi-a propus să aranjeze cărţile
pe rafturi:
i. raft după raft,
ii. alegând întotdeauna să completeze raftul curent cu cea mai groasă carte disponibilă,
iii. trecând la următorul raft numai în condiţiile în care pe raftul curent nu mai poate fi plasată
nicio carte dintre cele rămase şi
iv. asigurându-se că a plasat pe rafturi toate cărţile.
Cerinţă
Scrieţi un program care o poate ajuta pe bibliotecară să aranjeze cărţile pe rafturi în mod eficient,
conform regulilor enunţate mai sus.
Date de intrare
Se vor citi de la tastatură (fluxul stdin) următoarele date:
• de pe prima linie: două numere întregi D şi k, separate prin spaţiu, reprezentând D –
dimensiunea rafturilor exprimată în număr de pagini, k – numărul de dimensiuni diferite
pentru cărţile ce trebuie aranjate în bibliotecă;
• de pe următoarele k linii: câte două numere întregi n şi p, reprezentând numărul de cărţi n de
grosime p pagini ce trebuie aranjate în bibliotecă.
Cele k linii ce conțin informații despre cărți sunt date în ordinea inversă a grosimii p.
Toate liniile conţinând date de intrare sunt finalizate cu caracterul newline (tasta Enter).
Date de ieşire
Programul va afişa pe ecran (stream-ul standard de ieşire) m linii, corespunzătoare celor m rafturi pe
care a fost plasată cel puţin o carte, în ordinea completării lor (conform regulilor). Fiecare dintre cele
m linii va conţine o serie de numere întregi, separate prin spaţiu, reprezentând dimensiunile cărţilor
ce au fost plasate pe acel raft, în ordinea plasării lor pe raft (conform regulilor).
"""


# raft dupa raft
# completez raft cu cea mai groasa carte
# next raft daca nu mai pot pune nicio carte
# toate cartile pe raft
# prima linie D - dim raft expr in nr pag si k - nr de dim dif pt carti
# k linii: 2 nr n - nr carti de grosime p pag
# out m linii rafturi: dim carti si ordine plasare


# class Biblioteca:
#     def __init__(self, D, k, carti):
#         self.D = D
#         self.k = k
#         self.carti = carti
#
#     def caut_carti(self):
#         lista_raft = []
#         raft = []
#         capacitate = self.D
#         for i in range(len(self.carti)):
#             nr_carti, pagini = self.carti[i]
#             while nr_carti:
#                 if pagini >= capacitate:
#                     raft.append(pagini)
#                     capacitate -= pagini
#                     nr_carti -= 1
#                     self.carti[i] = nr_carti, pagini
#             if nr_carti == 0:
#                 self.carti[i] = [0, 0]
#             lista_raft.append(raft)
#         return lista_raft


import pytest
import pdb


def caut_carti(D, k, carti):
    # pdb.set_trace()
    lista_rafturi = []
    if len(carti) != k:
        raise ValueError('difera nr de intrari fata de k dat')
    for i in carti:
        if i[1] < 0 or D < 0:
            raise ValueError('nr invalid')
    i = 0
    while i < len(carti):
        raft = []
        pagini = carti[i][1]
        if pagini > D:
            raise ValueError('Prea multe pagini')
        nr_pagini_raft = pagini
        carti[i][0] -= 1
        if carti[i][0] >= 0:
            raft.append(pagini)
        for j in range(i, len(carti)):
            while nr_pagini_raft + carti[j][1] <= D and carti[i][0] >= 0 and carti[j][0] > 0:
                nr_pagini_raft += carti[j][1]
                carti[j][0] -= 1
                raft.append(carti[j][1])
        if len(raft) > 0:
            lista_rafturi.append(raft)
        if carti[i][0] <= 0:
            carti[i][0] = -1
            i += 1
    return lista_rafturi


def test_1():
    D = 200
    k = 5
    carti = [[2, 130], [4, 120], [2, 80], [3, 60], [7, 50]]
    assert caut_carti(D, k, carti) == [[130, 60], [130, 60], [120, 80], [120, 80], [120, 60], [120, 50], [50, 50, 50, 50], [50, 50]]


def test_2():
    D = 200
    k = 4
    carti = [[2, 130], [4, 120], [2, 80], [3, 60], [7, 50]]
    with pytest.raises(ValueError, match='difera nr de intrari fata de k dat') as excinfo:
        caut_carti(D, k, carti)
    print(excinfo.value)


def test_3():
    D = 200
    k = 5
    carti = [[2, 1300], [4, 120], [2, 80], [3, 60], [7, 50]]
    with pytest.raises(ValueError, match='Prea multe pagini') as excinfo:
        caut_carti(D, k, carti)
    print(excinfo.value)

def test_4():
    D = 0
    k = 5
    carti = [[2, -1], [4, -1], [2, -1], [3, -1], [7, -1]]
    with pytest.raises(ValueError, match='nr invalid') as excinfo:
        caut_carti(D, k, carti)
    print(excinfo.value)
