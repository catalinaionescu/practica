# zaruri suma fete care nu se vad
# prima linie n zaruri suprapuse
# 2 linie 5 fete viz pentru zar de sus
#  next linii 4 fete vizibile

n = int(input())
lista = []
sum_tot_zaruri = n * 6 * 7 / 2
sum_fete = 0
for i in range(n):
    lista = input().split()
    lista = map(int, lista)
    sum_fete += sum(lista)

print("%d" % (sum_tot_zaruri - sum_fete))
