import os
import time

os.system('clear')

print(f"                                                                                                                   ")
print(f"   ▄███████▄ ▄██   ▄       ███        ▄█    █▄     ▄██████▄  ███▄▄▄▄           ▄████████    ▄███████▄    ▄██████▄  ")
print(f"  ███    ███ ███   ██▄ ▀█████████▄   ███    ███   ███    ███ ███▀▀▀██▄        ███    ███   ███    ███   ███    ███ ")
print(f"  ███    ███ ███▄▄▄███    ▀███▀▀██   ███    ███   ███    ███ ███   ███        ███    ███   ███    ███   ███    █▀  ")
print(f"  ███    ███ ▀▀▀▀▀▀███     ███   ▀  ▄███▄▄▄▄███▄▄ ███    ███ ███   ███       ▄███▄▄▄▄██▀   ███    ███  ▄███        ")
print(f"▀█████████▀  ▄██   ███     ███     ▀▀███▀▀▀▀███▀  ███    ███ ███   ███      ▀▀███▀▀▀▀▀   ▀█████████▀  ▀▀███ ████▄  ")
print(f"  ███        ███   ███     ███       ███    ███   ███    ███ ███   ███      ▀███████████   ███          ███    ███ ")
print(f"  ███        ███   ███     ███       ███    ███   ███    ███ ███   ███        ███    ███   ███          ███    ███ ")
print(f" ▄████▀       ▀█████▀     ▄████▀     ███    █▀     ▀██████▀   ▀█   █▀         ███    ███  ▄████▀        ████████▀  ")
print(f"                                                                              ███    ███                           ")


jogador1 = input("Digite o nome do seu jogador: ")

print(f"Seja bem-vindo: {jogador1}! Vamos iniciar o jogo...")

tipo_classe = []
vida_classe = []

while True:
    try:
        classe = int(input("Antes de tudo, escolha sua classe: \n1. Mago \n2. Assasino \n3.Tanque \n : "))
        if classe == 1:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"{jogador1}! Agora você é um Mago! 🧙‍♂️ \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            classe = "Mago"
            vida = "100"
            tipo_classe.append(classe)
            vida_classe.append(vida)
            break
        elif classe == 2:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"{jogador1}! Agora você é um Assasino! 🥷 \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            classe = "Assasino"
            vida = "75"
            tipo_classe.append(classe)
            vida_classe.append(vida)
            break
        elif classe == 3:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"\n {jogador1}! Agora você é um Tanque! 💪👨‍🦲 \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            classe = "Tanque"
            vida = "200"
            tipo_classe.append(classe)
            vida_classe.append(vida)
            break

    except:
        print(" ❌ Entrada inválida, digite apenas números validos. ❌ ")

itens_arma = []

while True:
    try:
        arma = int(input("Escolha sua arma: \n1. Espada \n2. Machado \n3.Lança \n : "))
        if arma == 1:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"{jogador1}! Sua arma escolhida foi a Espada! ⚔️ \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            arma = "Espada"
            itens_arma.append(arma)
            break
        elif arma == 2:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"{jogador1}! Sua arma escolhida foi o Machado! 🪓 \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            arma = "Machado"
            itens_arma.append(arma)
            break
        elif arma == 3:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"\n {jogador1}! Sua arma escolhida foi a Lança! 🔱 \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            arma = "Lança"
            itens_arma.append(arma)
            break

    except:
        print(" ❌ Entrada inválida, digite apenas números validos. ❌ ")

itens_magicos = []


while True:
    try:
        magia = int(input("Agora vamos escolher nossa magia arcana: \n1.Raio de fogo \n2.Sopro gelado \n3.Soco flamejante\n : "))
        if magia == 1:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"\n {jogador1}! Sua magia escolhida foi o Raio de fogo! ⚡🔥 \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            magia = "Raio de fogo"
            itens_magicos.append(magia)
            break
        elif magia == 2:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"\n {jogador1}! Sua magia escolhida foi o Sopro gelado! 🌬️❄️ \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            magia = "Sopro gelado"
            itens_magicos.append(magia)
            break
        elif magia == 3:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"\n {jogador1}! Sua magia escolhida foi o Soco flamejante 🤜🔥 \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            magia = "Soco flamejante"
            itens_magicos.append(magia)
            break

    except ValueError:
        print(" ❌ Entrada inválida, digite apenas números validos. ❌ ")

