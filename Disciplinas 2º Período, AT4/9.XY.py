'''def somar_valores_xy(valores):
    if (valores != float):
        return True
    else:
        False

função = int(input('Digite o valor da sua função f(x) = y, utilizando apenas números inteiros:'))
for i in range(4):
    valor = int(input('Digite um valor para representar "X":'))
    somar = valor*função
'''


def somar_valores_xy(valores):
    if type(valores) != float:
        return True
    else:
        return False

função = int(input('Digite o valor da sua função f(x) = y, utilizando apenas números inteiros: '))
for i in range(4):
    valor_x = int(input('\nDigite um valor para representar "X": '))
    if somar_valores_xy(função):
        resultado = (valor_x * função)
        print(f'Resultado para f(X) = {valor_x}: {resultado}')
    else:
        print('\nA função não está corretamente definida. Certifique-se de usar números inteiros.')






