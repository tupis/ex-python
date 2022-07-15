valor_da_hora = float(input('Valor da hora:'))
qtd_horas = int(input('Quantidade de horas trabalhadas no mês:'))

salario_bruto = valor_da_hora * qtd_horas
inss = (8/100) * salario_bruto
sindicato = (5/100) * salario_bruto
ir = (11/100) * salario_bruto

salario_liquido = salario_bruto - inss - sindicato - ir

print(f' + Salário Bruto: R$ {salario_bruto}')
print(f' - IR: R$  {ir}')
print(f' - INSS: R$ {inss}')
print(f' - Sindicato: R$ {sindicato}')
print(f' = Salário Liquido: R$ {salario_liquido}')