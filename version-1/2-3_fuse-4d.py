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
atmos_limit = 5
planet = [5.2915158e+22,6e+5,288.15,0.0289644,101325,70000,'kerbin']

ergol_d = 1 #u.s-1
oxidizer_d = 2 #u.s-1
pousse_atm = 3 #kg.m.s-2
pousse_vlc = 4 #kg.m.s-2
isp_atm = 5 #s
isp_vlc = 6 #s
reacteurs = [[ 130,0.574,0.701, 16560, 20000,265,320, 240,0,'48-7S'],
             [ 500,1.596,1.951, 14780, 60000, 85,345, 390,1,'lv-909'],
             [1500,6.166,7.536,167969,215000,250,320,1200,1,'lv-t45'],
             [1250,7.105,8.684,205161,240000,265,310,1100,1,'lv-t30'],
             [0,0.0,0,0,0,0,0,0,0,'0']]

solid_d = 1
solid = 2
propulseurs = [[450  ,15.821,140,162909,192000,140,165,116,1,'rt-05'],
               [752.5,15.827,375,197897,227000,170,195,175,1,'rt-10'],
               [0,0.0,0,0,0,0,0,0,0,'0']]

engeins = [reacteurs,propulseurs]

ergol = 1 #u.s-1
oxidizer = 2 #u.s-1
multipl = -4
tanks = [[25  ,18,22,0,52  ,0,'oscar-b'],
         [62.5,45,55,8,54.1,1,'fl']]

stack = [[10,215,0,'ts-06'],
         [40,275,1,'ts-12']]

radial = [[25,600,0,'tt-38']]

coupling = [stack,radial]

## PHYSIQUE
import math

def PA_ATM(nombre):         return nombre / 101325
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

"la hauteur d'échelle est l'augmentation d'altitude pour laquelle la pression atmosphérique diminue d'un facteur e "
def HE(altitud):
    return R * planet[temperature] / planet[masse_moyen_mol] / GRAVIT(altitud)
def PRESSION(altitud): #pa
    if planet[atmos_limit]<=altitud : return 0
    return planet[pression_pa_0] * math.exp(-altitud / HE(altitud))

"L'impulsion spécifique définit l'efficacité d'un moteur."
def ISP(typ, moteur, altitud): #s
    return engeins[typ][moteur][isp_vlc] + PA_ATM(PRESSION(altitud)) * (engeins[typ][moteur][isp_atm] - engeins[typ][moteur][isp_vlc])

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
    return [[liste[i0]] for i0 in range(len(liste))]

typ = 0
taille = 1
q = 1*tanks[taille][multipl]+1
charg_kg  = pods[masse]
charg_cout= pods[cout]
def construc(moteur,
             fuse_moteur   = [-1],
             fuse_kg_vid   = [charg_kg],
             fuse_kg_fuel  = [0],
             fuse_kg_total = [0],
             fuse_cout     = [charg_cout]) :
    fuse_plan = [0]
    for i in range(1, q):
        fuse_plan     = numpy.append(fuse_plan    , i)
        fuse_moteur   = numpy.append(fuse_moteur  , moteur)
        fuse_kg_vid   = numpy.append(fuse_kg_vid  , fuse_kg_vid[0] + coupling[typ][taille][masse] + engeins[typ][moteur][masse] + i * tanks[taille][masse])
        fuse_cout     = numpy.append(fuse_cout    , fuse_cout[0]   + coupling[typ][taille][cout]  + engeins[typ][moteur][cout]  + i * tanks[taille][cout] + fuel_c(taille, i))
        fuse_kg_fuel  = numpy.append(fuse_kg_fuel , fuel_kg(taille, i))
        fuse_kg_total = numpy.append(fuse_kg_total, fuse_kg_vid[i] + fuse_kg_fuel[i])
    return fuse_plan, fuse_moteur, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout
# print(construc(1))

"retourne la dimention matriciel"
def dimension(matrice) :
    return len(numpy.shape(matrice))

