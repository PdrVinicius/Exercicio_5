##Crie um Algoritimo ultilizando lista para somar os valore de dividas,
# e mostre o resultado no final:

val = []

while True:
    print(' ')
    val.append(float(input('Informe o Valor da Divida: ')))
    print(' ')
    resp = str(input('Deseja Continuar? [S/N] '))
    print(' ')
    if resp in 'nN':
        break
print('O Valor total das suas Dividas é: ', (sum(val)))