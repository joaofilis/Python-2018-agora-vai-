from random import randint
from time import sleep
import os
nomes = ['bruno','cristopher','isadora','joão','kaio','vinicius']
while True:
    os.system('cls')
    print('=-'*20)
    nome = input('digite seu nome: ')
    print('=-'*20)
    sleep(1)
    valor = len(nomes)-1
    if valor == 0:
        print('=-'*20)
        print(f'{nome} você tidrou o(a) {nomes[0]}')
        print('=-'*20)
        break
    numero = randint(0,valor)
    if nome != nomes[numero] :
        print('=-'*20)
        print(f'{nome} você tidrou o(a){nomes[numero]}')
        print('=-'*20)
        nomes.remove(nomes[numero])
        sleep(5)
        os.system('cls')
    if len(nomes) == 0:
        break
print('=-'*20)
print('acabou')
print('=-'*20)
sleep(20)
