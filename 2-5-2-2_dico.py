# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# CONSTANTE
import matplotlib.pyplot
import numpy
import math
G = 6.674e-11  # Constante gravitationnelle m3⋅kg−1⋅s−2
R = 8.31446261815324  # Constante de gaz kg⋅m2.s−2⋅K−1⋅mol−1
base = 71

# Planet
"mss = masse de l'objet (kg)"
"ryn = rayonde de l'objet en mettre(m)"
"day = duré pour une revolution autour d'elle meme (s)"
"klvn = temperature moyenne de l'objet (K)"
"mol = masse molaire moyenne de l'objet (kg.mol-1)"
"pa = pression atmospherique a la surface de l'objet (kg⋅m−1⋅s−2)"
"atm = limite atmospherique de l'objet(m)"
"nom = nom l'objet" 
plnt={'mss':5.2915158e22, 'ryn':6e+5, 'day':21600, 'klv':288.15, 'mol':0.0289644, 'prs':101325, 'atm':70000, 'nom':'kerbin'}

# Parachut
"tll = diamettre de l'objet (m)"
"haut = hauteur de l'objet (m)"
"cout = cout de l'objet ($)"
chut_nom = ['mk12-r','mk16']
chut = {'mk12-r':{'mss': 75, 'cout':150, 'haut':0    , 'tll':0  },
        'mk16'  :{'mss':100, 'cout':422, 'haut':0.631, 'tll':0.6}}

#
"what = resrve electrique (w)"
"what_d = consomation electrique (w.s-1)"
bdyn ={'mss': 50, 'what_d':1.7/60, 'cout':300, 'haut':1    , 'tll':0.6, 'nom':'staysputnick'}
pods ={'mss':800, 'what_d':  0.2 , 'cout':635, 'haut':1.1  , 'tll':1.3, 'nom':'mk1'}
cntrl={'mss': 50, 'what_d':  0.3 , 'cout':600, 'haut':0.628, 'tll':0.6, 'nom':'SAS'}
cmm  ={'mss':  5, 'what_d': 20   , 'cout':300, 'haut':0    , 'tll':0  , 'nom':'16'}
elct ={'mss':  5, 'what'  :100   , 'cout': 80, 'haut':0    , 'tll': 0  , 'nom':'z-100'}

cplng_nom =['stck','rdl']
cplng_nom2=[['td-06','td-12','td-37','td-37'],['tt-38','tt-70','hdm']]
cplng={'stck':{'td-06':{'mss': 10, 'cout':150, 'haut':0.625, 'tll':0.6},
               'td-12':{'mss': 40, 'cout':200, 'haut':0    , 'tll':1.3},
               'td-25':{'mss':160, 'cout':300, 'haut':1    , 'tll':2.5},
               'td-37':{'mss':360, 'cout':375, 'haut':1    , 'tll':3.8}},
       'rdl' :{'tt-38':{'mss': 25, 'cout':600, 'haut':0    , 'tll':0},
               'tt-70':{'mss': 50, 'cout':700, 'haut':0    , 'tll':0},
               'hdm'  :{'mss':400, 'cout':770, 'haut':0    , 'tll':0}}}

"ergl = essence (u)"
"oxdzr = oxigene solide (u)"
"mltpl"
tanks_nom=['oscar-b','fl','x200','s3']
tanks={'oscar-b':{'mss':  25  , 'ergl':  18, 'oxdzr':  22, 'mltpl':0, 'cout': 52  , 'haut':0.625, 'tll':0.6},
       'fl'     :{'mss':  62.5, 'ergl':  45, 'oxdzr':  55, 'mltpl':8, 'cout': 54.1, 'haut':0.5  , 'tll':1.3},
       'x200'   :{'mss': 500  , 'ergl': 360, 'oxdzr': 440, 'mltpl':8, 'cout':351.5, 'haut':1    , 'tll':2.5},
       's3'     :{'mss':2250  , 'ergl':1620, 'oxdzr':1980, 'mltpl':3, 'cout':347.5, 'haut':2.665, 'tll':3.8}}

