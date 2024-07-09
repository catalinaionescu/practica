# prima linie prop
# 2 linie caractere per

txt = list(input())
tab = input().split()
dictio = {}
for i in tab:
    (key, value) = i.split(',')
    dictio[key] = value
for i in range(len(txt)):
    if dictio.get(txt[i]) != None:
        txt[i] = dictio[txt[i]]
print(''.join(txt), '\n')
