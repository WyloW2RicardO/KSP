# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

G = 6.674e-11   #Constante gravitationnelle m3⋅kg−1⋅s−2
R = 8.31446261815324 #Constante de gaz kg⋅m2.s−2⋅K−1⋅mol−1

masse = 0 #kg
nom = -1
taille = -2
cout = -3
pods = [800,635,1,'mk1']

rayon = 1 #m
temperature = 2 #K
masse_moyen_mol = 3 #kg.mol-1
pression_pa_0 = 4 #  kg⋅m −1⋅s −2
asl_limit = 5
planet = [5.2915158e+22,6e+5,288.15,0.0289644,101325,70000,'kerbin']

ergol_d = 1 #u.s-1
oxidizer_d = 2 #u.s-1
pousse_asl = 3 #kg.m.s-2
pousse_vac = 4 #kg.m.s-2
isp_asl = 5 #s
isp_vac = 6 #s
reacteurs = [[  20,  0.058,  0.071,     508,    2000,  80, 315,   110, 0, 'ant'],
             [ 130,  0.574,  0.701,   16560,   20000, 265, 320,   240, 0, 'spark'],
             [ 500,  1.596,  1.951,   14780,   60000,  85, 345,   390, 1, 'terrier'],
             [1500,  6.166,  7.536,  167969,  215000, 250, 320,  1200, 1, 'reliant'],
             [1250,  7.105,  8.684,  205161,  240000, 265, 310,  1100, 1, 'swivel'],
             [1750,  6.555,  8.012,   64286,  250000,  90, 350,  1300, 2, 'poodle'],
             [3000, 18.642, 22.784,  658750,  650000, 280, 320,  5300, 2, 'skipper'],
             [6000, 40.407, 54.275, 1379032, 1500000, 285, 310, 13000, 2, 'minsail'],
             [9000, 53.985, 65.982, 1205882, 2000000, 205, 340, 25000, 3, 'rhino'],
             [0,0.0,0,0,0,0,0,0,0,'0']]

solid_d = 1
solid = 2
propulseurs = [[  450  ,  15.821,   140,  162909,  192000, 140,165, 116, 1, 'flea'],
               [  752.5,  15.827,   375,  197897,  227000, 170,195, 175, 1, 'hammeur'],
               [ 1500  ,  19.423,   820,  250000,  300000, 175    , 210, 1, 'thumper'],
               [ 4500  ,  41.407,  2600,  593854,  670000, 195    , 220, 1, 'kickback'],
               [ 9000  , 100.494,  8000, 1515217, 1700000, 205    , 230, 2, 'thoroughbred'],
               [21000  , 190.926, 16400, 2948936, 3300000, 210    , 235, 2, 'clydesdal'],
               [0,0.0,0,0,0,0,0,0,0,'0']]

engeins = [reacteurs,propulseurs]

ergol = 1 #u.s-1
oxidizer = 2 #u.s-1
multipl = -4
tanks = [[  25  ,   18,   22, 0,  52  , 0, 'oscar-b'],
         [  62.5,   45,   55, 8,  54.1, 1, 'fl'],
         [ 500  ,  360,  440, 8, 351.5, 2, 'x200'],
         [2250  , 1620, 1980, 3, 347.5, 3, 's3']]

stack = [[ 10, 150, 0,'td-06'],
         [ 40, 200, 1,'td-12'],
         [160, 300, 2,'td-25'],
         [360, 375, 3,'td-37']]

radial = [[ 25, 600, 0,'tt-38'],
          [ 50, 700, 1,'tt-70'],
          [400, 770, 2,'hdm']]

coupling = [stack,radial]

## PHYSIQUE
import math

def PA_asl(nombre):         return nombre / 101325
def ergol_u_kg(nombre):     return nombre * 5
def oxidizer_u_kg(nombre):  return nombre * 5
def solid_u_kg(nombre):     return nombre * 2810 / 375
def ergol_u_c(nombre):      return nombre * 0.8
def oxidizer_u_c(nombre):   return nombre * 0.18
def solid_u_c(nombre):      return nombre * 225 / 375
def cout_multipl(nombre,reserv):
    return nombre * tanks[reserv][cout] + tanks[reserv][cout] * (tanks[reserv][multipl] + 1 - nombre) / tanks[reserv][multipl] - 4.25

def fuel_kg(taille, nombre) : return nombre * (ergol_u_kg(tanks[taille][ergol]) + oxidizer_u_kg(tanks[taille][oxidizer]))
def fuel_c(taille, nombre)  : return nombre * (ergol_u_c (tanks[taille][ergol]) + oxidizer_u_c (tanks[taille][oxidizer]))

