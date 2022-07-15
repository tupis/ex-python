pontos = 0

telefone = str(input("Telefonou para a vítima? ")).lower()
if telefone == 'sim':
    pontos += 1
lugar = str(input("Esteve no local do crime? ")).lower()
if lugar == 'sim':
    pontos += 1
morar = str(input("Mora perto da vítima? ")).lower()
if morar == 'sim':
    pontos += 1
deve = str(input("Devia para a vítima? ")).lower()
if deve == 'sim':
    pontos += 1
trabalhou = str(input("Já trabalhou com a vítima ?")).lower()
if trabalhou == 'sim':
    pontos += 1

if pontos == 2:
    print('Pessoa é suspeita')
elif pontos == 3 or pontos == 4:
    print('Pessoa é cúmplice')
elif pontos == 5:
    print("Pessoa é o assassino")
else:
    print("Pessoa é inocente")