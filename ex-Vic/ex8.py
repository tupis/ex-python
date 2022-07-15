numero = int(input('Valor do deve ser entre 10 e 600: '))

if numero > 10 and numero < 600:
    cem = int(numero / 100)
    numero -= (cem * 100)

    cinquenta = int(numero / 50)
    numero -= (cinquenta * 50)

    dez = int(numero / 10)
    numero -= (dez * 10)

    cinco = int(numero / 5)
    numero -= (cinco * 5)

    um = numero

    print(f'Notas R$100,00 = {cem}')
    print(f'Notas R$ 50,00 = {cinquenta}')
    print(f'Notas R$ 10,00 = {dez}')
    print(f'Notas R$  5,00 = {cinco}')
    print(f'Notas R$  1,00 = {um}')
else:
    print('Por favor insira um valor entre 10 e 600')
