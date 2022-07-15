#Primeiro cria-se um loop, uma condição para a primeira pergunta.
a = 1 
b = 0
while (a > b):
    numb1 = float(input("Digite o primeiro número: "))
    numb2 = float(input("Digite o segundo número: "))
    operação = int(input("Escolha a operação: \n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n"))
    soma = numb1 + numb2
    subtração = numb1 - numb2 
    multiplicação = numb1 * numb2 
    divisão = numb1 / numb2
    if (operação == 1):
        print(soma)
    elif (operação == 2):
        print(subtração)
    elif (operação == 3):
        print(multiplicação)
    elif (operação == 4):
        print(divisão)
    else:
        print("Insira um valor válido")
#Após efetuar a primeira operação, caso ele não deseje continuar com outra operação, necessita-se encerrar o loop, cria-se outra condição.
    nova_operação = int(input("Deseja fazer outra operação ?\n1 - Sim\n2 - Não\n"))
    if (nova_operação == 2): b = 1
    
    
    
