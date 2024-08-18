
matriz = []


def inserir(tmatriz):
    for j in range(tmatriz):
        linha = []  # Cria uma nova linha
        for i in range(tmatriz):
            valor = int(input(f'Digite o valor da linha {j}, coluna {i}: '))
            linha.append(valor)
        matriz.append(linha)


def mostrarrecursivo(linha=0,coluna=0):
    if linha >= len(matriz):
        return
    if coluna >= len(matriz[linha]):
        print()  # Muda de linha após exibir uma linha inteira
        mostrarrecursivo(linha + 1, 0)  # Vai para a próxima linha
    else:
        print(matriz[linha][coluna], end=" ")
        mostrarrecursivo(linha, coluna + 1)  # Continua na mesma linha


def main():
    tmatriz = int(input('Digite o tamanho da matriz (x*x):'))
    inserir(tmatriz)  # Insere os valores na matriz
    mostrarrecursivo()  # Exibe a matriz de forma recursiva


# Chama a função principal
main()

