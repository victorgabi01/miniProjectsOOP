from abc import ABC, abstractmethod

class GradinitaABC(ABC): #clasa abstracta

    #metode abstracte
    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError

#in pachetul clase gradinita vom defini doar clasele, in pachetul main acestea vor fi rulate