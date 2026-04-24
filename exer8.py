inventario = []

while True:
    print("\n===== INVENTÁRIO DE ATIVOS =====")
    print("[1] Cadastrar ativo")
    print("[2] Listar ativos")
    print("[3] Buscar por IP")
    print("[4] Alterar status")
    print("[5] Remover ativo")
    print("[6] Sair")
    opcao = input("\nOpção: ")

    if opcao == "1":
        try:
            nome = input("Nome do ativo: ")
            tipo = input("Tipo (servidor/estação/switch/roteador): ")
            ip   = input("IP: ")

            for ativo in inventario:
                if ativo["ip"] == ip:
                    raise ValueError(f"IP {ip} já cadastrado!")

            novo = {
                "nome": nome,
                "tipo": tipo,
                "ip": ip,
                "status": "ativo"
            }
            inventario.append(novo)
            print("Ativo cadastrado com sucesso!")

        except ValueError as e:
            print(f"Erro: {e}")

    elif opcao == "2":
        if not inventario:
            print("Nenhum ativo cadastrado.")
        else:
            for i, a in enumerate(inventario, 1):
                print(f"\n[{i}] {a['nome']} | {a['tipo']} | IP: {a['ip']} | {a['status']}")

    elif opcao == "3":
        ip = input("IP a buscar: ")
        encontrado = None
        for ativo in inventario:
            if ativo["ip"] == ip:
                encontrado = ativo
                break
        if encontrado:
            print(f"Encontrado: {encontrado['nome']} — {encontrado['tipo']} — {encontrado['status']}")
        else:
            print("IP não encontrado.")

    elif opcao == "4":
        ip = input("IP do ativo: ")
        try:
            for ativo in inventario:
                if ativo["ip"] == ip:
                    ativo["status"] = "inativo" if ativo["status"] == "ativo" else "ativo"
                    print(f"Status alterado para: {ativo['status']}")
                    break
            else:
                raise Exception("Ativo não encontrado.")
        except Exception as e:
            print(f"Erro: {e}")

    elif opcao == "5":
        ip = input("IP do ativo a remover: ")
        for ativo in inventario:
            if ativo["ip"] == ip:
                inventario.remove(ativo)
                print("Ativo removido.")
                break
        else:
            print("IP não encontrado.")

    elif opcao == "6":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
