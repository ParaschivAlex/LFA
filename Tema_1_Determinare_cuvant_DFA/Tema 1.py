f = open("arbore.txt")  # deschid fisierul cu date

cuvant = f.readline()  # prima linie contine cuvantul dat
lst = f.readline().split()  # a doua linie contine 3 variabile care sunt:
nrnoduri = int(lst[0])  # numarul de noduri al automatului
if lst[1].isnumeric():
    nodulinceput = int(lst[1])  # nodul de inceput
else:
    nodulinceput = lst[1]
nodfinal = lst[2:]  # nodul/nodurile finale

ok = bool(1)  # un ok de tip bool folosit mai tarziu

A = [[[] for j in range(nrnoduri)] for k in range(nrnoduri)]  # creez o matrice de adiacenta care
# contine liste vide (de exemplu A[i][j]=[]) pentru a putea adauga mai multe valori pe aceeasi pozitie

sir = f.readline()  # incep sa citesc restul de date
while sir:
    ls = sir.split()  # datele sunt de tipul X, Y, Z, unde:
    if ls[0].isnumeric():
        i = int(ls[0])  # X este nodul din care pleaca drumul
        j = int(ls[2])  # Z este nodul in care ajunge drumul
    else:
        i = ord(ls[0]) - ord('a')
        j = ord(ls[2]) - ord('a')
        print(i, j)
    A[i][j].append(ls[1])  # Y este codul/simbolul drumului de la X la Z
    sir = f.readline()

# incep sa parcurg matricea pentru a vedea daca cuvantul dat este valid

print(A)

try:
    ok1=nodulinceput.isalpha()
except:
    ok1=0

if ok1:
    poz = int(ord(nodulinceput) - ord('a'))
else:
    poz = nodulinceput

for x in cuvant:  # parcurg litera cu litera din cuvantul dat initial
    if x.isalnum():  # verific daca litera apartine alfabetului sau este un numar natural
        for k in range(nrnoduri):  # parcurg matricea pe coloane cu linia poz
            if x in A[poz][k]:  # verific daca litera este in lista, adica daca este drum de la poz la k cu simbolul x
                poz = k  # poz devine nodul la care s-a facut legatura precedenta
                break  # o luam de la capat
        else:  # daca nu s-a gasit un k pentru a satisface relatia
            ok = 0  # ok devine zero si automat raspunsul va fi NU

poz = str(poz)

if nodfinal[0].isalpha():
    listafinala = [str(ord(x) - ord('a')) for x in nodfinal]
    print(poz, listafinala, type(poz), type(listafinala[0]), ok)
    print("DA" if ((poz) in listafinala) and ok == 1 else "NU")
else:
    print(poz, nodfinal, type(poz), type(nodfinal[0]))
    print("DA" if (poz in nodfinal) and ok == 1 else "NU")
