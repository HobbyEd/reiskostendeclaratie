

class rit():
    def __init__ (self, 
                  startPostcode,
                  doelPostcode,
                  afstand,
                  omschrijving): 
        self.__startPostcode = startPostcode
        self.__doelPostcode = doelPostcode
        self.__afstand = afstand
        self.__omschrijving = omschrijving
        self.__nummer = 0

    def getStartPostcode(self): 
        return self.__startPostcode

    def getDoelPostcode(self): 
        return self.__doelPostcode

    def getAfstand(self): 
        return self.__afstand
    
    def zetNummer(self, nummer):
        self.__nummer = nummer
    
    def getNummer(self):
        return self.__nummer

    def getOmschrijving(self):
        return self.__omschrijving

    def __zetAfstand(self, afstand):
        self.__afstand = afstand

    def __zetStartPostcode(self, startPostcode):
        self.__startPostcode = startPostcode

    def __zetDoelPostcode(self, doelPostcode):
        self.__doelPostcode = doelPostcode
