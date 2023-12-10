# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

G = 6.674e-11   #Constante gravitationnelle m3⋅kg−1⋅s−2
R = 8.31446261815324 #Constante de gaz kg⋅m2.s−2⋅K−1⋅mol−1
base = 71

masse = 0 #kg
nom = -1
taille = -2 #m
haut = -3 #m
cout = -4
pods = [800, 635, 1.1, 1, 'mk1']

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

def fuel_kg_d(typ, moteur)  : return ergol_u_kg(engeins[typ][moteur][ergol_d]) + oxidizer_u_kg(engeins[typ][moteur][oxidizer_d])
def fuel_kg(taille, nombre) : return nombre * (ergol_u_kg(tanks[taille][ergol]) + oxidizer_u_kg(tanks[taille][oxidizer]))
def fuel_c(taille, nombre)  : return nombre * (ergol_u_c (tanks[taille][ergol]) + oxidizer_u_c (tanks[taille][oxidizer]))

def fuel_temp(kg_fuel, typ, moteur) : return kg_fuel / engeins[typ][moteur][ergol_d]

def vites_surface() : return planet[rayon] / planet[day]

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
    return     ISP(typ,moteur,altitud) * GRAVIT(0) * fuel_kg_d(typ, moteur)

"Le rapport poussée sur poids est un rapport qui définit la puissance des moteurs d'un engin par rapport à son propre poids."
def RPP(kg, typ, moteur, altitud, nombre=1): #>1
    return POUSSE(typ,moteur,altitud,nombre) / (kg * GRAVIT(altitud))
def a_GRAVIT(kg, typ,moteur, altitud, nombre=1):
    return GRAVIT(altitud) * (RPP(kg,typ,moteur,altitud,nombre) - 1)

"Changement de vitesse d'un vaisseau spatial mesuré en mètres par seconde (m/s)."
def D_v(kg_vid, kg_total,typ, moteur, altitud):
    return ISP(typ,moteur,altitud) * GRAVIT(0) * math.log(kg_total/ kg_vid)

## FONCTION
import numpy

"[0, 0] -> [[0], [0]]"
def liste_matrice(liste):
    return [[liste[i]] for i in range(len(liste))]

charg_haut = pods[haut] + base
charg_kg   = pods[masse]
charg_cout = pods[cout]
def construc(typ, taille, moteur,
             fuse_moteur   = [-1],
             fuse_haut     = [charg_haut],
             fuse_kg_vid   = [charg_kg],
             fuse_kg_fuel  = [0],
             fuse_cout     = [charg_cout]) :
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
q = 1 * 8 + 1
typ = 0
taille = 1
moteur = 2
fuse_1d_0plan, fuse_1d_1moteur, fuse_1d_2haut, fuse_1d_3kg_vid, fuse_1d_4kg_fuel, fuse_1d_5kg_total, fuse_1d_6cout = construc(typ, taille, moteur)
# print(fuse_1d_0plan, fuse_1d_1moteur, fuse_1d_2kg_vid, fuse_1d_3kg_fuel, fuse_1d_4kg_total, fuse_1d_5cout)

"retourne la dimention matriciel"
def dimension(matrice) : return len(numpy.shape(matrice))

def matric_liste(matrice, plan, j = 0) :
    if j < len(plan) : 
        return matric_liste(matrice[plan[j]], plan, j + 1)
    return matrice
# print(matric_liste([[0], [1]], [1], j = 0))

def dimension_plus(typ, taille, moteur, end_dim,
                   fuse_plan     = 0, 
                   fuse_moteur   = -1,
                   fuse_haut     = charg_haut,
                   fuse_kg_vid   = charg_kg,
                   fuse_kg_fuel  = 0, 
                   fuse_kg_total = 0, 
                   fuse_cout     = charg_cout) :
    dim = dimension(fuse_moteur)
    # print(dim, end_dim, moteur)
    if dim == 0 and end_dim == 1:
        fuse_plan, fuse_moteur, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout = construc(typ, taille, moteur, [fuse_moteur], [fuse_haut], [fuse_kg_vid], [fuse_kg_fuel], [fuse_cout])
        dim = dimension(fuse_moteur)
    if dim == 0 and end_dim > 1 :
        fuse_plan, fuse_moteur, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout = dimension_plus(typ, taille, moteur, end_dim - 1, fuse_plan, fuse_moteur, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout)
        dim = dimension(fuse_moteur)
        moteur += 1
    if dim > 0 and end_dim > 1 :
        fuse_plan     = liste_matrice(fuse_plan)
        fuse_moteur   = liste_matrice(fuse_moteur)
        fuse_haut     = liste_matrice(fuse_haut)
        fuse_kg_vid   = liste_matrice(fuse_kg_vid)
        fuse_kg_fuel  = liste_matrice(fuse_kg_fuel)
        fuse_kg_total = liste_matrice(fuse_kg_total)
        fuse_cout     = liste_matrice(fuse_cout)
        Q = range(len(fuse_moteur))
        for i in Q :
            print(fuse_moteur[i])
            fuse_plan[i], fuse_moteur[i], fuse_haut[i], fuse_kg_vid[i], fuse_kg_fuel[i], fuse_kg_total[i], fuse_cout[i] = dimension_plus(typ, taille, moteur, end_dim - 1, fuse_plan[i], fuse_moteur[i], fuse_haut[i], fuse_kg_vid[i], fuse_kg_fuel[i], fuse_kg_total[i], fuse_cout[i])
        dim = dimension(fuse_moteur)
    return fuse_plan, fuse_moteur, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout
# print(dimension_plus2(typ, taille, moteur, 2))

## TESTES
def dimension_matrice(dim, long, matrice = 0) :
    while dim != dimension(matrice) :
        matrice = [matrice for i in range(long)]
    return matrice

def dimension_decol(fuse_kg_total, typ, fuse_moteur,
                    fuse_agravit = 0) :
    dim0 = dimension(fuse_agravit)
    dim1 = dimension(fuse_moteur)
    # print(fuse_moteur)
    if dim0 == 0 and dim1 == 1 :
        # fuse_rpp     = [RPP     (fuse_kg_total[i], typ, int(fuse_moteur[i]), 0) for i in range(len(fuse_moteur))]
        fuse_agravit = [a_GRAVIT(fuse_kg_total[i], typ, int(fuse_moteur[i]), 0) for i in range(len(fuse_moteur))]
        dim0 = dimension(fuse_agravit)
    if dim0 == 0 and dim1 > 1 :
        for i in range(len(fuse_moteur)) :
            fuse_agravit = dimension_decol(fuse_kg_total[i], typ, fuse_moteur[i], fuse_agravit)
        dim0 = dimension(fuse_agravit)
    if dim0 > 0 and dim1 > 1 :
        for i in range(len(fuse_agravit)) :
            fuse_agravit[i] = dimension_decol(fuse_kg_total[i], typ, fuse_moteur[i], fuse_agravit[i])
        dim0 = dimension(fuse_agravit)
    # print(fuse_agravit)
    return fuse_agravit #fuse_rpp,

def dimension_min(fuse0_cout, fuse_agravit,
                  fuse1_cout = 0) :
  dim0 = dimension(fuse0_cout)
  dim1 = dimension(fuse1_cout)
  if dim1 == 0 and dim0 == 1 :
      fuse1_cout = [fuse0_cout[i] * (fuse_agravit[i] > 1) for i in range(len(fuse0_cout))]
      dim1 = dimension(fuse1_cout)
  if dim1 == 0 and dim0 > 1 :
      for i in range(len(fuse0_cout)) :
          fuse1_cout = dimension_min(fuse0_cout[i], fuse_agravit[i], fuse1_cout)
      dim1 = dimension(fuse1_cout)
  if dim1 > 0 and dim0 > 1 :
      for i in range(len(fuse0_cout)) :
          fuse1_cout[i] = dimension_min(fuse0_cout[i], fuse_agravit[i], fuse1_cout[i])
      dim1 = dimension(fuse1_cout)    
  return fuse1_cout

def EULER_1d(kg_fuel, typ, moteur, step = 1) : return range(0, int(fuel_temp(kg_fuel, typ, moteur)), step)
def APOG(kg_vid0, kg_fuel0, typ, moteur, ddz0, dz0, z0, temp0, angle0, step = 1) :
    ddz      = [ddz0]
    dz       = [dz0]
    z        = [z0]
    temp     = [temp0]
    kg_fuel  = [kg_fuel0]
    kg_total = [kg_vid0 + kg_fuel0]
    resist   = [0]
    gravit   = [GRAVIT(z[-1])]
    acceler  = [0]
    i = 1
    while len(z) == 1 or z[-1] > z[i - 1] :
        # print(i)
        temp       = numpy.append(temp    , temp[i - 1] + step)
        kg_fuel    = numpy.append(kg_fuel , kg_fuel[i - 1] - step * fuel_kg_d(typ, moteur))
        kg_total   = numpy.append(kg_total, kg_vid0 + kg_fuel[i])
        gravit     = numpy.append(gravit  , GRAVIT(z[i - 1]))
        resist     = numpy.append(resist  , 0)
        acceler    = numpy.append(acceler , -resist[i] / kg_total[i])
        ddz        = numpy.append(ddz     , acceler[i] * math.cos(angle0) - gravit[i])
        # print("APOG     ddz[i]    ",ddz[i])
        dz         = numpy.append(dz      , dz[i - 1] + step * ddz[i])
        # print("APOG     dz[i]     ",dz[i])
        if z[i - 1]  + step * dz[i - 1] + step * ddz[i] / 2 > 0 :
            # print(z[i - 1]  , step * dz[i - 1])
            z      = numpy.append(z       , z[i - 1]  + step * dz[i - 1] + step**2 * ddz[i] / 2)
        else :
            z      = numpy.append(z       , 0)
        # print(z)
        i += 1
    return z[i - 1]
