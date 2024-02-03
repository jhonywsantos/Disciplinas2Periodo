def soma_digitos(numero):
    numeros = str(numero)
    soma = 0
    
    for digito in numeros:
        soma += int(digito)
    return soma

valor = int(input('Digite um número inteiro: '))
resultado = soma_digitos(valor)
print(f'A soma dos dígitos do número {valor} é: {resultado}')
