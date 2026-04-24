import random
import string

senhas = {}

def avaliar_forca(senha):
    pontos = 0
    if len(senha) >= 8: pontos += 1
    if any(c.isupper() for c in senha): pontos += 1
    if any(c.islower() for c in senha): pontos += 1
    if any(c.isdigit() for c in senha): pontos += 1
    if any(c in "!@#$%&*" for c in senha): pontos += 1
    if pontos <= 2: return "fraca"
    elif pontos <= 4: return "média"
    else: return "forte"

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = ""
    for _ in range(tamanho):
        senha += random.choice(caracteres)
    return senha

while True:
    print("\nGERENCIADOR DE SENHAS")
    print("[1] Cadastrar senha")
    print("[2] Listar serviços")
    print("[3] Buscar senha por serviço")
    print("[4] Gerar senha aleatória")
    print("[5] Avaliar força de todas as senhas")
    print("[6] Exportar relatório")
    print("[7] Sair")
    opcao = input("\nOpção: ")

    if opcao == "1":
        try:
            servico = input("Serviço: ").strip()
            if not servico:
                raise ValueError("Nome do serviço não pode ser vazio.")
            if servico in senhas:
                raise ValueError(f"Serviço '{servico}' já cadastrado.")
            senha = input("Senha: ")
            senhas[servico] = senha
            forca = avaliar_forca(senha)
            print(f"Cadastrado! Força da senha: {forca}.")
        except ValueError as e:
            print(f"Erro: {e}")

    elif opcao == "2":
        if not senhas:
            print("Nenhum serviço cadastrado.")
        else:
            print("\nServiços cadastrados:")
            for i, servico in enumerate(senhas, 1):
                print(f"  {i}. {servico}")

    elif opcao == "3":
        try:
            servico = input("Serviço: ")
            if servico not in senhas:
                raise KeyError(servico)
            print(f"Senha de '{servico}': {senhas[servico]}")
        except KeyError:
            print("Serviço não encontrado.")

    elif opcao == "4":
        try:
            tamanho = int(input("Tamanho da senha: "))
            if tamanho < 1:
                raise ValueError()
            print(f"Senha gerada: {gerar_senha(tamanho)}")
        except ValueError:
            print("Digite um número válido.")

    elif opcao == "5":
        if not senhas:
            print("Nenhuma senha cadastrada.")
        else:
            print("\nForça das senhas:")
            for servico, senha in senhas.items():
                forca = avaliar_forca(senha)
                print(f"  {servico}: {forca}")

    elif opcao == "6":
        try:
            with open("relatorio_senhas.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write("RELATÓRIO DE SENHAS\n")
                arquivo.write("=" * 30 + "\n")
                for servico, senha in senhas.items():
                    forca = avaliar_forca(senha)
                    arquivo.write(f"{servico}: {senha} [{forca}]\n")
            print("Relatório exportado para 'relatorio_senhas.txt'.")
        except IOError:
            print("Erro ao escrever o arquivo.")

    elif opcao == "7":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
