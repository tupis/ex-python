qtd_notas = int(input("Quantas notas você deseja inserir ? "))

i = 0
soma_notas = 0

while i < qtd_notas:
    nota = int(input("Insira a nota: "))
    soma_notas += nota
    i += 1

media_notas = soma_notas / qtd_notas

print(f'A sua média é {media_notas}')