print("Seja Bem Vindo ao Quiz! ")
resp_user = input("Pronto(a) para testar seus conhecimentos? (S/N)")

if resp_user != "S":
    quit()

score = 0

print("Começando...")
print(
    "Quem desenvolveu o jogo GTA? \n (A) Rockstar Games \n (B) Ubsoft \n (C) Activision \n (D) EA \n (E) Nenhuma das opções"
)
resp1 = input("Resposta: ")

if resp1 == "A":
    print("Resposta Correta! \n")
    score = score + 1
else:
    print("Resposta Incorreta! \n")
print(
    "De quem é a famosa frase Penso, logo existo? \n (A) Platão \n (B) Galileu Galilei \n (C) Descartes \n (D) Sócrates \n (E) Francis Bacon "
)
resp2 = input("Resposta: ")

if resp2 == "C":
    print("Resposta Correta! \n")
    score = score + 1
else:
    print("Resposta Incorreta! \n")

print(
    "De onde é a invenção do chuveiro elétrico? \n (A) França \n (B) Inglaterra \n (C) Brasil \n (D) Austrália \n (E) Itália "
)
resp3 = input("Resposta: ")

if resp3 == "C":
    print("Resposta Correta! \n")
    score = score + 1
else:
    print("Resposta Incorreta! \n")

print(f"O quiz acabou. Sua pontuação foi: {score}/3")
