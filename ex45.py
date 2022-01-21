'''
Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô 
'''
from random import randint
from time import sleep
print('--==--=='*10)
print('''DIGITE A OPÇÃO DE JOGO:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA ''') 
print('--==--=='*10)
opition = int(input('Digite a sua opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
itens = ('pedra','papel','tesoura')
pc = randint(0,2)
print('O computador escolheu {} '.format(itens[pc]))
# 0 pedra, 1 papel, 2 tesoura
if opition == 1:
    if pc == 2:
        print("VOCÊ GANHOU!")
    elif pc == 1:
        print('VOCÊ PERDEU!')
    else:
        print('JOGO EMPATADO!')
elif opition == 2:
    if pc == 2:
        print('VOCÊ PERDEU!')
    elif pc == 1:
        print('JOGO EMPATADO')
    else:
        print('VOCÊ GANHOU!')
elif opition == 3:
    if pc == 0:
        print('VOCÊ PERDEU!')
    elif pc == 1:
        print('VOCÊ GANHOU!')
    else:
        print('JOGO EMPATADO!')