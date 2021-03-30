
def acceptor(cuvant):
    starecurenta = stare_initiala
    lungimecuvant = len(cuvant)
    tr = [stare_initiala]

    if len(cuvant) == 0 and stare_initiala in stari_finale:
        return "Da", tr
    elif len(cuvant) == 0 and stare_initiala not in stari_finale:
        return "Nu", tr
    for contor in range(len(cuvant)):
        ok = 0
        for transition in transitions:
            if transition[2] == cuvant[contor] and starecurenta == transition[0] and lungimecuvant != 1:
                ok = 1
                starecurenta = transition[1]
                lungimecuvant -= 1
                tr.append(starecurenta)
            elif transition[2] == cuvant[contor] and starecurenta == transition[0] and transition[1] in stari_finale and lungimecuvant == 1:
                tr.append(transition[1])
                return "Da", tr
            if ok == 1:
                break
        if ok == 0:
            return "Nu", tr


if __name__ == "__main__":
    fisier = input()

    stari_finale = []
    states = []
    words = []
    transitions = []

    with open(fisier) as f:
        s = f.readlines()

    nr_stari = int(s[0].split()[0])
    nr_tranzitii = int(s[0].split()[1])

    for i in range(1, len(s)):
        linie = s[i].strip("\n").split()

        if i <= nr_tranzitii:
            transitions.append((linie[0], linie[1], linie[2]))
        elif i == nr_tranzitii + 1:
            stare_initiala = linie[0]
        elif i == nr_tranzitii + 2:
            for j in range(len(linie)):
                stari_finale.append(linie[j])
        elif i == nr_tranzitii + 3:
            nr_cuvinte = int(linie[0])
        else:
            words.append(linie[0])

    for word in words:
        print(word)

        raspuns = acceptor(word)
        if raspuns[0] == "Da":
            print("DA" + "\n" + "Traseu: ", *raspuns[1])
            print("\n")
        else:
            print("NU" + "\n")
