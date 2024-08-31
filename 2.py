n1 = 0
n2 = 1
n = int(input(
    'Digite um número inteiro para verificarmos ' +
    'se está na sequência de Fibonacci: '
))

Fibonacci = []
Fibonacci.append(n1)
Fibonacci.append(n2)

for i in range (n1, n):
    n3 = n1 + n2
    Fibonacci.append(n3)
    n1 = n2
    n2 = n3

if n in Fibonacci:
    print(f'O número {n} percente a sequência de Fibonacci.') 
else:
    print(f'O número {n} não pertence a sequência de Fibonacci.')
