# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# COSTANTE
import matplotlib.pyplot
import numpy
import math
G = 6.674e-11  # Constante gravitationnelle m3⋅kg−1⋅s−2
R = 8.31446261815324  # Constante de gaz kg⋅m2.s−2⋅K−1⋅mol−1
base = 71

rayon = 1  # m
day = 2  # s
kelvin_0 = 3  # K
masse_moyen_mol = 4  # kg.mol-1
pression_pa_0 = 5  # kg⋅m −1⋅s −2
asl_limit = 6  # m
planet = [5.2915158e22, 6e+5, 21600, 288.15,
          0.0289644, 101325, 70000, 'kerbin']

masse = 0  # kg
nom = -1
taille = -2  # m
haut = -3  # m
cout = -4
chut = [[ 75, 150, 0    , 0  , 'mk12-r'],
        [100, 422, 0.631, 0.6, 'mk16']]

what_d = 1
bodyne =[ 50, 1.7/60, 300, 1, 0.6, 'staysputnick']
pods = [800, 0.2, 635, 1.1, 1.3, 'mk1']
control = [50, 0.3, 600, 0.628, 0.6, 'SAS']
comm = [5, 20, 300, 0, 0, '16']
what = 1
elect = [5, 100, 80, 0, 0, 'z-100']


stack = [[ 10, 150, 0.625, 0.6, 'td-06'],
         [ 40, 200, 0    , 1.3, 'td-12'],
         [160, 300, 1    , 2.5, 'td-25'],
         [360, 375, 1    , 3.8, 'td-37']]
radial = [[ 25, 600, 0, 0, 'tt-38'],
          [ 50, 700, 0, 0, 'tt-70'],
          [400, 770, 0, 0, 'hdm']]
coupling = [stack, radial]

ergol = 1  # u.s-1
oxidizer = 2  # u.s-1
multipl = -4
tanks = [[  25  ,   18,   22, 0,  52  , 0.625, 0.6, 'oscar-b'],
         [  62.5,   45,   55, 8,  54.1, 0.5  , 1.3, 'fl'],
         [ 500  ,  360,  440, 8, 351.5, 1    , 2.5, 'x200'],
         [2250  , 1620, 1980, 3, 347.5, 2.665, 3.8, 's3']]

ergol_d = 1  # u.s-1
oxidizer_d = 2  # u.s-1
pousse_asl = 3  # kg.m.s-2
pousse_vac = 4  # kg.m.s-2
isp_asl = 5  # s
isp_vac = 6  # s
reacteurs = [[  20,  0.058,  0.071,     508,    2000,  80, 315,   110, 0.3, 0.6, 'ant'],
             [ 130,  0.574,  0.701,   16560,   20000, 265, 320,   240, 0.4, 0.6, 'spark'],
             [ 500,  1.596,  1.951,   14780,   60000,  85, 345,   390, 0.8, 1.3, 'terrier'],
             [1500,  6.166,  7.536,  167969,  215000, 250, 320,  1200, 1.7, 1.3, 'reliant'],
             [1250,  7.105,  8.684,  205161,  240000, 265, 310,  1100, 1.7, 1.3, 'swivel'],
             [1750,  6.555,  8.012,   64286,  250000,  90, 350,  1300, 2.7, 2.5, 'poodle'],
             [3000, 18.642, 22.784,  658750,  650000, 280, 320,  5300, 2.4, 2.5, 'skipper'],
             [6000, 40.407, 54.275, 1379032, 1500000, 285, 310, 13000, 3  , 2.5, 'minsail'],
             [9000, 53.985, 65.982, 1205882, 2000000, 205, 340, 25000, 4.1, 3.8, 'rhino'],
             [0, 0.0, 0, 0, 0, 0, 0, 0, 0, '0']]
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
               [0, 0.0, 0, 0, 0, 0, 0, 0, 0, '0']]
engeins = [reacteurs, propulseurs]

# PHYSIQUE


def PA_atm(nombre)       : return nombre / 101325
def ergol_u_kg(nombre)   : return nombre * 5
def oxidizer_u_kg(nombre): return nombre * 5
def solid_u_kg(nombre)   : return nombre * 2810 / 375
def ergol_u_c(nombre)    : return nombre * 0.8
def oxidizer_u_c(nombre) : return nombre * 0.18
def solid_u_c(nombre)    : return nombre * 225 / 375


