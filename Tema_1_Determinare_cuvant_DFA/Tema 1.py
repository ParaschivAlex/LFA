f = open("arbore.txt")  # deschid fisierul cu date
cuvant = f.readline()  # prima linie contine cuvantul dat
lst = f.readline().split()  # a doua linie contine 3 variabile care sunt:
nrnoduri = int(lst[0])  # numarul de noduri al automatului
nodulinceput = int(lst[1])  # nodul de inceput
nodfinal = lst[2:]  # nodul/nodurile finale

ok = bool(1)  # un ok de tip bool folosit mai tarziu

A = [[[] for j in range(nrnoduri)] for k in range(nrnoduri)]  # creez o matrice de adiacenta care
# contine liste vide (de exemplu A[i][j]=[]) pentru a putea adauga mai multe valori pe aceeasi pozitie

sir = f.readline()  # incep sa citesc restul de date
while sir:
    ls = sir.split()  # datele sunt de tipul X, Y, Z, unde:
    i = int(ls[0])  # X este nodul din care pleaca drumul
    j = int(ls[2])  # Z este nodul in care ajunge drumul
    A[i][j].append(ls[1])  # Y este codul/simbolul drumului de la X la Z
    sir = f.readline()

# incep sa parcurg matricea pentru a vedea daca cuvantul dat este valid

poz = nodulinceput  # poz este initializat cu nodul de inceput
for x in cuvant:  # parcurg litera cu litera din cuvantul dat initial
    if x.isalnum():  # verific daca litera apartine alfabetului sau este un numar natural
        for k in range(nrnoduri):  # parcurg matricea pe coloane cu linia poz
            if x in A[poz][k]:  # verific daca litera este in lista, adica daca este drum de la poz la k cu simbolul x
                poz = k  # poz devine nodul la care s-a facut legatura precedenta
                break  # o luam de la capat
        else:  # daca nu s-a gasit un k pentru a satisface relatia
            ok = 0  # ok devine zero si automat raspunsul va fi NU

print("DA" if (str(poz) in nodfinal) and ok == 1 else "NU")  # daca ultimul poz se afla in lista cu nodul/nodurile
# finale si ok nu a devenit 0 atunci CUVANTUL ESTE ACCEPTAT
