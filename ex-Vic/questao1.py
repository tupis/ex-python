lado_1 = float(input("Digite o lado1: "))
lado_2 = float(input("Digite o lado2: "))
lado_3 = float(input("Digite o lado3: "))
#Verifica-se primeiro se o triângulo existe ou não
if (lado_1 + lado_2 < lado_3) or (lado_1 + lado_3 < lado_2) or (lado_2 + lado_3 < lado_1):
    print("Não é um triângulo")
#Dada a existência, verifica-se o tipo
elif (lado_1 == lado_2) and (lado_2 == lado_3):
    print("Triângulo equilátero")
elif (lado_1 == lado_2) or (lado_1 == lado_3) or (lado_2 == lado_3):
    print("Triângulo isóceles")
else: 
    print("Triângulo escaleno")