# def cout_multipl(reserv, nombre) : return nombre * tanks[reserv][cout] + tanks[reserv][cout] * (tanks[reserv][multipl] + 1 - nombre) / tanks[reserv][multipl] - 4.25
def fuel_kg(reserv) : return ergol_u_kg(tanks[reserv][ergol]) + oxidizer_u_kg(tanks[reserv][oxidizer])
def fuel_c(reserv)  : return ergol_u_c(tanks[reserv][ergol]) + oxidizer_u_c(tanks[reserv][oxidizer])

def fuel_kg_d(typ, moteur, nombre) :
    return nombre * (ergol_u_kg(engeins[typ][moteur][ergol_d]) + oxidizer_u_kg(engeins[typ][moteur][oxidizer_d]))
def fuel_temp(typ, moteur, nombre, kg_fuel):
    if moteur == -1 : return 0
    return kg_fuel / fuel_kg_d(typ, moteur, nombre)

def vites_surface(): return planet[rayon] / planet[day]

"La vitesse nécessaire pour échapper au puits de gravité d'une planète donnée"
def escap(altitud):  # m.s-1
    return math.sqrt(2*G*planet[masse]/(planet[rayon]+altitud))
def GRAVIT(altitud):  # m.s-2
    return G * planet[masse] / (planet[rayon] + altitud)**2

"la hauteur d'échelle est l'augmentation d'altitude pour laquelle la pression aslosphérique diminue d'un facteur e "
# def TEMP(altitud):
#     z_base_terre = [0,11000,20000,32000,47000,51000,71000,84852]
#     z_base_kerbin = z_base_terre * 70 /105
def HE():
    return R * planet[kelvin_0] / planet[masse_moyen_mol] / GRAVIT(0)
def PRESSION(altitud):  # pa
    if altitud >= planet[asl_limit] : return 0
    return planet[pression_pa_0] * math.exp(-altitud / HE())
    # return planet[pression_pa_0] * (1 - altitud * 6.5 / 1000 / planet[kelvin_0])**(5.255) # imajinair
    # z = [0, 2500, 5000, 7500, 10000, 15000, 20000, 25000, 30000, 40000, 50000, 60000, 70000]
    # p = 101
def DENSIT(altitud):
    return PRESSION(altitud) / R / planet[kelvin_0]

"L'impulsion spécifique définit l'efficacité d'un moteur."
def ISP(typ, moteur, nombre, altitud):  # s
    return nombre * (engeins[typ][moteur][isp_vac] + PA_atm(PRESSION(altitud)) * (engeins[typ][moteur][isp_asl] - engeins[typ][moteur][isp_vac]))


"la poussée est la force exercée par l'accélération de gaz"
def POUSSE(typ, moteur, nombre, altitud):
    return ISP(typ, moteur, nombre, altitud) * GRAVIT(0) * fuel_kg_d(typ, moteur, nombre)

"Le rapport poussée sur poids est un rapport qui définit la puissance des moteurs d'un engin par rapport à son propre poids."
def RPP(typ, moteur, nombre, altitud, kg):  # >1
    return nombre * POUSSE(typ, moteur, nombre, altitud) / (kg * GRAVIT(altitud))
def a_GRAVIT(typ, moteur, nombre, altitud, kg):
    return GRAVIT(altitud) * (RPP(typ, moteur, nombre, altitud, kg) - 1)


"Changement de vitesse d'un vaisseau spatial mesuré en mètres par seconde (m/s)."
def D_v(typ, moteur, nombre, altitud, kg_vid, kg_total):
    return ISP(typ, moteur, nombre, altitud) * GRAVIT(0) * math.log(kg_total / kg_vid)

def orbital_v(altitud, axe_grand_demi) :
    return math.sqrt(G * planet[masse] * (2 / (planet[rayon] + altitud) - 1 / axe_grand_demi))


# VARIABLE
min_0plan, min_1cout = 0, 0
deb_haut = pods[haut] + chut[1][haut] + base
deb_kg = pods[masse] + chut[1][masse]
deb_cout = pods[cout] + chut[1][cout]
deb_taille = pods[taille]
deb_moteur = 0
q = 1 * 8 + 1
dim = 1
but = 70000
step0 = 1
angle_max0 = 1

