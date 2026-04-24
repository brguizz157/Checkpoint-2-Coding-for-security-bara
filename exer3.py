lista_ips = []

while True:
    print("\nGERENCIADOR DE IPs")
    print("[1] Adicionar IP")
    print("[2] Remover IP")
    print("[3] Listar todos")
    print("[4] Buscar IP")
    print("[5] Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        ip = input("Digite o IP: ")
        if ip in lista_ips:
            print(f"IP {ip} já está na lista!")
        else:
            lista_ips.append(ip)
            print(f"IP {ip} adicionado com sucesso!")

    elif opcao == "2":
        ip = input("Digite o IP a remover: ")
        if ip in lista_ips:
            lista_ips.remove(ip)
            print(f"IP {ip} removido.")
        else:
            print("IP não encontrado na lista.")

    elif opcao == "3":
        if not lista_ips:
            print("A lista está vazia.")
        else:
            print("\nIPs cadastrados:")
            for i, ip in enumerate(lista_ips, 1):
                print(f"  {i}. {ip}")

    elif opcao == "4":
        ip = input("Digite o IP a buscar: ")
        if ip in lista_ips:
            posicao = lista_ips.index(ip) + 1 
            print(f"IP {ip} encontrado na posição {posicao}.")
        else:
            print("IP não encontrado.")

    elif opcao == "5":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