"ergl_d = debit de l'essence (u.s-1)"
"oxdzr_d = debit de l'oxigen liquide (u.s-1)"
"pss_asl = pousser du reacteur a l'altidude 0 (kg.m.s-2)"
"pss_vac = pousser du reacteur dans l'espace (kg.m.s-2)"
"isp_asl = (s)"
"isp_vac = (s)"
rctrs_nom = ['ant','spark','terrier','reliant','swivel','poodle','skipper','minsail','rhino']
rctrs = {'ant'    :{'mss':  20, 'ergl_d': 0.058, 'oxdzr_d': 0.071, 'pss_asl':    508, 'pss_vac':   2000, 'isp_asl': 80, 'isp_vac':315, 'cout':  110, 'haut':0.3, 'tll':0.6},
         'spark'  :{'mss': 130, 'ergl_d': 0.574, 'oxdzr_d': 0.701, 'pss_asl':  16560, 'pss_vac':  20000, 'isp_asl':265, 'isp_vac':320, 'cout':  240, 'haut':0.4, 'tll':0.6},
         'terrier':{'mss': 500, 'ergl_d': 1.596, 'oxdzr_d': 1.951, 'pss_asl':  14780, 'pss_vac':  60000, 'isp_asl': 85, 'isp_vac':345, 'cout':  390, 'haut':0.8, 'tll':1.3},
         'reliant':{'mss':1500, 'ergl_d': 6.166, 'oxdzr_d': 7.536, 'pss_asl': 167969, 'pss_vac': 215000, 'isp_asl':250, 'isp_vac':320, 'cout': 1200, 'haut':1.7, 'tll':1.3},
         'swivel' :{'mss':1250, 'ergl_d': 7.105, 'oxdzr_d': 8.684, 'pss_asl': 205161, 'pss_vac': 240000, 'isp_asl':265, 'isp_vac':310, 'cout': 1100, 'haut':1.7, 'tll':1.3},
         'poodle' :{'mss':1750, 'ergl_d': 6.555, 'oxdzr_d': 8.012, 'pss_asl':  64286, 'pss_vac': 250000, 'isp_asl': 90, 'isp_vac':350, 'cout': 1300, 'haut':2.7, 'tll':2.5},
         'skipper':{'mss':3000, 'ergl_d':18.642, 'oxdzr_d':22.784, 'pss_asl': 658750, 'pss_vac': 650000, 'isp_asl':280, 'isp_vac':320, 'cout': 5300, 'haut':2.4, 'tll':2.5},
         'minsail':{'mss':6000, 'ergl_d':40.407, 'oxdzr_d':54.275, 'pss_asl':1379032, 'pss_vac':1500000, 'isp_asl':285, 'isp_vac':310, 'cout':13000, 'haut':3  , 'tll':2.5},
         'rhino'  :{'mss':9000, 'ergl_d':53.985, 'oxdzr_d':65.982, 'pss_asl':1205882, 'pss_vac':2000000, 'isp_asl':205, 'isp_vac':340, 'cout':25000, 'haut':4.1, 'tll':3.8}}

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
    d = ergol_u_kg(engeins[typ][moteur][ergol_d]) + oxidizer_u_kg(engeins[typ][moteur][oxidizer_d])
    if typ == 1 :
        return nombre * d
    return d
def fuel_temp(typ, moteur, nombre, kg_fuel):
    if moteur == -1 : return 0
    return kg_fuel / fuel_kg_d(typ, moteur, nombre)

"La vites nécessaire pour échapper au puits de gravité d'une planète donnée"
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
    if altitud >= planet[atm_limit] : return 0
    return planet[pression_pa_0] * math.exp(-altitud / HE())
    # return planet[pression_pa_0] * (1 - altitud * 6.5 / 1000 / planet[kelvin_0])**(5.255) # imajinair
    # z = [0, 2500, 5000, 7500, 10000, 15000, 20000, 25000, 30000, 40000, 50000, 60000, 70000]
    # p = 101
def DENSIT(altitud):
    return PRESSION(altitud) / R / planet[kelvin_0]

"L'impulsion spécifique définit l'efficacité d'un moteur."
def ISP(typ, moteur, nombre, altitud):  # s
    a = engeins[typ][moteur][isp_vac] + PA_atm(PRESSION(altitud)) * (engeins[typ][moteur][isp_asl] - engeins[typ][moteur][isp_vac])
    if typ == 1 :
        return nombre * a
    return a


"la poussée est la force exercée par l'accélération de gaz"
def POUSSE(typ, moteur, nombre, altitud):
    return ISP(typ, moteur, nombre, altitud) * GRAVIT(0) * fuel_kg_d(typ, moteur, nombre)

"Le rapport poussée sur poids est un rapport qui définit la puissance des moteurs d'un engin par rapport à son propre poids."
def RPP(typ, moteur, nombre, altitud, kg):  # >1
    return nombre * POUSSE(typ, moteur, nombre, altitud) / (kg * GRAVIT(altitud))
