# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## COSTANTE
G = 6.674e-11   #Constante gravitationnelle m3⋅kg−1⋅s−2
R = 8.31446261815324 #Constante de gaz kg⋅m2.s−2⋅K−1⋅mol−1
base = 71

masse = 0 #kg
nom = -1
taille = -2 #m
haut = -3 #m
cout = -4
pods = [800, 635, 1.1, 1.3, 'mk1']

rayon = 1 # m
day = 2 # s
temperature = 3 # K
masse_moyen_mol = 4 # kg.mol-1
pression_pa_0 = 5 # kg⋅m −1⋅s −2
asl_limit = 6 # m
planet = [5.2915158e22, 6e+5, 21600, 288.15, 0.0289644, 101325, 70000,'kerbin']

ergol_d = 1 #u.s-1
oxidizer_d = 2 #u.s-1
pousse_asl = 3 #kg.m.s-2
pousse_vac = 4 #kg.m.s-2
isp_asl = 5 #s
isp_vac = 6 #s
reacteurs = [[  20,  0.058,  0.071,     508,    2000,  80, 315,   110, 0.3, 0.6, 'ant'],
             [ 130,  0.574,  0.701,   16560,   20000, 265, 320,   240, 0.4, 0.6, 'spark'],
             [ 500,  1.596,  1.951,   14780,   60000,  85, 345,   390, 0.8, 1.3, 'terrier'],
             [1500,  6.166,  7.536,  167969,  215000, 250, 320,  1200, 1.7, 1.3, 'reliant'],
             [1250,  7.105,  8.684,  205161,  240000, 265, 310,  1100, 1.7, 1.3, 'swivel'],
             [1750,  6.555,  8.012,   64286,  250000,  90, 350,  1300, 2.7, 2.5, 'poodle'],
             [3000, 18.642, 22.784,  658750,  650000, 280, 320,  5300, 2.4, 2.5, 'skipper'],
             [6000, 40.407, 54.275, 1379032, 1500000, 285, 310, 13000, 3  , 2.5, 'minsail'],
             [9000, 53.985, 65.982, 1205882, 2000000, 205, 340, 25000, 4.1, 3.8, 'rhino'],
             [0,0.0,0,0,0,0,0,0,0,'0']]

solid_d = 1
solid = 2
propulseurs = [[   75  ,   0.809,    40,   11012,   12500, 185, 210,    75,  1.8, 0.6, 'mite'],
               [  150  ,   1.897,    90,   26512,   30000, 190, 215,   150,  4  , 0.6, 'shrimp'],
               [  450  ,  15.821,   140,  162909,  192000, 140, 165,   200,  1.8, 1.3, 'flea'],
               [  752.5,  15.827,   375,  197897,  227000, 170, 195,   400,  2.9, 1.3, 'hammeur'],
               [ 1500  ,  19.423,   820,  250000,  300000, 175, 210,   850,  7.9, 1.3, 'thumper'],
               [ 4500  ,  41.407,  2600,  593854,  670000, 195, 220,  2700, 14.9, 1.3, 'kickback'],
               [ 9000  , 100.494,  8000, 1515217, 1700000, 205, 230,  9000, 12.3, 2.5, 'thoroughbred'],
               [21000  , 190.926, 16400, 2948936, 3300000, 210, 235, 18500, 22.3, 2.5, 'clydesdal'],
               [0,0.0,0,0,0,0,0,0,0,'0']]

engeins = [reacteurs,propulseurs]

ergol = 1 #u.s-1
oxidizer = 2 #u.s-1
multipl = -4
tanks = [[  25  ,   18,   22, 0,  52  , 0.625, 0.6, 'oscar-b'],
         [  62.5,   45,   55, 8,  54.1, 0.5  , 1.3, 'fl'],
         [ 500  ,  360,  440, 8, 351.5, 1    , 2.5, 'x200'],
         [2250  , 1620, 1980, 3, 347.5, 2.665, 3.8, 's3']]

stack = [[ 10, 150, 0.625, 0.6,'td-06'],
         [ 40, 200, 0    , 1.3,'td-12'],
         [160, 300, 1    , 2.5,'td-25'],
         [360, 375, 1    , 3.8,'td-37']]

