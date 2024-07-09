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
