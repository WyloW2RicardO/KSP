import pandas as PD

def LIRE(data,ligne,colone) :
    if colone in data.columns.values.tolist() :
        return data.loc[ligne, [colone]].values[0][0]
    else :
        return None

class LIRE_DONNEE :
    def __init__(self, datas, noms) :
        url='E:/Program/KSP/Donnee/' + datas + '.csv'
        try :
            PD.read_csv(url)
        except FileNotFoundError:
            print('dans LIRE_DONNEE :', datas, 'est mal ecrit')
            exit()
        else :
            self.data = PD.read_csv(url)
        self.nom=noms
        self.lgn = self.data['NOM'].isin([self.nom])
        self.est_dans = self.lgn.any()
        if not self.est_dans:
            print('dans LIRE_DONNEE :', self.nom, "n'est pas dans", self.data)
            exit()
        self.atm    =LIRE(self.data,self.lgn,'ATM')
        self.cout   =LIRE(self.data,self.lgn,'COUT')
        self.day    =LIRE(self.data,self.lgn,'DAY')
        self.ergl   =LIRE(self.data,self.lgn,'ERGL')
        self.ergl_d =LIRE(self.data,self.lgn,'ERGL_D')
        self.haut   =LIRE(self.data,self.lgn,'HAUT')
        self.isp_asl=LIRE(self.data,self.lgn,'ISP_ASL')
        self.isp_vac=LIRE(self.data,self.lgn,'ISP_VAC')
        self.klv    =LIRE(self.data,self.lgn,'KLV')
        self.mltpl  =LIRE(self.data,self.lgn,'MLTPL')
        self.mol    =LIRE(self.data,self.lgn,'MOL')
        self.mss    =LIRE(self.data,self.lgn,'MSS')
        self.oxdzr  =LIRE(self.data,self.lgn,'OXDZR')
        self.oxdzr_d=LIRE(self.data,self.lgn,'OXDZR_D')
        self.PRSSN    =LIRE(self.data,self.lgn,'PRSSN')
        self.PSSR_ASL=LIRE(self.data,self.lgn,'PSSR_ASL')
        self.PSSR_VAC=LIRE(self.data,self.lgn,'PSSR_VAC')
        self.DMTR    =LIRE(self.data,self.lgn,'DMTR')