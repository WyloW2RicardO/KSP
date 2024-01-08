import sys

#chemain=sys.path[0]
#n = len(chemain)-len('/testes')
#if not sys.path.__contains__(chemain[:n]):
#    sys.path.insert(0,chemain[:n])
#from metiers.donnee import planete

class test_donnee_planete():
    def test_nom(self):
        a=planete('kerbin')
        assert a.nom == 'kerbin'