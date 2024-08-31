import json

with open ('processo-seletivo/faturamento_diario.json', 'r') as arquivo:
    valores = json.load(arquivo)

faturamento_diario = []

for dia in valores['faturamento_diario']:
    if dia['valor'] > 0:
        faturamento_diario.append(dia['valor'])

media = sum(faturamento_diario) / len(faturamento_diario)

valor_superior_a_media = []

for faturamento in faturamento_diario:
    if faturamento > media:
        valor_superior_a_media.append(faturamento)

print('O menor valor de faturamento foi: R$', min(faturamento_diario))
print('O maior valor de faturamento foi: R$', max(faturamento_diario))
print('O Número de dias com faturamento acima da média foi:', 
      len(valor_superior_a_media))