# STRUCTURE


def taille_deb(table):
    i = 0
    while table[i][taille] != deb_taille:
        # print(table[i][taille])
        i += 1
    return i


def taille_fin(table):
    i = taille_deb(table)
    while table[i][taille] == deb_taille:
        i += 1
    return i - 1


"[0, 0] -> [[0], [0]]"
def liste_matrice(liste):
    return [[liste[i]] for i in range(len(liste))]

"retourne la dimention matriciel"
def dimension(matrice): return len(numpy.shape(matrice))

def matric_nombre(matrice, plan, j=0):
    if j < len(plan):
        return matric_nombre(matrice[plan[j]], plan, j + 1)
    return matrice

def dimension_matrice(dim, long, matrice=0):
    while dim != dimension(matrice):
        matrice = [matrice for i in range(long)]
    return matrice

def trac(nom, X, x_nom, Y, y_nom):
    matplotlib.pyplot.plot(X, Y)
    matplotlib.pyplot.title(nom)
    matplotlib.pyplot.xlabel(x_nom)
    matplotlib.pyplot.ylabel(y_nom)
    matplotlib.pyplot.show()

reserv = taille_deb(tanks)
reacteur_deb = taille_deb(reacteurs)
reacteur_fin = taille_fin(reacteurs)
propulseur_deb = taille_deb(propulseurs)
propulseur_fin = taille_fin(propulseurs)

def trac_plan(plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, step=step0, angle_max = angle_max0):
    global min_2temp, min_3angle, min_4altitud, min_5apog
    min_2temp, min_3angle, min_4altitud, x, dz, dx, ddz, ddx = EULER_plan(plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, step, angle_max)
    # print(x)
    kg_total = matric_nombre(fuse_kg_vid, plan) + matric_nombre(fuse_kg_fuel, plan)
    centre_masse_haut = matric_nombre(fuse_haut, plan)
    temp1, min_3angle, min_5apog, x1, dz1, dx1, ddz1, ddx1 = APOG(kg_total, min_2temp, min_3angle, min_4altitud, x, dz, dx, ddz, ddx, centre_masse_haut, step, angle_max)
    # print(x1)
    min_3angle *= 180 / math.pi
    matplotlib.pyplot.quiver(x1,min_5apog, ddx1, ddz1, color='r')
    matplotlib.pyplot.quiver(x1, min_5apog, dx1, dz1, color='g')
    matplotlib.pyplot.plot(x, min_4altitud)
    matplotlib.pyplot.title('vol')
    matplotlib.pyplot.xlabel('position')
    matplotlib.pyplot.ylabel('altitud')
    matplotlib.pyplot.show()