"La vitesse nécessaire pour échapper au puits de gravité d'une planète donnée"
def escap(altitud): #m.s-1
    return math.sqrt(2*G*planet[masse]/(planet[rayon]+altitud))

def GRAVIT(altitud): #m.s-2
    return G * planet[masse] / (planet[rayon] + altitud)**2

"la hauteur d'échelle est l'augmentation d'altitude pour laquelle la pression aslosphérique diminue d'un facteur e "
def HE(altitud):
    return R * planet[temperature] / planet[masse_moyen_mol] / GRAVIT(altitud)
def PRESSION(altitud): #pa
    if planet[asl_limit]<=altitud : return 0
    return planet[pression_pa_0] * math.exp(-altitud / HE(altitud))

"L'impulsion spécifique définit l'efficacité d'un moteur."
def ISP(typ, moteur, altitud): #s
    return engeins[typ][moteur][isp_vac] + PA_asl(PRESSION(altitud)) * (engeins[typ][moteur][isp_asl] - engeins[typ][moteur][isp_vac])

"la poussée est la force exercée par l'accélération de gaz"
def POUSSE(typ, moteur, altitud, nombre=1):
    if typ == 1:
        return ISP(typ,moteur,altitud) * GRAVIT(0) * solid_u_kg(engeins[typ][moteur][solid_d]) * nombre
    return ISP(typ,moteur,altitud) * GRAVIT(0) *(ergol_u_kg(engeins[typ][moteur][ergol_d]) + oxidizer_u_kg(engeins[typ][moteur][oxidizer_d]))

"Le rapport poussée sur poids est un rapport qui définit la puissance des moteurs d'un engin par rapport à son propre poids."
def RPP(kg, typ, moteur, altitud, nombre=1): #>1
    return POUSSE(typ,moteur,altitud,nombre) / kg / GRAVIT(altitud)
def a_GRAVIT(kg, typ,moteur, altitud, nombre=1):
    return GRAVIT(altitud) * (RPP(kg,typ,moteur,altitud,nombre) - 1)

"Changement de vitesse d'un vaisseau spatial mesuré en mètres par seconde (m/s)."
def D_v(kg_vid, kg_fuel,typ, moteur, altitud):
    return ISP(typ,moteur,altitud) * GRAVIT(0) * math.log((kg_vid + kg_fuel)/ kg_vid)

## FONCTION
import numpy

"[0, 0] -> [[0], [0]]"
def liste_matrice(liste):
    return [[liste[i]] for i in range(len(liste))]

q = 1 * 8 + 1
charg_kg   = pods[masse]
charg_cout = pods[cout]
def construc(typ, taille, moteur,
             fuse_moteur   = [-1],
             fuse_kg_vid   = [charg_kg],
             fuse_kg_fuel  = [0],
             fuse_cout     = [charg_cout]) :
    fuse_plan     = [0]
    fuse_kg_total = [fuse_kg_vid[0] + fuse_kg_fuel[0]]
    for i in range(1, q):
        fuse_plan     = numpy.append(fuse_plan    , i)
        fuse_moteur   = numpy.append(fuse_moteur  , moteur)
        fuse_kg_vid   = numpy.append(fuse_kg_vid  , fuse_kg_vid[0] + coupling[typ][taille][masse] + engeins[typ][moteur][masse] + i * tanks[taille][masse])
        fuse_cout     = numpy.append(fuse_cout    , fuse_cout[0]   + coupling[typ][taille][cout]  + engeins[typ][moteur][cout]  + i * tanks[taille][cout] + fuel_c(taille, i))
        fuse_kg_fuel  = numpy.append(fuse_kg_fuel , fuel_kg(taille, i))
        fuse_kg_total = numpy.append(fuse_kg_total, fuse_kg_vid[i] + fuse_kg_fuel[i])
    return fuse_plan, fuse_moteur, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout
typ = 0
taille = 1
moteur = 2
fuse_1d_0plan, fuse_1d_1moteur, fuse_1d_2kg_vid, fuse_1d_3kg_fuel, fuse_1d_4kg_total, fuse_1d_5cout = construc(typ, taille, moteur)
# print(fuse_1d_0plan, fuse_1d_1moteur, fuse_1d_2kg_vid, fuse_1d_3kg_fuel, fuse_1d_4kg_total, fuse_1d_5cout)

"retourne la dimention matriciel"
def dimension(matrice) :
    return len(numpy.shape(matrice))

