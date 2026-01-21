#velocidade media
def calcular_velocidade_media(distancia:float, tempo:float, unidade_medida="km/h"):
    if tempo == 0:
        return 0
    velocidade_media = distancia/tempo
    return f"{velocidade_media} {unidade_medida}"

#temperatura
def converter_temperatura(temperatura:float, unidade_medida="celsius"):
    if unidade_medida == "celsius":
        return temperatura *1.8+32
    elif unidade_medida == "farenheit":
        return (temperatura - 32) / 1.8
    else:
        return 0

#menu    
def exibir_menu():
    print("\nEu sou um gênio da física, o que você deseja que eu calcule?")
    print("1 - Velocidade média")
    print("2 - Converter temperatura")
    print("3 - Nada, quero sair!")

def aluno_de_fisica():
    op = 0
    while op != 3:
        exibir_menu()
        op = int(input("Informe a opção desejada: "))
        if op ==1:
            distancia_percorrida = float(input("informe a distância: "))
            tempo_viagem = float(input("informe o tempo da viagem: "))
            medida = input("Informe a unidade de medida: ")
            print(f"\nA velocidade média e de {calcular_velocidade_media(distancia_percorrida, tempo_viagem, medida)}")

        elif op == 2:
            temperatura_informada = float(input("Informe a temperatura: "))
            medida = input("Celsius ou farenheit? ")
            print(f"\nO resultado da conversão é de {converter_temperatura(temperatura_informada, medida)}")

        elif op == 3:
            print("Sem problemas, tchau!")
            break

        else:
            print("Opção inválida!")

aluno_de_fisica()