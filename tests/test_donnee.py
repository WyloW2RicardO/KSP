import unittest
import sys
sys.path.insert(0,'E:\\Program\\KSP')
from Metiers.Donnee import LIRE_DONNEE  # noqa: E402

class TEST_KERBIN(unittest.TestCase):
    def setUp(self):
        self.krbn=LIRE_DONNEE('planetes','kerbin')

    def TEST_NOM(self):
        self.assertEqual(self.krbn.nom, 'kerbin')
    
    def TEST_EST_DANS(self):
        self.assertTrue(self.krbn.est_dans)

    def TEST_ATM(self):
        self.assertEqual(self.krbn.atm, 70000)

    def TEST_COUT(self): # si c'est une information inexitante
        self.assertIsNone(self.krbn.cout)

if __name__ == '__main__':
    unittest.main(verbosity=2)