"rajoute un etage a la fusee"
def etage_plus(typ, taille, moteur,
               fuse_plan_liste,
               fuse_moteur_liste,
               fuse_kg_vid_liste,
               fuse_kg_fuel_liste,
               fuse_kg_total_liste,
               fuse_cout_liste):
    fuse0_plan     = liste_matrice(fuse_plan_liste)
    fuse0_moteur   = liste_matrice(fuse_moteur_liste)
    fuse0_kg_vid   = liste_matrice(fuse_kg_vid_liste)
    fuse0_kg_fuel  = liste_matrice(fuse_kg_fuel_liste)
    fuse0_kg_total = liste_matrice(fuse_kg_total_liste)
    fuse0_cout     = liste_matrice(fuse_cout_liste)
    # print(fuse2_1moteur)
    Q = len(fuse0_plan)
    for i0 in range(Q):
        fuse1_plan, fuse1_moteur, fuse1_kg_vid, fuse1_kg_fuel, fuse1_kg_total, fuse1_cout = construc(typ, taille, moteur, fuse0_moteur[i0], fuse0_kg_vid[i0], fuse0_kg_fuel[i0], fuse0_cout[i0])
        # print("fuse2_1moteur","[",i1,"]", fuse2_1moteur[i1])
        # print("fuse1_plan", fuse1_plan)
        fuse0_plan[i0]     = [numpy.append(fuse0_plan[i0][0],fuse1_plan[i1]) for i1 in range(len(fuse1_plan))]
        fuse0_moteur[i0]   = fuse1_moteur
        fuse0_kg_vid[i0]   = fuse1_kg_vid
        fuse0_kg_fuel[i0]  = fuse1_kg_fuel
        fuse0_kg_total[i0] = fuse1_kg_total
        fuse0_cout[i0]     = fuse1_cout
    return fuse0_plan, fuse0_moteur, fuse0_kg_vid, fuse0_kg_fuel, fuse0_kg_total, fuse0_cout       
typ = 0
taille = 1
moteur = 3
fuse_2d_0plan, fuse_2d_1moteur, fuse_2d_2kg_vid, fuse_2d_3kg_fuel, fuse_2d_4kg_total, fuse_2d_5cout = etage_plus(typ, taille, moteur,fuse_1d_0plan, fuse_1d_1moteur, fuse_1d_2kg_vid, fuse_1d_3kg_fuel, fuse_1d_4kg_total, fuse_1d_5cout)
# print(fuse_2d_0plan, fuse_2d_1moteur, fuse_2d_2kg_vid, fuse_2d_3kg_fuel, fuse_2d_4kg_total, fuse_2d_5cout)


def matric_liste(matrice, plan, j = 0) :
    if j < len(plan) : 
        return matric_liste(matrice[plan[j]], plan, j+1)
    return matrice
# print(matric_liste([[0], [1]], [1], j = 0))

def dimension_plus(typ, taille, moteur, end_dim,
                   fuse_plan     = 0, 
                   fuse_moteur   = 0, 
                   fuse_kg_vid   = 0, 
                   fuse_kg_fuel  = 0, 
                   fuse_kg_total = 0, 
                   fuse_cout     = 0) :
    dim = dimension(fuse_moteur)
    # print(dim, end_dim, moteur)
    if dim == 0 :
        fuse_plan, fuse_moteur, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout = construc(typ, taille, moteur)
        dim = dimension(fuse_moteur)
    if dim == 1 and end_dim > 2 :
        fuse_plan, fuse_moteur, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout = dimension_plus(typ, taille, moteur, end_dim - 1, fuse_plan, fuse_moteur, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout)
        dim = dimension(fuse_moteur)
        moteur += 1
    if dim > 1 and end_dim > 2 :
        Q = range(len(fuse_moteur))
        for i in Q :
            fuse_plan[i], fuse_moteur[i], fuse_kg_vid[i], fuse_kg_fuel[i], fuse_kg_total[i], fuse_cout[i] = dimension_plus(typ, taille, moteur, end_dim - 1, fuse_plan[i], fuse_moteur[i], fuse_kg_vid[i], fuse_kg_fuel[i], fuse_kg_total[i], fuse_cout[i])
        dim = dimension(fuse_moteur)
        moteur += 1
    if dim == 1 and end_dim == 2 :
        moteur += 1
        fuse_plan, fuse_moteur, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout = etage_plus(typ, taille, moteur, fuse_plan, fuse_moteur, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout)
        dim = dimension(fuse_moteur)
    # print(dim, end_dim, moteur)
    return fuse_plan, fuse_moteur, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout
typ = 0
taille = 1
end_dim = 1
moteur = 4 + 1 - end_dim
dim = 1
fuse0_0plan, fuse0_1moteur, fuse0_2kg_vid, fuse0_3kg_fuel, fuse0_4kg_total, fuse0_5cout = dimension_plus(typ, taille, moteur, end_dim)

