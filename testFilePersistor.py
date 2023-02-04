import unittest
import datetime 
from ritPerMaand import ritPerMaand
from rit import rit
from reisDag import reisDag
from filePersistor import filePersistor

class TestFilePersistor(unittest.TestCase):
    def testRitPerMaandOpslaan(self):
        __eenRit = rit("3446JZ", "3731GA", "21", "Naar de Boerderij")	
        __tweedeRit = rit("3731GA", "3446JZ", "22","Naar huis")
        __derdeRit = rit("3446JZ", "4101ET", "23", "Naar de Boerderij")
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

        __filePersistor = filePersistor()
        self.assertEqual(True, __filePersistor.persisteerRitPerMaand(__RittenInAugustus))

    def testRitPerMaandOphalen(self):
        __filePersistor = filePersistor()
        __RittenInAugustus = __filePersistor.getRitPerMaand(8, 2022)
        self.assertEqual(True, isinstance(__RittenInAugustus,ritPerMaand))
if __name__ == '__main__':
    unittest.main()
