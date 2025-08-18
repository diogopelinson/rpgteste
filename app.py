jogador1 = input("Digite o nome do seu jogador: ")


itens_arma = []

while True:
    try:
        arma = int(input("Escolha sua arma: \n1. Espada \n2. Machado \n3.Lança \n : "))
        if arma == 1:
            print(f"{jogador1} sua arma escolhida foi a Espada!\n")
            arma = "Espada"
            itens_arma.append(arma)
            break
        elif arma == 2:
            print(f"{jogador1} sua arma escolhida foi o Machado!\n")
            arma = "Machado"
            itens_arma.append(arma)
            break
        elif arma == 3:
            print(f"{jogador1} sua arma escolhida foi a Lança!\n")
            arma = "Lança"
            itens_arma.append(arma)
            break

    except:
        print("Entrada inválida, digite apenas números validos.")

itens_magicos = []


while True:
    try:
        magia = int(input("Agora vamos escolher nossa magia arcana: \n1.Raio de fogo \n2.Sopro gelado \n3.Soco flamejante\n : "))
        if magia == 1:
            print(f"{jogador1} sua magia escolhida foi o Raio de fogo!\n")
            magia = "Raio de fogo"
            itens_magicos.append(magia)
            break
        elif magia == 2:
            print(f"{jogador1} sua magia escolhida foi o Sopro gelado!\n")
            magia = "Sopro gelado"
            itens_magicos.append(magia)
            break
        elif magia == 3:
            print(f"{jogador1} sua magia escolhida foi o Soco flamejante\n")
            magia = "Soco flamejante"
            itens_magicos.append(magia)
            break

    except ValueError:
        print("Entrada inválida, digite apenas números validos.")


print(f"{jogador1} seu inventario atual esta assim:")

for i in itens_arma, itens_magicos:
        interador = 0
        print("- " + i[interador])
        interador += 1