def a_GRAVIT(typ, moteur, nombre, altitud, kg):
    return GRAVIT(altitud) * (RPP(typ, moteur, nombre, altitud, kg) - 1)


"Changement de vites d'un vaisseau spatial mesuré en mètres par seconde (m/s)."
def vites_ms(distance, temp): return distance / temp
def vites_angulair(temp): return 360 / temp #deg.s-1
def vites_orbital(R, axe_grand_demi) :
    return math.sqrt(G * planet[masse] * (2 / R - 1 / axe_grand_demi))
def vites_delta(typ, moteur, nombre, altitud, kg_vid, kg_total):
    return ISP(typ, moteur, nombre, altitud) * GRAVIT(0) * math.log(kg_total / kg_vid)

vites_k = vites_ms(2 * math.pi * planet[rayon], planet[day])
vites_deg_k = vites_angulair(planet[day])

# VARIABLE
min_0plan, min_1cout = 0, 0
deb_haut = pods[haut] + chut[1][haut] + base
deb_kg = pods[masse] + chut[1][masse]
deb_cout = pods[cout] + chut[1][cout]
deb_taille = pods[taille]
deb_moteur = 0
q = 1 * 8 + 1
dim = 1
but_altitud = 80000
but_dv =  escap(but_altitud)
step0 = 1
angle_max0 = 1

# STRUCTURE
def cord(liste, but) :
    i = 0
    while liste[i] != but :
        i += 1
    return i

def sheriq_cartesien(ligne, biais = 0) :
    return [(biais + ligne[0]) * math.cos(math.radians(ligne[2])) * math.cos(math.radians(ligne[1])),
            (biais + ligne[0]) * math.cos(math.radians(ligne[2])) * math.sin(math.radians(ligne[1])),
            (biais + ligne[0]) * math.sin(math.radians(ligne[2]))]

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
        matrice = [dimension_matrice(dim - 1, long, matrice) for i in range(long)]
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

def trac_plan(plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, step=step0, mod=3):
    global min_2temp, min_3pousse, min_4altitud, min_5apog
    min_2temp, kg_total, gravit_f, min_3pousse, acceler_f, acceler, vites, position, min_4altitud, min_5apog, dPHI = EULER_plan(mod, plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, step)
    # print(altitud)
    
    position1 = [sheriq_cartesien(min_5apog[i], planet[rayon]) for i in range(len(min_5apog))]
    
    max_angl = int(max([min_5apog[i][1] + 2*180*(min_5apog[i][1]<0) for i in range(len(min_5apog))]))
    matplotlib.pyplot.plot([planet[rayon]*math.cos(math.radians(i)) for i in range(max_angl)], [planet[rayon]*math.sin(math.radians(i)) for i in range(max_angl)], color = 'k')
    # print(max_angl)
        
    matplotlib.pyplot.plot(  [position1[i][0] for i in range(len(position1))], [position1[i][1] for i in range(len(position1))], color = 'g')
    matplotlib.pyplot.plot(  [position[i][0] for i in range(len(position))]  , [position[i][1] for i in range(len(position))])
    
    # matplotlib.pyplot.quiver([position1[i][0] for i in range(len(position1))], [position1[i][1] for i in range(len(position1))], [acceler1[i][0] for i in range(len(acceler1))], [acceler1[i][1] for i in range(len(acceler1))], color='r')
    matplotlib.pyplot.quiver([position[i][0] for i in range(len(position))]  , [position[i][1] for i in range(len(position))]  , [acceler[i][0] for i in range(len(acceler))]  , [acceler[i][1] for i in range(len(acceler))], color='r')
    
    a = [min_5apog[i][0] for i in range(len(min_4altitud), len(min_5apog))]
    cord_max_a = cord(a, max(a))
    cord_min_a = cord(a, min(a))
    matplotlib.pyplot.quiver([position1[cord_max_a][0], position1[cord_min_a][0]], [position1[cord_max_a][1], position1[cord_min_a][1]]  , [min_5apog[cord_max_a][0], min_5apog[cord_min_a][0]] , [min_5apog[cord_max_a][0], min_5apog[cord_min_a][0]], color='m')

    matplotlib.pyplot.title('vol')
    matplotlib.pyplot.xlabel('x')
    matplotlib.pyplot.ylabel('y')
    matplotlib.pyplot.show()

