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

def fuel_kg(nombre):return nombre*(ergol_u_kg(tanks[1][ergol])+oxidizer_u_kg(tanks[1][oxidizer]))
def fuel_c(nombre) :return nombre*(ergol_u_c(tanks[1][ergol]) +oxidizer_u_c(tanks[1][oxidizer]))

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

def liste2liste(liste):
    return [[liste[i0]] for i0 in range(len(liste))]

charg_kg  = pods[masse]
charg_cout= pods[cout]
def construc(moteur,
             fuse0_plan     = [0],
             fuse1_moteur   = [-1],
             fuse2_kg_vid   = [charg_kg],
             fuse3_kg_fuel  = [0],
             fuse4_kg_total = [0],
             fuse5_cout     = [charg_cout]):
    for i0 in range(1, q):
        fuse0_plan     = numpy.append(fuse0_plan    , i0)
        fuse1_moteur   = numpy.append(fuse1_moteur  , moteur)
        fuse2_kg_vid   = numpy.append(fuse2_kg_vid  , fuse2_kg_vid[0] + coupling[typ][1][masse] + engeins[typ][moteur][masse] + i0 * tanks[1][masse])
        fuse5_cout     = numpy.append(fuse5_cout    , fuse5_cout[0]   + coupling[typ][1][cout]  + engeins[typ][moteur][cout]  + i0 * tanks[1][cout] + fuel_c(i0))
        fuse3_kg_fuel  = numpy.append(fuse3_kg_fuel , fuel_kg(i0))
        fuse4_kg_total = numpy.append(fuse4_kg_total, fuse2_kg_vid[i0] + fuse3_kg_fuel[i0])
    return fuse0_plan, fuse1_moteur, fuse2_kg_vid, fuse3_kg_fuel, fuse4_kg_total, fuse5_cout

## TESTES
typ = 0
taille = 1
q = 1*tanks[taille][multipl]+1

moteur = 1
fuse0_0_plan, fuse0_1_moteur, fuse0_2_kg_vid, fuse0_3_kg_fuel, fuse0_4_kg_total, fuse0_5_cout = construc(moteur)
fuse0_0_plan     = liste2liste(fuse0_0_plan)
fuse0_1_moteur   = liste2liste(fuse0_1_moteur)
fuse0_2_kg_vid   = liste2liste(fuse0_2_kg_vid)
fuse0_3_kg_fuel  = liste2liste(fuse0_3_kg_fuel)
fuse0_4_kg_total = liste2liste(fuse0_4_kg_total)
fuse0_5_cout     = liste2liste(fuse0_5_cout)
# print(fuse0_5_cout)

moteur = 3
Q = len(fuse0_0_plan)
for i0 in range(Q):
    fuse1_0_plan, fuse1_1_moteur, fuse1_2_kg_vid, fuse1_3_kg_fuel, fuse1_4_kg_total, fuse1_5_cout = construc(moteur, fuse0_0_plan[i0], fuse0_1_moteur[i0], fuse0_2_kg_vid[i0], fuse0_3_kg_fuel[i0], fuse0_4_kg_total[i0], fuse0_5_cout[i0])
    print(fuse0_5_cout[i0], fuse1_5_cout)
    fuse0_0_plan[i0]     =  [numpy.append(fuse0_0_plan[i0][0], fuse1_0_plan[i1]) for i1 in range(len(fuse1_0_plan))]
    fuse0_1_moteur[i0]   = fuse1_1_moteur
    fuse0_2_kg_vid[i0]   = fuse1_2_kg_vid
    fuse0_3_kg_fuel[i0]  = fuse1_3_kg_fuel
    fuse0_4_kg_total[i0] = fuse1_4_kg_total
    fuse0_5_cout[i0]     = fuse1_5_cout