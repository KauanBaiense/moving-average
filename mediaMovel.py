import os
os.system('cls')
def fazTudo(lista, num):
    somat = []
    milei = []
    tam = len(lista)
    a = tam + 1 - num
    #Cria a matriz com a linhas e num colunas.
    matriz = [0] * a
    for i in range(a):
        matriz[i] = [0] * num
    #Armazena a matriz com os elementos da lista.
    for m in range(a):
        i = m
        for n in range(num):
            matriz[m][n] = lista[i]
            i += 1
    #Calcula a média móvel dos elementos anteriores ao parâmetro especificado.
    for j in range(num-1):
        milei.append(matriz[0][j])
    cont = 1
    for i in range(len(milei)):
        sublista = (milei[0:i+1])
        soma = sum(sublista)
        somat.append(soma/cont)
        cont +=1
    #Calcula a média móvel com base no parâmetro especificado.
    for m in range(a):
        soma = 0
        for n in range(num):
            soma += matriz[m][n]
        somat.append(soma / num)
    
    return somat, num
os.system('cls')
dados = []
escolha = str(input('Deseja utilizar os dados em .txt ou entrada manual?\nSe sim digite: s\nSenão digite: n\n: '))


with open('data.txt', 'r') as arquivo:
    for linha in arquivo:
        numero = float(linha.strip())
        dados.append(numero)
    
while True:
    try:
        n1 = int(input('Digite um parametro para a média móvel: '))
        n2 = int(input('Digite um parametro para a média móvel: '))
        if n1> 0 and n2 > 0:
            break
        else:
            print("Digite valores inteiros maiores que zero.")
    except ValueError:
        print("Digite valores inteiros maiores que zero.")
            

mediaMovel1, n1 = fazTudo(dados, n1)
mediaMovel2, n2 = fazTudo(dados, n2)
if n1>n2:
    res = n1
    n1 = n2
    n2 = res
    res = mediaMovel2
    mediaMovel2 = mediaMovel1
    mediaMovel1 = res


for i in range(len(mediaMovel1)):
    mediaMovel1[i] = round(mediaMovel1[i],4)
    mediaMovel2[i] = round(mediaMovel2[i],4)

print(mediaMovel1)
print(mediaMovel2)
print(n1)
print(n2)
tendencia = []
for i in range(len(mediaMovel1)):
    if mediaMovel1[i] > mediaMovel2[i]:
        tendencia.append('alta')
    elif mediaMovel1[i] < mediaMovel2[i]:
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

with open("saida.txt", "w") as arquivo:
    arquivo.write(f"DADOS{' ':<10}MM{n1}{' ':<12}MM{n2}{' ':<12}TENDENCIA\n")
    arquivo.write("-" * 65 + "\n")

    for i in range(len(dados)):
        numeros = str(dados[i])
        MM1 = str(mediaMovel1[i])
        MM2 = str(mediaMovel2[i])
        arquivo.write(f"{numeros:<15}{MM1:<15}{MM2:<15}{tendencia[i]}\n")

print("Saída gravada em 'saida.txt'.")