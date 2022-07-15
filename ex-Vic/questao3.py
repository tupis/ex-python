a = 1
b = 0

while a > b:
    # primeira linha utilizada para definir o valor que o cliente deseja sacar;
    numero = int(input("Valor para sacar entre 10 e 600: "))
    if ((numero >= 10) and (numero <= 600)):
        #Após definir valor, distinguir-se as variáveis de cada nota referente ao valor que ele deseja retirar, para assim ter quantidade de notas e valor;
        cem = int(numero / 100)
        numero = numero - (cem*100)
        cinquenta = int(numero/50)
        numero = numero - (cinquenta*50)
        dez = int(numero/10)
        numero = numero - (dez*10)
        cinco = int(numero/5)
        numero = numero - (cinco*5)
        um = numero
        #Por fim têm-se as quantidades de notas retiradas, conforme sua qauntidade e com base no valor que deseja-se sacar.
        print("Notas R$100,00 = ", cem)
        print("Notas R$ 50,00 = ", cinquenta)
        print("Notas R$ 10,00 = ", dez)
        print("Notas R$  5,00 = ", cinco)
        print("Notas R$  1,00 = ", um)
        b = 1
    else:
        print("por favor insira um valor entre 10 e 600")