radial = [[ 25, 600, 0, 0,'tt-38'],
          [ 50, 700, 0, 0,'tt-70'],
          [400, 770, 0, 0,'hdm']]

coupling = [stack,radial]

## VARIABLE
deb_haut   = pods[haut] + base
deb_kg     = pods[masse]
deb_cout   = pods[cout]
deb_moteur = 2
q = 2 * 8 + 1
typ = 0
taille = 1
end_dim = 3
dim = 1
but = 70000

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
def fuel_kg_d(typ, moteur, nombre = 1)  : return nombre * ergol_u_kg(engeins[typ][moteur][ergol_d]) + oxidizer_u_kg(engeins[typ][moteur][oxidizer_d])

def fuel_temp(typ, moteur, kg_fuel) : return kg_fuel / fuel_kg_d(typ, moteur)

def vites_surface() : return planet[rayon] / planet[day]

"La vitesse nécessaire pour échapper au puits de gravité d'une planète donnée"
def escap(altitud): #m.s-1
    return math.sqrt(2*G*planet[masse]/(planet[rayon]+altitud))

def GRAVIT(altitud): #m.s-2
    return G * planet[masse] / (planet[rayon] + altitud)**2

"la hauteur d'échelle est l'augmentation d'altitude pour laquelle la pression aslosphérique diminue d'un facteur e "
# def TEMP(altitud):
#     z_base_terre = [0,11000,20000,32000,47000,51000,71000,84852]
#     z_base_kerbin = z_base_terre * 70 /105
def HE():
    return R * planet[temperature] / planet[masse_moyen_mol] / GRAVIT(0)
def PRESSION(altitud): #pa
    # return planet[pression_pa_0] * math.exp(-altitud / HE()) # if planet[asl_limit] <= altitud : return 0
    return planet[pression_pa_0] * (1 - altitud * 279.65 / 1000 / planet[temperature])**(5.255) # imajinair
    # z = [0, 2500, 5000, 7500, 10000, 15000, 20000, 25000, 30000, 40000, 50000, 60000, 70000]
    # p = 101
    
def DENSIT(altitud, temp) :
    return PRESSION(altitud) / R / temp

"L'impulsion spécifique définit l'efficacité d'un moteur."
def ISP(altitud, typ, moteur): #s
    return engeins[typ][moteur][isp_vac] + PA_asl(PRESSION(altitud)) * (engeins[typ][moteur][isp_asl] - engeins[typ][moteur][isp_vac])

"la poussée est la force exercée par l'accélération de gaz"
def POUSSE(altitud, typ, moteur, nombre = 1):
    return ISP(altitud, typ, moteur) * GRAVIT(0) * fuel_kg_d(typ, moteur)

"Le rapport poussée sur poids est un rapport qui définit la puissance des moteurs d'un engin par rapport à son propre poids."
def RPP(altitud, typ, moteur, kg, nombre=1): #>1
    return POUSSE(altitud, typ, moteur, nombre) / (kg * GRAVIT(altitud))
def a_GRAVIT(altitud, typ, moteur, kg, nombre=1):
    return GRAVIT(altitud) * (RPP(altitud, typ, moteur, kg, nombre) - 1)

"Changement de vitesse d'un vaisseau spatial mesuré en mètres par seconde (m/s)."
def D_v(altitud, typ, moteur, kg_vid, kg_total):
    return ISP(altitud, typ, moteur) * GRAVIT(0) * math.log(kg_total / kg_vid)

## STRUCTURE
"[0, 0] -> [[0], [0]]"
def liste_matrice(liste):
    return [[liste[i]] for i in range(len(liste))]

"retourne la dimention matriciel"
def dimension(matrice) : return len(numpy.shape(matrice))

def matric_nombre(matrice, plan, j = 0) :
    if j < len(plan) : 
        return matric_nombre(matrice[plan[j]], plan, j + 1)
    return matrice

import matplotlib.pyplot
def trac(nom, X, x_nom, Y, y_nom) :
    matplotlib.pyplot.plot(X, Y)
    matplotlib.pyplot.title(nom)
    matplotlib.pyplot.xlabel(x_nom)
    matplotlib.pyplot.ylabel(y_nom)
    matplotlib.pyplot.show()

## FONCTION
import numpy

