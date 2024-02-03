def ano_bissexto(ano):

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

data = int(input('Digite um ano para verificar se é bissexto: '))
if ano_bissexto(data):
    print(f'O ano {data} é bissexto.')
else:
    print(f'O ano {data} não é bissexto.')