# FONCTION
def construc(typ, moteur,
             fuse_typ     = [0],
             fuse_moteur  = [-1],
             fuse_nombre  = [1],
             fuse_haut    = [deb_haut],
             fuse_kg_vid  = [deb_kg],
             fuse_kg_fuel = [0],
             fuse_cout    = [deb_cout]):
    fuse_plan = [0]
    fuse_kg_total = [fuse_kg_vid[0] + fuse_kg_fuel[0]]
    for i in range(1, q):
        fuse_plan   = numpy.append(fuse_plan    , i)
        fuse_typ    = numpy.append(fuse_typ     , typ)
        fuse_moteur = numpy.append(fuse_moteur  , moteur)
        if typ == 0 :
            fuse_nombre  = numpy.append(fuse_nombre , 1)
            fuse_haut    = numpy.append(fuse_haut   , fuse_haut[0]     + coupling[typ][reserv][haut]  + engeins[typ][moteur][haut]  + i *  tanks[reserv][haut])
            fuse_kg_vid  = numpy.append(fuse_kg_vid , fuse_kg_total[0] + coupling[typ][reserv][masse] + engeins[typ][moteur][masse] + i *  tanks[reserv][masse])
            fuse_cout    = numpy.append(fuse_cout   , fuse_cout[0]     + coupling[typ][reserv][cout]  + engeins[typ][moteur][cout]  + i * (tanks[reserv][cout] + fuel_c(reserv)))
            fuse_kg_fuel = numpy.append(fuse_kg_fuel, i * fuel_kg(reserv))
        elif typ == 1 and i == 1 :
            fuse_nombre  = numpy.append(fuse_nombre , 1)
            fuse_haut    = numpy.append(fuse_haut   , fuse_haut[0]     + coupling[0][reserv][haut]  + engeins[typ][moteur][haut])
            fuse_kg_vid  = numpy.append(fuse_kg_vid , fuse_kg_total[0] + coupling[0][reserv][masse] + engeins[typ][moteur][masse])
            fuse_cout    = numpy.append(fuse_cout   , fuse_cout[0]     + coupling[0][reserv][cout]  + engeins[typ][moteur][cout] + solid_u_c( engeins[typ][moteur][solid]))
            fuse_kg_fuel = numpy.append(fuse_kg_fuel, solid_u_kg(engeins[typ][moteur][solid]))
        else :
            fuse_nombre  = numpy.append(fuse_nombre , i)
            fuse_haut    = numpy.append(fuse_haut   , fuse_haut[0])
            fuse_kg_vid  = numpy.append(fuse_kg_vid , fuse_kg_total[0] + i * (coupling[typ][0][masse] + engeins[typ][moteur][masse]))
            fuse_cout    = numpy.append(fuse_cout   , fuse_cout[0]     + i * (coupling[typ][0][cout]  + engeins[typ][moteur][cout]  + solid_u_c( engeins[typ][moteur][solid])))
            fuse_kg_fuel = numpy.append(fuse_kg_fuel, i * solid_u_kg(engeins[typ][moteur][solid]))
        fuse_kg_total = numpy.append(fuse_kg_total, fuse_kg_vid[i] + fuse_kg_fuel[i])
    return fuse_plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout

"rajoute un etage a la fusee"
def dimension_base(end_dim,
                   typ = 0,
                   moteur = reacteur_deb,
                   fuse_typ      = 0,
                   fuse_moteur   = -1,
                   fuse_haut     = deb_haut,
                   fuse_kg_vid   = deb_kg,
                   fuse_kg_total = deb_kg,
                   fuse_cout     = deb_cout,
                   fuse_plan     = 0,
                   fuse_nombre   = 1,
                   fuse_kg_fuel  = 0):
    # print(moteur)
    # print(fuse_moteur)
    dim = dimension(fuse_moteur)
    if dim == 0 and end_dim == 1:
        fuse_plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout = construc(typ, moteur,
                                                                                                                    [fuse_typ],
                                                                                                                    [fuse_moteur],
                                                                                                                    [fuse_nombre],
                                                                                                                    [fuse_haut],
                                                                                                                    [fuse_kg_vid],
                                                                                                                    [fuse_kg_fuel],
                                                                                                                    [fuse_cout])
        dim = dimension(fuse_moteur)
    if dim == 0 and end_dim > 1:
        fuse_plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout = dimension_base(end_dim - 1,
                                                                                                                          typ,
                                                                                                                          moteur,
                                                                                                                          fuse_typ,
                                                                                                                          fuse_moteur,
                                                                                                                          fuse_haut,
                                                                                                                          fuse_kg_vid,
                                                                                                                          fuse_kg_total,
                                                                                                                          fuse_cout,
                                                                                                                          fuse_plan,
                                                                                                                          fuse_nombre,
                                                                                                                          fuse_kg_fuel)
        dim = dimension(fuse_moteur)
        # moteur += 1
    if dim > 0 and end_dim > 1:
        fuse_plan     = liste_matrice(fuse_plan)
        fuse_typ      = liste_matrice(fuse_typ)
        fuse_moteur   = liste_matrice(fuse_moteur)
        fuse_nombre   = liste_matrice(fuse_nombre)
        fuse_haut     = liste_matrice(fuse_haut)
        fuse_kg_vid   = liste_matrice(fuse_kg_vid)
        fuse_kg_fuel  = liste_matrice(fuse_kg_fuel)
        fuse_kg_total = liste_matrice(fuse_kg_total)
        fuse_cout     = liste_matrice(fuse_cout)
        # print('a',fuse_kg_fuel)
        if typ == 0 and moteur + 1 > reacteur_fin :
            typ = 1
            moteur = propulseur_deb
        else : moteur += 1
        Q = range(len(fuse_moteur))
        for i0 in Q:
            fuse1_plan, fuse1_typ, fuse1_moteur, fuse1_nombre, fuse1_haut, fuse1_kg_vid, fuse1_kg_fuel, fuse1_kg_total, fuse1_cout = dimension_base(end_dim - 1,
                                                                                                                                      typ,
                                                                                                                                      moteur,
                                                                                                                                      fuse_typ[i0][0],
                                                                                                                                      fuse_moteur[i0][0],
                                                                                                                                      fuse_haut[i0][0],
                                                                                                                                      fuse_kg_vid[i0][0],
                                                                                                                                      fuse_kg_total[i0][0],
                                                                                                                                      fuse_cout[i0][0],
                                                                                                                                      fuse_plan[i0][0],
                                                                                                                                      fuse_nombre[i0][0],
                                                                                                                                      fuse_kg_fuel[i0][0])
            # print('b',fuse1_kg_fuel)
            if dim < 2:
                fuse_plan[i0] = [numpy.append(fuse_plan[i0], fuse1_plan[i1]) for i1 in range(len(fuse1_plan))]
            else:
                fuse_plan[i0] = fuse1_plan
            # print(dim, end_dim, fuse1_typ)
            fuse_typ[i0]      = fuse1_typ
            fuse_moteur[i0]   = fuse1_moteur
            fuse_nombre[i0]   = fuse1_nombre
            fuse_haut[i0]     = fuse1_haut
            fuse_kg_vid[i0]   = fuse1_kg_vid
            fuse_kg_fuel[i0]  = fuse1_kg_fuel
            fuse_kg_total[i0] = fuse1_kg_total
            fuse_cout[i0]     = fuse1_cout
        dim = dimension(fuse_moteur)
    return fuse_plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout

def dimension_plus(end_dim, plan, deb_typ, deb_moteur, deb_haut, deb_kg, deb_cout,
                   typ_deb = 1,
                   moteur_deb = propulseur_deb) :
    fuse_plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout = dimension_base(end_dim, typ_deb, moteur_deb,
                                                                                                                                   fuse_typ      = deb_typ,
                                                                                                                                   fuse_moteur   = deb_moteur,
                                                                                                                                   fuse_haut     = deb_haut,
                                                                                                                                   fuse_kg_vid   = deb_kg,
                                                                                                                                   fuse_kg_total = deb_kg,
                                                                                                                                   fuse_cout     = deb_cout)
    return fuse_plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout

# CALCULS
def dimension_decol(typ, moteur, nombre, kg_total,
                    agravit=0):
    dim0 = dimension(agravit)
    dim1 = dimension(moteur)
    # print(fuse_moteur)
    if dim0 == 0 and dim1 == 1:
        # print(typ)
        agravit = [a_GRAVIT(int(typ[i]), int(moteur[i]), int(nombre[i]), 0, kg_total[i]) for i in range(len(moteur))]
        dim0 = dimension(agravit)
    if dim0 == 0 and dim1 > 1:
        agravit = [dimension_decol(typ[i], moteur[i], nombre[i], kg_total[i]) for i in range(len(moteur))]
        dim0 = dimension(agravit)
    return agravit  # fuse_rpp,

def dimension_dv(typ, moteur, nombre, kg_vid, kg_total, altitud,
                 dv=0):
    dim0 = dimension(dv)
    dim1 = dimension(moteur)
    if dim0 == 0 and dim1 == 1:
        # print(0, typ, fuse_moteur[0], fuse_kg_vid[0], fuse_kg_total[0])
        dv = [D_v(typ[0], moteur[0], nombre[0], altitud, kg_vid[0], kg_total[0])]
        for i in range(1, len(moteur)):
            dv = numpy.append(dv, dv[0] + D_v(typ[i], moteur[i], nombre[i], altitud, kg_vid[i], kg_total[i]))
        dim0 = dimension(dv)
    if dim0 == 0 and dim1 > 1:
        dv = [dimension_dv(typ[i], moteur[i], nombre[i], kg_vid[i], kg_total[i], altitud) for i in range(len(moteur))]
        dim0 = dimension(dv)
    # print(fuse_dv)
    return dv

