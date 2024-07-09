# • lconst <dst> <val> – se scrie valoarea <val> în registrul <dst>;
# • add <dst> <src0> <src> – se adună valorile din registrele <src0> și <src1> și rezultatul se
# scrie în registrul <dst>;
# • mul <dst> <src0> <src> – se înmulțesc valorile din registrele <src0> și <src1> și rezultatul se
# scrie în registrul <dst>;
# • div <dst> <src0> <src> – se împart valorile din registrele <src0> și <src1> și câtul se scrie în
# registrul <dst>;
# • print <reg> - se afișează valoarea din registrul <reg>.
# Dacă la execuția unei instrucțiuni de tip div împărțitorul este zero, se va afișa fraza Exception: line
# <index>, unde index reprezintă a câta instrucțiune nu a putut fi executată, iar programul se va încheia.
# Toate registrele au inițial valoarea 0.
# cit n comenzi

n = int(input())
lcom = []
for i in range(n):
    lcom.append(input())
com = []
reg = {}
# reg.values val reg
# reg.keys nume reg
ok = 1
for index, i in enumerate(lcom):
    com = i.split()
    if com[0] == 'lconst':
        if ok == 1:
            reg[com[1]] = com[2]
    if com[0] == 'print':
        if ok == 1:
            print(int(reg[com[1]]))
    if com[0] == 'add':
        if ok == 1:
            reg[com[1]] = int(reg[com[2]]) + int(reg[com[3]])
    if com[0] == 'mul':
        reg[com[1]] = int(reg[com[2]]) * int(reg[com[3]])
    if com[0] == 'div':
        try:
            reg[com[1]] = int(reg[com[2]]) / int(reg[com[3]])
        except ZeroDivisionError:
            ok = 0
            print("Exception: line", index+1)