def construc(typ, taille, moteur,
             fuse_moteur   = [-1],
             fuse_haut     = [deb_haut],
             fuse_kg_vid   = [deb_kg],
             fuse_kg_fuel  = [0],
             fuse_cout     = [deb_cout]) :
    fuse_plan     = [0]
    fuse_kg_total = [fuse_kg_vid[0] + fuse_kg_fuel[0]]
    for i in range(1, q):
        fuse_plan     = numpy.append(fuse_plan    , i)
        fuse_moteur   = numpy.append(fuse_moteur  , moteur)
        fuse_haut     = numpy.append(fuse_haut    , fuse_haut[0]   + coupling[typ][taille][haut]  + engeins[typ][moteur][haut]  + i * tanks[taille][haut])
        fuse_kg_vid   = numpy.append(fuse_kg_vid  , fuse_kg_vid[0] + coupling[typ][taille][masse] + engeins[typ][moteur][masse] + i * tanks[taille][masse])
        fuse_cout     = numpy.append(fuse_cout    , fuse_cout[0]   + coupling[typ][taille][cout]  + engeins[typ][moteur][cout]  + i * tanks[taille][cout] + fuel_c(taille, i))
        fuse_kg_fuel  = numpy.append(fuse_kg_fuel , fuel_kg(taille, i))
        fuse_kg_total = numpy.append(fuse_kg_total, fuse_kg_vid[i] + fuse_kg_fuel[i])
    return fuse_plan, fuse_moteur, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout

"rajoute un etage a la fusee"
def dimension_plus(typ, taille, end_dim,
                   moteur        = deb_moteur,
                   fuse_plan     = 0, 
                   fuse_moteur   = -1,
                   fuse_haut     = deb_haut,
                   fuse_kg_vid   = deb_kg, 
                   fuse_kg_fuel  = 0, 
                   fuse_kg_total = deb_kg,
                   fuse_cout     = deb_cout):
    # print(moteur)
    # print(fuse_moteur)
    dim = dimension(fuse_moteur)
    if dim == 0 and end_dim == 1 :
        fuse_plan, fuse_moteur, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout = construc(typ, taille, moteur,
                                                                                                          [fuse_moteur],
                                                                                                          [fuse_haut],
                                                                                                          [fuse_kg_vid],
                                                                                                          [fuse_kg_fuel],
                                                                                                          [fuse_cout])
        dim = dimension(fuse_moteur)
    if dim == 0 and end_dim > 1 :
        fuse_plan, fuse_moteur, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout = dimension_plus(typ, taille, end_dim - 1,
                                                                                                                moteur, 
                                                                                                                fuse_plan, 
                                                                                                                fuse_moteur, 
                                                                                                                fuse_haut, 
                                                                                                                fuse_kg_vid,
                                                                                                                fuse_kg_fuel, 
                                                                                                                fuse_kg_total,
                                                                                                                fuse_cout)
        dim = dimension(fuse_moteur)
        # moteur += 1
    if dim > 0 and end_dim > 1 :
        fuse_plan     = liste_matrice(fuse_plan)
        fuse_moteur   = liste_matrice(fuse_moteur)
        fuse_haut     = liste_matrice(fuse_haut)
        fuse_kg_vid   = liste_matrice(fuse_kg_vid)
        fuse_kg_fuel  = liste_matrice(fuse_kg_fuel)
        fuse_kg_total = liste_matrice(fuse_kg_total)
        fuse_cout     = liste_matrice(fuse_cout)
        # print('a',fuse_kg_fuel)
        moteur += 1
        Q = range(len(fuse_moteur))
        for i0 in Q :
            fuse1_plan, fuse1_moteur, fuse1_haut, fuse1_kg_vid, fuse1_kg_fuel, fuse1_kg_total, fuse1_cout = dimension_plus(typ, taille, end_dim - 1,
                                                                                                                           moteur, 
                                                                                                                           fuse_plan[i0][0], 
                                                                                                                           fuse_moteur[i0][0],
                                                                                                                           fuse_haut[i0][0],  
                                                                                                                           fuse_kg_vid[i0][0],
                                                                                                                           fuse_kg_fuel[i0][0],
                                                                                                                           fuse_kg_total[i0][0],
                                                                                                                           fuse_cout[i0][0])
            # print('b',fuse1_kg_fuel)
            if dim < 2 :
                fuse_plan[i0]    = [numpy.append(fuse_plan[i0], fuse1_plan[i1]) for i1 in range(len(fuse1_plan))]
            else : fuse_plan[i0] = fuse1_plan
            fuse_moteur[i0]   = fuse1_moteur
            fuse_haut[i0]     = fuse1_haut
            fuse_kg_vid[i0]   = fuse1_kg_vid
            fuse_kg_fuel[i0]  = fuse1_kg_fuel
            fuse_kg_total[i0] = fuse1_kg_total
            fuse_cout[i0]     = fuse1_cout
            # print(dim, end_dim, fuse_kg_fuel[i0])
        dim = dimension(fuse_moteur)
    return fuse_plan, fuse_moteur, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout

