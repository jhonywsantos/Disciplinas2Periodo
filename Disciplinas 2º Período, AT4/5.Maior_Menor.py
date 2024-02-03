def MaiorNumero(a, b, c):
    if a > b and a > c:
        return f'O maior número é {a}'
    elif b > a and b > c:
        return f'O maior número é {b}'
    elif c > a and c > b:
        return f'O maior número é {c}'
    
    elif a == b and a == c:
        return 'Todos os números têm o mesmo valor. Portanto, não existe um maior.'
    elif a == b:
        return f'Os maiores números são o primeiro ({a}) e o segundo ({b}), pois são iguais e maiores que o terceiro ({c}).'
    elif a == c:
        return f'Os maiores números são o primeiro ({a}) e o terceiro ({c}), pois são iguais e maiores que o segundo ({b}).'
    elif b == c:
        return f'Os maiores números são o segundo ({b}) e o terceiro ({c}), pois são iguais e maiores que o primeiro ({a}).'

def MenorNumero(a, b, c):
    if a < b and a < c:
        return f'O menor número é {a}'
    elif b < a and b < c:
        return f'O menor número é {b}'
    elif c < a and c < b:
        return f'O menor número é {c}'
    
    elif a == b and a == c:
        return 'Todos os números têm o mesmo valor. Portanto, não existe um menor.'
    elif a == b:
        return f'Os menores números são o primeiro ({a}) e o segundo ({b}), pois são iguais e menores que o terceiro ({c}).'
    elif a == c:
        return f'Os menores números são o primeiro ({a}) e terceiro ({c}), pois são iguais e menores que o segundo ({b}).'
    elif b == c:
        return f'Os menores números são o segundo ({b}) e o terceiro ({c}), pois são iguais e menores que o primeiro ({a}).'

a = float(input('Digite o valor do primeiro número:'))
b = float(input('Digite o valor do segundo número:'))
c = float(input('Digite o valor do terceiro número:'))

print(MaiorNumero(a, b, c))
print(MenorNumero(a, b, c))



