qtd_km = int(input("Qual a quantidade de quilômetros percorrido? "))
qtd_dias = int(input("Qual a quantidade de dias que você usou o carro? "))
price_km = int(input("Qual é o preço por quilômetro? "))
price_dia = int(input("Qual o preço por dia? "))

total = (price_km * qtd_km) + (price_dia * qtd_dias)

print(f'O preço total ficou por: R$ {total}')