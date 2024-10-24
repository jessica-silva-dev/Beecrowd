# Salário com Bônus
nome_vendedor = input()
salario_fixo = float(input())
total_vendas = float(input())
comissao = (0.15 * total_vendas) + salario_fixo
print(f"TOTAL = R$ {comissao:.2f}")