# FONCTION
def construc(typ, moteur,
             fuse_typ     = [0],
             fuse_moteur  = [-1],
             fuse_nombre  = [1],
             fuse_haut    = [deb_haut],
             fuse_kg_vid  = [deb_kg],
             fuse_kg_fuel = [0],
             fuse_cout    = [deb_cout],
             fuse_dv = [0]):
    i = 0
    fuse_plan = [i]
    fuse_kg_total = [fuse_kg_vid[i] + fuse_kg_fuel[i]]
    fuse_gravit = [a_GRAVIT(typ, moteur, fuse_nombre[i], but_altitud, fuse_kg_total[i])]
    # print(fuse_dv[i], fuse_gravit[i])
    while i + 1 < q : # and fuse_dv[i] < but_dv and fuse_gravit[i] > 1 
        # print(fuse_dv[i], fuse_gravit[i])
        i += 1
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
            fuse_haut    = numpy.append(fuse_haut   , fuse_haut[1])
            fuse_kg_vid  = numpy.append(fuse_kg_vid , fuse_kg_total[1] + i * engeins[typ][moteur][masse])
            fuse_cout    = numpy.append(fuse_cout   , fuse_cout[1]     + i * (engeins[typ][moteur][cout] + solid_u_c( engeins[typ][moteur][solid])))
            fuse_kg_fuel = numpy.append(fuse_kg_fuel, i * solid_u_kg(engeins[typ][moteur][solid]))
        fuse_kg_total = numpy.append(fuse_kg_total, fuse_kg_vid[i] + fuse_kg_fuel[i])
        fuse_dv       = numpy.append(fuse_dv      , fuse_dv[0] + vites_delta(typ, moteur, fuse_nombre[i], but_altitud, fuse_kg_vid[i], fuse_kg_total[i]))
        fuse_gravit   = numpy.append(fuse_gravit  , a_GRAVIT(typ, moteur, fuse_nombre[i], but_altitud, fuse_kg_total[i]))
    return fuse_plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout, fuse_dv, fuse_gravit

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
                   fuse_dv       = 0,
                   fuse_plan     = 0,
                   fuse_nombre   = 1,
                   fuse_kg_fuel  = 0,
                   fuse_gravit   = 0):
    dim = dimension(fuse_moteur)
    # print(dim)
    if dim == 0 and end_dim == 1:
        fuse_plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout, fuse_dv, fuse_gravit = construc(typ, moteur,
                                                                                                                    [fuse_typ],
                                                                                                                    [fuse_moteur],
                                                                                                                    [fuse_nombre],
                                                                                                                    [fuse_haut],
                                                                                                                    [fuse_kg_vid],
                                                                                                                    [fuse_kg_fuel],
                                                                                                                    [fuse_cout],
                                                                                                                    [fuse_dv])
        dim = dimension(fuse_moteur)
    if dim == 0 and end_dim > 1:
        fuse_plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout, fuse_dv, fuse_gravit = dimension_base(end_dim - 1,
                                                                                                                          typ,
                                                                                                                          moteur,
                                                                                                                          fuse_typ,
                                                                                                                          fuse_moteur,
                                                                                                                          fuse_haut,
                                                                                                                          fuse_kg_vid,
                                                                                                                          fuse_kg_total,
                                                                                                                          fuse_cout,
                                                                                                                          fuse_dv,
                                                                                                                          fuse_plan,
                                                                                                                          fuse_nombre,
                                                                                                                          fuse_kg_fuel,
                                                                                                                          fuse_gravit)
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
        fuse_dv       = liste_matrice(fuse_dv)
        fuse_gravit   = liste_matrice(fuse_gravit)
        # print('a',fuse_kg_fuel)
        if typ == 0 and moteur + 1 > reacteur_fin :
            typ = 1
            moteur = propulseur_deb
        else : moteur += 1
        Q = range(len(fuse_moteur))
        for i0 in Q:
            fuse1_plan, fuse1_typ, fuse1_moteur, fuse1_nombre, fuse1_haut, fuse1_kg_vid, fuse1_kg_fuel, fuse1_kg_total, fuse1_cout, fuse1_dv, fuse1_gravit = dimension_base(end_dim - 1,
                                                                                                                                      typ,
                                                                                                                                      moteur,
                                                                                                                                      fuse_typ[i0][0],
                                                                                                                                      fuse_moteur[i0][0],
                                                                                                                                      fuse_haut[i0][0],
                                                                                                                                      fuse_kg_vid[i0][0],
                                                                                                                                      fuse_kg_total[i0][0],
                                                                                                                                      fuse_cout[i0][0],
                                                                                                                                      fuse_dv[i0][0],
                                                                                                                                      fuse_plan[i0][0],
                                                                                                                                      fuse_nombre[i0][0],
                                                                                                                                      fuse_kg_fuel[i0][0],
                                                                                                                                      fuse_gravit [i0][0])
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
            fuse_dv[i0]       = fuse1_dv
            fuse_gravit[i0]   = fuse1_gravit
        dim = dimension(fuse_moteur)
    return fuse_plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_kg_total, fuse_cout, fuse_dv, fuse_gravit


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
        # print(typ[0], moteur[0], kg_vid[0], kg_total[0])
        dv = [vites_delta(typ[0], moteur[0], nombre[0], altitud, kg_vid[0], kg_total[0])]
        for i in range(1, len(moteur)):
            dv = numpy.append(dv, dv[0] + vites_delta(typ[i], moteur[i], nombre[i], altitud, kg_vid[i], kg_total[i]))
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
        cout1 = [cout0[i] * (fuse[i] >= but) for i in range(len(cout0))]
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
            if cout[i] != 0 and (cout[i] < min_cout or min_cout == 0):
                min_plan = plan[i]
                min_cout = cout[i]
    if dim > 1:
        for i in range(len(cout)):
            min_plan, min_cout = dimension_min(plan[i], cout[i], min_cout, min_plan)
    return min_plan, min_cout

