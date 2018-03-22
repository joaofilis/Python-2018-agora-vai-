def troca(alist,pos1,pos2):
    alist[pos1],alist[pos2] =  alist[pos2],alist[pos1]
    return alist

def indice_menor2(alist,primeiro):
    menor = primeiro
    for i in range(primeiro,len(alist)):
        if alist[menor] > alist[i]:
            menor = i
    return menor

def selectionsort(alist):
    ajustar = range(0,len(alist))
    for i in ajustar:
        indice_menor = indice_menor2(alist,i)
        temp = alist[i]
        alist[i] = alist[indice_menor]
        alist[indice_menor] = temp
    return alist


def mergesort(lista):
    if (len(lista) <= 1):
        return lista
    meio = int(len(lista)/2)
    metade1 = lista[:meio]
    metade2 = lista[meio:]
    metade1 = mergesort(metade1)
    #a partir daqui, metade1 está ordenada
    metade2 = mergesort(metade2)
    #a partir daqui, metade2 está ordenada
    juntas = merge(metade1,metade2)
    return juntas

def merge(lista1,lista2):
    i=0
    j=0
    resposta=[]
    while (i < len(lista1) and j < len(lista2)):
        if lista1[i] < lista2[j]:
            resposta.append(lista1[i])
            i = i + 1
        else:
            resposta.append(lista2[j])
            j = j + 1
    while (i < len(lista1)):
            resposta.append(lista1[i])
            i = i + 1
    while (j < len(lista2)):
            resposta.append(lista2[j])
            j = j + 1
    return resposta


import random
def gera_vetor(tamanho):
    a = []
    while(len(a)<tamanho):
       i = random.randint(1,200)
       a.append(i)
    return a

import time
def testa_selection(n):
   lista = gera_vetor(n)
   start=time.process_time()
   for i in range(1,1000):
      selectionsort(lista)
   end = time.process_time()
   return end-start

def testa_merge(n):
   lista = gera_vetor(n)
   start=time.process_time()
   for i in range(1,1000):
      mergesort(lista)
   end = time.process_time()
   return end-start

def verifica_velocidade():
    for n in [10,100,200,500]:
        print(str(n)+' elementos')
        print('mergesort levou: '+str(testa_merge(n)))
        print('selection levou: '+ str(testa_selection(n)))

import unittest

class TestStringMethods(unittest.TestCase):
   
    def test_00_troca(self):
        self.assertEqual(
          troca([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],5,6), 
          [3,44,38,5,47,36,15,26,27,2,46,4,19,50,48])
        self.assertEqual(
          troca([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],5,5), 
          [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48])
        self.assertEqual(
          troca([3,44],0,1), 
          [44,3])
        self.assertEqual(
          troca([3],0,0), 
          [3])

    
    def test_02_indice_menor2(self):
        self.assertEqual(
          indice_menor2([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],0), 
          9)
        self.assertEqual(
          indice_menor2([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],9), 
          9)
        self.assertEqual(
          indice_menor2([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],10), 
          11)


    def test_03_selection(self):
        self.assertEqual(
          selectionsort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]), 
          [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50])
        self.assertEqual(
          selectionsort([46,1,18,35,18,9,6,26,47,24,4,29,38,26,30,23,49,5,44,6]), 
          [1, 4, 5, 6, 6, 9, 18, 18, 23, 24, 26, 26, 29, 30, 35, 38, 44, 46, 47, 49])
        self.assertEqual(
          selectionsort( [1,5,15,20,18,30,35,35,38,45,47,48,50]), 
          [1,5,15,18,20,30,35,35,38,45,47,48,50])
    
    def test_04_mergesort(self):
        self.assertEqual(
          mergesort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]), 
          [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50])
        self.assertEqual(
          mergesort([46,1,18,35,18,9,6,26,47,24,4,29,38,26,30,23,49,5,44,6]), 
          [1, 4, 5, 6, 6, 9, 18, 18, 23, 24, 26, 26, 29, 30, 35, 38, 44, 46, 47, 49])
        self.assertEqual(
          mergesort( [1,5,15,20,18,30,35,35,38,45,47,48,50]), 
          [1,5,15,18,20,30,35,35,38,45,47,48,50])



    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