def dimension_test(cout0, fuse, but,
                   cout1=0):
    dim0 = dimension(cout0)
    dim1 = dimension(cout1)
    if dim1 == 0 and dim0 == 1:
        cout1 = [cout0[i] * (fuse[i] > but) for i in range(len(cout0))]
        dim1 = dimension(cout1)
    if dim1 == 0 and dim0 > 1:
        # print(dim1, dim0, cout0)
        cout1 = [dimension_test(cout0[i], fuse[i], but) for i in range(len(cout0))]
        dim1 = dimension(cout1)
    # print(dim1, dim0, cout1)
    return cout1

def dimension_min(plan, cout,
                  min_cout=0,
                  min_plan=0):
    dim = dimension(cout)
    if dim == 1:
        for i in range(len(cout)):
            # print(fuse_cout[i],min_cout)
            if cout[i] != 0 and (cout[i] <= min_cout or min_cout == 0):
                min_plan = plan[i]
                min_cout = cout[i]
    if dim > 1:
        for i in range(len(cout)):
            min_plan, min_cout = dimension_min(plan[i], cout[i], min_cout, min_plan)
    return min_plan, min_cout

def APOG(kg_total, temp, angle, altitud, x, dz, dx, ddz, ddx, centre_masse_haut, step=step0, angle_max = angle_max0):
    temp1 = numpy.copy(temp)
    angle1 = numpy.copy(angle)
    apog = numpy.copy(altitud)
    x1 = numpy.copy(x)
    dz1 = numpy.copy(dz)
    dx1 = numpy.copy(dx)
    ddz1 = numpy.copy(ddz)
    ddx1 = numpy.copy(ddx)
    # print(ddx)
    i = len(temp1) - 1
    # print(apog[i] , apog[i - 1])
    while (apog[i] < but and apog[i] > apog[i - 1]):  # or len(altitud) == len(apog)
        # print(i)
        temp1 = numpy.append(temp1, temp1[i] + step)
        gravit = GRAVIT(apog[i] - centre_masse_haut)
        resist = 0
        acceler = - resist / kg_total
        ddz1 = numpy.append(ddz1, acceler * math.cos(angle1[i]) - gravit)
        # print("APOG     ddz1[i]    ",ddz1[i + 1])
        ddx1 = numpy.append(ddx1, acceler * math.sin(angle1[i]))
        apog = numpy.append(
            apog, apog[i] + step * dz1[i] + step**2 * ddz1[i + 1] / 2)
        # print("APOG     apog[i+1]   ", apog[i + 1])
        x1 = numpy.append(x1, x1[i] + step * dx1[i] +
                          step**2 * ddx1[i + 1] / 2)
        # print("APOG     x1[i+1]   ", x1[i + 1])
        dz1 = numpy.append(dz1, dz1[i] + step * ddz1[i + 1])
        # print("APOG     dz[i]     ",dz[i])
        dx1 = numpy.append(dx1, dx1[i] + step * ddx1[i + 1])
        # print("APOG     dx[i]     ",dx[i])
        if dx1[i + 1] > 0:
            if 180 * abs(math.atan(dz1[i + 1] / dx1[i + 1]) - angle1[i]) / math.pi < angle_max:
                angle1 = numpy.append(angle1, math.atan(dz1[i + 1] / dx1[i + 1]))
            else :
                angle1 = numpy.append(angle1, angle1[i] + angle_max * math.pi / 180)
        else : angle1  = numpy.append(angle1, 0)
        i += 1
    return temp1, angle1, apog, x1, dz1, dx1, ddz1, ddx1