# vites_max = vites_ms_angle(but_altitud, vites_orbital(but_altitud, planet[rayon] + but_altitud))
# print(vites_max)
def EULER_3d(mod, typ, moteur, nombre, haut0, kg_vid0, kg_fuel0, 
             step = step0,
             temp      = None,
             kg_total  = None,
             gravit_f  = None,
             pousse_f  = None,
             acceler_f = None,
             acceler   = None,
             vites     = None,
             position  = None,
             altitud   = None,
             apog      = None,
             dPHI      = vites_deg_k) :
    
    d_fuel = step * fuel_kg_d(typ, moteur, nombre)
    centre_masse_haut = haut0 / 2
    apog_i = 0
    apog_acc_i_demi = 0
    phi = 0
    # print(dPHI == vites_angulair_k)
    if dPHI == vites_deg_k :
        i = 0
        temp2      = [0]
        kg_total2  = [kg_vid0 + kg_fuel0]
        pousse_f2  = [[0,0,0]] # coord  shérique, fusée hotogonal
        acceler_f2 = [[0,0,0]] # coord cartesien, fusée hotogonal
        acceler2   = [[0,0,0]] # coord cartesien, centre astre
        altitud2   = [[0,0,0]] # coord  shérique, centre astre
        apog2      = [[0,0,0]] # coord  shérique, centre astre
        vites2     = [[0,vites_k,0]] # coord cartesien, centre astre
        position2  = [[planet[rayon],0,0]] # coord cartesien, centre astre
        gravit_f2  = [[-GRAVIT(altitud2[i][0] - centre_masse_haut), 0 ,0]] # reper sherique, fusée hotogonal
    else :
        temp2      = numpy.copy(temp)
        kg_total2  = numpy.copy(kg_total)
        gravit_f2  = numpy.copy(gravit_f)
        pousse_f2  = numpy.copy(pousse_f)
        acceler_f2 = numpy.copy(acceler_f)
        acceler2   = numpy.copy(acceler)
        vites2     = numpy.copy(vites)
        position2  = numpy.copy(position)
        altitud2   = numpy.copy(altitud)
        apog2      = numpy.copy(apog)
        
    i = len(temp2) - 1
    # print(len(altitud2), len(apog2))
    a  = [altitud2[i2][0] for i2 in range(len(altitud2))]
    a1 = [   apog2[i2][0] for i2 in range(len(   apog2))]
    a2 = [   apog2[i2][0] for i2 in range(len(altitud2), len(apog2))]
    # max_angl_apog    = int(max([360*(apog2[i2-1][1]<0)*(apog2[i2][2]>0)       for i2 in range(len(apog2))]))
    max_angl_altitud = int(max([360*(altitud2[i2-1][1]<0)*(altitud2[i2][2]>0) for i2 in range(len(altitud2))]))
    while altitud2[i][0] >= 0 : # and altitud2[i][0] >= altitud2[i-1][0]
        if len(a2) == 0 :
            periaps = 0
        else :
            periaps = min(a2)
        # if mod == 3 : print(p >= planet[atm_limit], kg_total2[i] == kg_vid0)
        if (   (mod == 1 and (    kg_total2[i] == kg_vid0 or (typ == 0 and (max(a1) >= but_altitud
                                                                            or altitud2[i][0] < altitud2[i-1][0]))))
            or (mod == 3 and (kg_total2[i] == kg_vid0 or (typ == 0 and periaps >= planet[atm_limit])))
            or (mod == 2 and (max(a) >= but_altitud or altitud2[i][0] < altitud2[i-1][0]))
            or (mod == 4 and (max_angl_altitud >= 360 or altitud2[i][0] > planet[rayon]))) :
            return temp2, kg_total2, gravit_f2, pousse_f2, acceler_f2, acceler2, vites2, position2, altitud2, apog2, dPHI
        temp2 = numpy.append(temp2, i * step)
        i1 = i + 1
        if altitud2[i][0] <= planet[atm_limit] :
            v_f = sheriq_cartesien([math.sqrt(vites2[i][0]**2 + vites2[i][1]**2 + vites2[i][2]**2), math.atan2(vites2[i][1], vites2[i][0])-altitud2[i][1], 0])
            phi = math.atan(v_f[1]/v_f[0])
        # if altitud2[i][0] >= 10000 and altitud2[i][0] <= planet[atm_limit] :
        #     phi = 45 
        elif max(a1) >= but_altitud  and altitud2[i][0] >  planet[atm_limit] :
            phi = 90
        # print(altitud2[i])
        if  typ == 0 and mod == 3 and max(a1) >= but_altitud and apog_i == 0 :
            # print(mod)
            apog_i = cord(a1, max(a1))
            # print('apog_i', apog_i)
            apog_acc_i_precd = 1
            apog_acc_i = 0
            # apog_v_nec = math.sqrt(GRAVIT(apog2[apog_i][0] - centre_masse_haut) * planet[rayon]+apog2[apog_i][0])
            vites_init = 0 # vites_orbital(planet[rayon]+apog2[apog_i][0], (planet[rayon]+apog2[apog_i][0])/2)
            while apog_acc_i_precd > apog_acc_i or apog_acc_i_precd <= 1:
                apog_acc_i_precd = apog_acc_i
                apog_v_nec = math.sqrt(GRAVIT(apog2[apog_i][0] - centre_masse_haut) * planet[rayon]+apog2[apog_i][0]) - vites_init #vites_orbital(,  planet[rayon]+apog2[apog_i][0]) # - apog_v # planet[atm_limit] - 
                # print('apog_v_nec', apog_v_nec)
                apog_acc_f = 0
                apog_acc_i = 0
                while apog_acc_f < apog_v_nec :
                    kg_total0 = kg_total2[i] - d_fuel * step * apog_acc_i
                    apog_acc_f_sher = numpy.add(sheriq_cartesien([POUSSE(typ, moteur, nombre, apog2[apog_i][0]) / kg_total0, 90, 0]),
                                            sheriq_cartesien([GRAVIT(apog2[apog_i][0] - centre_masse_haut), 180, 0]))
                    # print('apog_acc_f_sher', apog_acc_f_sher)
                    apog_acc_f += math.sqrt(apog_acc_f_sher[0]**2 + apog_acc_f_sher[1]**2 + apog_acc_f_sher[2]**2)
                    apog_acc_i += 1
                apog_acc_i_demi = int(apog_acc_i / 2)
                vites_init = vites_orbital(planet[rayon]+apog2[apog_i - apog_acc_i_demi][0], (planet[rayon]+apog2[apog_i][0])/2)
            apog_acc_i_demi = int(apog_acc_i_precd / 2)
            # print('apog_acc_i_demi', apog_acc_i_demi)
        # if mod == 3 :
        #     print(typ == 1)
        #     print((mod == 1 or mod == 3) and (typ == 1 or (typ == 0 and (max(a1) < but_altitud or (apog_i != 0 and i > apog_i - apog_acc_i_demi and i < apog_i + apog_acc_i_demi)))))
        if (mod == 1 or mod == 3) and (typ == 1 or (typ == 0 and (max(a1) < but_altitud or (apog_i != 0 and i > apog_i - apog_acc_i_demi and i < apog_i + apog_acc_i_demi)))) :
            if kg_total2[i] - kg_vid0 > d_fuel * step :
                kg_total0 = kg_total2[i] - d_fuel * step
                # print(i , int(apog_i - apog_acc_i_demi), int(apog_i + apog_acc_i_demi))
            else :
                kg_total0 = kg_vid0
            pousse_f0 = [[POUSSE(typ, moteur, nombre, altitud2[i][0]) / kg_total2[i], phi, 0]]
        else :
            kg_total0 = kg_total2[i]
            pousse_f0 = [[0, phi, 0]]
        kg_total2 = numpy.append(kg_total2, kg_total0)
        pousse_f2 = numpy.append(pousse_f2, pousse_f0, 0)
        acceler_f2 = numpy.append(acceler_f2, [numpy.add(sheriq_cartesien(pousse_f2[i1]),
                                                         sheriq_cartesien(gravit_f2[i]))], 0)
        acceler2   = numpy.append(  acceler2, [numpy.add(sheriq_cartesien(numpy.add(pousse_f2[i1], [0, altitud2[i][1], 0])),
                                                         sheriq_cartesien(numpy.add( gravit_f2[i], [0, altitud2[i][1], 0])))], 0)
        vites2     = numpy.append(    vites2, [numpy.add(   vites2[i], numpy.dot(step * numpy.identity(3), acceler2[i1]))], 0)
        position2  = numpy.append( position2, [numpy.add(position2[i], numpy.dot(step * numpy.identity(3),   vites2[i1]))]  , 0)
        PHI = altitud2[i][2]
        PHI2 = math.degrees(math.atan2(position2[i1][1],position2[i1][0]))
        dPHI  = PHI - PHI2
        PHI = PHI2
        altitud2   = numpy.append(altitud2  , [[math.sqrt(position2[i1][0]**2 + position2[i1][1]**2 + position2[i1][2]**2) - planet[rayon], PHI, 0]], 0)
        gravit_f2  = numpy.append(gravit_f2 , [[GRAVIT(altitud2[i1][0] - centre_masse_haut), 180, 0]], 0)
        if  pousse_f2[i1][0] != 0 :
            temp1, kg_total1, gravit_f1, pousse_f1, acceler_f1, acceler1, vites1, position1, apog2, apog1, dPHI = EULER_3d(mod+1, typ, moteur, nombre, haut0, kg_vid0, kg_fuel0, step, temp2, kg_total2, gravit_f2, pousse_f2, acceler_f2, acceler2, vites2, position2, altitud2, apog2, dPHI)
        # max_angl_apog    = int(max([360*(   apog2[i2-1][1]<0)*(   apog2[i2][1]>0) for i2 in range(len(   apog2))]))
        max_angl_altitud = int(max([360*(altitud2[i2-1][1]<0)*(altitud2[i2][1]>0) for i2 in range(len(altitud2))]))
        a  = [altitud2[i2][0] for i2 in range(               len(altitud2))]
        a1 = [   apog2[i2][0] for i2 in range(               len(   apog2))]
        a2 = [   apog2[i2][0] for i2 in range(len(altitud2), len(   apog2))]
        i += 1
        # if mod == 1 or mod == 3 :
        #     print('  kg_total',  kg_total2[i])
        #     print('  gravit_f',  gravit_f2[i])
        #     print('  pousse_f',  pousse_f2[i])
        #     print(' acceler_f', acceler_f2[i])
        #     print('   acceler',   acceler2[i])
        #     print('     vites',     vites2[i])
        #     print('  position',  position2[i])
        #     print('   altitud',   altitud2[i])
        #     print('      apog', apog2[cord(a1, max(a1))])
        #     if len(a2) != 0 : print('   periaps',apog2[cord(a1,  min(a2))])
    # print('i', i)
    return temp2, kg_total2, gravit_f2, pousse_f2, acceler_f2, acceler2, vites2, position2, altitud2, apog2, dPHI
                             
