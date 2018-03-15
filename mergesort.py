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
'''
defina a funcao merge do mergesort como já discutido
'''
def merge(lista1,lista2):
    i = 0
    final = []
    x = 0
    if len(lista1)== 0 and len(lista2) == 0:
        return final
    if len(lista1) == 0:
        return lista2
    if len(lista2) == 0:
        return lista1
    while len(lista1) and len(lista2) >= i:
            if lista1[0] < lista2[0]:
                final.append(lista1[0])
                lista1 = lista1[1:]
            else:
                final.append(lista2[0])
                lista2 = lista2[1:]
    if len(lista1) == 0:
        while x < len(lista2):
            final.append(lista2[x])
            x = x+1
    elif len(lista2) == 0:
        while x < len(lista1):
            final.append(lista1[x])
            x = x+1
    return final


import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_01_merge_simple(self):
        self.assertEqual(merge([1,2,3],[4,5,6]), [1,2,3,4,5,6])
        self.assertEqual(merge([1,3,5],[2,4,6]), [1,2,3,4,5,6])
    
    def test_02_merge_vazios(self):
        self.assertEqual(merge([1,2,3],[]), [1,2,3])
        self.assertEqual(merge([],[2,4,6]), [2,4,6])
        self.assertEqual(merge([],[]), [])
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