## CALCULS
def dimension_decol(typ, fuse_moteur, fuse_kg_total,
                    fuse_agravit = 0) :
    dim0 = dimension(fuse_agravit)
    dim1 = dimension(fuse_moteur)
    # print(fuse_moteur)
    if dim0 == 0 and dim1 == 1 :
        fuse_agravit = [a_GRAVIT(0, typ, int(fuse_moteur[i]), fuse_kg_total[i]) for i in range(len(fuse_moteur))]
        dim0 = dimension(fuse_agravit)
    if dim0 == 0 and dim1 > 1 :
        fuse_agravit = [dimension_decol(typ, fuse_moteur[i], fuse_kg_total[i]) for i in range(len(fuse_moteur))]
        dim0 = dimension(fuse_agravit)
    return fuse_agravit #fuse_rpp,

def dimension_dv(typ, fuse_moteur, fuse_kg_vid, fuse_kg_total,
                 fuse_dv = 0) :
    dim0 = dimension(fuse_dv)
    dim1 = dimension(fuse_moteur)
    if dim0 == 0 and dim1 == 1 :
        # print(0, typ, fuse_moteur[0], fuse_kg_vid[0], fuse_kg_total[0])
        fuse_dv = [D_v(0, typ, fuse_moteur[0], fuse_kg_vid[0], fuse_kg_total[0])]
        for i in range(1, len(fuse_moteur)) :
            fuse_dv = numpy.append(fuse_dv, fuse_dv[0] + D_v(0, typ, fuse_moteur[i], fuse_kg_vid[i], fuse_kg_total[i]))
        dim0 = dimension(fuse_dv)
    if dim0 == 0 and dim1 > 1 :
        fuse_dv = [dimension_dv(typ, fuse_moteur[i], fuse_kg_vid[i], fuse_kg_total[i]) for i in range(len(fuse_moteur))]
        dim0 = dimension(fuse_dv)
    # print(fuse_dv)
    return fuse_dv

def dimension_matrice(dim, long, matrice = 0) :
    while dim != dimension(matrice) :
        matrice = [matrice for i in range(long)]
    return matrice

def dimension_test(fuse0_cout, fuse, but,
                  fuse1_cout = 0) :
  dim0 = dimension(fuse0_cout)
  dim1 = dimension(fuse1_cout)
  if dim1 == 0 and dim0 == 1 :
      fuse1_cout = [fuse0_cout[i] * (fuse[i] > but) for i in range(len(fuse0_cout))]
      dim1 = dimension(fuse1_cout)
  if dim1 == 0 and dim0 > 1 :
      fuse1_cout = [dimension_test(fuse0_cout[i], fuse[i], but) for i in range(len(fuse0_cout))]
      dim1 = dimension(fuse1_cout)  
  return fuse1_cout

def dimension_min(fuse_plan, fuse_cout,
                  min_cout = 0,
                  min_plan = 0) :
  dim = dimension(fuse_cout)
  if dim == 1 :
      for i in range(len(fuse_cout)):
          # print(fuse_cout[i],min_cout)
          if fuse_cout[i] != 0 and (fuse_cout[i] <= min_cout or min_cout == 0) :
              min_plan = fuse_plan[i]
              min_cout = fuse_cout[i]
  if dim > 1 :
      for i in range(len(fuse_cout)) :
          min_plan, min_cout = dimension_min(fuse_plan[i], fuse_cout[i], min_cout, min_plan)
  return min_plan, min_cout