def EULER_plan(mod, plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel,
               step = step0):
    # print(fuse_kg_fuel)
    temp, kg_total, gravit_f, pousse_f, acceler_f, acceler, vites, position, altitud, apog, dPHI = EULER_3d(mod, matric_nombre(fuse_typ, plan),
                                                                                                                          matric_nombre(fuse_moteur, plan),
                                                                                                                          matric_nombre(fuse_nombre, plan),
                                                                                                                          matric_nombre(fuse_haut, plan),
                                                                                                                          matric_nombre(fuse_kg_vid, plan),
                                                                                                                          matric_nombre(fuse_kg_fuel, plan),
                                                                                                                          step)
    plan1 = numpy.copy(plan)
    i = 1
    while plan1[-i] == 0:
        i += 1
    plan1[-i] = 0
    for i1 in range(i + 1, len(plan)+1):
        # if apog[-1] < but_altitud :
        if plan1[-i1] != 0:
            # print(plan1)
            temp, kg_total, gravit_f, pousse_f, acceler_f, acceler, vites, position, altitud, apog, dPHI = EULER_3d(mod, matric_nombre(fuse_typ, plan1),
                                                                                                                         matric_nombre(fuse_moteur, plan1),
                                                                                                                         matric_nombre(fuse_nombre, plan1),
                                                                                                                         matric_nombre(fuse_haut, plan1),
                                                                                                                         matric_nombre(fuse_kg_vid, plan1),
                                                                                                                         matric_nombre(fuse_kg_fuel, plan1),
                                                                                                                         step, temp, kg_total, gravit_f, pousse_f, acceler_f, acceler, vites, position, altitud, apog, dPHI)
            plan1[-i1] = 0
    # print(position)
    return temp, kg_total, gravit_f, pousse_f, acceler_f, acceler, vites, position, altitud, apog, dPHI

