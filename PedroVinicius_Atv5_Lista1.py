## Um professor Precisa sortear a ordem de aparesentação de trabalhos dos alunos,
# Faça um Algoritimo que leia o nome de quatro lideres de cada grupo e mostrar na ordem sorteada: 

import random
print(' ')
g1 = (input('Lider do Primeiro Grupo: '))
print(' ')
g2 = (input('Lider do Segundo Grupo: '))
print(' ')
g3 = (input('Lider do Terceiro Grupo: '))
print(' ')
g4 = (input('Lider do Quarto Grupo: '))
lista = [g1, g2, g3, g4]
random.shuffle(lista)
print(' ')
print('A ondem de Apresentação é: ')
print(' ')
print(lista)