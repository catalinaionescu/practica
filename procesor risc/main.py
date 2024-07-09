"""
Procesorul știe să execute următoarele instrucțiuni, pe care trebuie să le interpreteze și programul
vostru:
• lconst <dst> <val> – se scrie valoarea <val> în registrul <dst>;
• add <dst> <src0> <src> – se adună valorile din registrele <src0> și <src1> și rezultatul se
scrie în registrul <dst>;
• mul <dst> <src0> <src> – se înmulțesc valorile din registrele <src0> și <src1> și rezultatul se
scrie în registrul <dst>;
• div <dst> <src0> <src> – se împart valorile din registrele <src0> și <src1> și câtul se scrie în
registrul <dst>;
• print <reg> - se afișează valoarea din registrul <reg>.
Dacă la execuția unei instrucțiuni de tip div împărțitorul este zero, se va afișa fraza Exception: line
<index>, unde index reprezintă a câta instrucțiune nu a putut fi executată, iar programul se va încheia.
Toate registrele au inițial valoarea 0.
Cerinţă
Dându-se o secvență de instrucțiuni ca cele de mai sus, executați-le și afișați valorile printate de
program.
Date de intrare
Se va citi de la tastatură (fluxul standard de intrare, stdin) de pe prima linie un număr n, reprezentând
numărul de instrucțiuni. Pe următoarele n linii se află câte o instrucțiune din cele de mai sus.
Date de ieşire
Programul va afişa la consolă (stream-ul standard de ieşire, stdout), valorile printate de program (prin
instrucțiuni de tip print), câte una pe linie.
"""
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
crt = 1
for index, i in enumerate(lcom):
    com = i.split()
    if com[0] == 'lconst':
        if crt == 1:
            reg[com[1]] = com[2]
    if com[0] == 'print':
        if crt == 1:
            print(int(reg[com[1]]))
    if com[0] == 'add':
        if crt == 1:
            reg[com[1]] = int(reg[com[2]]) + int(reg[com[3]])
    if com[0] == 'mul':
        reg[com[1]] = int(reg[com[2]]) * int(reg[com[3]])
    if com[0] == 'div':
        try:
            reg[com[1]] = int(reg[com[2]]) / int(reg[com[3]])
        except ZeroDivisionError:
            crt = 0
            print("Exception: line", index+1)






