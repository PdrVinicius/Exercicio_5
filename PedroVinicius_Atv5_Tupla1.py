###Uma lanchonete precisa urgente de um Cardápio com 5 itens, 
# crie um Cardápio com tupla e mostre o resultado no final.

listagem = ('Coxinha', 2.50,
            'Pastel', 3.00,
            'Fatia de Bolo', 2.00,
            'Hot-Dog', 2.50,
            'Hamburguer', 3.00)
print('_'*20)
print(' ')
print(f'{"CARDÁPIO":^20}')
print('_'*20)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<20}', end='')
    else:
        print(f'{listagem[item]:>7.2f}')
print('_'*20)