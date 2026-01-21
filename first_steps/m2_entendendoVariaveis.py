print("[Enfermeira Draculaura]")
print("- Olá, você está no banco de sangue dos vampiros")
nome = input("Para criar seu cadastro precisamos do seu nome ")
peso = float(input (f"Ótimo, {nome}... Qual é o seu peso? Em KG... "))
altura = float(input("👀 Agora me diga sua altura em CM... "))
ano_nascimento = int(input("Em que ano você veio ao mundo? "))

altura_2 = (altura/100)*(altura/100)
idade = 2025 - ano_nascimento
peso_minimo = peso > 50

imc = peso/altura_2

if imc >= 18.4:
    veredito = "✅ Ótimo, seu corpo é forte o suficiente! "
else:
    veredito = "⛔️ Corpo muito fraquinho para doar... Faça um bulk, treine mais forte e volte daqui alguns meses."

if idade >= 16:
    maioridade = "✅ Ihu, você tem idade suficiente para doar!"
else:
    maioridade = "⛔️ Sai pra lá, de menor... Volte quando tiver mais do que 16 anos"

resultado = f"\t--[{nome}]---------------- \n\t{peso} KG, {altura} CM \n\tNasceu em {ano_nascimento}\n\t------------------------\n\n\tSeu veredito é...\n\t{maioridade}\n\t{veredito}"

print(resultado)