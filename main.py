
import sys
# print(sys.argv)

#un cuvant primeste sys.argv[1]

def acceptor(cuvant):
    # global stare_initiala, stari_finale, states, words, transitions, verif
    # ok = 0
    StareCurenta = stare_initiala
    lungimeCuvant = len(cuvant)

    if verif == 0: #are o singura stare initiala
        for i in range(len(cuvant)):  #parcurgem literele cuvantului dat
            ok=0
            for transition in transitions:
                if transition[1] == cuvant[i] and StareCurenta == transition[0] and lungimeCuvant != 1:
                    ok = 1 #am gasit o tranzitie care merge
                    StareCurenta = transition[2]
                    lungimeCuvant -= 1
                elif transition[1] == cuvant[i] and StareCurenta == transition[0] and transition[2] in stari_finale and lungimeCuvant == 1:
                    return "is accepted"
                if ok == 1:
                    break
            if ok == 0:
                return "is NOT accepted"



with open(sys.argv[1]) as f:
    s = f.readlines()

text = []

for line in s:
    if line[0] != "#":
        line = line.replace(",", " ").replace(":", "").replace("\t", "").replace("\n", "")
        text.append(line)

stari_finale = []
states = []
words = []
transitions = []
stare_initiala = -1

ok = 0

for i in range(len(text)):
    if text[i] == "Sigma":
        ok = 1
    if text[i] != "Sigma" and ok == 1:
        words.append(text[i].strip())
        if text[i] == "End":
            break

words = words[:len(words)-1]

ok = 0
verif = 0

for i in range(len(text)):
    if text[i] == "States":
        ok = 1
    if ok == 1 and text[i] != "States":
        if len(text[i].split()) == 1 and text[i] != "F" and text[i] != "S":
            states.append(text[i].strip())
        if len(text[i].split()) > 1:
            var = text[i].split()
            states.append(var[0].strip())

            if "F" in var:
                stari_finale.append(var[0].strip())
            if "S" in var and stare_initiala == -1:
                stare_initiala = var[0].strip()
            elif "S" in var and stare_initiala != -1 and verif == 0:
                print("Input-ul este gresit, deoarece nu pot exista mai multe stari initiale")
                verif = 1

        if text[i] == "End":
            break

states = states[:len(states)-1]

ok = 0

for i in range(len(text)):
    if text[i] == "Transitions":
        ok = 1
    if ok == 1 and text[i] != "Transitions" and text[i] != "End" and text[i] != "":
        lista = []
        var = text[i].split()

        lista.append(var[0])
        lista.append(var[1])
        lista.append(var[2])

        transitions.append(lista)
    if text[i] == "End" and ok == 1:
        break

print(f"Cuvantul {sys.argv[2]} {acceptor(sys.argv[2])}")

print("\n")

print(f"Sigma este: {words}")
print(f"Starile sunt {states}")
print(f"Starea initiala este: {stare_initiala}")
print(f"Starile finale sunt: {stari_finale}")
print(f"Tranzitiile sunt: {transitions}")

#
# print("\n")
#
# for transition in transitions:
#     if transition[0] in states and transition[2] in states and transition[1] in words:
#         print(f"Tranzitia {transition} este valida")
#     elif transition[0] not in states:
#         print(f"Tranzitia {transition} nu este valida, deoarece starea {transition[0]} nu apartine multimii States")
#     elif transition[2] not in states:
#         print(f"Tranzitia {transition} nu este valida, deoarece starea {transition[2]} nu apartine multimii States")
#     elif transition[1] not in words:
#         print(f"Tranzitia {transition} nu este valida, deoarece cuvantul {transition[1]} nu apartine multimii Words")
#

