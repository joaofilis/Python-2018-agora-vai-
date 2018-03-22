
'''
Implemente uma função recursiva soma_recursiva 
que recebe uma lista e retorna a soma
de todos os seus elementos 

por exemplo, soma_recursiva([1,2,3]) retorna 6
'''

def soma_recursiva(lista):
    return 12

'''defina uma função recursiva que retorna o maximo elemento de uma lista'''
def maximo(lista):
   return 1
'''
#dica: uma coisa que você vai usar é o calculo recursivo do 
#maximo de lista[1:]
#ou seja, para resolver maximo([4,2,3]) voce vai resolver
#o maximo de lista[1:], que é o máximo([2,3])
'''

'''
Implemente uma função recursiva conta_recursiva, que 
recebe uma lista e um numero, e diz quantas vezes o número
aparece na lista.

Por exemplo conta_recursiva([0,1,2,1,4],1) retorna 2
Por exemplo conta_recursiva([0,1,2,1,4],4) retorna 1
Por exemplo conta_recursiva([0,1,2,1,4],5) retorna 0
Por exemplo conta_recursiva([],5) retorna 0
'''

def conta_recursiva(lista, numero):
    return 0


'''
Agora, a idéia e re-implementar as funcoes, mas para listas de listas

Por exemplo, achar o maximo valor na lista [[[1,2,3],[4,5],11,4],9,8,4] (resposta 11)

Ou contar o numero de ocorrencias de 4 na lista [[[1,2,3],[4,5],11,4],9,8,4] (resposta 3)

Uma lista de listas pode conter listas que também contem listas: [[[[[1]]],2]] é uma lista lista de listas válida

Para ajudar, escrevi uma funcao eh_lista que retorna True se um objeto é lista e 
False se não é
'''
def eh_lista(a):
    return isinstance(a,list)


''' Escreva uma funcao soma_ll que recebe uma lista de listas e retorna a soma de 
todos os números
Por exemplo, soma_ll([[[1,2,3],[4,5],11,4],9,8,4]) é 46
'''
def soma_ll(lista):
    return 12

''' Escreva uma funcao maximo_ll que recebe uma lista de listas
e retorna o maior número que aparece nessa lista de listas.

Nao se preocupe com listas vazias: nenhuma das listas que você
receber conterá listas vazias'''
def maximo_ll(lista):
    return 12
    



import random
import unittest
import sys


class TestStringMethods(unittest.TestCase):

    
    def test_01_soma_funciona(self):
        self.assertEqual(soma_recursiva([1,2,3]),6)
        self.assertEqual(soma_recursiva([1,2,3,4]),10)
        self.assertEqual(soma_recursiva([-1,-2,-3,-4]),-10)
    
    def test_02_soma_pequena(self):
        self.assertEqual(soma_recursiva([1]),1)
        self.assertEqual(soma_recursiva([]),0)
        self.assertEqual(soma_recursiva([-3]),-3)

    def test_03_soma_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            soma_recursiva([1]*100)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)
    
    def test_04_max(self):
        self.assertEqual(maximo([1,2,3]), 3)
        self.assertEqual(maximo([3,2,1]), 3)
        self.assertEqual(maximo([3,10,15,30,2,1]), 30)
    
    def test_05_max_um_elemento(self):
        self.assertEqual(maximo([-1]), -1)
        self.assertEqual(maximo([3]), 3)
    
    def test_06_max_eh_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            maximo(list(range(100)))
            self.fail('a sua função maximo é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao maximo é recursiva')
        finally:
            sys.setrecursionlimit(1000)
    
    def test_07_conta(self):
         self.assertEqual(conta_recursiva([0,1,2,1,4],1), 2)
         self.assertEqual(conta_recursiva([0,1,2,1,4],4), 1)
         self.assertEqual(conta_recursiva([1,1],1), 2)
         self.assertEqual(conta_recursiva([1,1],2), 0)
         self.assertEqual(conta_recursiva([0,1,2,1,4],5), 0)
   
    def test_08_conta_pequena(self):
         self.assertEqual(conta_recursiva([],5), 0)
         self.assertEqual(conta_recursiva([5],5), 1)
         self.assertEqual(conta_recursiva([1],5), 0)
    
    def test_09_conta_recursiva(self):
        sys.setrecursionlimit(50)
        try:
            conta_recursiva([1]*100,1)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)

    def test_10_soma_ll(self):
        self.assertEqual(soma_ll([1,2,3]),6)
        self.assertEqual(soma_ll([1,2,3,4]),10)
        self.assertEqual(soma_ll([-1,-2,-3,-4]),-10)
        self.assertEqual(soma_ll([1]),1)
        self.assertEqual(soma_ll([]),0)
        self.assertEqual(soma_ll([-3]),-3)
        self.assertEqual(soma_ll([[],[]]),0)
        self.assertEqual(soma_ll([[1],[2]]),3)
        self.assertEqual(soma_ll([[[1,2,3],[4,5],11],9,8]),43)
        self.assertEqual(soma_ll([[[1,2,3],[4,5],11,4],9,8,4]),51)
        self.assertEqual(soma_ll([[-1],[1]]),0)
        self.assertEqual(soma_ll([[1],[[2],1]]),4)
    
    def test_11_max_ll(self):
        self.assertEqual(maximo_ll([1,2,3]), 3)
        self.assertEqual(maximo_ll([3,2,1]), 3)
        self.assertEqual(maximo_ll([3,10,15,30,2,1]), 30)
        self.assertEqual(maximo_ll([-1]), -1)
        self.assertEqual(maximo_ll([3]), 3)
        self.assertEqual(maximo_ll([3,[4]]), 4)
        self.assertEqual(maximo_ll([5,[4]]), 5)
        self.assertEqual(maximo_ll([[[1,2,3],[4,5],11,4],9,8,4]),11)
        self.assertEqual(maximo_ll([[[1,12,3],[4,5],11,4],9,8,4]),12)
    
    def test_12_conta_ll(self):
         self.assertEqual(conta_ll([0,1,2,1,4],1), 2)
         self.assertEqual(conta_ll([0,1,2,1,4],4), 1)
         self.assertEqual(conta_ll([1,1],1), 2)
         self.assertEqual(conta_ll([1,1],2), 0)
         self.assertEqual(conta_ll([0,1,2,1,4],5), 0)
         self.assertEqual(conta_ll([],5), 0)
         self.assertEqual(conta_ll([5],5), 1)
         self.assertEqual(conta_ll([1],5), 0)
         self.assertEqual(conta_ll([[[1,2,3],[4,5],11,4],9,8,4],4),3)
         self.assertEqual(conta_ll([[[1,2,3],[4,5],11,4],9,8,4],11),1)
         self.assertEqual(conta_ll([[[1,2,3],[4,5],11,4],9,8,4],15),0)
    


    


    
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