## TESTES
def dimension_matrice(dim, long, matrice = 0) :
    while dim != dimension(matrice) :
        matrice = [matrice for i in range(long)]
    return matrice

def dimension_decol(fuse_kg_total, typ, fuse_moteur, 
                    fuse_rpp = 0, 
                    fuse_agravit = 0) :
    dim0 = dimension(fuse_rpp)
    dim1 = dimension(fuse_moteur)
    # print(dim0,dim1)
    # print(fuse_rpp)
    # print("fuse_moteur",fuse_moteur)
    if dim0 == 0 and dim1 == 1 :
        # print(fuse_moteur)
        fuse_rpp     = [RPP     (fuse_kg_total[i], typ, int(fuse_moteur[i]), 0) for i in range(len(fuse_moteur))]
        fuse_agravit = [a_GRAVIT(fuse_kg_total[i], typ, int(fuse_moteur[i]), 0) for i in range(len(fuse_moteur))]
        # print(fuse_rpp)
        dim0 = dimension(fuse_rpp)
    if dim0 == 0 and dim1 > 1 :
        for i in range(len(fuse_moteur)) :
            fuse_rpp, fuse_agravit = dimension_decol(fuse_kg_total[i], typ, fuse_moteur[i], fuse_rpp, fuse_agravit)
        dim0 = dimension(fuse_rpp)
    if dim0 > 0 and dim1 > 1 :
        # print(dim0,dim1)
        for i in range(len(fuse_rpp)) :
            fuse_rpp[i], fuse_agravit[i] = dimension_decol(fuse_kg_total[i], typ, fuse_moteur[i], fuse_rpp[i], fuse_agravit[i])
        dim0 = dimension(fuse_rpp)
    return fuse_rpp, fuse_agravit

def dimension_min(fuse0_cout, fuse0_6rpp, fuse0_7agravit,
                  fuse1_cout = 0) :
  dim0 = dimension(fuse0_cout)
  dim1 = dimension(fuse1_cout)
  # print(dim0,dim1)
  # print(fuse_rpp)
  # print("fuse_moteur",fuse_moteur)
  if dim1 == 0 and dim0 == 1 :
      # print(fuse_moteur)
      fuse1_cout = [fuse0_cout[i] * (fuse0_6rpp[i] > 1) * (fuse0_7agravit[i] > 1) for i in range(len(fuse0_cout))]
      # print(fuse_rpp)
      dim1 = dimension(fuse1_cout)
  if dim1 == 0 and dim0 > 1 :
      for i in range(len(fuse0_cout)) :
          fuse1_cout = dimension_min(fuse0_cout[i], fuse0_6rpp[i], fuse0_7agravit[i], fuse1_cout)
      dim1 = dimension(fuse1_cout)
  if dim1 > 0 and dim0 > 1 :
      # print(dim0,dim1)
      for i in range(len(fuse0_cout)) :
          fuse1_cout[i] = dimension_min(fuse0_cout[i], fuse0_6rpp[i], fuse0_7agravit[i], fuse1_cout[i])
      dim1 = dimension(fuse1_cout)    
  return fuse1_cout

Z = 2
if Z > 0 :
    fuse0_6rpp, fuse0_7agravit = dimension_decol(fuse0_4kg_total, typ, fuse0_1moteur)
    if Z > 1 :
        fuse1_5cout = dimension_min(fuse0_5cout, fuse0_6rpp, fuse0_7agravit)
        # min_dv = escap(70000)
        # for i0 in range(q):
        #     for i1 in range(q):
        #         if  fuse0_7agravit[i0][i1] < 0 or fuse0_6rpp[i0][i1] <1 :
        #             fuse0_5cout[i0][i1] = 0
        
        # min1_plan = [0,0]
        # min2_cout = 0
        # for i0 in range(q):
        #     for i1 in range(q):
        #         if fuse0_5cout[i0][i1] != 0:
        #             if min2_cout == 0:
        #                 min1_plan = fuse0_0plan[i0][i1]
        #                 min2_cout = fuse0_5cout[i0][i1]
        #             elif fuse0_5cout[i0][i1] < min2_cout:
        #                 min1_plan = fuse0_0plan[i0][i1]
        #                 min2_cout = fuse0_5cout[i0][i1]
        #             elif fuse0_5cout[i0][i1] == min2_cout and i0>i1:
        #                 min1_plan = fuse0_0plan[i0][i1]
        #                 min2_cout = fuse0_5cout[i0][i1]