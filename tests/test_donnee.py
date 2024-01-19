import pytest
import sys

sys.path.insert(0, "E:\\Program\\KSP")
from Metiers import donnee  # noqa: E402


#class Test_KERBIN:
    #def setUp(self):
krbn = donnee.LIRES("planetes", "kerbin")
krbn1 = donnee.LIRES("planetes", "kerbi")

def test_NOM():
    assert krbn.nom == "kerbin"
    assert krbn1.nom == "kerbi"

def test_EST_DANS():
    assert krbn.est_dans == True  # noqa: E712
    assert krbn1.est_dans == False  # noqa: E712

def test_ATM():
    assert krbn.atm == 70000

def test_COUT():  # si c'est une information inexitante
    assert krbn.cout is None 


if __name__ == "__main__":
    pytest.main(["-v", "Tests\\test_donnee.py"])
