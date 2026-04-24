alunos = []

print("Digite os dados dos 5 alunos:\n")

for i in range(1, 6):
    nome = input(f"Nome do aluno {i}: ")
    nota = float(input(f"Nota de {nome}: "))

    alunos.append((nome, nota))

maior_nota = alunos[0][1]
menor_nota = alunos[0][1]
nome_maior = alunos[0][0]
nome_menor = alunos[0][0]
soma = 0

for nome, nota in alunos:
    soma += nota

    if nota > maior_nota:
        maior_nota = nota
        nome_maior = nome

    if nota < menor_nota:
        menor_nota = nota
        nome_menor = nome

media = soma / len(alunos)

print("\n===== RESULTADO =====")
print(f"Maior nota: {nome_maior} com {maior_nota}")
print(f"Menor nota: {nome_menor} com {menor_nota}")
print(f"Média da turma: {media:.2f}")

print("\nAlunos acima da média:")
for nome, nota in alunos:
    if nota > media:
        print(f"  {nome} — {nota}")