def EULER_3d(typ, moteur, nombre, haut0, kg_vid0, kg_fuel0,
             step = step0,
             angle_max = angle_max0,
             temp=[0],
             angle=[0],
             altitud=[0],
             x=[0],
             dz=[0],
             dx=[vites_surface()],
             ddz=[0],
             ddx=[0]):
    if altitud[-1] == 0:
        altitud = [haut0]
    centre_masse_haut = haut0 / 2
    # print(typ, moteur, nombre, kg_fuel0)
    debit = fuel_kg_d(typ, moteur, nombre)
    apog = [0]
    i = len(temp) - 1
    temp_max = fuel_temp(typ, moteur, nombre, kg_fuel0) + temp[i]
    # print(temp_max)
    while (typ == 1 and temp[i] < temp_max) or (typ == 0 and temp[i] < temp_max and altitud[i] < but and apog[-1] < but) :
        # print(i)
        temp = numpy.append(temp, temp[i] + step)
        kg_fuel = kg_fuel0 - i * step * debit
        kg_total = kg_vid0 + kg_fuel * (kg_fuel > 0)
        gravit = GRAVIT(altitud[i] - centre_masse_haut)
        resist = 0
        pousse = POUSSE(typ, moteur, nombre, altitud[i])
        # print("EULER_3d pousse    ",pousse)
        # print(ISP(typ, moteur, altitud[i - 1]))
        acceler = (pousse - resist) / kg_total
        # print("EULER_3d acceler   ",acceler)
        if acceler * math.cos(angle[i]) - gravit >= 0:
            ddz = numpy.append(ddz, acceler * math.cos(angle[i]) - gravit)
        else:
            ddz = numpy.append(ddz, 0)
        # print("EULER_3d ddz[i]    ",ddz[i])
        ddx = numpy.append(ddx, acceler * math.sin(angle[i]))
        # print("EULER_3d ddx[i]    ",ddx)
        altitud = numpy.append(
            altitud, altitud[i] + step * dz[i] + step**2 * ddz[i + 1] / 2)
        # print("EULER_3d altitud[i+1]",altitud[i+1])
        x = numpy.append(x, x[i] + step * dx[i] + step**2 * ddx[i + 1] / 2)
        # print("EULER_3d x[i+1] ", x[i + 1])
        dz = numpy.append(dz, dz[i] + step * ddz[i + 1])
        # print("EULER_3d dz[i]     ",dz[i])
        dx = numpy.append(dx, dx[i] + step * ddx[i + 1])
        # print("EULER_3d dx[i]     ",dx[i])
        if apog[-1] > but :
            angle = numpy.append(angle, 90 * math.pi / 180)
        elif altitud[i] > 10000 :
            angle = numpy.append(angle, 45 * math.pi / 180)
        else:
            angle = numpy.append(angle, 0)
        # print("EULER_3d angle[i]  ",angle[i])
        if typ == 0 :
            temp1, angle1, apog, x1, dz1, dx1, ddz1, ddx1 = APOG(kg_total, temp, angle, altitud, x, dz, dx, ddz, ddx, centre_masse_haut, step, angle_max)
        # print("EULER_3d apog[i]   ",apog[i])
        i += 1
        # print(altitud[i])
    return temp, angle, altitud, x, dz, dx, ddz, ddx

def EULER_plan(plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel,
               step = step0,
               angle_max = angle_max0):
    temp, angle, altitud, x, dz, dx, ddz, ddx = EULER_3d(matric_nombre(fuse_typ, plan),
                                                         matric_nombre(fuse_moteur, plan),
                                                         matric_nombre(fuse_nombre, plan),
                                                         matric_nombre(fuse_haut, plan),
                                                         matric_nombre(fuse_kg_vid, plan),
                                                         matric_nombre(fuse_kg_fuel, plan),
                                                         step, angle_max)
    plan1 = numpy.copy(plan)
    for i in range(1, len(plan)+1):
        # if apog[-1] < but :
        if plan1[-i] != 0:
            plan1[-i] = 0
            # print(altitud)
            temp, angle, altitud, x, dz, dx, ddz, ddx = EULER_3d(matric_nombre(fuse_typ, plan),
                                                                 matric_nombre(fuse_moteur, plan1),
                                                                 matric_nombre(fuse_nombre, plan1),
                                                                 matric_nombre(fuse_haut, plan1),
                                                                 matric_nombre(fuse_kg_vid, plan1),
                                                                 matric_nombre(fuse_kg_fuel, plan1),
                                                                 step, angle_max, temp, angle, altitud, x, dz, dx, ddz, ddx)
            return temp, angle, altitud, x, dz, dx, ddz, ddx

