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
pods = [800,600,1,'mk1']

rayon = 1 #m
temperature = 2 #K
masse_moyen_mol = 3 #kg.mol-1
pression_pa_0 = 4 #  kg⋅m −1⋅s −2
planet = [5.2915158e+22, 6e+5, 288.15, 0.0289644, 101325, 'kerbin']

d_ergol = 1 #u.s-1
d_oxidizer = 2 #u.s-1
pousse_atm = 3 #kg.m.s-2
pousse_vac = 4 #kg.m.s-2
isp_atm = 5 #s
isp_vac = 6 #s
reacteurs = [[ 130,0.574,0.701, 16560, 20000,265,320, 240,0,'48-7S'],
             [ 500,1.596,1.951, 14780, 60000, 85,345, 390,1,'lv-909'],
             [1500,6.166,7.536,167969,215000,250,320,1200,1,'lv-t45'],
             [1250,7.105,8.684,205161,240000,265,310,1100,1,'lv-t30']]

d_solid = 1
solid = 2
propulseurs = [[450  ,15.821,140,162909,192000,140,165,116,1,'rt-05'],
               [752.5,15.827,375,197897,227000,170,195,175,1,'rt-10']]

engeins = [reacteurs,propulseurs]

ergol = 1 #u.s-1
oxidizer = 2 #u.s-1
multipl = -4
tanks = [[25  ,18,22,0,52    ,0,'oscar-b'],
         [62.5,45,55,8,54.125,1,'fl']]

stack = [[10,215,0,'ts-06'],
         [40,275,1,'ts-12']]

radial = [[25,600,0,'tt-38']]

coupling = [stack,radial]

import math

def PA_ATM(nombre):         return nombre / 101325
def ergol_u_kg(nombre):     return nombre * 5
def oxidizer_u_kg(nombre):  return nombre * 5
def solid_u_kg(nombre):     return nombre * 2810 / 375
def ergol_u_c(nombre):      return nombre * 36 / 45
def oxidizer_u_c(nombre):   return nombre * 10 / 55
def solid_u_c(nombre):      return nombre * 225 / 375
def cout_multipl(nombre,reserv):
    return nombre * tanks[reserv][cout] + tanks[reserv][cout] * (tanks[reserv][multipl] + 1 - nombre) / tanks[reserv][multipl] - 4.25

"La vitesse nécessaire pour échapper au puits de gravité d'une planète donnée"
def escap(): #m.s-1
    return math.sqrt(2 * G * planet[masse] / planet[rayon])
print("Dv de liberation=",escap())

def GRAVIT(altitud): #m.s-2
    return G * planet[masse] / (planet[rayon] + altitud)**2

"la hauteur d'échelle est l'augmentation d'altitude pour laquelle la pression atmosphérique diminue d'un facteur e "
def HE(altitud):
    return R * planet[temperature] / planet[masse_moyen_mol] / GRAVIT(altitud)
def PRESSION(altitud): #pa
    return planet[pression_pa_0] * math.exp(-altitud / HE(altitud))

"L'impulsion spécifique définit l'efficacité d'un moteur."
def ISP(typ,moteur,altitud): #s
    return engeins[typ][moteur][isp_vac] + PA_ATM(PRESSION(altitud)) * (engeins[typ][moteur][isp_atm] - engeins[typ][moteur][isp_vac])

"la poussée est la force exercée par l'accélération de gaz"
def POUSSE(typ,moteur,altitud,nombre=1):
    if typ == 1:
        return ISP(typ,moteur,altitud) * GRAVIT(0) * solid_u_kg(engeins[typ][moteur][d_solid]) * nombre
    return ISP(typ,moteur,altitud) * GRAVIT(0) *(ergol_u_kg(engeins[typ][moteur][d_ergol]) + oxidizer_u_kg(engeins[typ][moteur][d_oxidizer]))

"Le rapport poussée sur poids est un rapport qui définit la puissance des moteurs d'un engin par rapport à son propre poids."
def RPP(kg,typ,moteur,altitud,nombre=1): #>1
    return POUSSE(typ,moteur,altitud,nombre) / kg / GRAVIT(altitud)
def a_GRAVIT(kg,typ,moteur,altitud,nombre=1):
    return GRAVIT(altitud) * (RPP(kg,typ,moteur,altitud,nombre) - 1)

"Changement de vitesse d'un vaisseau spatial mesuré en mètres par seconde (m/s)."
def D_v(kg_vid,kg_fuel,typ,moteur,altitud):
    return ISP(typ,moteur,altitud) * GRAVIT(0) * math.log( (kg_vid + kg_fuel)/ kg_vid)


