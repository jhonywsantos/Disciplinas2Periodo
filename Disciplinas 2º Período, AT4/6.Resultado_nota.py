def calcular_resultado(media, faltas):
    if media >= 7 and media < 9.5:
        return 'Aprovado!'
    elif media < 7:
        return 'Reprovado!'
    elif media > 9.5:
        return 'Aprovado com louvor.'
    elif faltas > 10:
        return 'Reprovado por falta!'

media = float(input('Informe o resultado da sua média: '))
faltas = int(input('Informe a sua quantidade de faltas: '))
resultado = calcular_resultado(media, faltas)
print(resultado)
