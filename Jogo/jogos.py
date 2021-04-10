import forca
import advinhacao

print("**********************************")
print("********Escolha seu jogo**********")
print("**********************************")

print("(1) Forca (2) Advinhação)")

jogo = int(input("Qual jogo?"))

if jogo == 1:
    print("jogando forca")
    forca.jogar()
elif jogo == 2:
    print("jogando advinhação")
    advinhacao.jogar()
