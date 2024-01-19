import pandas


def LIRE(data, ligne, colone):
    if colone in data.columns.values.tolist():
        l = data.loc[ligne, [colone]].values.tolist()
        #print(l)
        return l[0][0]
    else:
        return None


class LIRES:
    def __init__(self, datas, noms):
        url = "E:/Program/KSP/Donnees/" + datas + ".csv"
        try:
            pandas.read_csv(url)
        except FileNotFoundError:
            print("dans LIRES :", datas, "est mal ecrit")
        else:
            self.data = pandas.read_csv(url)
        self.nom = noms
        self.lgn = self.data["NOM"].isin([self.nom])
        self.est_dans = self.lgn.any()
        if not self.est_dans:
            print("dans LIRES :", self.nom, "n'est pas dans", self.data["NOM"])
        else:
            self.atm = LIRE(self.data, self.lgn, "ATM")
            self.cout = LIRE(self.data, self.lgn, "COUT")
            self.day = LIRE(self.data, self.lgn, "DAY")
            self.dmtr = LIRE(self.data, self.lgn, "DMTR")
            self.ergl = LIRE(self.data, self.lgn, "ERGL")
            self.ergl_d = LIRE(self.data, self.lgn, "ERGL_D")
            self.haut = LIRE(self.data, self.lgn, "HAUT")
            self.isp_asl = LIRE(self.data, self.lgn, "ISP_ASL")
            self.isp_vac = LIRE(self.data, self.lgn, "ISP_VAC")
            self.klvn = LIRE(self.data, self.lgn, "KLVN")
            self.mltpl = LIRE(self.data, self.lgn, "MLTPL")
            self.mol = LIRE(self.data, self.lgn, "MOL")
            self.mss = LIRE(self.data, self.lgn, "MSS")
            self.oxdzr = LIRE(self.data, self.lgn, "OXDZR")
            self.oxdzr_d = LIRE(self.data, self.lgn, "OXDZR_D")
            self.prssn = LIRE(self.data, self.lgn, "PRSSN")
            self.pssr_asl = LIRE(self.data, self.lgn, "PSSR_ASL")
            self.pssr_vac = LIRE(self.data, self.lgn, "PSSR_VAC")
            self.ryn = self.dmtr / 2
            self.type = LIRE(self.data, self.lgn, "TYPE")
