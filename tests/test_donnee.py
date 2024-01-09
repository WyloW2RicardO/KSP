import unittest
import sys
sys.path.insert(0,'E:\\Program\\KSP')
from metiers.donnee import lire_donnee  # noqa: E402

class test_donnee_planete(unittest.TestCase):
    def setUp(self):
        self.krbn=lire_donnee('planetes','kerbin')

    def test_nom(self):
        self.assertEqual(self.krbn.nom, 'kerbin')
    
    def test_est_dans(self):
        self.assertTrue(self.krbn.est_dans)

    def test_atm(self):
        self.assertEqual(self.krbn.atm, 70000)

    def test_cout(self):
        self.assertIsNone(self.krbn.cout)

if __name__ == '__main__':
    unittest.main(verbosity=2)