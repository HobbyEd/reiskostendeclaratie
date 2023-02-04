import unittest
from rit import rit

class Test_Rit(unittest.TestCase):
    def test_rit(self):
        eenRit = rit("3446JZ", "3731GA", "21", "Naar de Boerderij")
        self.assertEqual("3446JZ", eenRit.getStartPostcode())
        self.assertEqual("3731GA", eenRit.getDoelPostcode())
        self.assertEqual("21", eenRit.getAfstand())
if __name__ == '__main__':
    unittest.main()
