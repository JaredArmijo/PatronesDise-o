

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def correr(self):
        pass

class Conejo(Animal):
    def correr(self):
        print("Run conejo method called")

class Raton(Animal):
    def correr(self):
        print("Run raton method called")

class Delfin:
    def nadar(self):
        print("method called")

        

class DelfinAdapter(Animal):
    def __init__(self):
        self._delfin = Delfin()
        
    def Correr(self):
        print("correr adapter called")

class Maraton:
    def __init__(self):
        self.bad = Conejo()
        self.tom = Raton()
        self.nemo = DelfinAdapter()
        self.nemo.correr()
        self.bad.correr()
        self.tom.correr
#1
        
        
        
