#   Crie um programa que leia o nome de varios jogadores e quantas partidas eles jogaram.
#   Depois vai ler a quantidade de gols feitos em cada partida e o total de gols.
#   No final, tudo isso será guardado em um dicionário e apresentado no final. incluindo
#   um sistema de visualização de detalhes do aproveitamento de cada jogador.

gols = list()
jogador = dict()
time = list()

while True:
    jogador['Nome'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas Partidas {jogador["Nome"]} jogou? '))

    if partidas > 0:
        for c in range(0, partidas):
            gols.append(int(input(f'     Quantos gols na {c+1}º partida? ')))
        jogador['Gols'] = gols[:]
        jogador['Total'] = sum(gols)
    time.append(jogador.copy())

    while True:
        op = str(input('Deseja Inserir outro Jogador? [S/N]')).upper().strip()[0]
        if op in 'SN':
            jogador.clear()
            gols.clear()
            break
        print('Opção inválida! Tente novamente.')
    if op == 'N':
        break

print('-='*20)
print(f'{"Cod":<5}{"NOME":<10}{"Total":<10}{"Gols":<10}')
for i, j in enumerate(time):
    print(f'{i:<5}{j["Nome"]:<10}{j["Total"]:<10}{j["Gols"]}')


print('-='*20)
print(' ')