def dimension_altitud(fuse_plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_cout,
                      step=step0,
                      fuse_apog=0):
    dim0 = dimension(fuse_cout)
    dim1 = dimension(fuse_apog)
    if dim1 == 0 and dim0 == 1:
        # print(fuse_moteur)
        fuse_apog = []
        for i in range(len(fuse_plan)):
            if fuse_cout[i] > 0:
                temp, angle, altitud, x, dz, dx, ddz, ddx = EULER_plan(fuse_plan[i], fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, step)
                kg_total = matric_nombre(fuse_kg_vid, fuse_plan[i]) + matric_nombre(fuse_kg_fuel, fuse_plan[i])
                centre_masse_haut = matric_nombre(fuse_haut, fuse_plan[i])
                temp1, angle1, apog, x1, dz1, dx1, ddz1, ddx1 = APOG(kg_total, temp, angle, altitud, x, dz, dx, ddz, ddx, centre_masse_haut, step)
            else:
                apog = [0]
            fuse_apog = numpy.append(fuse_apog, apog[-1])
        dim1 = dimension(fuse_apog)
    # print(dim1,dim0)
    if dim1 == 0 and dim0 > 1:
        fuse_apog = [dimension_altitud(fuse_plan[i], fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_cout[i], step) for i in range(len(fuse_plan))]
        dim1 = dimension(fuse_apog)
    return fuse_apog


## TESTES
# trac('nivelement barometrique', [PRESSION(i) for i in range(but)], 'pression (pa)', [i for i in range(but)], 'altitud (m)')
# trac_plan([16,16], typ, fuse0_1moteur, fuse0_2haut, fuse0_3kg_vid, fuse0_4kg_fuel)
Z = 6
z = 0
if Z > z:
    fuse_0plan, fuse_1typ, fuse_2moteur, fuse_3nombre, fuse_4haut, fuse_5kg_vid, fuse_6kg_fuel, fuse_7kg_total, fuse_8cout = dimension_base(1 + reacteur_fin - reacteur_deb)
    print('Z', Z - z)
z += 1
if Z > z :
    fuse_10dv   = dimension_dv(fuse_1typ, fuse_2moteur, fuse_3nombre, fuse_5kg_vid, fuse_7kg_total, but)
    fuse_8cout1 = dimension_test(fuse_8cout, fuse_10dv, orbital_v(but, planet[rayon] + but))
    min_0plan, min_1cout = dimension_min(fuse_0plan, fuse_8cout1)
    print(min_0plan, min_1cout)
    print('Z', Z - z)
z += 1
if Z > z :
    end_dim = 1 + propulseur_fin - propulseur_deb
    fuse_0plan, fuse_1typ, fuse_2moteur, fuse_3nombre, fuse_4haut, fuse_5kg_vid, fuse_6kg_fuel, fuse_7kg_total, fuse_8cout = dimension_plus(end_dim, min_0plan,
                                                                                                                                            matric_nombre(fuse_1typ     , min_0plan),
                                                                                                                                            matric_nombre(fuse_2moteur  , min_0plan),
                                                                                                                                            matric_nombre(fuse_4haut    , min_0plan),
                                                                                                                                            matric_nombre(fuse_7kg_total, min_0plan),
                                                                                                                                            matric_nombre(fuse_8cout    , min_0plan))
    step0 = end_dim
    angle_max0 = step0  # d°
    print('Z', Z - z)
z += 1
if Z > z :
    fuse_9decol = dimension_decol(fuse_1typ, fuse_2moteur, fuse_3nombre, fuse_7kg_total)
    fuse_8cout1 = dimension_test(fuse_8cout, fuse_9decol, 1)
    print('Z', Z - z)
z += 1
if Z > z :
    fuse_11apog = dimension_altitud(fuse_0plan, fuse_1typ, fuse_2moteur, fuse_3nombre, fuse_4haut, fuse_5kg_vid, fuse_6kg_fuel, fuse_8cout1)
    fuse_8cout1 = dimension_test(fuse_8cout1, fuse_11apog, but)
    min_0plan, min_1cout = dimension_min(fuse_0plan, fuse_8cout1)
    print(min_0plan, min_1cout)
    print('Z', Z - z)
z += 1
if Z > z :
    if dimension(min_0plan) == 1:
        if len(min_0plan) == dimension(fuse_2moteur):
            trac_plan(min_0plan, fuse_1typ, fuse_2moteur, fuse_3nombre, fuse_4haut, fuse_5kg_vid, fuse_6kg_fuel, 1, 360)
    print('Z', Z - z)
