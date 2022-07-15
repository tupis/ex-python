a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))

if (a == 0) or (b == 0) or (c == 0):
    print('Não é um triângulo')
elif (a + b < c) or (a + c < b) or (b + c < a):
    print('Não é um triângulo')
elif (a == b) and (a == c):
    print('Equilátero')
elif (a == b) or (a == c) or (b == c):
    print('Isósceles')
else:
    print('Escaleno')