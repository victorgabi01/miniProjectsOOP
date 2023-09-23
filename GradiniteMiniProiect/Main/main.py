from GradiniteMiniProiect.ClaseGradinita.GradinitaPrivata import GradinitaPrivata
from GradiniteMiniProiect.ClaseGradinita.GradinitaPublica import GradinitaPublica
from GradiniteMiniProiect.ClaseGradinita.GradinitaPublica25 import GradinitaPublica25
#am importat fisierele celor doua clase de interes
if __name__ == '__main__': #lasam asta si codam dupa el

    gradinita_privata_1 = GradinitaPrivata() #initializare obiecte
    #apelare meotde
    gradinita_privata_1.activitate_practica()
    gradinita_privata_1.ora_de_somn()

    gradinita_publica_1 = GradinitaPublica()
    gradinita_publica_1.ora_de_somn()
    gradinita_publica_1.activitate_practica()

    gradinita_publica_25 = GradinitaPublica25()
    gradinita_publica_25.ora_de_somn()
    gradinita_publica_25.activitate_practica()

    #obiect pt a testa culoarea scrisului
    gradinita_publica_25.calcul_buline_rosii()

    #apelare metoda introduceti informatii elevi pe obiectul gradinitapublica25
    gradinita_publica_25.introduceti_informatii_elevi()

