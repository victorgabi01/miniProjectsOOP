from GradiniteMiniProiect.ClaseGradinita.GradinitaPublica import GradinitaPublica
from GradiniteMiniProiect.ClaseGradinita.PrintColorString import PrintColorString
#importam si clasa PrintColorString pt a colora scrisul
class GradinitaPublica25(GradinitaPublica): #clasa care mosteneste clasa GradiPublica

    #vom crea 3 atribute , public, protected, privat

    adresa = None
    _nume_gradinita = None
    __director_gradinita = None

    def __init__(self, adresa, nume_gradinita, director_gradinita): #constructor
        self.adresa = adresa
        self._nume_gradinita = nume_gradinita
        self.__director_gradinita = director_gradinita

    @property #intializare getter, setter, deleter pt atributul privat
    def director_gradinita(self):
        pass

    @director_gradinita.getter
    def director_gradinita(self):
        return self.__director_gradinita

    @director_gradinita.setter
    def director_gradinita(self, director_nou):
        self.__director_gradinita = director_nou

    @director_gradinita.deleter
    def director_gradinita(self):
        self.__director_gradinita = None

    def descrie(self): #metode unde folosim cele 3 atribute
        print(f'Gradinita are adresa {self.adresa}, se numeste {self._nume_gradinita} si direcotrul ei este {self.__director_gradinita}')


    def activitate_practica(self):
        print('Copiii se joaca pe balansoar')

    def ora_de_somn(self):
        print('Copiii dorm la ora 2')

    '''
    In interiorul clasei GradinitaPublica25 creati o noua metoda care sa primeasca de la tastatura numarul de buline rosii 
    pe care le-a primit fiecare elev in parte, procesati-le si calculati media aritmetica a numarului de buline rosii. 
    Daca aceasta este mai mare decat cinci, printati pe ecran: “Elevii acestei gradinite sunt foarte neastamparati”.
    '''
    def calcul_buline_rosii(self):
        suma_buline = 0 #intializarea sumei
        nr_copii = int(input('Introduceti nr. de copii:\n'))
        for copil in range(1, nr_copii +1 ):#de la primul la ultimul copil
            numar_buline = int(input(f'Introduceti numarul de buline rosii pentru copilul {copil}: ')) #valoarea copil este un index
            suma_buline += numar_buline #adunam bulinele de la toti copiii
        medie_buline_aritmetica = suma_buline / nr_copii
        print(f'Media bulinelor este: {medie_buline_aritmetica}')
        if medie_buline_aritmetica > 5:
            print(f' {PrintColorString.RED} Copiii sunt obraznici {PrintColorString.RESET}')
            #Am apelat clasa de colorat, la incp punem rosu si la final dam reset, altfel va ramane mereu rosu

    '''
    In interiorul clasei GradinitaPublica25 creati o noua metoda care sa primeasca de la tastatura un dictionar care sa 
    contina o serie de perechi cheie:valoare si dictionare imbricate (embedded, nested) care sa contina urmatoarele informatii:
     numele elevului, numele parintilor, varsta elevului, activitatea preferata. Printati pentru fiecare elev toate 
     informatiile de mai sus.
    '''
    ''' 
    { 1 : { 'nume' : 'Matei',  'nume_parinit' : 'Ion si Maria', 'varsta_elev' : 9, 'activitate_preferata' : 'colorat' }, 2 : { 'nume' : 'Roxana', 'nume_parinit' : 'Ionel si Maria', 'varsta_elev' : 10, 'activitate_preferata' : 'pictat' } }

     
    '''

    def introduceti_informatii_elevi(self):
        __info = eval(input('Introduceti datele despre elev:\n'))#eval preia input-uri si interpreteaza codul, intelge ca info e dictionar, chiar daca nu are date initial, ca si cum ar fi un cod real
        for elev_cheie, detalii_value in __info.items():
            print(f'Elevul numarul {elev_cheie}')
            for date_cheie, date_value in detalii_value.items():
                print(f'{date_cheie} : {date_value}')