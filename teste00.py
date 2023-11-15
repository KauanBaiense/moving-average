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
m1 = []
m2 = []
num1 = 0
num2 = 0

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

m1, num1 = fazTudo(teste.copy())
m2, num2 = fazTudo(teste.copy())

formatted_m1 = [f'{valor:.4f}' for valor in m1]
formatted_m2 = [f'{valor:.4f}' for valor in m2]

print(formatted_m1)
print('---------------')
print(formatted_m2)
print(num1)
print(num2)
dif = abs(num1 - num2)

if num1 < num2:
    m2 = m1[:dif] + m2
else:
    m1 = m2[:dif] + m1

for i in range(len(m1)):
    if m1[i]<m2[i]:
        



print('---------------------------------------------------------')
print( )
formatted_m1 = [f'{valor:.4f}' for valor in m1]
formatted_m2 = [f'{valor:.4f}' for valor in m2]

print(formatted_m1)
print('---------------')
print(formatted_m2)
