def fazTudo(lista):
    somat = []
    num = int(input('N: '))
    tam = len(lista)
    a = tam + 1 - num

    matriz = [0] * a
    for i in range(a):
        matriz[i] = [0] * num

    for m in range(a):
        i = m
        for n in range(num):
            matriz[m][n] = lista[i]
            i += 1
    for m in range(a):
        for n in range(num):
            vetor.append(matriz[m][n])
        soma = sum(vetor)
        somat.append(soma / num)
        vetor.clear()
    return somat, num

vetor = []
lista = []
tendencia = []
vetor1 = []
vetor2 = []
number1 = 0
number2 = 0

c = int(input('Usar seus dados 1-SIM ou 0-NAO: '))
if c != 0:
    elemento = input("Digite um número (ou 'fim' para encerrar): ")
    while elemento.lower() != 'fim':
        try:
            numero = float(elemento)
            lista.append(numero)
        except ValueError:
            print("Digite um número válido.")

        elemento = input("Digite um número (ou 'fim' para encerrar): ")

teste = [4.159,4.1293,4.0841,4.0556,4.1071,4.0954,4.1104,4.1095,4.1097,4.1293]

vetor1, number1 = fazTudo(teste.copy())
vetor2, number2 = fazTudo(teste.copy())
'''
formatted_vetor1 = [f'{valor:.4f}' for valor in vetor1]
formatted_vetor2 = [f'{valor:.4f}' for valor in vetor2]

print(formatted_vetor1)
print('---------------')
print(formatted_vetor2)
print(number1)
print(number2)
'''
dif = abs(number1 - number2)

if number1 < number2:
    vetor2 = vetor1[:dif] + vetor2
else:
    vetor1 = vetor2[:dif] + vetor1

for i in range(len(vetor1)):
    if vetor1[i] > vetor2[i]:
        tendencia.append('alta')
    elif vetor1[i] < vetor2[i]:
        tendencia.append('queda')
    else:
        tendencia.append('constante')

for i in range(len(tendencia) - 1):
    if tendencia[i] == tendencia[i+1]:
        if tendencia[i] == 'queda':
            tendencia[i+1] = 'queda constante'
        elif tendencia[i] == 'alta':
            tendencia[i+1] = 'alta constante'

for i in range(len(tendencia) - 1):
    if tendencia[i] == 'queda constante' and tendencia[i+1] == 'queda':
        tendencia[i+1] = 'queda constante'
    elif tendencia[i] == 'alta constante' and tendencia[i+1] == 'alta':
        tendencia[i+1] = 'alta constante'
        


for i in range(len(tendencia)):
    print(f'{tendencia[i]}',end=' ')
    print()


print('---------------------------------------------------------')
print( )
formatted_vetor1 = [f'{valor:.4f}' for valor in vetor1]
formatted_vetor2 = [f'{valor:.4f}' for valor in vetor2]

print(formatted_vetor1)
print('---------------')
print(formatted_vetor2)
