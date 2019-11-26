# Visitor/FlowerVisitors.py
# Demonstration of "visitor" pattern.
from __future__ import generators
import random
from abc import ABC, abstractmethod

# La jerarquia de flor no se puede cambiar.
class Flor(object):
    def accept(self, visitor):
        visitor.visit(self)
    def polinizar(self, polinizador):
        print(self, "polinizado por", polinizador)
    def eat(self, eater):
        print(self, "comido por", eater)
    def __str__(self):
        return self.__class__.__name__

class Gladiolo(Flor): pass
class Ranunculo(Flor): pass
class Crisantemo(Flor): pass

class Visitor(ABC):
    @abstractmethod
    def __str__(self):
        pass
        
class Polinizador(Visitor): pass
class Depredador(Visitor): pass

# Añadir la capacidad de hacer actividades "Abeja":
class Abeja(Polinizador):
    def __str__(self):
        return self.__class__.__name__
    def visit(self, flor):
        flor.polinizar(self)

# Añadir la capacidad de hacer actividades "Pajaros":
class Pajaros(Polinizador):
    def __str__(self):
        return self.__class__.__name__
    def visit(self, flor):
        flor.polinizar(self)

# Añadir la capacidad de hacer actividades "gusano": 
class Gusano(Depredador):
    def __str__(self):
        return self.__class__.__name__
    def visit(self, flor):
        flor.eat(self)

def florGen(n):
    flwrs = Flor.__subclasses__()
    for i in range(n):
        yield random.choice(flwrs)()

# Es casi como si tuviera un método para realizar 
# varias operaciones de "Bug" en todas las flores: 
abeja = Abeja()
pajaros = Pajaros()
gusano = Gusano()
for flor in florGen(10):
    flor.accept(abeja)
    flor.accept(pajaros)
    flor.accept(gusano)