## teste
import matplotlib.pyplot as plt
import numpy as np
typ = 0
moteur = 1
altitud = 70000
kg_rpp_max = POUSSE(typ,moteur,altitud) / GRAVIT(altitud)
print("poid limite de poussé du reacteur",moteur,"=",kg_rpp_max)
kg_agravit_max = POUSSE(typ,moteur,altitud) / GRAVIT(altitud) / (1/GRAVIT(altitud) +1)
print("poid limite de accélération du reacteur",moteur,"=",kg_agravit_max)
kg_max = min(kg_rpp_max,kg_agravit_max)
kg_charg   = pods[masse] + coupling[typ][1][masse]
cout_charg = pods[cout]  + coupling[typ][1][cout]
print("poid à charge =",kg_charg)
if kg_max > kg_charg :
    if typ == 1:
        b = range(int((kg_max-kg_charg)
                      /(engeins[typ][moteur][masse]+solid_u_kg(engeins[typ][moteur][solid]))))
        kg = [kg_charg
              +a*(engeins[typ][moteur][masse]+solid_u_kg(engeins[typ][moteur][solid])) for a in b]
        kg_fuel = [a*solid_u_kg(engeins[typ][moteur][solid]) for a in b]
        nombre = [a for a in b]
        cout_fuse  = [cout_charg
                      +a*(engeins[typ][moteur][cout]+solid_u_c(tanks[1][solid])) for a in b]
    else:
        b = range(int((kg_max-kg_charg-engeins[typ][moteur][masse])
                /(tanks[1][masse]+ergol_u_kg(tanks[1][ergol])+oxidizer_u_kg(tanks[1][oxidizer]))))
        kg = [kg_charg+engeins[typ][moteur][masse]+
              a*(tanks[1][masse]+ergol_u_kg(tanks[1][ergol])+oxidizer_u_kg(tanks[1][oxidizer])) for a in b]
        kg[0] -= engeins[typ][moteur][masse]
        kg_fuel = [a * (ergol_u_kg(tanks[1][ergol]) + oxidizer_u_kg(tanks[1][oxidizer])) for a in b]
        nombre = [1 for a in b]
        cout_fuse  = [cout_charg+engeins[typ][moteur][cout]
                      +a*(tanks[1][cout] + ergol_u_c(tanks[1][ergol]) + oxidizer_u_c(tanks[1][oxidizer])) for a in b]

    kg_vid  = [kg[a] - kg_fuel[a] for a in b]       
    rpp     = [RPP(kg[a],typ,moteur,altitud,nombre[a]) for a in b]
    a_gravit= [a_GRAVIT(kg[a],typ,moteur,altitud,nombre[a]) for a in b]
    delta_v = [D_v(kg_vid[a],kg_fuel[a],typ,moteur,altitud) for a in b]
    rappor_dv_cout = [delta_v[a] / cout_fuse[a] for a in b]
    
    # fig, ax = plt.subplots()
    # ax.plot(kg, rpp,'bo')
    # ax.plot(kg, a_gravit)
    # plt.show()
    # fig, ax = plt.subplots()
    # ax.plot(kg_fuel, delta_v)
    # plt.show()
    # fig, ax = plt.subplots()
    # ax.plot(b, rappor_dv_cout)
    # plt.show()

moteur = 2
kg_rpp_max = POUSSE(typ,moteur,altitud) / GRAVIT(altitud)
print("poid limite de poussé du reacteur",moteur,"=",kg_rpp_max)
kg_agravit_max = POUSSE(typ,moteur,altitud) / GRAVIT(altitud) / (1/GRAVIT(altitud) +1)
print("poid limite de accélération du reacteur",moteur,"=",kg_agravit_max)
kg_max = min(kg_rpp_max,kg_agravit_max)
kg2 = [[] for c in b]
kg_fuel2 = [[] for c in b]
cout_fuse2 = [[] for c in b]
kg_vid2 = [[] for c in b]
rpp2 = [[] for c in b]
a_gravit2 = [[] for c in b]
delta_v2 = [[] for c in b]
rappor_dv_cout2 = [[] for c in b]
for c in range(len(kg)):
    kg_charg = kg[c]
    cout_charg = cout_fuse[c]
    if kg_max > kg_charg:
        print(c)
        if typ == 1:
            b = range(int((kg_max - kg_charg)
                          /(engeins[typ][moteur][masse] + solid_u_kg(engeins[typ][moteur][solid]))))
            kg2[c] = [kg_charg
                   +a*(engeins[typ][moteur][masse] + solid_u_kg(engeins[typ][moteur][solid])) for a in b]
            kg_fuel2[c] = [a*solid_u_kg(engeins[typ][moteur][solid]) for a in b]
            nombre = [a for a in b]
            cout_fuse2[c]  = [cout_charg+
                           a*(engeins[typ][moteur][cout] + solid_u_c(tanks[1][solid])) for a in b]         
        else:
            b = range(int((kg_max -kg_charg -engeins[typ][moteur][masse])
                          /(tanks[1][masse]+ergol_u_kg(tanks[1][ergol])+oxidizer_u_kg(tanks[1][oxidizer]))))
            kg2[c] = [kg_charg +engeins[typ][moteur][masse]
                   +a*(tanks[1][masse]+ergol_u_kg(tanks[1][ergol])+oxidizer_u_kg(tanks[1][oxidizer])) for a in b]
            kg2[c][0] -= engeins[typ][moteur][masse]
            kg_fuel2[c] = [a*(ergol_u_kg(tanks[1][ergol]) + oxidizer_u_kg(tanks[1][oxidizer])) for a in b]
            nombre = [1 for a in b]
            cout_fuse2[c]  = [cout_charg+engeins[typ][moteur][cout]+
                           a*(tanks[1][cout]+ergol_u_c(tanks[1][ergol])+oxidizer_u_c(tanks[1][oxidizer])) for a in b]

        kg_vid2[c]  = [kg2[c][a] - kg_fuel2[c][a] for a in b]       
        rpp2[c]     = [RPP(kg2[c][a],typ,moteur,altitud,nombre[a]) for a in b]
        a_gravit2[c]= [a_GRAVIT(kg2[c][a],typ,moteur,altitud,nombre[a]) for a in b]
        delta_v2[c] = [D_v(kg_vid2[c][a],kg_fuel2[c][a],typ,moteur,altitud) for a in b]
        rappor_dv_cout2[c] = [delta_v2[c][a] / cout_fuse2[c][a] for a in b]
