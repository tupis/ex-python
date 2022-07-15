atleta = str(input("Qual o nome do(a) atleta ? "))
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))
nota5 = float(input("Insira a quinta nota: "))
nota6 = float(input("Insira a sexta nota: "))
nota7 = float(input("Insira a sétima nota: "))


notas = [nota1, nota2, nota3, nota4, nota5, nota6, nota7]
new_notas = []
melhor_nota = 0
pior_nota = 0
somar_new_notas = 0

print("Atleta: ", atleta)

for nota in notas:
  print("Nota: ", nota)

notas.sort()

for nota in notas:
  if nota == notas[0] or nota == notas[len(notas) - 1]:
    if nota > melhor_nota:
      melhor_nota = nota
  else:
    new_notas.append(nota)

for nota in new_notas:
  somar_new_notas += nota

pior_nota = notas[0]

media =  somar_new_notas / len(new_notas)

print("")
print("")
print("Resultado final:")
print("Atleta: ", atleta)
print("Melhor nota: ", melhor_nota)
print("Pior notaa: ", pior_nota)
print("Média: ", media)