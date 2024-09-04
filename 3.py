import json

with open ('dados.json', 'r') as arquivo:
    valores = json.load(arquivo)

faturamento_diario = []

for valor in valores:
    if valor['valor'] > 0:
        faturamento_diario.append(valor['valor'])

menor = min(faturamento_diario)
maior = max(faturamento_diario)
media = sum(faturamento_diario) / len(faturamento_diario)

valor_superior_a_media = []

for faturamento in faturamento_diario:
    if faturamento > media:
        valor_superior_a_media.append(faturamento)


print(f'O menor valor de faturamento foi: R$ {menor:.2f}')
print(f'O maior valor de faturamento foi: R$ {maior:.2f}')
print(f'A média de faturamento foi: {media:.2f}')
print(f'O Número de dias com faturamento acima da média foi:', 
      len(valor_superior_a_media))
