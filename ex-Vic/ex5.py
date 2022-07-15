import math
metros_quadrados = int(input("Quantos metros quadrados você deseja pintar? "))

litros = (metros_quadrados / 6) * 1.1

lata = math.ceil((litros / 18))
preco_lata = 80
apenas_lata = (lata * preco_lata)

galao = math.ceil((litros / 3.6))
preco_galao = 25
apenas_galao = galao * preco_galao

mistura_lata = int((litros / 18))
litros -= (mistura_lata * 18)
mistura_galao = math.ceil(litros / 3.6)

preco_mistura_lata = (mistura_lata * 80)
preco_mistura_galao = (mistura_galao * 25)
preco_total_mistura = preco_mistura_galao + preco_mistura_lata

print(galao)
print(lata)


print(f'Comprando apenas galão você gastará: R$ {apenas_galao:.2f}')
print(f'Comprando apenas latas você gastará: R$ {apenas_lata:.2f}')
print(f'Comprando misturado você precisará de {mistura_lata} latas, custando R$ {preco_mistura_lata:.2f} e {mistura_galao:.2f} galões, custando R$ {preco_mistura_galao:.2f}, totalizando R$ {preco_total_mistura:.2f}')