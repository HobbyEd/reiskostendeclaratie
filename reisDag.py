import datetime

class reisDag(): 
    def __init__ (self, 
                  datum): 
        self.__datum = datum
        self.__rit = []
        self.__totaalAfstand = 0
        self.__totaalKosten = 0
        
    def nieuweRitToevoegen(self, rit):
        self.__rit.append (rit)
        rit.zetNummer(len(self.__rit))
        self.__totaalAfstand += int(rit.getAfstand())
        self.__totaalKosten += int(rit.getAfstand()) * 0.19

    def verwijderRit(self, rit):
        self.__rit.remove(rit)
        self.__totaalAfstand -= int(rit.getAfstand())
        self.__totaalKosten -= int(rit.getAfstand()) * 0.19

    def getAlleRitten(self): 
        return self.__rit
    
    def getAantalRitten(self):
        return len(self.__rit)
        
    def getTotaalAfstand(self):
        return self.__totaalAfstand

    def getTotaalKosten(self):
        return self.__totaalKosten

    def getMaand(self):
        if not isinstance(self.__datum, datetime.date):
            datum = datetime.datetime.strptime(self.__datum, "%d-%m-%Y") 
        else:
            datum = self.__datum
        return datum.month

    def getDatum(self):
        if isinstance(self.__datum, datetime.date):
            return str(self.__datum.strftime("%d-%m-%Y"))
        else: 
            return self.__datum

    def zetTotaalAfstand(self, totaalAfstand):
        self.__totaalAfstand = totaalAfstand

    def zetTotaalKosten(self, totaalKosten):
        self.__totaalKosten = totaalKosten