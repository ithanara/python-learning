import random
alvo = random.randint(1,100)
#print(alvo)
fim = False

while fim == False:
    try:
        chute = int(input('Diga um número de 1 a 100: '))
        calculo = chute - alvo
        if calculo == 0:
                print('voce acertou!')
                fim = True
        else:
                if abs(calculo) > 30:
                    print ('muito frio')
                elif abs(calculo) >= 16:
                    print ('frio')
                elif abs(calculo) >= 6:
                    print ('quente')
                else:
                    print ('muito quente')
    except ValueError as e:
        print (f'Letras não valem! \n Detalhes do erro: {e}')