n = int(input())
m = {}
ok = 0
for i in range(n):
    key = input()
    if key not in m:
        m[key] = 0
    m[key] += 1
    if m[key] > 2 and ok == 0:
        sus = key
        ok = 1

if ok == 1:
    print(sus)
else:
    print("JOC OK")


