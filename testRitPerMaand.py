import unittest
from ritPerMaand import ritPerMaand
from rit import rit
from reisDag import reisDag

class TestRitPerMaand(unittest.TestCase):
    __eenRit = rit("3446JZ", "3731GA", "21", "Naar de Boerderij")	
    __tweedeRit = rit("3731GA", "3446JZ", "21", "Naar huis")	

    __derdeRit = rit("3446JZ", "4101ET", "25", "Naar de Boerderij")
    __vierdeRit = rit("4011ET", "3446JZ", "25", "Naar huis")	

    __eenReisdag = reisDag("13-08-2022")
    __eenReisdag.nieuweRitToevoegen(__eenRit)
    __eenReisdag.nieuweRitToevoegen(__tweedeRit)

    __tweedeReisdag = reisDag("14-08-2022")
    __tweedeReisdag.nieuweRitToevoegen(__derdeRit)
    __tweedeReisdag.nieuweRitToevoegen(__vierdeRit)

    __RittenInAugustus = ritPerMaand(8, 2022)
    __RittenInAugustus.nieuweReisDagToevoegen(__eenReisdag)
    __RittenInAugustus.nieuweReisDagToevoegen(__tweedeReisdag)

    def testTotaalAfstand(self):
        self.assertEqual(92, self.__RittenInAugustus.getTotaalAfstand())

    def testTotaalKosten(self):
        self.assertEqual(17.48, self.__RittenInAugustus.getTotaalKosten())
    
    def testGetMaand(self):
        self.assertEqual(8, self.__RittenInAugustus.getMaand()) 

    def testAantalReisDagen(self):
        self.assertEqual(2, self.__RittenInAugustus.getAantalReisDagen())

if __name__ == '__main__':
    unittest.main()
