import unittest
from reisDag import reisDag
from rit import rit

class TestDagRit(unittest.TestCase):
    __eersteRit = rit("3446JZ", "3731GA", "21", "Naar de Boerderij")
    __tweedeRit = rit("3446JZ", "3731GA", "21","Naar huis")
    __eenReisdag = reisDag("13-08-2022")

    __eenReisdag.nieuweRitToevoegen(__eersteRit)
    __eenReisdag.nieuweRitToevoegen(__tweedeRit)

    def testTotaalAfstand(self):
        self.assertEqual(42, self.__eenReisdag.getTotaalAfstand())

    def testTotaalKosten(self):
        self.assertEqual(7.98, self.__eenReisdag.getTotaalKosten())

    def testGetMaand(self): 
        self.assertEqual(8, self.__eenReisdag.getMaand())

    def testAantalRiten(self):
        self.assertEqual(2, self.__eenReisdag.getAantalRitten())

if __name__ == '__main__':
    unittest.main()
