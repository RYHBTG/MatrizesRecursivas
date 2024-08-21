# Relatório final do projeto
#### Autor: Héberton Santiago 18/08/2024

~~~python
matriz = []


def inserir(linha,coluna):
    for j in range(linha):
        linha = []  # Cria uma nova linha
        for i in range(coluna):
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
    linha = int(input('Digite o tamanho da matriz (x*x):'))
    coluna = int(input('Digite o tamanho da matriz (x*x):'))
    inserir(linha,coluna)  # Insere os valores na matriz
    mostrarrecursivo()  # Exibe a matriz de forma recursiva


# Chama a função principal
main()

~~~~

### Começemos por partes:
Para começar a programação primeiro deve-se criar uma matriz vazia para prosseguir com o código sem erros

Em seguida começamos pela função de inserimento, o usuário fornece um valor na classe **main()**, em seguida este valor é levado até a classe **inserir(linha,coluna)**

Após o usuário ter fornecido o tamanho da matriz por completo, o programa segue para a função de inserir valores na matriz, onde o usuário insere os valores desejados.

### Mostrar Recursivamente
Agora que a matriz está preenchida, o programa segue para a função de **mostrarrecursivo()**,para isso seguiremos por partes o que cada *if* realiza:
- **if linha >= len(matriz)**: Nesse caso, o programa irá conferir se todos os itens da linha foram exibidos.
- **if coluna >= len(matriz[linha])**: Aqui o programa faz uma verificação para saber se a coluna é menor ou igual ao tamanho da linha, e caso for ira pular para a próxima e continuar exibindo
- **else: print(matriz[linha][coluna])**: Aqui o programa ira exibir item por item
- **mostrarrecursivo(linha + 1, coluna)**: E aqui é o somatório aonde vai adicionando valores afim de percorrer toda coluna em cada uma das linhas
## E após finalizar todo o processo, o programa se encerra deixando o usuário com o resultado do que construiu:
### Este é um exemplo de uma matriz 2x2
![alt text](image-2.png)


