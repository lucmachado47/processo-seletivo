Estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53,
}

total = sum(Estados.values())

for estado, valor in Estados.items():
    percentual = valor * 100 / total
    print(f'{estado}: {percentual:.2f}%')