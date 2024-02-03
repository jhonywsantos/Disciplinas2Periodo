def Verificar_Sinal(Numero):
    if Numero<0:
        return 'N'
    else:
        return 'P'
    
Valor = float(input('Digite o valor de um número:'))
resultado = Verificar_Sinal(Valor)
print(f'O resultado do sinal resulta em: {resultado}')