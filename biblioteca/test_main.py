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


class Biblioteca:
    def __init__(self, D, k, carti):
        self.D = D
        self.k = k
        self.carti = carti

    def caut_carti(self):
        lista_raft = []
        raft = []
        capacitate  = self.D
        for i in range(len(self.carti)):
            nr_carti, pagini = self.carti[i]
            while nr_carti:
                if pagini >= capacitate:
                    raft.append(pagini)
                    capacitate -= pagini
                    nr_carti -= 1
                    self.carti[i] = nr_carti, pagini
            if nr_carti == 0:
                self.carti[i] = [0, 0]
            lista_raft.append(raft)
        return lista_raft

def test_1():
    D = 200
    k = 5
    carti = [[2, 1300], [4, 120], [2, 80], [3, 60], [7, 50]]
    rafturi = Biblioteca(D, k, carti)
    assert rafturi.caut_carti() == [[130, 60],
                                      [130, 60],
                                      [120, 80],
                                      [120, 80],
                                      [120, 60],
                                      [120, 50],
                                      [50, 50, 50, 50],
                                      [50, 50]]


# voiam sa scot direct din lista cartile care s-au pus pe raft si sa fac while in carti doar ca mi a dat eroare, imi zicea ca e out of range

def test_2():
    D = 200
    k = 5
    carti = [[2, 130], [4, 120], [2, 80], [3, 60], [7, 50]]
    rafturi = Biblioteca(D, k, carti)
    assert rafturi.caut_carti() == [[130, 60],
                                      [130, 60],
                                      [120, 80],
                                      [120, 80],
                                      [120, 60],
                                      [120, 50],
                                      [50, 50, 50, 50],
                                      [50, 50]]


test_1()
test_2()
