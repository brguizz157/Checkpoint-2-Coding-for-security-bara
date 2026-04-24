texto = input("Digite um texto: ")

texto = texto.lower()

palavras = texto.split()

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

palavra_top = ordenado[0][0]

print("\n===== FREQUÊNCIA DAS PALAVRAS =====")
for palavra, qtd in ordenado:
    if palavra == palavra_top:
        print(f"  * {palavra}: {qtd}x  <- mais usada")
    else:
        print(f"    {palavra}: {qtd}x")
