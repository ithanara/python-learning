inimigos = [(50,30),(100,100),(10,90)]
numero_inimigos = 3
fim = False

print("\nBoas vindas à bathailha naval! Você vê 3 inimigos em seu radar...")
print("\n.˳˳.⋅ॱ˙˙ॱ⋅.˳˳.⋅ॱ˙˙ॱ⋅.˳˳.⋅.˳˳.⋅ॱ˙˙ॱ⋅.˳˳.⋅ॱ˙˙ॱ⋅.˳˳.⋅ॱ˙˙ॱ⋅.˳˳.⋅")

while fim == False:
    try:
        print(f"\n👾 Inimigos restantes: {numero_inimigos}")
        x = int(input("\nOnde você joga? Primeiro o X: "))
        y = int(input("E agora manda o Y: "))

        if (x, y) in inimigos:
            inimigos.remove((x, y))
            numero_inimigos = numero_inimigos - 1
            print("\nAcertou um barco, miseravi!")
            print("\n.˳˳.⋅ॱ˙˙ॱ⋅.˳˳🚢˳.⋅ॱ˙˙ॱ⋅.˳˳.⋅ॱ˙")
        else:
            print("\n--- 😩 Acertou a água! ---")

        if numero_inimigos == 0:
            fim = True
            print("\n🎉🎉🎉 Você venceu, parabéns! 🎉🎉🎉")
    except ValueError:
        print("✋ Digite números inteiros, por favor!")
    except KeyboardInterrupt:
        print("\nJogo interrompido pelo usuário.")
        break
