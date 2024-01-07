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
def ISP(typ,moteur,altitud): #s
    return engeins[typ][moteur][isp_vlc] + PA_ATM(PRESSION(altitud)) * (engeins[typ][moteur][isp_atm] - engeins[typ][moteur][isp_vlc])

"la poussée est la force exercée par l'accélération de gaz"
def POUSSE(typ,moteur,altitud,nombre=1):
    if typ == 1:
        return ISP(typ,moteur,altitud) * GRAVIT(0) * solid_u_kg(engeins[typ][moteur][solid_d]) * nombre
    return ISP(typ,moteur,altitud) * GRAVIT(0) *(ergol_u_kg(engeins[typ][moteur][ergol_d]) + oxidizer_u_kg(engeins[typ][moteur][oxidizer_d]))

"Le rapport poussée sur poids est un rapport qui définit la puissance des moteurs d'un engin par rapport à son propre poids."
def RPP(kg,typ,moteur,altitud,nombre=1): #>1
    return POUSSE(typ,moteur,altitud,nombre) / kg / GRAVIT(altitud)
def a_GRAVIT(kg,typ,moteur,altitud,nombre=1):
    return GRAVIT(altitud) * (RPP(kg,typ,moteur,altitud,nombre) - 1)

"Changement de vitesse d'un vaisseau spatial mesuré en mètres par seconde (m/s)."
def D_v(kg_vid,kg_fuel,typ,moteur,altitud):
    return ISP(typ,moteur,altitud) * GRAVIT(0) * math.log( (kg_vid + kg_fuel)/ kg_vid)


## teste
typ = 0
taille = 1
q = 1*tanks[taille][multipl]+1
charg_kg  = pods[masse]
charg_cout= pods[cout]


fuse0_plan    =[[0]    for i0 in range(q)]
fuse1_moteur  =[-1         for i0 in range(q)]
fuse2_kg_vid  =[charg_kg   for i0 in range(q)]
fuse3_kg_fuel =[0          for i0 in range(q)]
fuse4_kg_total=[0          for i0 in range(q)]
fuse5_cout    =[charg_cout for i0 in range(q)]

for i0 in range(q):
    nombre=0
    if i0 > 0 :
        nombre               =i0
        fuse1_moteur[i0] =1
        fuse2_kg_vid[i0]+=coupling[typ][1][masse]+engeins[typ][fuse1_moteur[i0]][masse]
        fuse5_cout[i0]  +=coupling[typ][1][cout] +engeins[typ][fuse1_moteur[i0]][cout]
    fuse1_0_plan=[i0]
    fuse2_kg_vid[i0] +=nombre*tanks[1][masse]
    fuse3_kg_fuel[i0] =fuel_kg(nombre)
    fuse4_kg_total[i0]=fuse2_kg_vid[i0]+fuse3_kg_fuel[i0]
    fuse5_cout[i0]   +=fuel_c(nombre)+nombre*tanks[1][cout]

Z = 0
if Z == 1 :
    fuse6_rpp    =[[0 for i1 in range(q)] for i0 in range(q)]
    fuse7_agravit=[[0 for i1 in range(q)] for i0 in range(q)]
    fuse8_deltav =[[0 for i1 in range(q)] for i0 in range(q)]
    for i0 in range(q):
        for i1 in range(q):
            fuse6_rpp[i0][i1]    = RPP(fuse4_kg_total[i0][i1],typ,fuse1_moteur[i0][i1],0)
            fuse7_agravit[i0][i1]= a_GRAVIT(fuse4_kg_total[i0][i1],typ,fuse1_moteur[i0][i1],0)
            fuse8_deltav[i0][i1] = D_v(fuse2_kg_vid[i0][i1],fuse3_kg_fuel[i0][i1],typ,fuse1_moteur[i0][i1],0)

    min0_dv = escap(70000)
    for i0 in range(q):
        for i1 in range(q):
            if fuse8_deltav[i0][i1] < min0_dv or fuse7_agravit[i0][i1] < 1 or fuse6_rpp[i0][i1] <1 :
                fuse5_cout[i0][i1]= 0
                fuse6_rpp[i0][i1]      = 0
                fuse7_agravit[i0][i1]  = 0
                fuse8_deltav[i0][i1]   = 0
    
    min1_plan = [0,0]
    min2_cout = 0
    for i0 in range(q):
        for i1 in range(q):
            if fuse5_cout[i0][i1] != 0:
                if min2_cout == 0:
                    min1_plan = fuse0_plan[i0][i1]
                    min2_cout = fuse5_cout[i0][i1]
                elif fuse5_cout[i0][i1] < min2_cout:
                    min1_plan = fuse0_plan[i0][i1]
                    min2_cout = fuse5_cout[i0][i1]
                elif fuse5_cout[i0][i1] == min2_cout and i0>i1:
                    min1_plan = fuse0_plan[i0][i1]
                    min2_cout = fuse5_cout[i0][i1]

# from mpl_toolkits import mplot3d
# import numpy as np
# import matplotlib.pyplot as plt
 
# fig = plt.figure()
 
# # syntax for 3-D projection
# ax = plt.axes(projection ='3d')
 
# # defining all 3 axes
# I0,I1 = np.meshgrid(range(q), range(q))
 
# # plotting
# ax.plot_surface(I0, I1, fuse5_cout)
# plt.tight_layout()
# plt.show()