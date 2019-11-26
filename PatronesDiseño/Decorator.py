from abc import ABC, abstractmethod

class Miche(ABC):
    @abstractmethod
    def precio(self):
        pass
class Cliente(Miche):
    print('Adquiere miche')

class Extra(Miche, ABC):
    def __init__(self, miche):
        self._miche = miche

    @abstractmethod
    def precio(self):
        pass

class MasClamato(Extra):
    def precio(self):
        self._miche.precio()
    


class MasChile(Extra):
    def precio(self):
        self._miche.precio()


class MicheTradicional(Miche):
    def precio(self):
        print('Precio michelada tradicional')

def main():
    concrete_miche = MicheTradicional()
    concrete_miche_a = MasClamato(concrete_miche)
    concrete_miche_b = MasChile(concrete_miche_a)
    concrete_miche_b.precio()

if __name__ == "__main__":
    main()
