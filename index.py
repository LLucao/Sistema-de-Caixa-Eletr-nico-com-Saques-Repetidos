nome = input("Digite seu nome: ")
saldo = float(input("Digite o saldo inicial: "))

saques_aprovados = 0
total_sacado = 0.0

while saldo > 0:
    saque = float(input("Digite o valor do saque (0 para sair): "))
    
    if saque == 0:
        break
    elif saque < 0:
        print("Valor inválido. Tente novamente.")
    elif saque > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= saque
        saques_aprovados += 1
        total_sacado += saque
        print(f"Saque de R${saque:.2f} aprovado. Saldo atual: R${saldo:.2f}")

print("\n--- Atendimento encerrado ---")
print(f"Cliente: {nome}")
print(f"Saques aprovados: {saques_aprovados}")
print(f"Total sacado: R${total_sacado:.2f}")
print(f"Saldo final: R${saldo:.2f}")

