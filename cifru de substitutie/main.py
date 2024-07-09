
"""
Cerinţă
Dându-se un text de intrare şi un tabel de substituţie, să se scrie un program care să cripteze textul
de intrare.
Date de intrare
Pe prima linie citită de la tastatură (stream-ul stdin) se află textul de intrare. Pe următoarea linie se
află perechi de câte două caractere: caracterul din textul de intrare şi caracterul cu care acesta
trebuie înlocuit. Cele două caractere sunt separate prin virgulă şi perechile sunt separate prin spaţiu.
Doar literele mici (26), literele mari (26) şi cifrele (10) se vor înlocui în text, în total tabelul de
substituţie are deci 62 de elemente. Lungimea maximă a textului este de 1000 de caractere. Ambele
linii se termină cu apăsarea tastei Enter (caracterul newline, \n).
Date de ieşire
Programul va afişa pe ecran (stream-ul standard de ieşire), pe o singură linie, textul criptat. Din
textul de intrare se vor înlocui doar literele mici şi mari şi cifrele, restul caracterelor rămânând
nemodificate. Linia se termină obligatoriu cu caracterul newline (\n).
"""



# prima linie prop
# 2 linie caractere per

txt = list(input())
tabel = input().split()
dictio = {}
for i in tabel:
    (key, value) = i.split(',')
    dictio[key] = value
for i in range(len(txt)):
    if dictio.get(txt[i]) != None:
        txt[i] = dictio[txt[i]]
print(''.join(txt), '\n')