os.system('clear')

print(f"\n-----------------------------------------------")
print(f"{jogador1} seu inventario atual esta assim:")
print(f"                                               ")


for i in itens_arma, itens_magicos, tipo_classe, vida_classe:
        interador = 0
        print("- " + i[interador])
        interador += 1

print(f"-----------------------------------------------\n\n\n")

jogador2 = input("Agora, vamos dar a vez para o segundo jogador! Digite seu nome: ")

tipo2_classe = []
vida2_classe = []

while True:
    try:
        classe = int(input("Antes de tudo, escolha sua classe: \n1. Mago \n2. Assasino \n3.Tanque \n : "))
        if classe == 1:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"{jogador2}! Agora você é um Mago! 🧙‍♂️ \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            classe = "Mago"
            vida = "100"
            tipo2_classe.append(classe)
            vida2_classe.append(vida)
            break
        elif classe == 2:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"{jogador2}! Agora você é um Assasino! 🥷 \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            classe = "Assasino"
            vida = "75"
            tipo2_classe.append(classe)
            vida2_classe.append(vida)
            break
        elif classe == 3:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"\n {jogador2}! Agora você é um Tanque! 💪👨‍🦲 \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            classe = "Tanque"
            vida = "200"
            tipo2_classe.append(classe)
            vida2_classe.append(vida)
            break

    except:
        print(" ❌ Entrada inválida, digite apenas números validos. ❌ ")

itens2_arma = []

while True:
    try:
        arma = int(input("Escolha sua arma: \n1. Espada \n2. Machado \n3.Lança \n : "))
        if arma == 1:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"{jogador2}! Sua arma escolhida foi a Espada! ⚔️ \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            arma = "Espada"
            itens2_arma.append(arma)
            break
        elif arma == 2:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"{jogador2}! Sua arma escolhida foi o Machado! 🪓 \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            arma = "Machado"
            itens2_arma.append(arma)
            break
        elif arma == 3:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"\n {jogador2}! Sua arma escolhida foi a Lança! 🔱 \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            arma = "Lança"
            itens2_arma.append(arma)
            break

    except:
        print(" ❌ Entrada inválida, digite apenas números validos. ❌ ")

itens2_magicos = []


while True:
    try:
        magia = int(input("Agora vamos escolher nossa magia arcana: \n1.Raio de fogo \n2.Sopro gelado \n3.Soco flamejante\n : "))
        if magia == 1:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"\n {jogador2}! Sua magia escolhida foi o Raio de fogo! ⚡🔥 \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            magia = "Raio de fogo"
            itens2_magicos.append(magia)
            break
        elif magia == 2:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"\n {jogador2}! Sua magia escolhida foi o Sopro gelado! 🌬️❄️ \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            magia = "Sopro gelado"
            itens2_magicos.append(magia)
            break
        elif magia == 3:
            print(f"\n-----------------------------------------------")
            print(f"                                               ")
            print(f"\n {jogador2}! Sua magia escolhida foi o Soco flamejante 🤜🔥 \n")
            print(f"                                               ")
            print(f"-----------------------------------------------")
            magia = "Soco flamejante"
            itens2_magicos.append(magia)
            break

    except ValueError:
        print(" ❌ Entrada inválida, digite apenas números validos. ❌ ")

os.system('clear')

print(f"\n-----------------------------------------------")
print(f"{jogador2} seu inventario atual esta assim:")
print(f"                                               ")


for j in itens2_arma, itens2_magicos, tipo2_classe, vida2_classe:   
        interador2 = 0
        print("- " + j[interador2])
        interador2 += 1

print(f"-----------------------------------------------\n\n\n")


time.sleep(5)

# Adicionando segundo jogador, implementar metodo para melhorar a adição do segundo jogador
# Fazendo comparações de classes, Ex: se o jgr1 selecionar Mago, o jgr2 não poderá selecionar
# O mesmo;
#
# Adicionar método para poder iniciar o jogo.