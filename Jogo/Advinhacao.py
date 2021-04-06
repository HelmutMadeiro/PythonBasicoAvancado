print("**********************************")
print("bem vindo no jogo da adivinhacao ")
print("**********************************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")

print("voce chutou ", chute_str)

chute = int(chute_str)

if numero_secreto == chute:
    print("Voce acertou")
else:
    print("Voce errou")
