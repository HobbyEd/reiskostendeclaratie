class ritPerMaand():
    def __init__ (self, 
                  maand, 
                  jaar):
        try: 
            maand = int(maand)
            jaar = int(jaar)
            if maand >= 1 and maand <= 12:
                self.__maand = maand
                self.__jaar = jaar
                self.__reisDagen = []
                self.__totaalAfstand = 0
                self.__totaalKosten = 0
        except: 
            print("Maand moet een getal tussen 1 en 12 zijn")


    def nieuweReisDagToevoegen(self, reisDag):
        try: 
            if int(reisDag.getMaand()) == int(self.__maand):
                self.__reisDagen.append(reisDag)
                self.__totaalAfstand += reisDag.getTotaalAfstand()
                self.__totaalKosten += reisDag.getTotaalKosten()
        except:
            print("Deze reisdag hoort niet bij deze maand")

    def verwijderReisDag(self, reisDag):
        self.__reisDagen.remove(reisDag)
        self.__totaalAfstand -= int(reisDag.getTotaalAfstand())
        self.__totaalKosten -= int(reisDag.getTotaalKosten())

    def getAlleReisDagen(self): 
        return self.__reisDagen

    def getAantalReisDagen(self):
        return len(self.__reisDagen)

    def getMaand(self):
        return self.__maand
    
    def getJaar(self):
        return self.__jaar

    def getTotaalAfstand(self):
        return self.__totaalAfstand

    def getTotaalKosten(self):
        return self.__totaalKosten

    def zetTotaalAfstand(self, totaalAfstand):
        self.__totaalAfstand = totaalAfstand
    
    def zetTotaalKosten(self, totaalKosten):
        self.__totaalKosten = totaalKosten
    