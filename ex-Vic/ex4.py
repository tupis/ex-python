sexo = int(input('Escolha: 1- Sexo Masculino / 2- Sexo Feminino: '))
altura = float(input('Altura: '))
peso = float(input('Peso: '))

peso_ideal = 0

def calcularPesoIdeal ():
	if peso < peso_ideal:
		print('Abaixo do peso ideal!')
	elif peso == peso_ideal:
		print('No peso ideal!')
	else:
		print('Acima do peso ideal!')

	print(f'peso ideal: {peso_ideal}KG')

if sexo == 1 :
	peso_ideal = (72.7 * altura) - 58
	calcularPesoIdeal()
elif sexo == 2:
	peso_ideal = (62.1 * altura) - 44.7
	calcularPesoIdeal()
else:
	print('Por favor insira um valor correto')