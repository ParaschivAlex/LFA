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


ok1 = 0  # ok pt a vedea daca folosim cifre sau litere pentru noduri


try:
    if nodulinceput.isalpha():  # da eroare daca nu e litera si foloesc try si except
        ok1 = 1
except:
    ok1 = 0


# print(nodulinceput,ok1)
if ok1 == 1:
        poz = int(ord(nodulinceput) - ord('a'))
        #print(poz)
else:
    poz = nodulinceput


sir = f.readline()  # incep sa citesc restul de date
while sir:
    ls = sir.split()  # datele sunt de tipul X, Y, Z, unde:
    if ls[0].isnumeric():
        i = int(ls[0])  # X este nodul din care pleaca drumul
        j = int(ls[2])  # Z este nodul in care ajunge drumul
    else:
        i = int(ord(ls[0]) - ord('a'))
        j = int(ord(ls[2]) - ord('a'))
        #print(i, j)
    A[i][j].append(ls[1])  # Y este codul/simbolul drumului de la X la Z
    #print(A)
    sir = f.readline()


# incep sa parcurg matricea pentru a vedea daca cuvantul dat este valid


for x in cuvant:  # parcurg litera cu litera din cuvantul dat initial
    if x.isalnum():  # verific daca litera apartine alfabetului sau este un numar natural
        for k in range(nrnoduri):  # parcurg matricea pe coloane cu linia poz
            # print(type(k),type(poz))
            if x in A[poz][k]:  # verific daca litera este in lista, adica daca este drum de la poz la k cu simbolul x
                poz = k  # poz devine nodul la care s-a facut legatura precedenta
                break  # o luam de la capat
        else:  # daca nu s-a gasit un k pentru a satisface relatia
            ok = 0  # ok devine zero si automat raspunsul va fi NU


poz = str(poz)


if nodfinal[0].isalpha():
    poz = int(poz)
    poz = chr(ord('a') + poz)
    #listafinala = [str(ord(x) - ord(nodulinceput)) for x in nodfinal]
    #print(poz, listafinala, type(poz), type(listafinala[0]), ok)
    print("DA" if (poz in nodfinal) and ok == 1 else "NU")


# aici schimb valorile din lista de noduri finale din litere in cifrele lor (a=0, c=2, e =4...)
# o alta abordare era functia chr care face din numar, caracterul ascii corespunzator
# poz = int(poz)
# poz = chr(ord('a') + poz)
# print(poz, nodfinal, type(poz), type(nodfinal[0]), ok)


else:
    print("DA" if (poz in nodfinal) and ok == 1 else "NU")