def EULER_1d(typ, moteur, kg_fuel, step = 1) : return range(0, int(fuel_temp(kg_fuel, typ, moteur)), step)
def APOG(but, angle, temp, typ, moteur, z0, z1, dz, dx, kg_total, step = 1) :
    i = 1
    while (z0[-1] < but and z0[-1] > z0[i - 1]) or len(z0)==1:
        # print(i)
        temp    = numpy.append(temp   , temp[i - 1] + step)
        gravit  = GRAVIT(z0[i - 1] - z1)
        resist  = 0
        acceler = - resist / kg_total
        ddz     = acceler * math.cos(angle[i - 1]) - gravit
        # print("APOG     ddz[i]    ",ddz[i])
        ddx     = acceler * math.sin(angle[i - 1])
        # print(ddx[i])
        if z0[i - 1]  + step * dz + step**2 * ddz / 2 > 0 :
            # print(z[i - 1]  , step * dz[i - 1])
            z0  = numpy.append(z0 , z0[i - 1]  + step * dz + step**2 * ddz / 2)
        else :
            z0  = numpy.append(z0 , 0)
        dz      = dz + step * ddz
        # print("APOG     dz[i]     ",dz[i])
        dx      = dx + step * ddx
        # print(z)
        if dx > 0 :
            # if 180 * abs(math.atan(dz / dx) - angle[i - 1]) / math.pi < 1 :
            angle = numpy.append(angle, math.atan(dz / dx))
            # else : 
            #     angle = numpy.append(angle, angle[i - 1] + 1 * math.pi / 180)
        else : angle  = numpy.append(angle, 0)
        i += 1
    temp  = temp[  : len(temp)  - 1]
    z0    = z0[    : len(z0)    - 1]
    angle = angle[ : len(angle) - 1]
    return temp, z0, angle
def EULER_3d(but, typ, moteur, z0, kg_vid0, kg_fuel0, step = 1) :
    kg_fuel  = [kg_fuel0]
    z1       = z0 / 2
    z3       = [z0]
    dz       = 0
    dx       = vites_surface()
    x        = [0]
    temp0    = [0]
    temp1   = [0]
    kg_total = kg_vid0 + kg_fuel0
    gravit   = GRAVIT(z3[-1] - z1)
    angle0   = [0]
    angle1   = [0]
    apog     = [0]
    i        = 1
    # print(kg_fuel0)
    temp_max = fuel_temp(typ, moteur, kg_fuel0)
    # print(temp_max)
    while temp0[-1] < temp_max and z3[-1] < but and apog[-1] < but :
        temp0    = numpy.append(temp0   , i * step)
        kg_fuel  = kg_fuel0 - i * step * fuel_kg_d(typ, moteur) #numpy.append(kg_fuel , kg_fuel[i - 1] - step * fuel_kg_d(typ, moteur))
        kg_total = kg_vid0 + kg_fuel                            #numpy.append(kg_total, kg_vid0 + kg_fuel[i])
        gravit   = GRAVIT(z3[i - 1] - z1)                       #numpy.append(gravit  , GRAVIT(z3[i - 1] - z1))
        resist   = 0                                            #numpy.append(resist  , 0)
        pousse   = POUSSE(z3[i - 1], typ, moteur)               #numpy.append(pousse  , POUSSE(z3[i - 1], typ, moteur))
        acceler  = (pousse - resist) / kg_total                 #numpy.append(acceler , (pousse[i] - resist[i]) / kg_total[i])
        # print("EULER_3d acceler[i]",acceler[i])
        if acceler * math.cos(angle0[i - 1]) - gravit >= 0 :
            ddz  = acceler * math.cos(angle0[i - 1]) - gravit    #numpy.append(ddz     , acceler[i] * math.cos(angle[i - 1]) - gravit[i])
        else :
            ddz  = 0                                            #numpy.append(ddz     , 0)
        # print("EULER_3d ddz[i]    ",ddz[i])
        ddx      = acceler * math.sin(angle0[i - 1])             #numpy.append(ddx     , acceler[i] * math.sin(angle[i - 1]))
        # print(ddx[i])
        z3       = numpy.append(z3      , z3[i - 1] + step * dz + step**2 * ddz / 2)
        # print("EULER_3d z[i]      ",z[i])
        x        = numpy.append(x       , x[i - 1]  + step * dx + step**2 * ddx / 2)
        dz       = dz + step * ddz                              #numpy.append(dz      , dz[i - 1] + step * ddz[i])
        # print("EULER_3d dz[i]     ",dz[i])
        dx       = dx + step * ddx                              #numpy.append(dx      , dx[i - 1] + step * ddx[i])
        if dx > 0 :
            # if 180 * abs(math.atan(dz / dx) - angle0[i - 1]) / math.pi < 1 :
            angle0 = numpy.append(angle0 , math.atan(dz / dx))
            # else : 
            #     angle0 = numpy.append(angle0 , angle0[i - 1] + 1 * math.pi / 180)
        else : angle0  = numpy.append(angle0 , 0)
        # print("EULER_3d angle[i]  ",angle[i])
        temp1, apog, angle1 = APOG(but, [angle0[i]], [temp0[i]], typ, moteur, [z3[i]], z1, dz, dx, kg_total, step)
        # print("EULER_3d apog[i]   ",apog[i])
        i += 1
    return temp0, z3, angle0, temp1, apog, angle1

