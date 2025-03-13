def TelaInicial():
    print("1 - Logar")
    print("2 - Registrar")
    print("3 - Sair")
    opcao = int(input("Escolha: "))

    if opcao == 1:
        print("Bem Vindo")
    elif opcao == 2:
        print("Efetue seu cadastro")
    elif opcao == 3:
        print("Saindo do Sistema...")
    else:
        print("Opção Invalida")

TelaInicial()

