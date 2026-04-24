acessos = {
    "192.168.1.1", "10.0.0.5", "172.16.0.3",
    "192.168.1.100", "45.33.32.156", "8.8.8.8"
}

blacklist = {
    "45.33.32.156", "185.220.101.5",
    "192.168.1.100", "23.129.64.214"
}

detectados = acessos & blacklist

seguros = acessos - blacklist

nao_apareceram = blacklist - acessos

todos = acessos | blacklist

print("===== RELATÓRIO DE SEGURANÇA =====")

print(f"\n[ALERTA] IPs maliciosos detectados ({len(detectados)}):")
for ip in detectados:
    print(f"  x {ip}")

print(f"\n[OK] IPs seguros ({len(seguros)}):")
for ip in seguros:
    print(f"  v {ip}")

print(f"\n[INFO] IPs da blacklist que não apareceram ({len(nao_apareceram)}):")
for ip in nao_apareceram:
    print(f"  ? {ip}")

print(f"\n[TOTAL] IPs únicos considerando ambas as listas: {len(todos)}")
