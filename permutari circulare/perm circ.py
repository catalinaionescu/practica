n = int(input())
bin = []
while n > 0:
    m = int(n % 2)
    bin.append(m)
    n = int(n / 2)
bin = bin[::-1]
maxi = 0
for i in range(len(bin)):
    m = bin[len(bin) - 1]
    bin.insert(0, m)
    bin.pop()
    new = 0
    for j in range(len(bin)):
        new += bin[j] * pow(2, j)
    if new > maxi:
        maxi = new

print(maxi)