def dimension_orbit(mod, fuse_plan, fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_cout, 
                      step=step0,
                      fuse_orbit=0):
    dim0 = dimension(fuse_cout)
    dim1 = dimension(fuse_orbit)
    if dim1 == 0 and dim0 == 1:
        # print(fuse_moteur)
        fuse_orbit = []
        for i in range(len(fuse_plan)):
            if fuse_cout[i] > 0:
                print(fuse_plan[i])
                temp,  kg_total,  gravit_f,  pousse_f,  acceler_f,  acceler,  vites,  position, altitud, apog,  dPHI  = EULER_plan(mod, fuse_plan[i], fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, step)
                if mod == 3 :
                    max_orbit = int(max([360*(apog[i1-1][1]<0)*(apog[i1][1]>=0) for i1 in range(1, len(apog))]))
                elif mod == 1 :
                    max_orbit = int(max([apog[i1][0] for i1 in range(len(apog))]))
                    # print(apog)
            else:
                max_orbit = 0
            fuse_orbit = numpy.append(fuse_orbit, max_orbit)
        dim1 = dimension(fuse_orbit)
    # print(dim1,dim0)
    if dim1 == 0 and dim0 > 1:
        fuse_orbit = [dimension_orbit(mod, fuse_plan[i], fuse_typ, fuse_moteur, fuse_nombre, fuse_haut, fuse_kg_vid, fuse_kg_fuel, fuse_cout[i], step) for i in range(len(fuse_plan))]
        dim1 = dimension(fuse_orbit)
    return fuse_orbit