def EULER_3d(kg_vid0, kg_fuel0, typ, moteur, z0, but, step = 1) :
    ddz      = [0]
    dz       = [0]
    z        = [z0]
    z1       = z0 / 2
    ddx      = [0]
    dx       = [vites_surface()]
    x        = [0]
    temp     = [0]
    kg_fuel  = [kg_fuel0]
    kg_total = [kg_vid0 + kg_fuel0]
    pousse   = [0]
    resist   = [0]
    gravit   = [GRAVIT(z[-1] - z1)]
    angle    = [0]
    acceler  = [0]
    apog     = [0]
    i        = 1
    temp_max = fuel_temp(kg_fuel0, typ, moteur)
    while temp[-1] < temp_max and z[-1] < but and apog[-1] < but :
        temp      = numpy.append(temp    , temp[i - 1] + step)
        kg_fuel   = numpy.append(kg_fuel , kg_fuel[i - 1] - step * fuel_kg_d(typ, moteur))
        kg_total  = numpy.append(kg_total, kg_vid0 + kg_fuel[i])
        gravit    = numpy.append(gravit  , GRAVIT(z[i - 1] - z1))
        resist    = numpy.append(resist  , 0)
        pousse    = numpy.append(pousse  , POUSSE(typ, moteur, z[i - 1]))
        acceler   = numpy.append(acceler , (pousse[i] - resist[i]) / kg_total[i])
        # print("EULER_3d acceler[i]",acceler[i])
        if acceler[i] * math.cos(angle[i - 1]) - gravit[i] >= 0 :
            ddz   = numpy.append(ddz     , acceler[i] * math.cos(angle[i - 1]) - gravit[i])
        else :
            ddz   = numpy.append(ddz     , 0)
        # print("EULER_3d ddz[i]    ",ddz[i])
        ddx       = numpy.append(ddx     , acceler[i] * math.sin(angle[i - 1]))
        # print(ddx[i])
        dz        = numpy.append(dz      , dz[i - 1] + step * ddz[i])
        # print("EULER_3d dz[i]     ",dz[i])
        dx        = numpy.append(dx      , dx[i - 1] + step * ddx[i])
        z         = numpy.append(z       , z[i - 1]  + step * dz[i - 1] + step**2 * ddz[i] / 2)
        # print("EULER_3d z[i]      ",z[i])
        x         = numpy.append(x       , x[i - 1]  + step * dx[i - 1] + step**2 * ddx[i] / 2)
        if dx[i] > 0 :
            angle = numpy.append(angle   , math.atan(dz[i] / dx[i]))
        else : 
            angle = numpy.append(angle   , 0)
        # print("EULER_3d angle[i]  ",angle[i])
        apog      = numpy.append(apog    , APOG(kg_vid0, kg_fuel[i], typ, moteur, ddz[i], dz[i], z[i], temp[i], angle[i]))
        # print("EULER_3d apog[i]   ",apog[i])
        i += 1
    return temp, z, angle

q = 2 * 8 + 1
typ = 0
taille = 1
end_dim = 1
moteur = 4 + 1 - end_dim
dim = 1
fuse0_0plan, fuse0_1moteur, fuse0_2haut, fuse0_3kg_vid, fuse0_4kg_fuel, fuse0_5kg_total, fuse0_6cout = dimension_plus(typ, taille, moteur, end_dim)

Z = 3
if Z > 0 :
    fuse0_7agravit = dimension_decol(fuse0_5kg_total, typ, fuse0_1moteur)
    if Z > 1 :
        fuse1_6cout = dimension_min(fuse0_6cout, fuse0_7agravit)
        
        fuse0_8deltav =[]
        for i0 in range(q):
            fuse0_8deltav = numpy.append(fuse0_8deltav, D_v(fuse0_3kg_vid[i0],fuse0_5kg_total[i0],typ,int(fuse0_1moteur[i0]),0))
        but = 70000
        min_0dv = escap(but)
        for i0 in range(q):
            if fuse0_8deltav[i0] < min_0dv:
                fuse1_6cout[i0] = 0
    
        min_1plan = []
        min_2cout = 0
        for i0 in range(q):
            if fuse1_6cout[i0] != 0:
                if  min_2cout == 0:
                    min_1plan = fuse0_0plan[i0]
                    min_2cout = fuse1_6cout[i0]
                elif fuse1_6cout[i0] <  min_2cout:
                    min_1plan = fuse0_0plan[i0]
                    min_2cout = fuse1_6cout[i0]
                elif fuse1_6cout[i0] ==  min_2cout :
                    min_1plan = fuse0_0plan[i0]
                    min_2cout = fuse1_6cout[i0]

        # print(temp_ligne)
        if Z > 2 :
            import matplotlib.pyplot
            
            ligne0_0temp, ligne0_1altitud, ligne0_2angle = EULER_3d(fuse0_3kg_vid[min_1plan], fuse0_4kg_fuel[min_1plan], typ, moteur, fuse0_2haut[min_1plan], but)
            ligne0_2angle *= 180 / math.pi
            matplotlib.pyplot.plot(ligne0_0temp, ligne0_2angle)
            matplotlib.pyplot.title('Approximate angle x temp')
            matplotlib.pyplot.xlabel('temp (s)')
            matplotlib.pyplot.ylabel('angle (deg)')
            matplotlib.pyplot.show()