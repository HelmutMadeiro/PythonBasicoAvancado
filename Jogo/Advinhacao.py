print("**********************************")
print("bem vindo no jogo da adivinhação ")
print("**********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")

print("voce chutou ", chute_str)

chute = int(chute_str)

if numero_secreto == chute:
    print("Voce acertou!!!")
else:
    print("Voce errou")
