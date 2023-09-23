from GradiniteMiniProiect.ClaseGradinita.GradinitaABC import GradinitaABC #Iportam fisierul gradinita in gradinitapublica

class GradinitaPrivata(GradinitaABC):
    #metode
    def activitate_practica(self):
        print('Copiii invata sa modeleze plastilina')

    def ora_de_somn(self):
        print('Copiii se culca la ora 3')

    __info = None #atribut privat

    #constructor pt atributul privat care va fi citit la tastatura
    def __init__(self,info = eval(input('Introduceti informatii despre noul elev:\n')) ): #folosim eval pt a interpreta codul ca si cum ar fi real
        self.__info = info
    @property #initializare getter, setter, deleter pt atribtul privat
    def adauga_elevi(self):
        pass
    @adauga_elevi.getter
    def adauga_elevi(self):
        return self.__info

    @adauga_elevi.setter
    def adauga_elevi(self, elev_nou_info):
        self.__info = elev_nou_info

    @adauga_elevi.deleter
    def adauga_elevi(self):
        self.__info = None
    def adauga_elevi_descriere(self, **kwargs): #dictionar informartii elevi
        for elev_cheie, detalii_value in self.__info.items():
            print(f'Elevul este {elev_cheie}')
            for date_cheie, date_value in detalii_value.items():
                print(f'{date_cheie} : {date_value}')

    '''
    {'Oana Popescu':{'varsta':'8', 'an_inscriere':'2021'}, 'Marian Pisica':{'varsta':'7', 'an_inscriere':'2022'}} # ce punem la tastatura
    {'valoare_nume':{'varsta':'valoare_varsta', 'an_inscriere':'valoare an inscriere'}} #legenda structura
 

    '''
