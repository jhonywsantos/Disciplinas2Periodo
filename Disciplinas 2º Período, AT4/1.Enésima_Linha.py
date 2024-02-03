def imprimir_enésima(n):
    for i in range(1, n + 1):
        linha = ' '.join(str(i) for _ in range(i))
        print(linha)

n_informado = int(input('Digite um valor inteiro para n: '))
imprimir_enésima(n_informado)