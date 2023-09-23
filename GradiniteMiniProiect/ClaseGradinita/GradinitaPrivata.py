from GradiniteMiniProiect.ClaseGradinita.GradinitaABC import GradinitaABC #Iportam fisierul gradinita in gradinitapublica

class GradinitaPrivata(GradinitaABC):
    #metode
    def activitate_practica(self):
        print('Copiii invata sa modeleze plastilina')

    def ora_de_somn(self):
        print('Copiii se culca la ora 3')
