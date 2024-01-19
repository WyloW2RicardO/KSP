import pytest
import sys

sys.path.insert(0, "E:\\Program\\KSP")
from Metiers.donnee import LIRES  # noqa: E402
from Metiers import physique  # noqa: E402


# class Test_KERBIN_ALTITUDE:
# def setUp(self):
krbn = LIRES("planetes", "kerbin")
alttd0 = 0
alttd1 = krbn.atm + 10000


def test_VITESSE_ORBITAL():
    assert physique.VITESSE_ORBITAL(krbn, krbn.ryn + alttd0) > 1715
    assert physique.VITESSE_ORBITAL(krbn, krbn.ryn + alttd1) > 1661


def test_GRAVITE():
    assert physique.GRAVITE(krbn, krbn.ryn + alttd0) > 9
    assert physique.GRAVITE(krbn, krbn.ryn + alttd1) > 7


def test_HAUTEUR_ECHALLE():
    assert physique.HAUTEUR_ECHALLE(krbn) > 8431


def test_PRESSION():
    assert physique.PRESSION(krbn, alttd0) == 101325.0
    assert physique.PRESSION(krbn, alttd1) == 0


def test_DENSITER():
    assert physique.DENSITER(krbn, alttd0) > 42
    assert physique.DENSITER(krbn, alttd1) == 0


if __name__ == "__main__":
    pytest.main(["-v", "Tests\\test_physique.py"])
