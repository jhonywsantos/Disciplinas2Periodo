def Agendar_Suite(tipo_suite):
    tipo_lower = tipo_suite.lower()
    if tipo_lower in {'individual', '1'}:
        return 1
    elif tipo_lower in {'dupla', '2'}:
        return 2
    elif tipo_lower in {'tripla', '3'}:
        return 3
    else:
        return None

while True:
    tipo = input(f"\nInforme qual das opções abaixo deseja, utilizando o nome ou suas numerações: Individual (1), Dupla (2), Tripla (3), ou 'sair' para encerrar: ")
    if tipo.lower() == 'sair':
        break

    Tipo_suite = Agendar_Suite(tipo)
    if Tipo_suite is not None:
        Quant_dias = int(input('Quantos dias pretende permanecer na suíte?'))
        
        if Tipo_suite == 1:
            Individual = float(125.00)
            receber = Individual * Quant_dias * 0.85
        elif Tipo_suite == 2:
            Dupla = float(140.00)
            receber = Dupla * Quant_dias * 0.85
        elif Tipo_suite == 3:
            Tripla = float(180.00)
            receber = Tripla * Quant_dias * 0.85 

        print(f'\nO valor a ser pago pela suíte escolhida por {Quant_dias} dias (com desconto de 15%) é: R${receber:.2f}')
    else:
        print('\nOpção inválida. Por favor, escolha entre Individual (1), Dupla (2), Tripla (3) ou digite "sair" para encerrar.')
