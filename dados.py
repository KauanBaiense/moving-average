def fazTudo(lista, num):
    somat = []
    milei = []
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
    mostraMatriz(matriz,a,num)
    
    for j in range(num-1):
        milei.append(matriz[0][j])
    cont = 1
    for i in range(len(milei)):
        sublista = (milei[0:i+1])
        soma = sum(sublista)
        somat.append(soma/cont)
        cont +=1
    for m in range(a):
        soma = 0
        for n in range(num):
            soma += matriz[m][n]
        somat.append(soma / num)

    return somat, num
def mostraMatriz(matriz,a,num):
    for m in range(a):
        for n in range(num):
            print(f'{matriz[m][n]}', end=' ')
        print()

dadosss = [1,2,3,4,5,6,7,8,9,10]
dadossss = [4.159,4.1293,4.0841,4.0556,4.1071,4.0954,4.1104,4.1095,4.1097,4.1293]

with open('data.txt', 'r') as file:
    dados = [float(line.strip()) for line in file]
n = 5

mediaMovel, num = fazTudo(dados, n)

for i in range(len(mediaMovel)):
    mediaMovel[i] = round(mediaMovel[i],4)

print(mediaMovel)
print(num)



