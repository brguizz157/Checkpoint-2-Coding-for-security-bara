logs = [
    "INFO | 192.168.1.1 | Login bem-sucedido",
    "ERROR | 45.33.32.156 | Tentativa de acesso negada",
    "WARNING | 10.0.0.5 | Porta incomum detectada",
    "ERROR | 45.33.32.156 | Força bruta detectada",
    "INFO | 172.16.0.3 | Arquivo transferido",
    "ERROR | 10.0.0.5 | Falha de autenticação",
    "LOG MALFORMADO SEM SEPARADORES",
    "WARNING | 45.33.32.156 | Scan de portas",
]

contagem_nivel = {"INFO": 0, "WARNING": 0, "ERROR": 0}

erros_por_ip = {}

malformados = 0

for log in logs:
    try:
        partes = log.split(" | ")

        if len(partes) != 3:
            raise ValueError("Log mal formatado")

        nivel, ip, mensagem = partes 

        if nivel in contagem_nivel:
            contagem_nivel[nivel] += 1

        if nivel == "ERROR":
            if ip in erros_por_ip:
                erros_por_ip[ip] += 1
            else:
                erros_por_ip[ip] = 1

    except ValueError:
        malformados += 1
        print(f"[AVISO] Log ignorado (mal formatado): {log}")

ip_mais_erros = max(erros_por_ip, key=erros_por_ip.get) if erros_por_ip else "nenhum"

print("\nRELATÓRIO DE LOGS")
print(f"INFO:    {contagem_nivel['INFO']}")
print(f"WARNING: {contagem_nivel['WARNING']}")
print(f"ERROR:   {contagem_nivel['ERROR']}")
print(f"Logs malformados ignorados: {malformados}")
print(f"\nIP com mais erros: {ip_mais_erros} ({erros_por_ip.get(ip_mais_erros, 0)} erros)")
