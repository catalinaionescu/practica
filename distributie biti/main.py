# 2 cate 2 biti
# r1 rap nr ap per m m/m put
# r2 rap frec bit/put bit
# amandoua mai mici sau eg cu 110% out e 1

n = int(input())
dig = input()
l = []
dic = {'count_00': 0, 'count_01': 0, 'count_10': 0, 'count_11': 0}
for i in dig:
    l.append(int(i))

if l.count(0) > l.count(1):
    try:
        r2 = l.count(0) / l.count(1)
    except ZeroDivisionError:
        r2 = float('inf')
else:
    try:
        r2 = l.count(1) / l.count(0)
    except ZeroDivisionError:
        r2 = float('inf')

for i in range(0, len(l) - 1, 2):
    if str(l[i]) + str(l[i + 1]) == '00':
        dic['count_00'] += 1
    elif str(l[i]) + str(l[i + 1]) == '01':
        dic['count_01'] += 1
    elif str(l[i]) + str(l[i + 1]) == '10':
        dic['count_10'] += 1
    else:
        dic['count_11'] += 1
mini = 5000
for i in dic.values():
    if i < mini and i != 0:
        mini = i
if l.count(1) != 0 and l.count(0) != 0:
    try:
        r1 = float(max(dic.values()) / mini)
    except ZeroDivisionError:
        r1 = float('inf')
else:
    r1 = float('NaN')
print(f"{r1:.2f} {r2:.2f}")
if r1 == 'inf' or 'r2' == 'inf':
    print(0)
elif r1 and r2 <= 1.1:
    print(1)
else:
    print(0)