def dimension_altitud(but, typ, fuse_moteur, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_cout, 
                      fuse_altitud = 0) :
    dim0 = dimension(fuse_moteur)
    dim1 = dimension(fuse_altitud)
    if dim1 == 0 and dim0 == 1 :
        # print(fuse_moteur)
        fuse_altitud = []
        for i in range(len(fuse_moteur)) :
            if fuse_cout[i] > 0 :
                lligne0_temp, ligne0_altitud, ligne0_angle, ligne1_temp, ligne1_altitud, ligne1_angle = EULER_3d(but, typ, fuse_moteur[i], fuse_haut[i], fuse_kg_vid[i], fuse_kg_fuel[i])
            else : ligne1_altitud = [0]
            fuse_altitud = numpy.append(fuse_altitud, ligne1_altitud[-1])
        dim1 = dimension(fuse_altitud)
    # print(dim1,dim0)
    if dim1 == 0 and dim0 > 1 :
        fuse_altitud = [dimension_altitud(but, typ, fuse_moteur[i], fuse_haut[i], fuse_kg_vid[i], fuse_kg_fuel[i], fuse_cout[i]) for i in range(len(fuse_moteur))]
        dim1 = dimension(fuse_altitud)
    return fuse_altitud

## TESTES

# trac('nivelement barometrique', [PRESSION(i) for i in range(but)], 'pression (pa)', [i for i in range(but)], 'altitud (m)')
fuse0_0plan, fuse0_1moteur, fuse0_2haut, fuse0_3kg_vid, fuse0_4kg_fuel, fuse0_5kg_total, fuse0_6cout = dimension_plus(typ, taille, end_dim)
Z = 2
if Z > 0 :
    fuse0_7agravit = dimension_decol(typ, fuse0_1moteur, fuse0_5kg_total)
    fuse0_8dv      = dimension_dv(typ, fuse0_1moteur, fuse0_3kg_vid, fuse0_5kg_total)
    fuse0_6cout1   = dimension_test(fuse0_6cout, fuse0_7agravit, 1)
    fuse0_6cout1   = dimension_test(fuse0_6cout1, fuse0_8dv, escap(but))
    fuse0_9altitud = dimension_altitud(but, typ, fuse0_1moteur, fuse0_2haut, fuse0_3kg_vid, fuse0_4kg_fuel, fuse0_6cout1)
    fuse0_6cout1   = dimension_test(fuse0_6cout1, fuse0_9altitud, but)
    min_plan, min_cout = dimension_min(fuse0_0plan, fuse0_6cout1)
    if dimension(min_plan) == 1 :   
        if len(min_plan) == dimension(fuse0_1moteur) :
            ligne0_temp, ligne0_altitud, ligne0_angle, ligne1_temp, ligne1_altitud, ligne1_angle = EULER_3d(but, typ, 
                                                                                                        matric_nombre(fuse0_1moteur , min_plan), 
                                                                                                        matric_nombre(fuse0_2haut   , min_plan), 
                                                                                                        matric_nombre(fuse0_3kg_vid , min_plan), 
                                                                                                        matric_nombre(fuse0_4kg_fuel, min_plan))
        ligne0_angle *= 180 / math.pi
        ligne1_angle *= 180 / math.pi
        trac('vole', ligne0_altitud, 'altitud (m)', ligne0_angle, 'angle (deg)')
