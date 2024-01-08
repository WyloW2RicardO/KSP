from pandas import read_csv
import sys

#chemain=sys.path[0]
#print(chemain)
#n = len(chemain)-len('/metiers')
#print(sys.path.__contains__(chemain[:n]))
#if not sys.path.__contains__(chemain[:n]):
#    sys.path.insert(0,chemain[:n])
print(sys.path)

plnt_data=read_csv('./donnees/planetes.csv')
class planete:
    nom:str
    def __init__(self,nom):
        self.nom=nom
    def lgn(self):
        return plnt_data['NOM'].isin([str(self.nom)])
    def mss(self):
        return float(plnt_data.loc[self.lgn,'MSS'].item())