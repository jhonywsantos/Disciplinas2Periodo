def imprimir_enésima_invertida(n):
    for i in range(n, 0, -1):
        linha = ' '.join(str(i) for _ in range(i))
        print(linha)

n_informado = int(input('Digite um valor inteiro para n: '))
imprimir_enésima_invertida(n_informado)
