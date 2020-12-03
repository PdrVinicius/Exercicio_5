#Uma Professora pediu para seus alunos do Segundo ano estudarem numeros pares para a prova,
# Desenvolva um programa que leia quatro valores pelo teclado. e mostre o resultado para ajudar os alunos:


num = (int(input('1º valor:')), int(input('2º valor:')), int(input('3º valor:')), int(input('4º valor:')))
print(num)
print('Esses são Pares: ', end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' ') 