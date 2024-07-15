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

def caut_carti(D, carti, nr_carti):
    for i in range(len(carti)):
            for j in range(carti[i][0]):
                if carti[i][1] <= D and carti[i][0] > 0:  # carti[i][0] e nr de carti si carti[i][1] e nr de pagini
                    print(carti[i][1], end=" ")
                    D -= carti[i][1]
                    carti[i][0] -= 1
                    nr_carti -= 1
                    if carti[i][0] < 0:  # daca nu mai am carti opresc cautarea
                        break
                if carti[i][1] > D:  # daca o carte are prea multe pagini opresc cautarea si trec la urmatoarea
                    break
    print()
    return nr_carti


D, k = map(int, input().split())
carti = []
nr_carti = 0
for i in range(k):
    carti.append(list(map(int, input().split())))
    nr_carti += carti[i][0]  # am facut suma tot a cartilor ca sa imi fie mai usor sa le scad
while nr_carti:
    nr_carti = caut_carti(D, carti, nr_carti)

# voiam sa scot direct din lista cartile care s-au pus pe raft si sa fac while in carti doar ca mi a dat eroare, imi zicea ca e out of range