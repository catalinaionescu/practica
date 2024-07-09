# burse med descr stud integr cu med > 8
# m nr stud
# n nr disc
# p nr de burse
# 2*m linii <NS> nume stud next linie: notele <Nn>

linie_inp = input()
m, n, p = map(int, linie_inp.split())
catalog = {}
for i in range(m):
    name = input()
    note = input().split()
    note = list(map(int, note))
    catalog[name] = note
maxi = 8
contor = 0
for key, value in catalog.items():
    ok = 1
    med = 0
    for i in value:
        if i < 5:
            ok = 0
            break
        med += float(i/n)
    if ok == 1 and med > 8:
        contor += 1
        if med > maxi:
            maxi = med
            name = key

if contor > p:
    print(p)
else:
    print(contor - 1)
print(f"{name} {maxi:.2f}")
