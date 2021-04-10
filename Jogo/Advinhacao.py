print("**********************************")
print("bem vindo no jogo da adivinhação ")
print("**********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")

print("voce chutou ", chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto


if acertou:
    print("Voce acertou !!!")
else:
    if maior:
        print("Voce errou! O seu chute foi maior que o numero secreto")
    elif menor:
        print("Voce errou! O seu chute foi menor que o numero secreto")

print("Fim de jogo")
