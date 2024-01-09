import pandas as pd

def lire(data,ligne,colone) :
    if colone in data.columns.values.tolist() :
        return data.loc[ligne, [colone]].values[0][0]
    else :
        return None

class lire_donnee :
    def __init__(self, datas, noms) :
        url='E:/Program/KSP/donnees/' + datas + '.csv'
        try :
            pd.read_csv(url)
        except FileNotFoundError:
            print('dans lire_donnee :', datas, 'est mal ecrit')
            exit()
        else :
            self.data = pd.read_csv(url)
        self.nom=noms
        self.lgn = self.data['NOM'].isin([self.nom])
        self.est_dans = self.lgn.any()
        if not self.est_dans:
            print('dans lire_donnee :', self.nom, "n'est pas dans", self.data)
            exit()
        self.atm    =lire(self.data,self.lgn,'ATM')
        self.cout   =lire(self.data,self.lgn,'COUT')
        self.day    =lire(self.data,self.lgn,'DAY')
        self.ergl   =lire(self.data,self.lgn,'ERGL')
        self.ergl_d =lire(self.data,self.lgn,'ERGL_D')
        self.haut   =lire(self.data,self.lgn,'HAUT')
        self.isp_asl=lire(self.data,self.lgn,'ISP_ASL')
        self.isp_vac=lire(self.data,self.lgn,'ISP_VAC')
        self.klv    =lire(self.data,self.lgn,'KLV')
        self.mltpl  =lire(self.data,self.lgn,'MLTPL')
        self.mol    =lire(self.data,self.lgn,'MOL')
        self.mss    =lire(self.data,self.lgn,'MSS')
        self.oxdzr  =lire(self.data,self.lgn,'OXDZR')
        self.oxdzr_d=lire(self.data,self.lgn,'OXDZR_D')
        self.prs    =lire(self.data,self.lgn,'PRS')
        self.pss_asl=lire(self.data,self.lgn,'PSS_ASL')
        self.pss_vac=lire(self.data,self.lgn,'PSS_VAC')
        self.tll    =lire(self.data,self.lgn,'TLL')