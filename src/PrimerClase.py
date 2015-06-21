'''
Created on 21/6/2015

@author: tony
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        print("Que ")

    def imprimir(self):
        print("prueba de impresion", sep=' ', end='\n', flush=False)
        
c = MyClass()
c.imprimir()