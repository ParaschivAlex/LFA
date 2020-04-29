if __name__ == "__main__":


    f = open("date.txt")


    dictionar_principal = {}  # dictionarul unde tinem toate
    # datele de tip (stare_initiala --- simbol alfabet --- stare_finala)
    nr_stari = int(f.readline())
    nr_alfabet = int(f.readline())  # numarul de elemente din alfabet
    starile_FINALE_FINALE = f.readline().split()
    simboluri_alfabet = f.readline().split()
    starile = f.readline().split()

    lst_vida = []
    help = []
    help.append('%')

    prima_linie = f.readline().split()
    stare_init_aux = prima_linie[0]
    simbol = prima_linie[1]
    stari_finale = prima_linie[2:]
    print(stare_init_aux, simbol, stari_finale)
    dictionar_principal[stare_init_aux] = {}
    dictionar_principal[stare_init_aux][simbol] = stari_finale  # Adaug in dictionar datele de mai sus
    date = f.readlines()

    for linie in date:
        linie = linie.split()  # extrag elementele in forma: stare_finala, simbol, starile_finale aferente
        stare_init = linie[0]
        simbol = linie[1]
        stari_finale = linie[2:]
        print(stare_init, simbol, stari_finale)
        if stare_init_aux != stare_init:
            dictionar_principal[stare_init] = {}
        if stari_finale != help:
            # print(type(help),type(stari_finale))
            dictionar_principal[stare_init][simbol] = stari_finale  # Adaug in dictionar datele de mai sus
        else:
            dictionar_principal[stare_init][simbol] = lst_vida
        stare_init_aux = stare_init

    print(dictionar_principal)  # Afisez dictionarul final rezultat AFN-ului

    stari_noi = []  # lista pentru starile noi din dfa (de exemplu q01 ca in pdf-ul dat)
    dfa = {}  # dictionar pentru dfa

    keyss = list(list(dictionar_principal.keys())[0])  # prima cheie din nfa (adica starile initiale)
    print(list(dictionar_principal.keys()))
    print(keyss)

    symbols = list(dictionar_principal[keyss[0]].keys())  # simbolurile alfabetului
    print(symbols)
    print(dictionar_principal[keyss[0]])  # simbolul si starile pentru prima stare

    dfa[keyss[0]] = {}  # Creez un dictionar in dictionar pentru dfa si creez si spatiu pentru prima stare
    # formez prima linie a dfa-ului:
    for i in range(nr_alfabet):  # i de la 0 la numarul de elemente ale alfabetului
        x = "".join(dictionar_principal[keyss[0]][symbols[i]])  # x este un cuvant format
        # din toate starile finale ale primei stari (in
        # legatura si cu simbolul alfabetului)
        print(x)  # "abcde"  si "de"
        dfa[keyss[0]][symbols[i]] = x  # pun cuvantul in dfa
        if x not in keyss and x != "":  # daca nu s-a mai folosit cuvantul:
            stari_noi.append(x)  # o pun in lista pentru stari de tip "q01" (din q0 si q1 /// alea noi)
            keyss.append(x)  # si pun si cheia (in lista cu stari initiale)

    print(stari_noi)
    while len(stari_noi) != 0:  # daca lista de stari noi nu este vida inseamna ca putem continua
        dfa[stari_noi[0]] = {}  # iau primul element al listei de stari noi pentru verificare
        for k in range(len(stari_noi[0])):  # k de la 0 la lungimea primei stari noi
            print(stari_noi, "ACESTEA SUNT NOILE STARI")
            for i in range(len(symbols)):  # i de la 0 la lungimea simbolurilor alfabetului
                aux = []  # lista auxiliara
                for j in range(len(stari_noi[0])):  # j la fel ca si k
                    aux.extend(dictionar_principal[stari_noi[0][j]][symbols[i]])  # reuniunea dintre stari (qo, q1 ->q01)
                    print(aux, j, len(stari_noi[0]))  # aux = 24 ||| pentru fiecare stare si simbol
                    # bag in aux starile finale aferente

                cuv = ""
                cuv = cuv.join(aux)  # cuvant nou pentru elementele de mai sus
                if cuv not in keyss:  # daca cuvantul este unic
                    stari_noi.append(cuv)  # il pun ca mai sus in lista de stari noi "q01"
                    keyss.append(cuv)  # si pun si cheia
                dfa[stari_noi[0]][symbols[i]] = cuv  # pun cuvantul in dfa

        stari_noi.remove(stari_noi[0])  # sterg primul element la fiecare parcurgere pana devine lista vida

    print(dfa)

    dfa_stari = list(dfa.keys())
    dfa_stari_finale = []
    for litera in starile_FINALE_FINALE:  # pentru fiecare simbol din lista de stari finale ale nfa-ului
        for stare_dfa in dfa_stari:  # o caut in fiecare stare a dfa-ului
            if litera in stare_dfa:  # daca o gasesc, atunci starea e si finala
                dfa_stari_finale.append(stare_dfa)

    print("Starile finale ale DFA-ului : ", dfa_stari_finale)
