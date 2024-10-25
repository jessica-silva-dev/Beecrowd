# Calcular simples
codigo_produto1, numero_qtd1, valor_produto1 = input().split()
codigo_produto1 = int(codigo_produto1)
numero_qtd1 = int(numero_qtd1)
valor_produto1 = float(valor_produto1)

codigo_produto2, numero_qtd2, valor_produto2 = input().split()
codigo_produto2 = int(codigo_produto2)
numero_qtd2 = int(numero_qtd2)
valor_produto2 = float(valor_produto2)

soma_produtos = (valor_produto1 * numero_qtd1) + (valor_produto2 * numero_qtd2)

print(f"VALOR A PAGAR: R$ {soma_produtos:.2f}")