"rajoute un etage a la fusee"
def dimension_plus(moteur,
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
        fuse1_plan, fuse1_moteur, fuse1_kg_vid, fuse1_kg_fuel, fuse1_kg_total, fuse1_cout = construc(moteur, fuse0_moteur[i0], fuse0_kg_vid[i0], fuse0_kg_fuel[i0], fuse0_kg_total[i0], fuse0_cout[i0])
        # print("fuse2_1moteur","[",i1,"]", fuse2_1moteur[i1])
        # print("fuse1_plan", fuse1_plan)
        fuse0_plan[i0]     = [numpy.append(fuse0_plan[i0][0],fuse1_plan[i1]) for i1 in range(len(fuse1_plan))]
        fuse0_moteur[i0]   = fuse1_moteur
        fuse0_kg_vid[i0]   = fuse1_kg_vid
        fuse0_kg_fuel[i0]  = fuse1_kg_fuel
        fuse0_kg_total[i0] = fuse1_kg_total
        fuse0_cout[i0]     = fuse1_cout
    return fuse0_plan, fuse0_moteur, fuse0_kg_vid, fuse0_kg_fuel, fuse0_kg_total, fuse0_cout
# print(dimension_plus(2,
#                       [   0 ,    1  ,    2  ,    3  ,    4  ,    5  ,    6  ,    7  ,    8],
#                       [  -1 ,    1  ,    1  ,    1  ,    1  ,    1  ,    1  ,    1  ,    1],
#                       [ 800., 1402.5, 1465. , 1527.5, 1590. , 1652.5, 1715. , 1777.5, 1840. ],
#                       [   0 ,  500  , 1000  , 1500  , 2000  , 2500  , 3000  , 3500  , 4000],
#                       [   0., 1902.5, 2465. , 3027.5, 3590. , 4152.5, 4715. , 5277.5, 5840. ],
#                       [ 635., 1400. , 1500. , 1600. , 1700. , 1800. , 1900. , 2000. , 2100.]))


def matric_liste(matrice, plan, j = 0) :
    if j < len(plan) : 
        return matric_liste(matrice[plan[j]], plan, j+1)
    return matrice
# print(matric_liste([[0], [1]], [1], j = 0))


## TESTES

moteur = 0
fuse0_0plan, fuse0_1moteur, fuse0_2kg_vid, fuse0_3kg_fuel, fuse0_4kg_total, fuse0_5cout = construc(moteur)
# print("fuse0_0plan", numpy.array(fuse0_0plan))

moteur = 1
fuse0_0plan, fuse0_1moteur, fuse0_2kg_vid, fuse0_3kg_fuel, fuse0_4kg_total, fuse0_5cout = dimension_plus(moteur, fuse0_0plan, fuse0_1moteur, fuse0_2kg_vid, fuse0_3kg_fuel, fuse0_4kg_total, fuse0_5cout)
# print("fuse0_0plan", numpy.array(fuse0_0plan))

moteur = 2
Q0 = len(fuse0_0plan)
for i0 in range(Q0):
    # print("fuse0_0plan", "[", i0, "]", numpy.array(fuse0_0plan[i0]))
    fuse0_0plan[i0], fuse0_1moteur[i0], fuse0_2kg_vid[i0], fuse0_3kg_fuel[i0], fuse0_4kg_total[i0], fuse0_5cout[i0] = dimension_plus(moteur, fuse0_0plan[i0], fuse0_1moteur[i0], fuse0_2kg_vid[i0], fuse0_3kg_fuel[i0], fuse0_4kg_total[i0], fuse0_5cout[i0])
    # print("fuse0_0plan", "[", i0, "]", numpy.array(fuse0_0plan[i0]))

moteur = 3
Q1 = len(fuse0_0plan)
for i0 in range(Q0) :
    fuse1_0plan     = fuse0_0plan[i0]
    fuse1_1moteur   = fuse0_1moteur[i0]
    fuse1_2kg_vid   = fuse0_2kg_vid[i0]
    fuse1_3kg_fuel  = fuse0_3kg_fuel[i0]
    fuse1_4kg_total = fuse0_4kg_total[i0]
    fuse1_5cout     = fuse0_5cout[i0]
    for i1 in range(Q1) :
        fuse1_0plan[i1], fuse1_1moteur[i1], fuse1_2kg_vid[i1], fuse1_3kg_fuel[i1], fuse1_4kg_total[i1], fuse1_5cout[i1] = dimension_plus(moteur, fuse1_0plan[i1], fuse1_1moteur[i1], fuse1_2kg_vid[i1], fuse1_3kg_fuel[i1], fuse1_4kg_total[i1], fuse1_5cout[i1])
    fuse0_0plan[i0]     = fuse1_0plan
    fuse0_1moteur[i0]   = fuse1_1moteur
    fuse0_2kg_vid[i0]   = fuse1_2kg_vid
    fuse0_3kg_fuel[i0]  = fuse1_3kg_fuel
    fuse0_4kg_total[i0] = fuse1_4kg_total
    fuse0_5cout[i0]     = fuse1_5cout

Z = 0
if Z > 0 :
    fuse6_rpp     = []
    fuse7_agravit = []
    fuse8_deltav =[]
    for i0 in range(q):
        fuse6_rpp     = numpy.append(fuse6_rpp    ,RPP(     fuse4_kg_total[i0],typ,int(fuse1_moteur[i0]),0))
        fuse7_agravit = numpy.append(fuse7_agravit,a_GRAVIT(fuse4_kg_total[i0],typ,int(fuse1_moteur[i0]),0))
        fuse8_deltav = numpy.append(fuse8_deltav, D_v(fuse2_kg_vid[i0],fuse3_kg_fuel[i0],typ,int(fuse1_moteur[i0]),0))

    min0_dv = escap(70000)
    for i0 in range(q):
        if fuse6_rpp[i0] <1 or fuse7_agravit[i0] < 1 or fuse8_deltav[i0] < min0_dv:
            fuse5_cout[i0] = 0

    min1_plan = []
    min2_cout = 0
    for i0 in range(q):
        if fuse5_cout[i0] != 0:
            if min2_cout == 0:
                min1_plan = fuse0_plan[i0]
                min2_cout = fuse5_cout[i0]
            elif fuse5_cout[i0] < min2_cout:
                min1_plan = fuse0_plan[i0]
                min2_cout = fuse5_cout[i0]
            elif fuse5_cout[i0] == min2_cout :
                min1_plan = fuse0_plan[i0]
                min2_cout = fuse5_cout[i0]