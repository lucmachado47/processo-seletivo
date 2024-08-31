string = str(input('Digite qualquer string para ser invertida: '))
#invertida = string[::-1]
string_invertida = ''

for letra in range(len(string) -1, -1, -1):
    string_invertida += string[letra]

print(string_invertida)