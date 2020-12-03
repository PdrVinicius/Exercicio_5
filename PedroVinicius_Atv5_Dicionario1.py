#   Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#   e mostre o resultado no final.

print(' ')
aluno = {'Nome': str(input('Insira o Nome do Aluno: ')).strip(),
         'Média': float(input('Insira a Média do Aluno: '))}

if aluno['Média'] >= 7:
    print(' ')
    aluno['Situação'] = 'Aprovado(a)'
    print(' ')
else:
    aluno['Situação'] = 'Reprovado(a)'
    print(' ')

for i, j in aluno.items():
    print(f'{i}: {j}')
    print(' ')