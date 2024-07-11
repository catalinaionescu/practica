"""
Mesajele sunt formate doar din cifre şi v-aţi dat seama că mesajele au
fost codate folosind un cifru simplu. Mesajul original era format din majusculele limbii engleze,
fiecare dintre acestea fiind convertite într-un număr, folosind următoarea corespondență:
• A → 1
• B → 2
• ...
• Z →26
Din moment ce mesajul apare ca un șir de cifre neîntrerupte, există multe moduri în care ar putea
fi decodat, dar cei care le transmit s-au gândit la următorul scenariu:
• Când următoarele două cifre din mesaj pot fi interpretate ca un număr de două cifre pe care
îl putem decoda, le vom interpreta astfel, ignorând posibilitatea interpretării unei singure
cifre.
• Dacă pe poziţia curentă se află un 0, secvenţa 0x se va interpreta ca x, unde x este orice
cifră între 1 şi 9, iar cifra x se va decoda ca atare. (Exemplu: 01 → 1 → A).
• Două cifre de 0 consecutive vor fi decodate ca un spațiu.

Cerinţă
Să se decodeze mesajul, folosind scenariul de mai sus.
Date de intrare
Pe o singură linie se va citi un şir de cifre neîntrerupte, reprezentând mesajul codat.
Date de ieşire
Se va afişa, pe o singură linie, mesajul decodat. Linia se va termina obligatoriu cu un caracter
newline ("\n").
"""

# alfabet: a=1, .. z=26
# daca am 01 ignor 0
# daca am 2 cifre una langa alta le iau impreuna si sunt sub 27


txt_cod = input()
txt_decod = ''
i = 0
while i < len(txt_cod):
    if 0 < int(txt_cod[i] + txt_cod[i+1]) < 27:  # daca cifrele sunt intre 0 si 27 atunci sunt litere
        txt_decod += chr(int(txt_cod[i] + txt_cod[i+1]) + 64)
        i += 2
    elif int(txt_cod[i]) == 0 and int(txt_cod[i+1]) == 0:  # daca cifrele sunt 00 atunci spatiul gol
        txt_decod += ' '
        i += 2
    else:
        txt_decod += chr(int(txt_cod[i]) + 64)
        i += 1
print(txt_decod)