## TESTES
# trac('nivelement barometrique', [PRESSION(i) for i in range(but_altitud)], 'pression (pa)', [i for i in range(but_altitud)], 'altitud (m)')
# trac_plan([16,16], typ, fuse0_1moteur, fuse0_2haut, fuse0_3kg_vid, fuse0_4kg_fuel)
Z = 4
z = 0
if Z > z:
    end_dim = 1 + reacteur_fin - reacteur_deb + 2 #+ propulseur_fin - propulseur_deb
    step0 = end_dim
    angle_max0 = step0  # d°
    fuse_0plan, fuse_1typ, fuse_2moteur, fuse_3nombre, fuse_4haut, fuse_5kg_vid, fuse_6kg_fuel, fuse_7kg_total, fuse_8cout, fuse_9dv, fuse_10gravit = dimension_base(end_dim)
    fuse_8cout1 = dimension_test(fuse_8cout, fuse_9dv, but_dv)
z += 1
print('Z', Z - z)
# if Z > z :
#     fuse_9dv1 = dimension_dv(fuse_1typ, fuse_2moteur, fuse_3nombre, fuse_5kg_vid, fuse_7kg_total, 0)
#     fuse_8cout1 = dimension_test(fuse_8cout, fuse_9dv1, but_dv)
# z += 1
# print('Z', Z - z)
if Z > z :
    fuse_10gravit1 = dimension_decol(fuse_1typ, fuse_2moteur, fuse_3nombre, fuse_7kg_total)
    fuse_8cout1 = dimension_test(fuse_8cout1, fuse_10gravit1, 1)
z += 1
print('Z', Z - z)
if Z > z :
    min_0plan, min_1cout = dimension_min(fuse_0plan, fuse_8cout1)
    print(min_0plan, min_1cout)
    if dimension(min_0plan) == 1:
        if len(min_0plan) == dimension(fuse_2moteur):
            trac_plan(min_0plan, fuse_1typ, fuse_2moteur, fuse_3nombre, fuse_4haut, fuse_5kg_vid, fuse_6kg_fuel, 1, 3)
z += 1
print('Z', Z - z)
