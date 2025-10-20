
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


print(f"\n-----------------------------------------------")
print(f"                                               ")
print(f"\n {jogador1} seu inventario atual esta assim:")
print(f"                                               ")
print(f"-----------------------------------------------")


for i in itens_arma, itens_magicos, tipo_classe, vida_classe:
        interador = 0
        print("- " + i[interador])
        interador += 1




